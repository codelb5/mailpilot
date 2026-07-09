"""
FastAPI application factory.
"""

from fastapi import FastAPI
from contextlib import asynccontextmanager

from src.core.config import settings
from src.database.mongodb import MongoManager


@asynccontextmanager
async def lifespan(app: FastAPI):

    await MongoManager.connect()

    yield

    await MongoManager.disconnect()


app = FastAPI(title=settings.APP_NAME, version=settings.APP_VERSION, lifespan=lifespan)
