from src.auth.google_oauth import GoogleOAuthService
from src.services.google_user_service import GoogleUserService
from src.clients.google_user_client import GoogleUserClient


def get_google_oauth():

    return GoogleOAuthService()


def get_google_user_client() -> GoogleUserClient:

    return GoogleUserClient()
