import json
from typing import Any, Dict, List, Tuple, Type, TypeVar, Union, cast

import attr

from ..models.product_stream_meta_attr import ProductStreamMetaAttr
from ..models.product_stream_tags import ProductStreamTags
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProductStream")


@attr.s(auto_attribs=True)
class ProductStream:
    """product stream serializer"""

    uuid: str
    name: str
    errata: str
    builds: str
    components: str
    upstream: str
    cpe: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    tags: Union[Unset, ProductStreamTags] = UNSET
    products: Union[Unset, List[str]] = UNSET
    product_versions: Union[Unset, List[str]] = UNSET
    product_variants: Union[Unset, List[str]] = UNSET
    channels: Union[Unset, List[str]] = UNSET
    meta_attr: Union[Unset, ProductStreamMetaAttr] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        uuid = self.uuid
        name = self.name
        errata = self.errata
        builds = self.builds
        components = self.components
        upstream = self.upstream
        cpe = self.cpe
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

        product_variants: Union[Unset, List[str]] = UNSET
        if not isinstance(self.product_variants, Unset):
            product_variants = self.product_variants

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
        if cpe is not UNSET:
            field_dict["cpe"] = cpe
        if description is not UNSET:
            field_dict["description"] = description
        if tags is not UNSET:
            field_dict["tags"] = tags
        if products is not UNSET:
            field_dict["products"] = products
        if product_versions is not UNSET:
            field_dict["product_versions"] = product_versions
        if product_variants is not UNSET:
            field_dict["product_variants"] = product_variants
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
        cpe = self.cpe if self.cpe is UNSET else (None, str(self.cpe), "text/plain")
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

        product_variants: Union[Unset, Tuple[None, str, str]] = UNSET
        if not isinstance(self.product_variants, Unset):
            _temp_product_variants = self.product_variants
            product_variants = (None, json.dumps(_temp_product_variants), "application/json")

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
        if cpe is not UNSET:
            field_dict["cpe"] = cpe
        if description is not UNSET:
            field_dict["description"] = description
        if tags is not UNSET:
            field_dict["tags"] = tags
        if products is not UNSET:
            field_dict["products"] = products
        if product_versions is not UNSET:
            field_dict["product_versions"] = product_versions
        if product_variants is not UNSET:
            field_dict["product_variants"] = product_variants
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

        cpe = d.pop("cpe", UNSET)

        description = d.pop("description", UNSET)

        _tags = d.pop("tags", UNSET)
        tags: Union[Unset, ProductStreamTags]
        if isinstance(_tags, Unset):
            tags = UNSET
        else:
            tags = ProductStreamTags.from_dict(_tags)

        products = cast(List[str], d.pop("products", UNSET))

        product_versions = cast(List[str], d.pop("product_versions", UNSET))

        product_variants = cast(List[str], d.pop("product_variants", UNSET))

        channels = cast(List[str], d.pop("channels", UNSET))

        _meta_attr = d.pop("meta_attr", UNSET)
        meta_attr: Union[Unset, ProductStreamMetaAttr]
        if isinstance(_meta_attr, Unset):
            meta_attr = UNSET
        else:
            meta_attr = ProductStreamMetaAttr.from_dict(_meta_attr)

        product_stream = cls(
            uuid=uuid,
            name=name,
            errata=errata,
            builds=builds,
            components=components,
            upstream=upstream,
            cpe=cpe,
            description=description,
            tags=tags,
            products=products,
            product_versions=product_versions,
            product_variants=product_variants,
            channels=channels,
            meta_attr=meta_attr,
        )

        product_stream.additional_properties = d
        return product_stream

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
