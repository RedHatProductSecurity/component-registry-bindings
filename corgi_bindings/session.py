import importlib
from types import ModuleType
from typing import Any, Callable, Dict, List, Union

from .bindings.python_client import AuthenticatedClient, models
from .bindings.python_client.types import UNSET
from .constants import (
    ALL_SESSION_OPERATIONS,
    CORGI_API_VERSION,
    CORGI_BINDINGS_API_PATH,
    CORGI_BINDINGS_USERAGENT,
    RESOURCE_TO_MODEL_MAPPING,
)

corgi_status_retrieve = importlib.import_module(
    f"{CORGI_BINDINGS_API_PATH}.{CORGI_API_VERSION}_status_retrieve",
    package="corgi_bindings",
)


class OperationUnsupported(Exception):
    """Session operation is unsupported exception"""

    pass


def get_sync_function(api_module: ModuleType) -> Callable:
    """
    Get 'sync' function from API module if available (response example is defined in schema)
    or get basic 'sync_detailed' function (response example is not defined in schema)
    """
    return getattr(api_module, "sync", getattr(api_module, "sync_detailed"))


def new_session(corgi_server_uri: str, verify_ssl: Union[str, bool] = True):
    """Create a new session for selected Component Registry (Corgi) URI"""

    # strip trailing slash
    if corgi_server_uri.endswith("/"):
        corgi_server_uri = corgi_server_uri[:-1]

    return Session(base_url=corgi_server_uri, verify_ssl=verify_ssl)


class Session:
    """Simple session wrapper which encapsulates the client"""

    def __init__(self, base_url: str, verify_ssl: Union[str, bool] = True):

        self.__client = AuthenticatedClient(
            base_url=base_url,
            headers={"User-Agent": CORGI_BINDINGS_USERAGENT},
            verify_ssl=verify_ssl,
        )

        self.builds = SessionOperationsGroup(self.__client, "builds")
        self.components = SessionOperationsGroup(self.__client, "components")
        self.lifecycles = SessionOperationsGroup(
            self.__client, "lifecycles", ("retrieve", "list")
        )
        self.products = SessionOperationsGroup(self.__client, "products")
        self.product_versions = SessionOperationsGroup(
            self.__client, "product_versions"
        )
        self.product_streams = SessionOperationsGroup(self.__client, "product_streams")
        self.product_variants = SessionOperationsGroup(
            self.__client, "product_variants"
        )
        self.channels = SessionOperationsGroup(self.__client, "channels")

    def status(self):
        status_fn = get_sync_function(corgi_status_retrieve)
        return status_fn(client=self.__client)


class SessionOperationsGroup:
    """
    Group of the CRUD and extra operations for one specific resource
    """

    def __init__(
        self,
        client: AuthenticatedClient,
        resource_name: str,
        allowed_operations: List[str] = ALL_SESSION_OPERATIONS,
    ):
        self.client = client
        self.resource_name = resource_name
        self.allowed_operations = allowed_operations

    @property
    def model_name(self) -> str:
        if self.resource_name in RESOURCE_TO_MODEL_MAPPING:
            # from mapping
            return RESOURCE_TO_MODEL_MAPPING[self.resource_name]
        else:
            # parse it from the resource name
            name_components = self.resource_name.split("_")
            name_components[-1] = name_components[-1][:-1]
            return "".join(name_component.title() for name_component in name_components)

    @property
    def model(self):
        return getattr(models, self.model_name)

    def __get_method_module(self, resource_name: str, method: str) -> ModuleType:
        # import endpoint module based on a method
        return importlib.import_module(
            f"{CORGI_BINDINGS_API_PATH}.{CORGI_API_VERSION}_{resource_name}_{method}",
            package="corgi_bindings",
        )

    # CRUD operations

    def retrieve(self, id, **kwargs):
        if "retrieve" in self.allowed_operations:
            method_module = self.__get_method_module(
                resource_name=self.resource_name, method="retrieve"
            )
            sync_fn = get_sync_function(method_module)
            return sync_fn(id, client=self.client, **kwargs)
        else:
            raise OperationUnsupported(
                'Operation "update" is not supported for the '
                f'"{self.resource_name}" resource.'
            )

    def retrieve_list(self, **kwargs):
        if "list" in self.allowed_operations:
            method_module = self.__get_method_module(
                resource_name=self.resource_name, method="list"
            )
            sync_fn = get_sync_function(method_module)
            return sync_fn(client=self.client, **kwargs)
        else:
            raise OperationUnsupported(
                'Operation "update" is not supported for the '
                f'"{self.resource_name}" resource.'
            )

    def create(self, form_data: Dict[str, Any]):
        if "create" in self.allowed_operations:
            model = getattr(models, self.model_name)
            transformed_data = model.from_dict(form_data)

            method_module = self.__get_method_module(
                resource_name=self.resource_name, method="create"
            )
            sync_fn = get_sync_function(method_module)
            return sync_fn(
                client=self.client,
                form_data=transformed_data,
                multipart_data=UNSET,
                json_data=UNSET,
            )
        else:
            raise OperationUnsupported(
                'Operation "update" is not supported for the '
                f'"{self.resource_name}" resource.'
            )

    def update(self, id, form_data: Dict[str, Any]):
        if "update" in self.allowed_operations:
            transformed_data = self.model.from_dict(form_data)

            method_module = self.__get_method_module(
                resource_name=self.resource_name, method="update"
            )
            sync_fn = get_sync_function(method_module)
            return sync_fn(
                id,
                client=self.client,
                form_data=transformed_data,
                multipart_data=UNSET,
                json_data=UNSET,
            )
        else:
            raise OperationUnsupported(
                'Operation "update" is not supported for the '
                f'"{self.resource_name}" resource.'
            )

    def delete(self, id):
        if "destroy" in self.allowed_operations:
            method_module = self.__get_method_module(
                resource_name=self.resource_name, method="destroy"
            )
            sync_fn = get_sync_function(method_module)
            return sync_fn(
                id,
                client=self.client,
            )
        else:
            raise OperationUnsupported(
                'Operation "delete" is not supported for the '
                f'"{self.resource_name}" resource.'
            )

    # Extra operations

    def search(self, searched_text: str):
        if "search" in self.allowed_operations:
            method_module = self.__get_method_module(
                resource_name=self.resource_name, method="retrieve_list"
            )
            sync_fn = get_sync_function(method_module)
            return sync_fn(client=self.client, search=searched_text)
        else:
            raise OperationUnsupported(
                'Operation "search" is not supported for the '
                f'"{self.resource_name}" resource.'
            )
