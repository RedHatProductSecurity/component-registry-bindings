from typing import Any, Dict, Optional, Union

import requests

from ...client import Client
from ...models.paginated_component_list import PaginatedComponentList
from ...models.v1_components_list_namespace import V1ComponentsListNamespace
from ...models.v1_components_list_type import V1ComponentsListType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    arch: Union[Unset, None, str] = UNSET,
    channels: Union[Unset, None, str] = UNSET,
    description: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    namespace: Union[Unset, None, V1ComponentsListNamespace] = UNSET,
    nevra: Union[Unset, None, str] = UNSET,
    nvr: Union[Unset, None, str] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    product_streams: Union[Unset, None, str] = UNSET,
    product_variants: Union[Unset, None, str] = UNSET,
    product_versions: Union[Unset, None, str] = UNSET,
    products: Union[Unset, None, str] = UNSET,
    provides: Union[Unset, None, str] = UNSET,
    re_name: Union[Unset, None, str] = UNSET,
    re_purl: Union[Unset, None, str] = UNSET,
    re_upstream: Union[Unset, None, str] = UNSET,
    release: Union[Unset, None, str] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    sources: Union[Unset, None, str] = UNSET,
    tags: Union[Unset, None, int] = UNSET,
    type: Union[Unset, None, V1ComponentsListType] = UNSET,
    upstreams: Union[Unset, None, str] = UNSET,
    version: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/v1/components".format(
        client.base_url,
    )

    headers: Dict[str, Any] = client.get_headers()

    json_namespace: Union[Unset, None, str] = UNSET
    if not isinstance(namespace, Unset):

        json_namespace = V1ComponentsListNamespace(namespace).value if namespace else None

    json_type: Union[Unset, None, str] = UNSET
    if not isinstance(type, Unset):

        json_type = V1ComponentsListType(type).value if type else None

    params: Dict[str, Any] = {
        "arch": arch,
        "channels": channels,
        "description": description,
        "limit": limit,
        "name": name,
        "namespace": json_namespace,
        "nevra": nevra,
        "nvr": nvr,
        "offset": offset,
        "product_streams": product_streams,
        "product_variants": product_variants,
        "product_versions": product_versions,
        "products": products,
        "provides": provides,
        "re_name": re_name,
        "re_purl": re_purl,
        "re_upstream": re_upstream,
        "release": release,
        "search": search,
        "sources": sources,
        "tags": tags,
        "type": json_type,
        "upstreams": upstreams,
        "version": version,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "params": params,
    }


def _parse_response(*, response: requests.Response) -> Optional[PaginatedComponentList]:
    if response.status_code == 200:
        _response_200 = response.json()
        response_200: PaginatedComponentList
        if isinstance(_response_200, Unset):
            response_200 = UNSET
        else:
            response_200 = PaginatedComponentList.from_dict(_response_200)

        return response_200
    return None


def _build_response(*, response: requests.Response) -> Response[PaginatedComponentList]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    arch: Union[Unset, None, str] = UNSET,
    channels: Union[Unset, None, str] = UNSET,
    description: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    namespace: Union[Unset, None, V1ComponentsListNamespace] = UNSET,
    nevra: Union[Unset, None, str] = UNSET,
    nvr: Union[Unset, None, str] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    product_streams: Union[Unset, None, str] = UNSET,
    product_variants: Union[Unset, None, str] = UNSET,
    product_versions: Union[Unset, None, str] = UNSET,
    products: Union[Unset, None, str] = UNSET,
    provides: Union[Unset, None, str] = UNSET,
    re_name: Union[Unset, None, str] = UNSET,
    re_purl: Union[Unset, None, str] = UNSET,
    re_upstream: Union[Unset, None, str] = UNSET,
    release: Union[Unset, None, str] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    sources: Union[Unset, None, str] = UNSET,
    tags: Union[Unset, None, int] = UNSET,
    type: Union[Unset, None, V1ComponentsListType] = UNSET,
    upstreams: Union[Unset, None, str] = UNSET,
    version: Union[Unset, None, str] = UNSET,
) -> Response[PaginatedComponentList]:
    kwargs = _get_kwargs(
        client=client,
        arch=arch,
        channels=channels,
        description=description,
        limit=limit,
        name=name,
        namespace=namespace,
        nevra=nevra,
        nvr=nvr,
        offset=offset,
        product_streams=product_streams,
        product_variants=product_variants,
        product_versions=product_versions,
        products=products,
        provides=provides,
        re_name=re_name,
        re_purl=re_purl,
        re_upstream=re_upstream,
        release=release,
        search=search,
        sources=sources,
        tags=tags,
        type=type,
        upstreams=upstreams,
        version=version,
    )

    response = requests.get(
        verify=client.verify_ssl,
        auth=client.auth,
        timeout=client.timeout,
        **kwargs,
    )
    response.raise_for_status()

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    arch: Union[Unset, None, str] = UNSET,
    channels: Union[Unset, None, str] = UNSET,
    description: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    namespace: Union[Unset, None, V1ComponentsListNamespace] = UNSET,
    nevra: Union[Unset, None, str] = UNSET,
    nvr: Union[Unset, None, str] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    product_streams: Union[Unset, None, str] = UNSET,
    product_variants: Union[Unset, None, str] = UNSET,
    product_versions: Union[Unset, None, str] = UNSET,
    products: Union[Unset, None, str] = UNSET,
    provides: Union[Unset, None, str] = UNSET,
    re_name: Union[Unset, None, str] = UNSET,
    re_purl: Union[Unset, None, str] = UNSET,
    re_upstream: Union[Unset, None, str] = UNSET,
    release: Union[Unset, None, str] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    sources: Union[Unset, None, str] = UNSET,
    tags: Union[Unset, None, int] = UNSET,
    type: Union[Unset, None, V1ComponentsListType] = UNSET,
    upstreams: Union[Unset, None, str] = UNSET,
    version: Union[Unset, None, str] = UNSET,
) -> Optional[PaginatedComponentList]:
    """View for api/v1/components"""

    return sync_detailed(
        client=client,
        arch=arch,
        channels=channels,
        description=description,
        limit=limit,
        name=name,
        namespace=namespace,
        nevra=nevra,
        nvr=nvr,
        offset=offset,
        product_streams=product_streams,
        product_variants=product_variants,
        product_versions=product_versions,
        products=products,
        provides=provides,
        re_name=re_name,
        re_purl=re_purl,
        re_upstream=re_upstream,
        release=release,
        search=search,
        sources=sources,
        tags=tags,
        type=type,
        upstreams=upstreams,
        version=version,
    ).parsed
