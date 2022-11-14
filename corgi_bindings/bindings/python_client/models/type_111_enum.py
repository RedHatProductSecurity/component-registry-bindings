from enum import Enum


class Type111Enum(str, Enum):
    BREW = "BREW"
    KOJI = "KOJI"

    def __str__(self) -> str:
        return str(self.value)
