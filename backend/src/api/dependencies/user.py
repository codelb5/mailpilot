from fastapi import Depends

from src.api.dependencies.repositories import (
    get_user_repository,
)
from src.database.repositories.user_repository import UserRepository
from src.services.user_service import UserService


def get_user_service(
    repository: UserRepository = Depends(
        get_user_repository,
    ),
) -> UserService:
    """
    Returns a UserService instance.
    """

    return UserService(repository)
