from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.component_detail import ComponentDetail
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uuid: str,
    *,
    client: Client,
    form_data: ComponentDetail,
    multipart_data: ComponentDetail,
    json_body: ComponentDetail,
) -> Dict[str, Any]:
    url = "{}/api/v1/components/{uuid}".format(
        client.base_url,
        uuid=uuid,
    )

    headers: Dict[str, Any] = client.get_headers()

    json_json_body: Dict[str, Any] = UNSET
    if not isinstance(json_body, Unset):
        json_body.to_dict()

    multipart_multipart_data: Dict[str, Any] = UNSET
    if not isinstance(multipart_data, Unset):
        multipart_data.to_multipart()

    return {
        "url": url,
        "headers": headers,
        "data": form_data.to_dict(),
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
    form_data: ComponentDetail,
    multipart_data: ComponentDetail,
    json_body: ComponentDetail,
) -> Response[ComponentDetail]:
    kwargs = _get_kwargs(
        uuid=uuid,
        client=client,
        form_data=form_data,
        multipart_data=multipart_data,
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
    form_data: ComponentDetail,
    multipart_data: ComponentDetail,
    json_body: ComponentDetail,
) -> Optional[ComponentDetail]:
    """Raise NotImplementedError for Model Entity DELETE / POST / PUT and tag HEAD / OPTIONS.

    This mess can just go away once we implement all of these methods."""

    return sync_detailed(
        uuid=uuid,
        client=client,
        form_data=form_data,
        multipart_data=multipart_data,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    uuid: str,
    *,
    client: Client,
    form_data: ComponentDetail,
    multipart_data: ComponentDetail,
    json_body: ComponentDetail,
) -> Response[ComponentDetail]:
    kwargs = _get_kwargs(
        uuid=uuid,
        client=client,
        form_data=form_data,
        multipart_data=multipart_data,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.put(**kwargs)

    return _build_response(response=response)


async def asyncio(
    uuid: str,
    *,
    client: Client,
    form_data: ComponentDetail,
    multipart_data: ComponentDetail,
    json_body: ComponentDetail,
) -> Optional[ComponentDetail]:
    """Raise NotImplementedError for Model Entity DELETE / POST / PUT and tag HEAD / OPTIONS.

    This mess can just go away once we implement all of these methods."""

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            form_data=form_data,
            multipart_data=multipart_data,
            json_body=json_body,
        )
    ).parsed
