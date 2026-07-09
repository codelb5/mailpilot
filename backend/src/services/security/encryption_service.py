"""
Encryption service.
"""

from cryptography.fernet import Fernet, InvalidToken

from src.core.config import settings


class EncryptionService:
    """
    Handles encryption and decryption of sensitive values.
    """

    def __init__(self) -> None:
        self._cipher = Fernet(settings.CRYPTO_KEY.encode())

    def encrypt(
        self,
        value: str | None,
    ) -> str | None:
        """
        Encrypt a string.

        Args:
            value: Plain text value.

        Returns:
            Encrypted value, or None if the input is None.
        """

        if value is None:
            return None

        return self._cipher.encrypt(value.encode("utf-8")).decode("utf-8")

    def decrypt(
        self,
        value: str | None,
    ) -> str | None:
        """
        Decrypt an encrypted string.

        Args:
            value: Encrypted value.

        Returns:
            Plain text value, or None if the input is None.

        Raises:
            ValueError: If the encrypted value is invalid.
        """

        if value is None:
            return None

        try:
            return self._cipher.decrypt(value.encode("utf-8")).decode("utf-8")

        except InvalidToken as ex:
            raise ValueError("Invalid encrypted value.") from ex
