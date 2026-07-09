"""
Base MongoDB repository.
"""

from typing import Any, Generic, TypeVar
from datetime import datetime, UTC
from collections.abc import Mapping
from pydantic import BaseModel
from motor.motor_asyncio import (
    AsyncIOMotorCollection,
    AsyncIOMotorDatabase,
)

ModelType = TypeVar("ModelType", bound=BaseModel)

from .types import MongoQuery, MongoUpdate


class BaseRepository(Generic[ModelType]):
    """
    Base repository for MongoDB collections.
    """

    def __init__(
        self,
        database: AsyncIOMotorDatabase,
        collection_name: str,
        model: type[ModelType],
    ) -> None:

        self._model = model

        self._database = database

        self._collection: AsyncIOMotorCollection = database[collection_name]

    async def create(self, model: ModelType) -> ModelType:
        """
        Insert one document.
        """

        await self._collection.insert_one(
            model.model_dump(by_alias=True, mode="python")
        )

        return model

    async def find_one(
        self,
        query: MongoQuery,
    ) -> ModelType | None:
        """
        Find a single document.
        """

        document = await self._collection.find_one(query)

        if document is None:
            return None

        return self._model.model_validate(document)

    async def find_many(
        self,
        query: MongoQuery,
    ) -> list[ModelType]:
        """
        Find multiple documents.
        """

        documents = []

        async for document in self._collection.find(query):

            documents.append(self._model.model_validate(document))

        return documents

    async def update(
        self,
        query: MongoQuery,
        update: MongoUpdate,
    ) -> bool:
        """
        Update one document.
        """

        update["updated_at"] = datetime.now(UTC)

        result = await self._collection.update_one(
            query,
            {
                "$set": update,
            },
        )

        return result.modified_count > 0

    async def delete(
        self,
        query: MongoQuery,
    ) -> bool:
        """
        Delete one document.
        """

        result = await self._collection.delete_one(
            query,
        )

        return result.deleted_count > 0

    async def exists(
        self,
        query: MongoQuery,
    ) -> bool:
        """
        Check whether a document exists.
        """

        return await self.find_one(query) is not None

    async def count(
        self,
        query: MongoQuery,
    ) -> int:
        """
        Count documents.
        """

        return await self._collection.count_documents(query)
