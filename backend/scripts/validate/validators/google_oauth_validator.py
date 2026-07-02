import json
from pathlib import Path

from src.auth.google_oauth import GoogleOAuth
from src.core.config import settings

from .base_validator import BaseValidator


class GoogleOAuthValidator(BaseValidator):

    @property
    def name(self) -> str:
        return "Google OAuth Validation"

    def validate(self):

        self.validate_configuration()

        self.validate_credentials_file()

        self.validate_credentials_json()

        self.validate_oauth_flow()

        self.validate_authorization_url()

    # --------------------------------------------------

    def validate_configuration(self):

        self.credentials_file = self.check_not_empty(
            "Credentials File",
            settings.GOOGLE_CREDENTIALS_FILE,
        )

        self.redirect_uri = self.check_not_empty(
            "Redirect URI",
            settings.GOOGLE_REDIRECT_URI,
        )

        self.scopes = self.check_not_empty(
            "Scopes",
            settings.GOOGLE_SCOPES,
        )

        print("Configuration Loaded\n")

    # --------------------------------------------------

    def validate_credentials_file(self):

        self.credentials_path = self.check(
            "Locate Credentials File",
            Path,
            self.credentials_file,
        )

        if not self.credentials_path.exists():

            raise FileNotFoundError(self.credentials_path)

        print(f"📄 {self.credentials_path.resolve()}\n")

    # --------------------------------------------------

    def validate_credentials_json(self):

        with open(
            self.credentials_path,
            "r",
            encoding="utf-8",
        ) as file:

            self.credentials = json.load(file)

        self.oauth_config = self.credentials.get("installed") or self.credentials.get(
            "web"
        )

        if self.oauth_config is None:

            raise RuntimeError(
                "credentials.json must contain either " "'installed' or 'web'"
            )

        print("OAuth Configuration\n")

        required = [
            "client_id",
            "client_secret",
            "auth_uri",
            "token_uri",
            "redirect_uris",
        ]

        for field in required:

            if field not in self.oauth_config:

                raise RuntimeError(f"{field} missing")

            print(f"   ✅ {field}")

        print()

    # --------------------------------------------------

    def validate_oauth_flow(self):

        self.oauth = self.check(
            "Initialize Google OAuth",
            GoogleOAuth,
        )

        self.flow = self.check(
            "Create OAuth Flow",
            self.oauth.create_flow,
        )

    # --------------------------------------------------

    def validate_authorization_url(self):

        url, state = self.check(
            "Generate Authorization URL",
            self.oauth.create_authorization_request,
        )

        print("Authorization URL")
        print("-" * 80)

        print(url)

        print()

        print("State")
        print("-" * 80)

        print(state)
