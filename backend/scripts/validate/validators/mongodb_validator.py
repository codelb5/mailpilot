from src.database.mongodb import MongoManager

from .async_base_validator import AsyncBaseValidator


class MongoDBValidator(AsyncBaseValidator):

    @property
    def name(self) -> str:
        return "MongoDB Validation"

    async def validate(self) -> None:
        
        self.step("Connecting to database..!")

        await MongoManager.connect()

        db = MongoManager.get_database()

        await db.command("ping")

        self.success(f"Connected to database: {db.name}")

        await MongoManager.disconnect()
