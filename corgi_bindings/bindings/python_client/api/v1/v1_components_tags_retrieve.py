from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.component_detail import ComponentDetail
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uuid: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/api/v1/components/{uuid}/tags".format(
        client.base_url,
        uuid=uuid,
    )

    headers: Dict[str, Any] = client.get_headers()

    return {
        "url": url,
        "headers": headers,
    }


def _parse_response(*, response: httpx.Response) -> Optional[ComponentDetail]:
    if response.status_code == 200:
        _response_200 = response.json()
        response_200: ComponentDetail
        if isinstance(_response_200, Unset):
            response_200 = UNSET
        else:
            response_200 = ComponentDetail.from_dict(_response_200)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[ComponentDetail]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    uuid: str,
    *,
    client: Client,
) -> Response[ComponentDetail]:
    kwargs = _get_kwargs(
        uuid=uuid,
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
    uuid: str,
    *,
    client: Client,
) -> Optional[ComponentDetail]:
    """Get all tags on component."""

    return sync_detailed(
        uuid=uuid,
        client=client,
    ).parsed


async def asyncio_detailed(
    uuid: str,
    *,
    client: Client,
) -> Response[ComponentDetail]:
    kwargs = _get_kwargs(
        uuid=uuid,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    uuid: str,
    *,
    client: Client,
) -> Optional[ComponentDetail]:
    """Get all tags on component."""

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
        )
    ).parsed
