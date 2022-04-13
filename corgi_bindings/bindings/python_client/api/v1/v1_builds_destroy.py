from typing import Any, Dict

import httpx

from ...client import Client
from ...types import Response


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


def _build_response(*, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=None,
    )


def sync_detailed(
    build_id: int,
    *,
    client: Client,
) -> Response[Any]:
    kwargs = _get_kwargs(
        build_id=build_id,
        client=client,
    )

    response = httpx.delete(
        verify=client.verify_ssl,
        auth=client.auth,
        timeout=client.timeout,
        **kwargs,
    )
    response.raise_for_status()

    return _build_response(response=response)


async def asyncio_detailed(
    build_id: int,
    *,
    client: Client,
) -> Response[Any]:
    kwargs = _get_kwargs(
        build_id=build_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.delete(**kwargs)

    return _build_response(response=response)
