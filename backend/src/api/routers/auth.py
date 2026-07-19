from fastapi import APIRouter, Depends, HTTPException, Query
from fastapi.responses import RedirectResponse
import traceback

from src.api.dependencies import (
    get_google_oauth,
    get_google_user_client,
    get_oauth_session_store,
    get_user_service,
    get_oauth_token_service,
)
from src.auth.google_oauth import GoogleOAuthService
from src.auth.oauth_session_store import OAuthSessionStore
from src.models.auth import AuthorizationRequest
from src.schemas.auth import AuthUser
from src.schemas.common import ApiResponse
from src.clients.google_user_client import GoogleUserClient
from src.services.user_service import UserService
from src.services.oauth_token_service import OAuthTokenService

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
    google_user_client: GoogleUserClient = Depends(get_google_user_client),
    user_service: UserService = Depends(get_user_service),
    oauth_token_service: OAuthTokenService = Depends(
        get_oauth_token_service,
    ),
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

        user_profile = google_user_client.get_profile(credentials=credentials)

        user = await user_service.sync_google_user(auth_user=user_profile)

        await oauth_token_service.save_google_credentials(
            user=user,
            credentials=credentials,
        )

        return ApiResponse[AuthUser](
            message="Authentication Successful", data=user_profile
        )

    except Exception as ex:

        # traceback.print_exc()
        # raise
        raise HTTPException(
            status_code=400,
            detail=str(ex),
        )
