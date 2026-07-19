"""
Base validator for asynchronous validation.
"""

from __future__ import annotations
import traceback
from abc import abstractmethod
from time import perf_counter
from typing import Any, Awaitable, Callable

from .validator_base import ValidatorBase


class AsyncBaseValidator(ValidatorBase):
    """
    Base class for all asynchronous validators.
    """

    @abstractmethod
    async def validate(self) -> None:
        """
        Execute all validation steps.
        """
        ...

    async def check_async(
        self,
        description: str,
        func: Callable[..., Awaitable[Any]],
        *args,
        **kwargs,
    ) -> Any:
        """
        Execute an asynchronous validation step.
        """

        print(f"🔍 {description}")

        try:
            result = await func(*args, **kwargs)

            print("   ✅ Passed\n")

            return result

        except Exception as ex:
            print("   ❌ Failed\n")
            raise RuntimeError(f"{description} failed.\n{ex}") from ex

    # ==================================================
    # Runner
    # ==================================================

    async def run(self) -> bool:
        """
        Execute the validator.
        """

        print()
        print("=" * 80)
        print(self.name)
        print("=" * 80)

        start = perf_counter()

        try:
            await self.validate()

            duration = (perf_counter() - start) * 1000

            print("=" * 80)
            print(f"✅ Validation Successful ({duration:.2f} ms)")
            print("=" * 80)

            return True

        except Exception as ex:

            duration = (perf_counter() - start) * 1000

            print("=" * 80)
            print("❌ Validation Failed")
            print("=" * 80)

            # print(ex)
            traceback.print_exc()
            print()
            print(repr(ex))

            print(f"\nDuration: {duration:.2f} ms")

            return False
