from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.paginated_component_detail_list import PaginatedComponentDetailList
from ...models.v1_components_list_tags import V1ComponentsListTags
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
    offset: Union[Unset, None, int] = UNSET,
    product_streams: Union[Unset, None, str] = UNSET,
    product_variants: Union[Unset, None, str] = UNSET,
    product_versions: Union[Unset, None, str] = UNSET,
    products: Union[Unset, None, str] = UNSET,
    provides: Union[Unset, None, str] = UNSET,
    purl: Union[Unset, None, str] = UNSET,
    release: Union[Unset, None, str] = UNSET,
    rname: Union[Unset, None, str] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    sources: Union[Unset, None, str] = UNSET,
    tags: Union[Unset, None, V1ComponentsListTags] = UNSET,
    type: Union[Unset, None, V1ComponentsListType] = UNSET,
    upstream: Union[Unset, None, str] = UNSET,
    version: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/v1/components".format(
        client.base_url,
    )

    headers: Dict[str, Any] = client.get_headers()

    json_tags: Union[Unset, None, Dict[str, Any]] = UNSET
    if not isinstance(tags, Unset):
        json_tags = tags.to_dict() if tags else None

    json_type: Union[Unset, None, str] = UNSET
    if not isinstance(type, Unset):

        json_type = V1ComponentsListType(type).value if type else None

    params: Dict[str, Any] = {
        "arch": arch,
        "channels": channels,
        "description": description,
        "limit": limit,
        "name": name,
        "offset": offset,
        "product_streams": product_streams,
        "product_variants": product_variants,
        "product_versions": product_versions,
        "products": products,
        "provides": provides,
        "purl": purl,
        "release": release,
        "rname": rname,
        "search": search,
        "sources": sources,
        "type": json_type,
        "upstream": upstream,
        "version": version,
    }
    if not isinstance(json_tags, Unset) and json_tags is not None:
        params.update(json_tags)
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[PaginatedComponentDetailList]:
    if response.status_code == 200:
        _response_200 = response.json()
        response_200: PaginatedComponentDetailList
        if isinstance(_response_200, Unset):
            response_200 = UNSET
        else:
            response_200 = PaginatedComponentDetailList.from_dict(_response_200)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[PaginatedComponentDetailList]:
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
    offset: Union[Unset, None, int] = UNSET,
    product_streams: Union[Unset, None, str] = UNSET,
    product_variants: Union[Unset, None, str] = UNSET,
    product_versions: Union[Unset, None, str] = UNSET,
    products: Union[Unset, None, str] = UNSET,
    provides: Union[Unset, None, str] = UNSET,
    purl: Union[Unset, None, str] = UNSET,
    release: Union[Unset, None, str] = UNSET,
    rname: Union[Unset, None, str] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    sources: Union[Unset, None, str] = UNSET,
    tags: Union[Unset, None, V1ComponentsListTags] = UNSET,
    type: Union[Unset, None, V1ComponentsListType] = UNSET,
    upstream: Union[Unset, None, str] = UNSET,
    version: Union[Unset, None, str] = UNSET,
) -> Response[PaginatedComponentDetailList]:
    kwargs = _get_kwargs(
        client=client,
        arch=arch,
        channels=channels,
        description=description,
        limit=limit,
        name=name,
        offset=offset,
        product_streams=product_streams,
        product_variants=product_variants,
        product_versions=product_versions,
        products=products,
        provides=provides,
        purl=purl,
        release=release,
        rname=rname,
        search=search,
        sources=sources,
        tags=tags,
        type=type,
        upstream=upstream,
        version=version,
    )

    response = httpx.get(
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
    offset: Union[Unset, None, int] = UNSET,
    product_streams: Union[Unset, None, str] = UNSET,
    product_variants: Union[Unset, None, str] = UNSET,
    product_versions: Union[Unset, None, str] = UNSET,
    products: Union[Unset, None, str] = UNSET,
    provides: Union[Unset, None, str] = UNSET,
    purl: Union[Unset, None, str] = UNSET,
    release: Union[Unset, None, str] = UNSET,
    rname: Union[Unset, None, str] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    sources: Union[Unset, None, str] = UNSET,
    tags: Union[Unset, None, V1ComponentsListTags] = UNSET,
    type: Union[Unset, None, V1ComponentsListType] = UNSET,
    upstream: Union[Unset, None, str] = UNSET,
    version: Union[Unset, None, str] = UNSET,
) -> Optional[PaginatedComponentDetailList]:
    """View for api/v1/components"""

    return sync_detailed(
        client=client,
        arch=arch,
        channels=channels,
        description=description,
        limit=limit,
        name=name,
        offset=offset,
        product_streams=product_streams,
        product_variants=product_variants,
        product_versions=product_versions,
        products=products,
        provides=provides,
        purl=purl,
        release=release,
        rname=rname,
        search=search,
        sources=sources,
        tags=tags,
        type=type,
        upstream=upstream,
        version=version,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    arch: Union[Unset, None, str] = UNSET,
    channels: Union[Unset, None, str] = UNSET,
    description: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    product_streams: Union[Unset, None, str] = UNSET,
    product_variants: Union[Unset, None, str] = UNSET,
    product_versions: Union[Unset, None, str] = UNSET,
    products: Union[Unset, None, str] = UNSET,
    provides: Union[Unset, None, str] = UNSET,
    purl: Union[Unset, None, str] = UNSET,
    release: Union[Unset, None, str] = UNSET,
    rname: Union[Unset, None, str] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    sources: Union[Unset, None, str] = UNSET,
    tags: Union[Unset, None, V1ComponentsListTags] = UNSET,
    type: Union[Unset, None, V1ComponentsListType] = UNSET,
    upstream: Union[Unset, None, str] = UNSET,
    version: Union[Unset, None, str] = UNSET,
) -> Response[PaginatedComponentDetailList]:
    kwargs = _get_kwargs(
        client=client,
        arch=arch,
        channels=channels,
        description=description,
        limit=limit,
        name=name,
        offset=offset,
        product_streams=product_streams,
        product_variants=product_variants,
        product_versions=product_versions,
        products=products,
        provides=provides,
        purl=purl,
        release=release,
        rname=rname,
        search=search,
        sources=sources,
        tags=tags,
        type=type,
        upstream=upstream,
        version=version,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    arch: Union[Unset, None, str] = UNSET,
    channels: Union[Unset, None, str] = UNSET,
    description: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    product_streams: Union[Unset, None, str] = UNSET,
    product_variants: Union[Unset, None, str] = UNSET,
    product_versions: Union[Unset, None, str] = UNSET,
    products: Union[Unset, None, str] = UNSET,
    provides: Union[Unset, None, str] = UNSET,
    purl: Union[Unset, None, str] = UNSET,
    release: Union[Unset, None, str] = UNSET,
    rname: Union[Unset, None, str] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    sources: Union[Unset, None, str] = UNSET,
    tags: Union[Unset, None, V1ComponentsListTags] = UNSET,
    type: Union[Unset, None, V1ComponentsListType] = UNSET,
    upstream: Union[Unset, None, str] = UNSET,
    version: Union[Unset, None, str] = UNSET,
) -> Optional[PaginatedComponentDetailList]:
    """View for api/v1/components"""

    return (
        await asyncio_detailed(
            client=client,
            arch=arch,
            channels=channels,
            description=description,
            limit=limit,
            name=name,
            offset=offset,
            product_streams=product_streams,
            product_variants=product_variants,
            product_versions=product_versions,
            products=products,
            provides=provides,
            purl=purl,
            release=release,
            rname=rname,
            search=search,
            sources=sources,
            tags=tags,
            type=type,
            upstream=upstream,
            version=version,
        )
    ).parsed
