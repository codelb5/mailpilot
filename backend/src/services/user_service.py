"""
User service.
"""

from src.database.repositories.user_repository import UserRepository
from src.models.users import User
from src.schemas.auth import AuthUser


class UserService:
    """
    Handles MailPilot user business logic.
    """

    def __init__(
        self,
        repository: UserRepository,
    ) -> None:

        self._repository = repository

    async def sync_google_user(
        self,
        auth_user: AuthUser,
    ) -> User:
        """
        Synchronize a Google authenticated user with MailPilot.
        """

        user = await self._repository.find_by_email(
            auth_user.email,
        )

        if user is None:

            user = User(
                email=auth_user.email,
                display_name=auth_user.name,
                profile_picture=auth_user.picture,
                email_verified=auth_user.email_verified,
            )

            return await self._repository.create(user)

        await self._repository.update_last_login(
            user.id,
        )

        updated_user = await self._repository.find_by_email(
            user.email,
        )

        if updated_user is None:
            raise RuntimeError("Failed to reload user after updating last login.")

        return updated_user
