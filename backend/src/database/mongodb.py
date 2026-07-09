"""
MongoDB Connection Manager.
"""

from motor.motor_asyncio import (
    AsyncIOMotorClient,
    AsyncIOMotorDatabase,
)

from src.core.config import settings


class MongoManager:
    """
    Manages the application's MongoDB connection.
    """

    _client: AsyncIOMotorClient | None = None

    _database: AsyncIOMotorDatabase | None = None

    @classmethod
    async def connect(cls) -> None:
        """
        Establish MongoDB connection.
        """

        if cls._client is not None:
            return

        cls._client = AsyncIOMotorClient(
            settings.MONGODB_URI,
        )

        cls._database = cls._client[settings.MONGODB_DATABASE]

    @classmethod
    async def disconnect(cls) -> None:
        """
        Close MongoDB connection.
        """

        if cls._client is None:
            return

        cls._client.close()

        cls._client = None
        cls._database = None

    @classmethod
    def get_database(
        cls,
    ) -> AsyncIOMotorDatabase:
        """
        Return the active database.
        """

        if cls._database is None:
            raise RuntimeError("MongoDB connection has not been initialized.")

        return cls._database
