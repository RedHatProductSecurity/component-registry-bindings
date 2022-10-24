from typing import Dict, List

CORGI_API_VERSION: str = "v1"
CORGI_BINDINGS_USERAGENT: str = "corgi-bindings-1.0.0"
CORGI_BINDINGS_API_PATH: str = f".bindings.python_client.api.{CORGI_API_VERSION}"

# all available session operations
ALL_SESSION_OPERATIONS: List[str] = (
    "retrieve",
    "update",
    "list",
    "create",
    "destroy",
    "search",
)

# mapping for resources which model names are different from the endpoint name
RESOURCE_TO_MODEL_MAPPING: Dict[str, str] = {
    "lifecycles": "AppStreamLifeCycle",
    "components": "ComponentDetail",
    "builds": "SoftwareBuild",
}
