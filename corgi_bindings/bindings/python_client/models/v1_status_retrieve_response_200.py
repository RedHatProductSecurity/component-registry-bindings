import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.v1_status_retrieve_response_200_components import V1StatusRetrieveResponse200Components
from ..models.v1_status_retrieve_response_200_product_streams import V1StatusRetrieveResponse200ProductStreams
from ..models.v1_status_retrieve_response_200_product_versions import V1StatusRetrieveResponse200ProductVersions
from ..models.v1_status_retrieve_response_200_products import V1StatusRetrieveResponse200Products
from ..types import UNSET, Unset

T = TypeVar("T", bound="V1StatusRetrieveResponse200")


@attr.s(auto_attribs=True)
class V1StatusRetrieveResponse200:
    """ """

    status: Union[Unset, str] = UNSET
    dt: Union[Unset, datetime.datetime] = UNSET
    service_version: Union[Unset, str] = UNSET
    rest_api_version: Union[Unset, str] = UNSET
    components: Union[Unset, V1StatusRetrieveResponse200Components] = UNSET
    products: Union[Unset, V1StatusRetrieveResponse200Products] = UNSET
    product_versions: Union[Unset, V1StatusRetrieveResponse200ProductVersions] = UNSET
    product_streams: Union[Unset, V1StatusRetrieveResponse200ProductStreams] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status = self.status
        dt: Union[Unset, str] = UNSET
        if not isinstance(self.dt, Unset):
            dt = self.dt.isoformat()

        service_version = self.service_version
        rest_api_version = self.rest_api_version
        components: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.components, Unset):
            components = self.components.to_dict()

        products: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.products, Unset):
            products = self.products.to_dict()

        product_versions: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.product_versions, Unset):
            product_versions = self.product_versions.to_dict()

        product_streams: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.product_streams, Unset):
            product_streams = self.product_streams.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if status is not UNSET:
            field_dict["status"] = status
        if dt is not UNSET:
            field_dict["dt"] = dt
        if service_version is not UNSET:
            field_dict["service_version"] = service_version
        if rest_api_version is not UNSET:
            field_dict["rest_api_version"] = rest_api_version
        if components is not UNSET:
            field_dict["components"] = components
        if products is not UNSET:
            field_dict["products"] = products
        if product_versions is not UNSET:
            field_dict["product_versions"] = product_versions
        if product_streams is not UNSET:
            field_dict["product_streams"] = product_streams

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        status = d.pop("status", UNSET)

        _dt = d.pop("dt", UNSET)
        dt: Union[Unset, datetime.datetime]
        if isinstance(_dt, Unset):
            dt = UNSET
        else:
            dt = isoparse(_dt)

        service_version = d.pop("service_version", UNSET)

        rest_api_version = d.pop("rest_api_version", UNSET)

        _components = d.pop("components", UNSET)
        components: Union[Unset, V1StatusRetrieveResponse200Components]
        if isinstance(_components, Unset):
            components = UNSET
        else:
            components = V1StatusRetrieveResponse200Components.from_dict(_components)

        _products = d.pop("products", UNSET)
        products: Union[Unset, V1StatusRetrieveResponse200Products]
        if isinstance(_products, Unset):
            products = UNSET
        else:
            products = V1StatusRetrieveResponse200Products.from_dict(_products)

        _product_versions = d.pop("product_versions", UNSET)
        product_versions: Union[Unset, V1StatusRetrieveResponse200ProductVersions]
        if isinstance(_product_versions, Unset):
            product_versions = UNSET
        else:
            product_versions = V1StatusRetrieveResponse200ProductVersions.from_dict(_product_versions)

        _product_streams = d.pop("product_streams", UNSET)
        product_streams: Union[Unset, V1StatusRetrieveResponse200ProductStreams]
        if isinstance(_product_streams, Unset):
            product_streams = UNSET
        else:
            product_streams = V1StatusRetrieveResponse200ProductStreams.from_dict(_product_streams)

        v1_status_retrieve_response_200 = cls(
            status=status,
            dt=dt,
            service_version=service_version,
            rest_api_version=rest_api_version,
            components=components,
            products=products,
            product_versions=product_versions,
            product_streams=product_streams,
        )

        v1_status_retrieve_response_200.additional_properties = d
        return v1_status_retrieve_response_200

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
