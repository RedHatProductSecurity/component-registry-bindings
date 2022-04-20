import json
from typing import Any, Dict, List, Tuple, Type, TypeVar, Union, cast

import attr

from ..models.product_variant_meta_attr import ProductVariantMetaAttr
from ..models.product_variant_tags import ProductVariantTags
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProductVariant")


@attr.s(auto_attribs=True)
class ProductVariant:
    """product variant (errata) serializer"""

    uuid: str
    name: str
    errata: str
    builds: str
    components: str
    upstream: str
    description: Union[Unset, str] = UNSET
    tags: Union[Unset, ProductVariantTags] = UNSET
    products: Union[Unset, List[str]] = UNSET
    product_versions: Union[Unset, List[str]] = UNSET
    product_streams: Union[Unset, List[str]] = UNSET
    channels: Union[Unset, List[str]] = UNSET
    meta_attr: Union[Unset, ProductVariantMetaAttr] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        uuid = self.uuid
        name = self.name
        errata = self.errata
        builds = self.builds
        components = self.components
        upstream = self.upstream
        description = self.description
        tags: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags.to_dict()

        products: Union[Unset, List[str]] = UNSET
        if not isinstance(self.products, Unset):
            products = self.products

        product_versions: Union[Unset, List[str]] = UNSET
        if not isinstance(self.product_versions, Unset):
            product_versions = self.product_versions

        product_streams: Union[Unset, List[str]] = UNSET
        if not isinstance(self.product_streams, Unset):
            product_streams = self.product_streams

        channels: Union[Unset, List[str]] = UNSET
        if not isinstance(self.channels, Unset):
            channels = self.channels

        meta_attr: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.meta_attr, Unset):
            meta_attr = self.meta_attr.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if name is not UNSET:
            field_dict["name"] = name
        if errata is not UNSET:
            field_dict["errata"] = errata
        if builds is not UNSET:
            field_dict["builds"] = builds
        if components is not UNSET:
            field_dict["components"] = components
        if upstream is not UNSET:
            field_dict["upstream"] = upstream
        if description is not UNSET:
            field_dict["description"] = description
        if tags is not UNSET:
            field_dict["tags"] = tags
        if products is not UNSET:
            field_dict["products"] = products
        if product_versions is not UNSET:
            field_dict["product_versions"] = product_versions
        if product_streams is not UNSET:
            field_dict["product_streams"] = product_streams
        if channels is not UNSET:
            field_dict["channels"] = channels
        if meta_attr is not UNSET:
            field_dict["meta_attr"] = meta_attr

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        uuid = self.uuid if self.uuid is UNSET else (None, str(self.uuid), "text/plain")
        name = self.name if self.name is UNSET else (None, str(self.name), "text/plain")
        errata = self.errata if self.errata is UNSET else (None, str(self.errata), "text/plain")
        builds = self.builds if self.builds is UNSET else (None, str(self.builds), "text/plain")
        components = self.components if self.components is UNSET else (None, str(self.components), "text/plain")
        upstream = self.upstream if self.upstream is UNSET else (None, str(self.upstream), "text/plain")
        description = self.description if self.description is UNSET else (None, str(self.description), "text/plain")
        tags: Union[Unset, Tuple[None, str, str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = (None, json.dumps(self.tags.to_dict()), "application/json")

        products: Union[Unset, Tuple[None, str, str]] = UNSET
        if not isinstance(self.products, Unset):
            _temp_products = self.products
            products = (None, json.dumps(_temp_products), "application/json")

        product_versions: Union[Unset, Tuple[None, str, str]] = UNSET
        if not isinstance(self.product_versions, Unset):
            _temp_product_versions = self.product_versions
            product_versions = (None, json.dumps(_temp_product_versions), "application/json")

        product_streams: Union[Unset, Tuple[None, str, str]] = UNSET
        if not isinstance(self.product_streams, Unset):
            _temp_product_streams = self.product_streams
            product_streams = (None, json.dumps(_temp_product_streams), "application/json")

        channels: Union[Unset, Tuple[None, str, str]] = UNSET
        if not isinstance(self.channels, Unset):
            _temp_channels = self.channels
            channels = (None, json.dumps(_temp_channels), "application/json")

        meta_attr: Union[Unset, Tuple[None, str, str]] = UNSET
        if not isinstance(self.meta_attr, Unset):
            meta_attr = (None, json.dumps(self.meta_attr.to_dict()), "application/json")

        field_dict: Dict[str, Any] = {}
        field_dict.update({key: (None, str(value), "text/plain") for key, value in self.additional_properties.items()})
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if name is not UNSET:
            field_dict["name"] = name
        if errata is not UNSET:
            field_dict["errata"] = errata
        if builds is not UNSET:
            field_dict["builds"] = builds
        if components is not UNSET:
            field_dict["components"] = components
        if upstream is not UNSET:
            field_dict["upstream"] = upstream
        if description is not UNSET:
            field_dict["description"] = description
        if tags is not UNSET:
            field_dict["tags"] = tags
        if products is not UNSET:
            field_dict["products"] = products
        if product_versions is not UNSET:
            field_dict["product_versions"] = product_versions
        if product_streams is not UNSET:
            field_dict["product_streams"] = product_streams
        if channels is not UNSET:
            field_dict["channels"] = channels
        if meta_attr is not UNSET:
            field_dict["meta_attr"] = meta_attr

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        uuid = d.pop("uuid", UNSET)

        name = d.pop("name", UNSET)

        errata = d.pop("errata", UNSET)

        builds = d.pop("builds", UNSET)

        components = d.pop("components", UNSET)

        upstream = d.pop("upstream", UNSET)

        description = d.pop("description", UNSET)

        _tags = d.pop("tags", UNSET)
        tags: Union[Unset, ProductVariantTags]
        if isinstance(_tags, Unset):
            tags = UNSET
        else:
            tags = ProductVariantTags.from_dict(_tags)

        products = cast(List[str], d.pop("products", UNSET))

        product_versions = cast(List[str], d.pop("product_versions", UNSET))

        product_streams = cast(List[str], d.pop("product_streams", UNSET))

        channels = cast(List[str], d.pop("channels", UNSET))

        _meta_attr = d.pop("meta_attr", UNSET)
        meta_attr: Union[Unset, ProductVariantMetaAttr]
        if isinstance(_meta_attr, Unset):
            meta_attr = UNSET
        else:
            meta_attr = ProductVariantMetaAttr.from_dict(_meta_attr)

        product_variant = cls(
            uuid=uuid,
            name=name,
            errata=errata,
            builds=builds,
            components=components,
            upstream=upstream,
            description=description,
            tags=tags,
            products=products,
            product_versions=product_versions,
            product_streams=product_streams,
            channels=channels,
            meta_attr=meta_attr,
        )

        product_variant.additional_properties = d
        return product_variant

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
