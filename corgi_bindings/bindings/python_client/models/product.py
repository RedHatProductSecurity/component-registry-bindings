import json
from typing import Any, Dict, List, Tuple, Type, TypeVar, Union, cast

import attr

from ..models.product_meta_attr import ProductMetaAttr
from ..models.product_tags import ProductTags
from ..types import UNSET, Unset

T = TypeVar("T", bound="Product")


@attr.s(auto_attribs=True)
class Product:
    """product detail serializer"""

    uuid: str
    name: str
    errata: str
    builds: str
    components: str
    upstream: str
    description: Union[Unset, None, str] = UNSET
    tags: Union[Unset, ProductTags] = UNSET
    product_versions: Union[Unset, None, List[str]] = UNSET
    product_streams: Union[Unset, None, List[str]] = UNSET
    product_variants: Union[Unset, None, List[str]] = UNSET
    channels: Union[Unset, None, List[str]] = UNSET
    meta_attr: Union[Unset, None, ProductMetaAttr] = UNSET
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

        product_versions: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.product_versions, Unset):
            if self.product_versions is None:
                product_versions = None
            else:
                product_versions = self.product_versions

        product_streams: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.product_streams, Unset):
            if self.product_streams is None:
                product_streams = None
            else:
                product_streams = self.product_streams

        product_variants: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.product_variants, Unset):
            if self.product_variants is None:
                product_variants = None
            else:
                product_variants = self.product_variants

        channels: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.channels, Unset):
            if self.channels is None:
                channels = None
            else:
                channels = self.channels

        meta_attr: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.meta_attr, Unset):
            meta_attr = self.meta_attr.to_dict() if self.meta_attr else None

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
        if product_versions is not UNSET:
            field_dict["product_versions"] = product_versions
        if product_streams is not UNSET:
            field_dict["product_streams"] = product_streams
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
        description = self.description if self.description is UNSET else (None, str(self.description), "text/plain")
        tags: Union[Unset, Tuple[None, str, str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = (None, json.dumps(self.tags.to_dict()), "application/json")

        product_versions: Union[Unset, Tuple[None, str, str]] = UNSET
        if not isinstance(self.product_versions, Unset):
            if self.product_versions is None:
                product_versions = None
            else:
                _temp_product_versions = self.product_versions
                product_versions = (None, json.dumps(_temp_product_versions), "application/json")

        product_streams: Union[Unset, Tuple[None, str, str]] = UNSET
        if not isinstance(self.product_streams, Unset):
            if self.product_streams is None:
                product_streams = None
            else:
                _temp_product_streams = self.product_streams
                product_streams = (None, json.dumps(_temp_product_streams), "application/json")

        product_variants: Union[Unset, Tuple[None, str, str]] = UNSET
        if not isinstance(self.product_variants, Unset):
            if self.product_variants is None:
                product_variants = None
            else:
                _temp_product_variants = self.product_variants
                product_variants = (None, json.dumps(_temp_product_variants), "application/json")

        channels: Union[Unset, Tuple[None, str, str]] = UNSET
        if not isinstance(self.channels, Unset):
            if self.channels is None:
                channels = None
            else:
                _temp_channels = self.channels
                channels = (None, json.dumps(_temp_channels), "application/json")

        meta_attr: Union[Unset, Tuple[None, str, str]] = UNSET
        if not isinstance(self.meta_attr, Unset):
            meta_attr = (None, json.dumps(self.meta_attr.to_dict()), "application/json") if self.meta_attr else None

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
        if product_versions is not UNSET:
            field_dict["product_versions"] = product_versions
        if product_streams is not UNSET:
            field_dict["product_streams"] = product_streams
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

        description = d.pop("description", UNSET)

        _tags = d.pop("tags", UNSET)
        tags: Union[Unset, ProductTags]
        if isinstance(_tags, Unset):
            tags = UNSET
        else:
            tags = ProductTags.from_dict(_tags)

        product_versions = cast(List[str], d.pop("product_versions", UNSET))

        product_streams = cast(List[str], d.pop("product_streams", UNSET))

        product_variants = cast(List[str], d.pop("product_variants", UNSET))

        channels = cast(List[str], d.pop("channels", UNSET))

        _meta_attr = d.pop("meta_attr", UNSET)
        meta_attr: Union[Unset, None, ProductMetaAttr]
        if _meta_attr is None:
            meta_attr = None
        elif isinstance(_meta_attr, Unset):
            meta_attr = UNSET
        else:
            meta_attr = ProductMetaAttr.from_dict(_meta_attr)

        product = cls(
            uuid=uuid,
            name=name,
            errata=errata,
            builds=builds,
            components=components,
            upstream=upstream,
            description=description,
            tags=tags,
            product_versions=product_versions,
            product_streams=product_streams,
            product_variants=product_variants,
            channels=channels,
            meta_attr=meta_attr,
        )

        product.additional_properties = d
        return product

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
