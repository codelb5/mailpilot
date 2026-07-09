"""
Google User Service.
"""

from google.oauth2.credentials import Credentials

from src.clients.google_user_client import GoogleUserClient
from src.schemas.auth import AuthUser


class GoogleUserService:

    def __init__(self, client: GoogleUserClient):
        self.client = client

    def get_profile(self, credentials: Credentials) -> AuthUser:

        profile = self.client.get_profile(credentials)

        return AuthUser(
            email=profile["email"],
            name=profile["name"],
            picture=profile.get("picture"),
            email_verified=profile.get("verified_email", False),
        )
