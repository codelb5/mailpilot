from fastapi import APIRouter, Depends
from fastapi.responses import RedirectResponse

from src.api.dependencies import get_google_oauth
from src.auth.google_oauth import GoogleOAuth

router = APIRouter(
    prefix="/api/v1/auth",
    tags=["Authentication"],
)


@router.get("/login")
async def login(
    oauth: GoogleOAuth = Depends(get_google_oauth),
):
    """
    Redirect user to Google login.
    """

    authorization_url, state = oauth.create_authorization_request()

    return RedirectResponse(url=authorization_url)
