"""
Business service dependencies.
"""

from fastapi import Depends

from src.api.dependencies.google import get_google_oauth
from src.api.dependencies.repositories import get_oauth_token_repository
from src.api.dependencies.security import get_encryption_service

from src.auth.google_oauth import GoogleOAuthService
from src.database.repositories import OAuthTokenRepository
from src.services.oauth_token_service import OAuthTokenService
from src.services.security.encryption_service import EncryptionService


def get_oauth_token_service(
    repository: OAuthTokenRepository = Depends(
        get_oauth_token_repository,
    ),
    encryption: EncryptionService = Depends(
        get_encryption_service,
    ),
    oauth: GoogleOAuthService = Depends(
        get_google_oauth,
    ),
) -> OAuthTokenService:

    return OAuthTokenService(
        repository=repository,
        encryption=encryption,
        oauth=oauth,
    )
