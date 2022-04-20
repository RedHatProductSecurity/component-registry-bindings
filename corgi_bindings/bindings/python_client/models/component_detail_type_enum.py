from enum import Enum


class ComponentDetailTypeEnum(str, Enum):
    CONTAINER_IMAGE = "CONTAINER_IMAGE"
    MAVEN = "MAVEN"
    NPM = "NPM"
    RHEL_MODULE = "RHEL_MODULE"
    RPM = "RPM"
    SRPM = "SRPM"
    UNKNOWN = "UNKNOWN"
    UPSTREAM = "UPSTREAM"

    def __str__(self) -> str:
        return str(self.value)
