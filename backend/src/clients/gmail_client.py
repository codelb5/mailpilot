"""
Google Gmail client.
"""

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import Resource, build


class GmailClient:
    """
    Handles communication with the Gmail API.
    """

    def __init__(self) -> None:
        pass

    def _build_service(self, credentials: Credentials):
        """
        Create a Gmail API service.
        """

        return build(serviceName="gmail", version="v1", credentials=credentials)

    def get_profile(
        self,
        credentials: Credentials,
    ) -> dict:
        """
        Get Gmail profile.
        """
        service = self._build_service(credentials=credentials)

        return service.users().getProfile(userId="me").execute()

    def list_messages(
        self,
        credentials: Credentials,
    ):
        """
        List Gmail messages.
        """
        raise NotImplementedError

    def get_message(
        self,
        credentials: Credentials,
        message_id: str,
    ):
        """
        Get a Gmail message.
        """
        raise NotImplementedError

    def get_labels(
        self,
        credentials: Credentials,
    ):
        """
        List Gmail labels.
        """
        raise NotImplementedError
