"""
MailPilot user domain model.
"""

from datetime import UTC, datetime

from pydantic import EmailStr, HttpUrl, Field

from src.models.common import DomainModel


class User(DomainModel):
    """
    MailPilot user.
    """

    email: EmailStr

    display_name: str

    profile_picture: HttpUrl | None = None

    email_verified: bool = False

    provider: str = "google"

    last_login_at: datetime = Field(
        default_factory=lambda: datetime.now(UTC),
    )
