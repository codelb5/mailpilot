"""
Google User API Client.
"""

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

from src.schemas.auth import AuthUser


class GoogleUserClient:
    """
    Client for Google's OAuth2 UserInfo API.
    """

    def get_profile(self, credentials: Credentials) -> AuthUser:
        """
        Fetch the authenticated user's profile.
        """

        service = build(
            "oauth2",
            "v2",
            credentials=credentials,
        )

        profile = service.userinfo().get().execute()

        return AuthUser(
            email=profile["email"],
            name=profile["name"],
            picture=profile.get("picture"),
            email_verified=profile.get(
                "verified_email",
                False,
            ),
        )
