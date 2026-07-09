from abc import ABC, abstractmethod
from time import perf_counter
from typing import Any, Callable
import asyncio


class AsyncBaseValidator(ABC):
    """
    Base class for all validators.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """
        Display name of the validator.
        """
        ...

    def step(self, message: str) -> None:
        print(f"→ {message}")

    def success(self, message: str) -> None:
        print(f"✓ {message}")

    @abstractmethod
    async def validate(self) -> None:
        """
        Execute all validation steps.
        """
        ...

    # --------------------------------------------------
    # Validation Helpers
    # --------------------------------------------------

    def check(
        self,
        description: str,
        func: Callable[..., Any],
        *args,
        **kwargs,
    ) -> Any:
        """
        Execute a validation step.
        """

        print(f"🔍 {description}")

        try:

            result = func(*args, **kwargs)

            print("   ✅ Passed\n")

            return result

        except Exception as ex:

            print("   ❌ Failed\n")

            raise RuntimeError(f"{description} failed.\n{ex}") from ex

    def check_not_empty(
        self,
        description: str,
        value: Any,
    ) -> Any:
        """
        Ensure a configuration value exists.
        """

        print(f"🔍 {description}")

        if value is None:
            raise RuntimeError(f"{description} is None")

        if isinstance(value, str) and not value.strip():
            raise RuntimeError(f"{description} is empty")

        print("   ✅ Passed\n")

        return value

    # --------------------------------------------------
    # Runner
    # --------------------------------------------------

    def run(self) -> bool:

        print("\n")
        print("=" * 80)
        print(self.name)
        print("=" * 80)

        start = perf_counter()

        try:

            asyncio.run(self.validate())

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

            print(ex)

            print(f"\nDuration : {duration:.2f} ms")

            return False
