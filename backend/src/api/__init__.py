from fastapi import FastAPI

from src.api.middleware import log_requests
from src.api.routers.health import router as health_router
from src.core.config import settings
from src.core.logging import setup_logging


def create_app() -> FastAPI:
    """
    Create and configure the FastAPI application.
    """

    setup_logging()

    app = FastAPI(
        title=settings.APP_NAME,
        version=settings.APP_VERSION,
        debug=settings.DEBUG,
    )

    app.middleware("http")(log_requests)

    app.include_router(health_router)

    return app
