"""
Google OAuth service.
"""

import json
from datetime import datetime
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
        self._client_config = self._load_client_config()

    def _load_client_config(
        self,
    ):
        with open(
            settings.GOOGLE_CREDENTIALS_FILE,
            encoding="utf-8",
        ) as file:

            credentials = json.load(file)

        return credentials["web"]

    def create_flow(self) -> Flow:
        """
        Create Google OAuth Flow.
        """

        # flow = Flow.from_client_secrets_file(
        #     client_secrets_file=settings.GOOGLE_CREDENTIALS_FILE,
        #     scopes=self.scopes,
        #     autogenerate_code_verifier=True,
        # )
        flow = Flow.from_client_config(
            client_config={
                "web": self._client_config,
            },
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

    def create_credentials(
        self,
        *,
        access_token: str,
        refresh_token: str | None,
        expiry: datetime | None,
        scopes: list[str],
    ) -> Credentials:
        """
        Create Google Credentials from stored OAuth data.
        """

        return Credentials(
            token=access_token,
            refresh_token=refresh_token,
            token_uri=self._client_config["token_uri"],
            client_id=self._client_config["client_id"],
            client_secret=self._client_config["client_secret"],
            scopes=scopes,
            expiry=expiry,
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
