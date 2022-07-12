from typing import Any, Dict, Optional

import requests

from ...client import Client
from ...models.app_stream_life_cycle import AppStreamLifeCycle
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: int,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/api/v1/lifecycles/{id}".format(
        client.base_url,
        id=id,
    )

    headers: Dict[str, Any] = client.get_headers()

    return {
        "url": url,
        "headers": headers,
    }


def _parse_response(*, response: requests.Response) -> Optional[AppStreamLifeCycle]:
    if response.status_code == 200:
        _response_200 = response.json()
        response_200: AppStreamLifeCycle
        if isinstance(_response_200, Unset):
            response_200 = UNSET
        else:
            response_200 = AppStreamLifeCycle.from_dict(_response_200)

        return response_200
    return None


def _build_response(*, response: requests.Response) -> Response[AppStreamLifeCycle]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    id: int,
    *,
    client: Client,
) -> Response[AppStreamLifeCycle]:
    kwargs = _get_kwargs(
        id=id,
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
    id: int,
    *,
    client: Client,
) -> Optional[AppStreamLifeCycle]:
    """View for api/v1/lifecycles"""

    return sync_detailed(
        id=id,
        client=client,
    ).parsed
