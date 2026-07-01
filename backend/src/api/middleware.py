"""
Application middleware.
"""

import time

from fastapi import Request

from src.core.logging import get_logger

logger = get_logger(__name__)


async def log_requests(request: Request, call_next):
    """
    Log every incoming request.
    """

    start_time = time.time()

    response = await call_next(request)

    duration = round((time.time() - start_time) * 1000, 2)

    logger.info(
        "%s %s | %s | %.2f ms",
        request.method,
        request.url.path,
        response.status_code,
        duration,
    )

    return response
