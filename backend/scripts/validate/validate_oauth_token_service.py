import asyncio


from .bootstrap import (
    build_dependencies,
    create_mongo_manager,
)
from .validators.oauth_token_service_validator import OAuthTokenServiceValidator


async def main():
    manager = await create_mongo_manager()

    try:
        deps = build_dependencies(manager)

        validator = OAuthTokenServiceValidator(deps=deps)

        await validator.validate()

    finally:
        await manager.disconnect()


if __name__ == "__main__":
    asyncio.run(main())
