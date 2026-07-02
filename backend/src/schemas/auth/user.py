"""
Authentication schemas.
"""

from pydantic import BaseModel, EmailStr, Field


class AuthUser(BaseModel):
    """
    Authenticated Google user.
    """

    email: EmailStr

    name: str = Field(
        ...,
        description="Google account display name",
    )

    picture: str | None = Field(
        default=None,
        description="Profile picture URL",
    )

    email_verified: bool = Field(
        default=False,
        description="Whether the email is verified by Google",
    )
