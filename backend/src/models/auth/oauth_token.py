"""
OAuth Token domain model.
"""

from datetime import UTC, datetime

from pydantic import Field

from src.models.common import DomainModel


class OAuthToken(DomainModel):
    """
    Represents OAuth credentials stored by MailPilot.
    """

    user_id: str

    provider: str = "google"

    access_token: str

    refresh_token: str | None = None

    expiry: datetime | None = None

    scopes: list[str] = Field(default_factory=list)

    token_type: str = "Bearer"

    @property
    def is_expired(self) -> bool:
        """
        Returns whether the access token has expired.
        """

        if self.expiry is None:
            return False

        return self.expiry <= datetime.now(UTC)

    @classmethod
    def build(
        cls,
        *,
        user_id: str,
        access_token: str,
        refresh_token: str | None,
        expiry: datetime | None,
        scopes: list[str] | None,
        provider: str = "google",
        token_type: str = "Bearer",
    ) -> "OAuthToken":
        """
        Create an OAuthToken domain model.
        """

        return cls(
            user_id=user_id,
            provider=provider,
            access_token=access_token,
            refresh_token=refresh_token,
            expiry=expiry,
            scopes=scopes or [],
            token_type=token_type,
        )
