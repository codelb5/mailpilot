"""
Validate Gmail Cient
"""

import asyncio

from .bootstrap import build_dependencies, create_mongo_manager
from .validators.gmail_client_validator import GmailClientValidator


async def main():

    manager = await create_mongo_manager()

    try:
        deps = build_dependencies(manager=manager)

        validator = GmailClientValidator(deps=deps)

        await validator.run()

    finally:
        await manager.disconnect()


if __name__ == "__main__":
    asyncio.run(main())
