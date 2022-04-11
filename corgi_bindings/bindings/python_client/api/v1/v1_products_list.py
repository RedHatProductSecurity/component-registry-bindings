from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.paginated_product_list import PaginatedProductList
from ...models.v1_products_list_tags import V1ProductsListTags
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    channels: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    product_streams: Union[Unset, None, str] = UNSET,
    product_variants: Union[Unset, None, str] = UNSET,
    product_versions: Union[Unset, None, str] = UNSET,
    products: Union[Unset, None, str] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    tags: Union[Unset, None, V1ProductsListTags] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/v1/products".format(
        client.base_url,
    )

    headers: Dict[str, Any] = client.get_headers()

    json_tags: Union[Unset, None, Dict[str, Any]] = UNSET
    if not isinstance(tags, Unset):
        json_tags = tags.to_dict() if tags else None

    params: Dict[str, Any] = {
        "channels": channels,
        "limit": limit,
        "name": name,
        "offset": offset,
        "product_streams": product_streams,
        "product_variants": product_variants,
        "product_versions": product_versions,
        "products": products,
        "search": search,
    }
    if not isinstance(json_tags, Unset) and json_tags is not None:
        params.update(json_tags)
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[PaginatedProductList]:
    if response.status_code == 200:
        _response_200 = response.json()
        response_200: PaginatedProductList
        if isinstance(_response_200, Unset):
            response_200 = UNSET
        else:
            response_200 = PaginatedProductList.from_dict(_response_200)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[PaginatedProductList]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    channels: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    product_streams: Union[Unset, None, str] = UNSET,
    product_variants: Union[Unset, None, str] = UNSET,
    product_versions: Union[Unset, None, str] = UNSET,
    products: Union[Unset, None, str] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    tags: Union[Unset, None, V1ProductsListTags] = UNSET,
) -> Response[PaginatedProductList]:
    kwargs = _get_kwargs(
        client=client,
        channels=channels,
        limit=limit,
        name=name,
        offset=offset,
        product_streams=product_streams,
        product_variants=product_variants,
        product_versions=product_versions,
        products=products,
        search=search,
        tags=tags,
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
    channels: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    product_streams: Union[Unset, None, str] = UNSET,
    product_variants: Union[Unset, None, str] = UNSET,
    product_versions: Union[Unset, None, str] = UNSET,
    products: Union[Unset, None, str] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    tags: Union[Unset, None, V1ProductsListTags] = UNSET,
) -> Optional[PaginatedProductList]:
    """View for api/v1/products"""

    return sync_detailed(
        client=client,
        channels=channels,
        limit=limit,
        name=name,
        offset=offset,
        product_streams=product_streams,
        product_variants=product_variants,
        product_versions=product_versions,
        products=products,
        search=search,
        tags=tags,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    channels: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    product_streams: Union[Unset, None, str] = UNSET,
    product_variants: Union[Unset, None, str] = UNSET,
    product_versions: Union[Unset, None, str] = UNSET,
    products: Union[Unset, None, str] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    tags: Union[Unset, None, V1ProductsListTags] = UNSET,
) -> Response[PaginatedProductList]:
    kwargs = _get_kwargs(
        client=client,
        channels=channels,
        limit=limit,
        name=name,
        offset=offset,
        product_streams=product_streams,
        product_variants=product_variants,
        product_versions=product_versions,
        products=products,
        search=search,
        tags=tags,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    channels: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    product_streams: Union[Unset, None, str] = UNSET,
    product_variants: Union[Unset, None, str] = UNSET,
    product_versions: Union[Unset, None, str] = UNSET,
    products: Union[Unset, None, str] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    tags: Union[Unset, None, V1ProductsListTags] = UNSET,
) -> Optional[PaginatedProductList]:
    """View for api/v1/products"""

    return (
        await asyncio_detailed(
            client=client,
            channels=channels,
            limit=limit,
            name=name,
            offset=offset,
            product_streams=product_streams,
            product_variants=product_variants,
            product_versions=product_versions,
            products=products,
            search=search,
            tags=tags,
        )
    ).parsed
