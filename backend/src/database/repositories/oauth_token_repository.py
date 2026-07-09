from datetime import datetime, UTC
from motor.motor_asyncio import AsyncIOMotorDatabase


from .base_repository import BaseRepository
from src.models.auth import OAuthToken


class OAuthTokenRepository(BaseRepository[OAuthToken]):

    COLLECTION_NAME = "oauth_tokens"

    def __init__(
        self,
        database: AsyncIOMotorDatabase,
    ) -> None:
        super().__init__(
            database=database, collection_name=self.COLLECTION_NAME, model=OAuthToken
        )

    async def find_by_user_id(self, user_id: str) -> OAuthToken | None:

        query = {"user_id": user_id}

        return await self.find_one(query=query)

    async def find_by_provider(
        self,
        user_id: str,
        provider: str,
    ) -> OAuthToken | None:

        query = {
            "user_id": user_id,
            "provider": provider,
        }

        return await self.find_one(query=query)

    async def update_tokens(
        self,
        user_id: str,
        access_token: str,
        refresh_token: str | None,
        expiry: datetime | None,
    ) -> bool:

        query = {
            "user_id": user_id,
        }
        update_obj = {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "expiry": expiry,
        }

        return await self.update(query=query, update=update_obj)

    async def delete_by_user_id(
        self,
        user_id: str,
    ) -> bool:

        query = {
            "user_id": user_id,
        }

        return await self.delete(query=query)
