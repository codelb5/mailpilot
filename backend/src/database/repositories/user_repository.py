"""
User repository.
"""

from datetime import datetime, UTC
from motor.motor_asyncio import AsyncIOMotorDatabase


from .base_repository import BaseRepository
from src.models.users import User


class UserRepository(BaseRepository[User]):
    """
    Repository for MailPilot users.
    """

    COLLECTION_NAME = "users"

    def __init__(
        self,
        database: AsyncIOMotorDatabase,
    ) -> None:

        super().__init__(
            database=database, collection_name=self.COLLECTION_NAME, model=User
        )

    async def find_by_email(
        self,
        email: str,
    ) -> User | None:
        """
        Find user by email.
        """

        return await self.find_one(
            {
                "email": email,
            }
        )

    async def update_last_login(
        self,
        userid: str,
    ) -> bool:
        """
        Update user's last login.
        """

        now = datetime.now(UTC)

        return await self.update(
            {
                "id": userid,
            },
            {"last_login_at": now},
        )
