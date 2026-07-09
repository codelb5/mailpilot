"""
Shared validator dependencies.
"""

from dataclasses import dataclass

from motor.motor_asyncio import AsyncIOMotorDatabase

from src.database.repositories import (
    OAuthTokenRepository,
    UserRepository,
)
from src.services.security.encryption_service import EncryptionService
from src.auth.google_oauth import GoogleOAuthService
from src.services.oauth_token_service import OAuthTokenService
from src.services.user_service import UserService


@dataclass(slots=True)
class Dependencies:
    """
    Shared dependencies used by validator scripts.
    """

    database: AsyncIOMotorDatabase

    #
    # Repositories
    #
    user_repository: UserRepository
    oauth_token_repository: OAuthTokenRepository

    #
    # Infrastructure Services
    #
    encryption_service: EncryptionService
    google_oauth_service: GoogleOAuthService

    #
    # Business Services
    #
    user_service: UserService
    oauth_token_service: OAuthTokenService
