from fastapi import Depends
from motor.motor_asyncio import AsyncIOMotorDatabase

from src.api.dependencies.database import get_database
from src.database.repositories.user_repository import (
    UserRepository,
)


def get_user_repository(
    database: AsyncIOMotorDatabase = Depends(get_database),
) -> UserRepository:
    """
    Return a UserRepository instance.
    """

    return UserRepository(database)
