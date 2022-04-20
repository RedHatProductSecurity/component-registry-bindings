from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.paginated_channel_list import PaginatedChannelList
from ...models.v1_channels_list_type import V1ChannelsListType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    limit: Union[Unset, None, int] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    tags: Union[Unset, None, str] = UNSET,
    type: Union[Unset, None, V1ChannelsListType] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/v1/channels".format(
        client.base_url,
    )

    headers: Dict[str, Any] = client.get_headers()

    json_type: Union[Unset, None, str] = UNSET
    if not isinstance(type, Unset):

        json_type = V1ChannelsListType(type).value if type else None

    params: Dict[str, Any] = {
        "limit": limit,
        "name": name,
        "offset": offset,
        "search": search,
        "tags": tags,
        "type": json_type,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[PaginatedChannelList]:
    if response.status_code == 200:
        _response_200 = response.json()
        response_200: PaginatedChannelList
        if isinstance(_response_200, Unset):
            response_200 = UNSET
        else:
            response_200 = PaginatedChannelList.from_dict(_response_200)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[PaginatedChannelList]:
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
    tags: Union[Unset, None, str] = UNSET,
    type: Union[Unset, None, V1ChannelsListType] = UNSET,
) -> Response[PaginatedChannelList]:
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
    tags: Union[Unset, None, str] = UNSET,
    type: Union[Unset, None, V1ChannelsListType] = UNSET,
) -> Optional[PaginatedChannelList]:
    """View for api/v1/channels"""

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
    tags: Union[Unset, None, str] = UNSET,
    type: Union[Unset, None, V1ChannelsListType] = UNSET,
) -> Response[PaginatedChannelList]:
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
    tags: Union[Unset, None, str] = UNSET,
    type: Union[Unset, None, V1ChannelsListType] = UNSET,
) -> Optional[PaginatedChannelList]:
    """View for api/v1/channels"""

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
