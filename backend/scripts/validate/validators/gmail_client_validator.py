"""
Validate GmailClient.
"""

from google.oauth2.credentials import Credentials

from src.models.users import User
from src.core.config import settings

from scripts.validate.dependencies import Dependencies
from scripts.validate.validators import AsyncBaseValidator


class GmailClientValidator(AsyncBaseValidator):
    """
    Validates GmailClient.
    """

    def __init__(self, deps: Dependencies) -> None:

        self._deps = deps

    @property
    def name(self) -> str:
        """
        Display name of the validator.
        """

        return "Gmail Client"

    async def _get_user(self) -> User:
        """
        Get the validator user.
        """

        user = await self._deps.user_service.get_by_email(
            email=settings.VALIDATOR_GOOGLE_EMAIL
        )

        assert (
            user is not None
        ), f"User {settings.VALIDATOR_GOOGLE_EMAIL} was not found!"

        return user

    async def _get_google_credentials(
        self,
        user: User,
    ):
        """
        Load Google credentials.
        """

        return await self._deps.oauth_token_service.get_google_credentials(
            user_id=user.id
        )

    def _get_profile(
        self,
        credentials: Credentials,
    ):
        """
        Get Gmail profile.
        """
        return self._deps.gmail_client.get_profile(credentials=credentials)

    def _verify_profile(
        self,
        user: User,
        profile: dict,
    ):
        """
        Verify Gmail profile.
        """

        assert profile["emailAddress"] == user.email

        assert profile.get("messagesTotal") is not None
        assert profile.get("threadsTotal") is not None

    async def validate(self) -> None:
        """
        Validate GmailClient.
        """

        self.section("Arrange")

        user = await self.check_async(description="Loading User", func=self._get_user)
        credentials = await self.check_async(
            description="Loading Google Credentials",
            func=self._get_google_credentials,
            user=user,
        )

        self.section("Act")

        profile = self.check(
            description="Fetching Gmail Profile",
            func=self._get_profile,
            credentials=credentials,
        )

        self.section("Verify")

        self.check(
            description="Verifying Gmail Profile",
            func=self._verify_profile,
            user=user,
            profile=profile
        )
