"""
OAuth Token service.
"""

# type.ignore
from datetime import datetime
from google.oauth2.credentials import Credentials

from src.auth.google_oauth import GoogleOAuthService
from src.database.repositories.oauth_token_repository import OAuthTokenRepository
from src.models.auth import OAuthToken
from src.models.users import User
from src.services.security.encryption_service import EncryptionService


class OAuthTokenService:
    """
    Handles persistence of OAuth credentials.
    """

    def __init__(
        self,
        repository: OAuthTokenRepository,
        encryption: EncryptionService,
        oauth: GoogleOAuthService,
    ) -> None:

        self._repository = repository
        self._encryption = encryption
        self._oauth = oauth

    def _encrypt(
        self,
        value: str | None,
    ) -> str | None:
        """
        Encrypt a sensitive value.
        """

        return self._encryption.encrypt(value)

    def _decrypt(
        self,
        value: str | None,
    ) -> str | None:
        """
        Decrypt a sensitive value.
        """

        return self._encryption.decrypt(value)

    def _build_oauth_token(
        self,
        user: User,
        credentials: Credentials,
    ) -> OAuthToken:

        return OAuthToken.build(
            user_id=user.id,
            access_token = self._encrypt(
                credentials.token,
            ),
            refresh_token=self._encrypt(
                credentials.refresh_token,
            ),
            expiry=credentials.expiry,
            scopes=credentials.scopes,
        )

    def _decrypt_oauth_token(
        self,
        *,
        token: OAuthToken,
    ) -> OAuthToken:
        """
        Decrypt an OAuth token.
        """

        return OAuthToken.build(
            user_id=token.user_id,
            provider=token.provider,
            access_token=self._decrypt(
                token.access_token,
            ),
            refresh_token=self._decrypt(
                token.refresh_token,
            ),
            expiry=token.expiry,
            scopes=token.scopes,
            token_type=token.token_type,
        )

    async def save_google_credentials(
        self,
        user: User,
        credentials: Credentials,
    ) -> OAuthToken:
        """
        Save Google OAuth credentials.
        """

        existing = await self._repository.find_by_provider(
            user_id=user.id,
            provider="google",
        )

        token = self._build_oauth_token(user=user, credentials=credentials)

        if existing is None:

            return await self._repository.create(
                token,
            )

        query_obj = {"_id": existing.id}
        update_obj = token.model_dump(exclude={"_id", "created_at"}, by_alias=True)

        await self._repository.update(query=query_obj, update=update_obj)

        saved_credentials = await self._repository.find_by_provider(
            user_id=user.id,
            provider="google",
        )

        if saved_credentials is None:
            raise RuntimeError("Failed to save OAuth credentials.")

        return saved_credentials

    async def get_google_credentials(
        self,
        *,
        user_id: str,
    ) -> Credentials:
        """
        Load Google OAuth credentials for a user.
        """

        token = await self._repository.find_by_provider(
            user_id=user_id,
            provider="google",
        )

        if token is None:
            raise ValueError("Google OAuth credentials not found.")

        token = self._decrypt_oauth_token(
            token=token,
        )

        return self._oauth.create_credentials(
            access_token=token.access_token,
            refresh_token=token.refresh_token,
            expiry=token.expiry,
            scopes=token.scopes,
        )

    async def delete_google_credentials(
        self,
        *,
        user_id: str,
    ) -> bool:
        """
        Delete stored Google OAuth credentials.
        """

        return await self._repository.delete_by_user_id(
            user_id=user_id,
        )
