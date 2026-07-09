from google.oauth2.credentials import Credentials


from .async_base_validator import AsyncBaseValidator
from src.models.users import User
from src.schemas.auth import AuthUser
from scripts.validate.dependencies import Dependencies

# type: ignore


class OAuthTokenServiceValidator(AsyncBaseValidator):

    def __init__(self, deps: Dependencies) -> None:
        self._deps = deps

    @property
    def name(self) -> str:
        """
        Display name of the validator.
        """

        return "OAuthTokenService"

    async def _create_test_user(
        self,
    ) -> User:
        """
        Create a test user.
        """

        auth_user = self._build_test_profile()

        return await self._deps.user_service.sync_google_user(
            auth_user=auth_user,
        )

    def _build_test_credentials(
        self,
    ) -> Credentials:
        """
        Build test Google credentials.
        """

        return Credentials(
            token="test-access-token",
            refresh_token="test-refresh-token",
            token_uri="https://oauth2.googleapis.com/token",
            client_id="test-client-id",
            client_secret="test-client-secret",
            scopes=[
                "https://www.googleapis.com/auth/gmail.modify",
            ],
        )

    def _build_test_profile(
        self,
    ) -> AuthUser:
        """
        Build a test Google user profile.
        """

        return AuthUser(
            email="oauth-validator@mailpilot.com",
            name="OAuth Validator",
            picture=None,
            email_verified=True,
        )

    async def _save_credentials(
        self,
        *,
        user: User,
        credentials: Credentials,
    ) -> None:
        """
        Save credentials.
        """
        await self._deps.oauth_token_service.save_google_credentials(
            user=user, credentials=credentials
        )

    async def _verify_encrypted_storage(
        self,
        *,
        user: User,
        credentials: Credentials,
    ) -> None:
        """
        Verify encrypted storage.
        """

        filter = {"user_id": user.id, "provider": user.provider}
        document = await self._deps.database["oauth_tokens"].find_one()

        assert document is not None

        assert document["access_token"] != credentials.token

        assert document["refresh_token"] != credentials.refresh_token

    async def _verify_loaded_credentials(
        self,
        *,
        user: User,
        credentials: Credentials,
    ) -> None:
        """
        Verify reconstructed credentials.
        """

        loaded_credentials = (
            await self._deps.oauth_token_service.get_google_credentials(
                user_id=user.id,
            )
        )

        assert loaded_credentials.token == credentials.token, "Access token mismatch"

        assert (
            loaded_credentials.refresh_token == credentials.refresh_token
        ), "Refresh token mismatch"

        assert loaded_credentials.scopes == credentials.scopes, "Scopes mismatch"

    async def _cleanup(
        self,
        *,
        user: User,
    ) -> None:
        """
        Remove validator data.
        """

        #
        # Delete OAuth Token
        #
        deleted = await self._deps.oauth_token_service.delete_google_credentials(
            user_id=user.id,
        )

        assert deleted, "Failed to delete OAuth token."

        #
        # Verify OAuth Token Deletion
        #
        token = await self._deps.oauth_token_repository.find_by_provider(
            user_id=user.id,
            provider="google",
        )

        assert token is None, "OAuth token still exists after deletion."

        #
        # Delete User
        #
        delete_query = {"_id": user.id}
        deleted = await self._deps.user_repository.delete(query=delete_query)

        assert deleted, "Failed to delete test user."

        #
        # Verify User Deletion
        #
        user_email = await self._deps.user_repository.find_by_email(email=user.email)

        assert user_email is None, "Test user still exists after deletion."

    async def validate(self) -> None:

        user = await self._create_test_user()

        credentials = self._build_test_credentials()

        await self._save_credentials(
            user=user,
            credentials=credentials,
        )

        await self._verify_encrypted_storage(
            user=user,
            credentials=credentials,
        )

        await self._verify_loaded_credentials(
            user=user,
            credentials=credentials,
        )

        await self._cleanup(
            user=user,
        )

        return None
