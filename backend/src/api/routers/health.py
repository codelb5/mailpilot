"""
Health check endpoints.
"""

from fastapi import APIRouter

from src.core.config import settings

router = APIRouter(
    prefix="/health",
    tags=["Health"],
)


@router.get("")
async def health_check():
    """
    Health check endpoint.
    """

    return {
        "status": "healthy",
        "application": settings.APP_NAME,
        "version": settings.APP_VERSION,
    }