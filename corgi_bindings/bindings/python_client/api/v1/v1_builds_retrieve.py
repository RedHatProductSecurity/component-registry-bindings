from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.software_build_detail import SoftwareBuildDetail
from ...types import UNSET, Response, Unset


def _get_kwargs(
    build_id: int,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/api/v1/builds/{build_id}".format(
        client.base_url,
        build_id=build_id,
    )

    headers: Dict[str, Any] = client.get_headers()

    return {
        "url": url,
        "headers": headers,
    }


def _parse_response(*, response: httpx.Response) -> Optional[SoftwareBuildDetail]:
    if response.status_code == 200:
        _response_200 = response.json()
        response_200: SoftwareBuildDetail
        if isinstance(_response_200, Unset):
            response_200 = UNSET
        else:
            response_200 = SoftwareBuildDetail.from_dict(_response_200)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[SoftwareBuildDetail]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    build_id: int,
    *,
    client: Client,
) -> Response[SoftwareBuildDetail]:
    kwargs = _get_kwargs(
        build_id=build_id,
        client=client,
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
    build_id: int,
    *,
    client: Client,
) -> Optional[SoftwareBuildDetail]:
    """View for api/v1/builds"""

    return sync_detailed(
        build_id=build_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    build_id: int,
    *,
    client: Client,
) -> Response[SoftwareBuildDetail]:
    kwargs = _get_kwargs(
        build_id=build_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    build_id: int,
    *,
    client: Client,
) -> Optional[SoftwareBuildDetail]:
    """View for api/v1/builds"""

    return (
        await asyncio_detailed(
            build_id=build_id,
            client=client,
        )
    ).parsed
