from abc import ABC, abstractmethod
from time import perf_counter
from typing import Any, Callable


from .validator_base import ValidatorBase


class BaseValidator(ValidatorBase):
    """
    Base class for all validators.
    """

    @abstractmethod
    def validate(self) -> None:
        """
        Execute all validation steps.
        """
        pass
    
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

            self.validate()

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
