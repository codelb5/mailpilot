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

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


settings = Settings()
