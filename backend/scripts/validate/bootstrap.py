"""
Validator bootstrap utilities.
"""

from motor.motor_asyncio import AsyncIOMotorDatabase

from src.database.mongodb import MongoManager
from src.database.repositories import (
    OAuthTokenRepository,
    UserRepository,
)
from src.services.security.encryption_service import EncryptionService
from src.auth.google_oauth import GoogleOAuthService
from src.services.oauth_token_service import OAuthTokenService
from src.services.user_service import UserService

from .dependencies import Dependencies
from .validators.async_base_validator import AsyncBaseValidator


async def create_mongo_manager() -> MongoManager:
    """
    Create a MongoDB database connection.
    """

    manager = MongoManager()

    await manager.connect()

    return manager


def build_dependencies(manager: MongoManager) -> Dependencies:
    """
    Create validator dependencies.
    """

    database = manager.get_database()

    #
    # Repositories
    #
    user_repository = UserRepository(database)

    oauth_token_repository = OAuthTokenRepository(
        database,
    )

    #
    # Infrastructure Services
    #
    encryption_service = EncryptionService()

    google_oauth_service = GoogleOAuthService()

    #
    # Business Services
    #
    user_service = UserService(
        repository=user_repository,
    )

    oauth_token_service = OAuthTokenService(
        repository=oauth_token_repository,
        encryption=encryption_service,
        oauth=google_oauth_service,
    )

    return Dependencies(
        database=database,
        user_repository=user_repository,
        oauth_token_repository=oauth_token_repository,
        encryption_service=encryption_service,
        google_oauth_service=google_oauth_service,
        user_service=user_service,
        oauth_token_service=oauth_token_service,
    )
