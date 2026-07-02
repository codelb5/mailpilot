"""
OAuth token domain model.
"""

from datetime import datetime

from pydantic import Field

from src.models.common import DomainModel


class OAuthToken(DomainModel):
    """
    OAuth token for an external provider.
    """

    user_id: str

    provider: str = "google"

    access_token: str

    refresh_token: str | None = None

    expiry: datetime | None = None

    scopes: list[str] = Field(default_factory=list)
