from enum import Enum


class V1BuildsListType(str, Enum):
    BREW = "BREW"
    KOJI = "KOJI"
    PNC = "PNC"

    def __str__(self) -> str:
        return str(self.value)
