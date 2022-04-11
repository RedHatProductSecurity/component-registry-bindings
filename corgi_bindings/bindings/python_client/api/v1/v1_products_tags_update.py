from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.product import Product
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uuid: str,
    *,
    client: Client,
    json_body: Product,
) -> Dict[str, Any]:
    url = "{}/api/v1/products/{uuid}/tags".format(
        client.base_url,
        uuid=uuid,
    )

    headers: Dict[str, Any] = client.get_headers()

    json_json_body: Dict[str, Any] = UNSET
    if not isinstance(json_body, Unset):
        json_json_body = json_body.to_dict()

    return {
        "url": url,
        "headers": headers,
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Product]:
    if response.status_code == 200:
        _response_200 = response.json()
        response_200: Product
        if isinstance(_response_200, Unset):
            response_200 = UNSET
        else:
            response_200 = Product.from_dict(_response_200)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[Product]:
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
    json_body: Product,
) -> Response[Product]:
    kwargs = _get_kwargs(
        uuid=uuid,
        client=client,
        json_body=json_body,
    )

    response = httpx.put(
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
    json_body: Product,
) -> Optional[Product]:
    """Set new tags on component, without removing any older values.

    Sequence tags have their values merged. To remove a tag, GET all the current tags. Then
    POST all of them back, except the tags to be removed."""

    return sync_detailed(
        uuid=uuid,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    uuid: str,
    *,
    client: Client,
    json_body: Product,
) -> Response[Product]:
    kwargs = _get_kwargs(
        uuid=uuid,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.put(**kwargs)

    return _build_response(response=response)


async def asyncio(
    uuid: str,
    *,
    client: Client,
    json_body: Product,
) -> Optional[Product]:
    """Set new tags on component, without removing any older values.

    Sequence tags have their values merged. To remove a tag, GET all the current tags. Then
    POST all of them back, except the tags to be removed."""

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            json_body=json_body,
        )
    ).parsed
