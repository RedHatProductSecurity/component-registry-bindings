from enum import Enum


class V1ComponentsListType(str, Enum):
    CONTAINER_IMAGE = "CONTAINER_IMAGE"
    GOLANG = "GOLANG"
    MAVEN = "MAVEN"
    NPM = "NPM"
    PYPI = "PYPI"
    RHEL_MODULE = "RHEL_MODULE"
    RPM = "RPM"
    SRPM = "SRPM"
    UNKNOWN = "UNKNOWN"
    UPSTREAM = "UPSTREAM"

    def __str__(self) -> str:
        return str(self.value)
