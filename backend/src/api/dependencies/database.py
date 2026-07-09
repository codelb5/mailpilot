from motor.motor_asyncio import AsyncIOMotorDatabase

from src.database.mongodb import MongoManager


def get_database() -> AsyncIOMotorDatabase:
    """
    Returns the active Mongo database.
    """

    return MongoManager.get_database()