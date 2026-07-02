from fastapi import APIRouter, Depends, HTTPException, Query
from fastapi.responses import RedirectResponse

from src.api.dependencies import (
    get_google_oauth,
    get_google_user_service,
    get_oauth_session_store,
)
from src.auth.google_oauth import GoogleOAuthService
from src.auth.oauth_session_store import OAuthSessionStore
from src.models.auth import AuthorizationRequest
from src.schemas.auth import AuthUser
from src.schemas.common import ApiResponse
from src.services.google_user_service import GoogleUserService

router = APIRouter(
    prefix="/api/v1/auth",
    tags=["Authentication"],
)


@router.get("/login")
async def login(
    oauth: GoogleOAuthService = Depends(get_google_oauth),
    oauth_session_store: OAuthSessionStore = Depends(get_oauth_session_store),
):
    """
    Redirect user to Google login.
    """

    authorization: AuthorizationRequest = oauth.create_authorization_request()

    oauth_session_store.create(
        state=authorization.state, code_verifier=authorization.code_verifier
    )

    return RedirectResponse(url=authorization.url)


@router.get("/callback", response_model=ApiResponse[AuthUser])
async def callback(
    code: str = Query(...),
    state: str | None = Query(None),
    oauth: GoogleOAuthService = Depends(get_google_oauth),
    oauth_session_store: OAuthSessionStore = Depends(get_oauth_session_store),
    google_user: GoogleUserService = Depends(get_google_user_service),
):
    """
    Google OAuth callback.
    """

    try:

        session = oauth_session_store.get(state=state)

        credentials = oauth.exchange_code(
            code=code, code_verifier=session.code_verifier
        )

        oauth_session_store.delete(state=state)

        profile = google_user.get_profile(credentials)

        return ApiResponse[AuthUser](message="Authentication Successful", data=profile)

    except Exception as ex:

        raise HTTPException(
            status_code=400,
            detail=str(ex),
        )
