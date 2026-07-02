"""
Application configuration.

All application settings should be defined here.
Environment variables are loaded from the .env file.
"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Global application settings.
    """

    APP_NAME: str = "MailPilot"
    APP_VERSION: str = "0.1.0"
    DEBUG: bool = True
    HOST: str = "0.0.0.0"
    PORT: int = 8000

    # Google OAuth
    GOOGLE_CREDENTIALS_FILE: str
    GOOGLE_REDIRECT_URI: str
    GOOGLE_SCOPES: str

    # MongoDB URI
    MONGODB_URI: str
    MONGODB_DATABASE: str

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


settings = Settings()
