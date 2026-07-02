"""
Google OAuth service.
"""

from google_auth_oauthlib.flow import Flow

from src.core.config import settings
import logging


class GoogleOAuth:
    """
    Handles Google OAuth authentication.
    """

    def __init__(self):

        self.scopes = [scope.strip() for scope in settings.GOOGLE_SCOPES.split(",")]

    # def create_flow(self) -> Flow:
    #     """
    #     Create OAuth Flow.
    #     """

    #     return Flow.from_client_config(
    #         {
    #             "web": {
    #                 "client_id": settings.GOOGLE_CLIENT_ID,
    #                 "client_secret": settings.GOOGLE_CLIENT_SECRET,
    #                 "auth_uri": settings.GOOGLE_AUTH_URI,
    #                 "token_uri": settings.GOOGLE_TOKEN_URI,
    #                 "redirect_uris": [settings.GOOGLE_REDIRECT_URI],
    #             }
    #         },
    #         scopes=self.scopes,
    #     )

    def create_flow(self) -> Flow:
        """
        Create Google OAuth Flow.
        """

        logging.debug("Log Credentials: ", settings.GOOGLE_CREDENTIALS_FILE)
        flow = Flow.from_client_secrets_file(
            settings.GOOGLE_CREDENTIALS_FILE,
            scopes=self.scopes,
        )

        flow.redirect_uri = settings.GOOGLE_REDIRECT_URI

        return flow

    def create_authorization_request(self):
        """
        Create Google authorization request.
        """

        flow = self.create_flow()

        authorization_url, state = flow.authorization_url(
            access_type="offline",
            include_granted_scopes="true",
            prompt="consent",
        )

        return authorization_url, state
