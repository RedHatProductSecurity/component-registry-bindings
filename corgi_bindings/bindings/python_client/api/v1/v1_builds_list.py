from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.paginated_software_build_detail_list import PaginatedSoftwareBuildDetailList
from ...models.v1_builds_list_tags import V1BuildsListTags
from ...models.v1_builds_list_type import V1BuildsListType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    limit: Union[Unset, None, int] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    tags: Union[Unset, None, V1BuildsListTags] = UNSET,
    type: Union[Unset, None, V1BuildsListType] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/v1/builds".format(
        client.base_url,
    )

    headers: Dict[str, Any] = client.get_headers()

    json_tags: Union[Unset, None, Dict[str, Any]] = UNSET
    if not isinstance(tags, Unset):
        json_tags = tags.to_dict() if tags else None

    json_type: Union[Unset, None, str] = UNSET
    if not isinstance(type, Unset):

        json_type = V1BuildsListType(type).value if type else None

    params: Dict[str, Any] = {
        "limit": limit,
        "name": name,
        "offset": offset,
        "search": search,
        "type": json_type,
    }
    if not isinstance(json_tags, Unset) and json_tags is not None:
        params.update(json_tags)
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[PaginatedSoftwareBuildDetailList]:
    if response.status_code == 200:
        _response_200 = response.json()
        response_200: PaginatedSoftwareBuildDetailList
        if isinstance(_response_200, Unset):
            response_200 = UNSET
        else:
            response_200 = PaginatedSoftwareBuildDetailList.from_dict(_response_200)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[PaginatedSoftwareBuildDetailList]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    limit: Union[Unset, None, int] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    tags: Union[Unset, None, V1BuildsListTags] = UNSET,
    type: Union[Unset, None, V1BuildsListType] = UNSET,
) -> Response[PaginatedSoftwareBuildDetailList]:
    kwargs = _get_kwargs(
        client=client,
        limit=limit,
        name=name,
        offset=offset,
        search=search,
        tags=tags,
        type=type,
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
    limit: Union[Unset, None, int] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    tags: Union[Unset, None, V1BuildsListTags] = UNSET,
    type: Union[Unset, None, V1BuildsListType] = UNSET,
) -> Optional[PaginatedSoftwareBuildDetailList]:
    """View for api/v1/builds"""

    return sync_detailed(
        client=client,
        limit=limit,
        name=name,
        offset=offset,
        search=search,
        tags=tags,
        type=type,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    limit: Union[Unset, None, int] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    tags: Union[Unset, None, V1BuildsListTags] = UNSET,
    type: Union[Unset, None, V1BuildsListType] = UNSET,
) -> Response[PaginatedSoftwareBuildDetailList]:
    kwargs = _get_kwargs(
        client=client,
        limit=limit,
        name=name,
        offset=offset,
        search=search,
        tags=tags,
        type=type,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    limit: Union[Unset, None, int] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    tags: Union[Unset, None, V1BuildsListTags] = UNSET,
    type: Union[Unset, None, V1BuildsListType] = UNSET,
) -> Optional[PaginatedSoftwareBuildDetailList]:
    """View for api/v1/builds"""

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            name=name,
            offset=offset,
            search=search,
            tags=tags,
            type=type,
        )
    ).parsed
