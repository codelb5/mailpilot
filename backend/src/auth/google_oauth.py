"""
Google OAuth service.
"""

from google_auth_oauthlib.flow import Flow
from google.oauth2.credentials import Credentials

from src.core.config import settings
from src.models.auth import AuthorizationRequest


class GoogleOAuthService:
    """
    Handles Google OAuth authentication.
    """

    def __init__(self):

        self.scopes = [scope.strip() for scope in settings.GOOGLE_SCOPES.split(",")]
        # print("Google Self Scopes:", self.scopes)

    def create_flow(self) -> Flow:
        """
        Create Google OAuth Flow.
        """

        flow = Flow.from_client_secrets_file(
            client_secrets_file=settings.GOOGLE_CREDENTIALS_FILE,
            scopes=self.scopes,
            autogenerate_code_verifier=True,
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

        return AuthorizationRequest(
            url=authorization_url,
            state=state,
            code_verifier=flow.code_verifier,
        )

    def exchange_code(
        self,
        code: str,
        code_verifier: str,
    ) -> Credentials:

        flow = self.create_flow()

        flow.code_verifier = code_verifier

        flow.fetch_token(code=code)

        return flow.credentials
