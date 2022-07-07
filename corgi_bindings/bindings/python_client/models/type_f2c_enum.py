from enum import Enum


class TypeF2CEnum(str, Enum):
    BREW = "BREW"
    PNC = "PNC"
    KOJI = "KOJI"

    def __str__(self) -> str:
        return str(self.value)
