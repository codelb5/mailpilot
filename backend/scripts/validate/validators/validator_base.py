from abc import ABC, abstractmethod
from typing import Any, Callable


class ValidatorBase(ABC):
    # ==================================================
    # Metadata
    # ==================================================

    @property
    @abstractmethod
    def name(self) -> str:
        """
        Display name of the validator.
        """
        ...

    # ==================================================
    # Logging Helpers
    # ==================================================

    def section(self, title: str) -> None:
        """
        Print a validation section.
        """

        print()
        print("-" * 60)
        print(title)
        print("-" * 60)

    def step(self, message: str) -> None:
        print(f"→ {message}")

    def success(self, message: str) -> None:
        print(f"✓ {message}")

    # ==================================================
    # Validation Helpers
    # ==================================================

    def check(
        self,
        description: str,
        func: Callable[..., Any],
        *args,
        **kwargs,
    ) -> Any:
        """
        Execute a synchronous validation step.
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

    # ==================================================
    # Assertion Helpers
    # ==================================================

    def assert_equal(
        self,
        actual: Any,
        expected: Any,
        message: str,
    ) -> None:
        """
        Assert two values are equal.
        """

        if actual != expected:
            raise AssertionError(
                f"{message}\n" f"Expected: {expected}\n" f"Actual  : {actual}"
            )

    def assert_not_none(
        self,
        value: Any,
        message: str,
    ) -> None:
        """
        Assert a value is not None.
        """

        if value is None:
            raise AssertionError(message)

    def assert_true(
        self,
        condition: bool,
        message: str,
    ) -> None:
        """
        Assert a condition is True.
        """

        if not condition:
            raise AssertionError(message)
