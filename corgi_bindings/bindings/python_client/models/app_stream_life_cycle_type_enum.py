from enum import Enum


class AppStreamLifeCycleTypeEnum(str, Enum):
    MODULE = "module"
    PACKAGE = "package"
    SCL = "scl"

    def __str__(self) -> str:
        return str(self.value)
