"""
Google User API Client.
"""

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build


class GoogleUserClient:
    """
    Client for Google's OAuth2 UserInfo API.
    """

    def get_profile(self, credentials: Credentials) -> dict:
        """
        Fetch the authenticated user's profile.
        """

        service = build(
            "oauth2",
            "v2",
            credentials=credentials,
        )

        profile = service.userinfo().get().execute()

        return profile
