from src.services.security.encryption_service import EncryptionService


def get_encryption_service() -> EncryptionService:
    """
    Returns the crypto service.
    """

    return EncryptionService()
