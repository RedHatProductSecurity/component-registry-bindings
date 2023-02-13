from enum import Enum


class NamespaceEnum(str, Enum):
    UPSTREAM = "UPSTREAM"
    REDHAT = "REDHAT"

    def __str__(self) -> str:
        return str(self.value)
