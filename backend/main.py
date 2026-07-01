"""
Application entry point for MailPilot.
"""

import uvicorn

from src.api import create_app
from src.core.config import settings

app = create_app()

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG,
    )