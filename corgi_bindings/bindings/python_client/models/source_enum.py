from enum import Enum


class SourceEnum(str, Enum):
    DEFAULT = "default"
    PREVIOUS_RELEASE = "previous_release"
    PRP = "prp"
    CONFIRMED = "confirmed"
    OVERRIDE = "override"

    def __str__(self) -> str:
        return str(self.value)
