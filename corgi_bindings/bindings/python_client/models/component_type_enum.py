from enum import Enum


class ComponentTypeEnum(str, Enum):
    CONTAINER_IMAGE = "CONTAINER_IMAGE"
    GOLANG = "GOLANG"
    MAVEN = "MAVEN"
    NPM = "NPM"
    RHEL_MODULE = "RHEL_MODULE"
    RPM = "RPM"
    SRPM = "SRPM"
    PYPI = "PYPI"
    UNKNOWN = "UNKNOWN"
    UPSTREAM = "UPSTREAM"

    def __str__(self) -> str:
        return str(self.value)
