"""
Base domain model.
"""

from datetime import UTC, datetime
from uuid import uuid4

from pydantic import BaseModel, ConfigDict, Field


class DomainModel(BaseModel):
    """
    Base class for all MailPilot domain models.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        extra="ignore",
        validate_assignment=True,
    )

    id: str = Field(
        default_factory=lambda: str(uuid4()),
        alias="_id",
    )

    created_at: datetime = Field(
        default_factory=lambda: datetime.now(UTC),
    )

    updated_at: datetime = Field(
        default_factory=lambda: datetime.now(UTC),
    )
