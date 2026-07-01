"""
FastAPI application factory.
"""

from fastapi import FastAPI

from src.core.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
)
