"""
User Repository validator.
"""

from uuid import uuid4

from src.database.mongodb import MongoManager
from src.database.repositories.user_repository import UserRepository
from src.models.users import User

from .async_base_validator import AsyncBaseValidator


class UserRepositoryValidator(AsyncBaseValidator):
    """
    Validate UserRepository CRUD operations.
    """

    @property
    def name(self) -> str:
        return "User Repository Validation"

    async def validate(self) -> None:

        await MongoManager.connect()

        database = MongoManager.get_database()

        repository = UserRepository(database)

        email = f"test-{uuid4().hex[:8]}@mailpilot.dev"

        user = User(
            email=email,
            display_name="Test User",
        )

        try:

            self.step("Creating User...")

            created_user = await repository.create(user)

            assert created_user.id == user.id

            self.success("✓ User Created")

            self.step("Finding User...")

            loaded_user = await repository.find_by_email(
                email=user.email,
            )

            assert loaded_user is not None
            assert loaded_user.email == user.email
            assert loaded_user.display_name == user.display_name

            self.success("✓ User Retrieved")

            self.step("Checking User Exists...")

            exists = await repository.exists(
                {
                    "email": user.email,
                }
            )

            assert exists is True

            self.success("✓ User Exists")

            self.step("Updating Last Login...")

            previous_login = loaded_user.last_login_at

            updated = await repository.update_last_login(
                user.id,
            )

            assert updated is True

            refreshed_user = await repository.find_by_email(
                user.email,
            )

            assert refreshed_user is not None
            assert refreshed_user.last_login_at > previous_login

            self.success("✓ Last Login Updated")

            self.step("Counting Users...")

            count = await repository.count({})

            assert count > 0

            self.success(f"✓ User Count: {count}")

        finally:

            self.step("Cleaning Up...")

            await repository.delete(
                {
                    "_id": user.id,
                }
            )

            deleted_user = await repository.find_by_email(
                user.email,
            )

            assert deleted_user is None

            self.success("✓ User Deleted")

            await MongoManager.disconnect()
