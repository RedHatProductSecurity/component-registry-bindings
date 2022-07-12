from typing import Any, Dict, Optional

import requests

from ...client import Client
from ...models.product import Product
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uuid: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/api/v1/products/{uuid}".format(
        client.base_url,
        uuid=uuid,
    )

    headers: Dict[str, Any] = client.get_headers()

    return {
        "url": url,
        "headers": headers,
    }


def _parse_response(*, response: requests.Response) -> Optional[Product]:
    if response.status_code == 200:
        _response_200 = response.json()
        response_200: Product
        if isinstance(_response_200, Unset):
            response_200 = UNSET
        else:
            response_200 = Product.from_dict(_response_200)

        return response_200
    return None


def _build_response(*, response: requests.Response) -> Response[Product]:
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
) -> Response[Product]:
    kwargs = _get_kwargs(
        uuid=uuid,
        client=client,
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
    uuid: str,
    *,
    client: Client,
) -> Optional[Product]:
    """View for api/v1/products"""

    return sync_detailed(
        uuid=uuid,
        client=client,
    ).parsed
