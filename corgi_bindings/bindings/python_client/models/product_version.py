from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.component_list import ComponentList
from ..models.product_version_meta_attr import ProductVersionMetaAttr
from ..models.tag import Tag
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProductVersion")


@attr.s(auto_attribs=True)
class ProductVersion:
    """ """

    link: str
    uuid: str
    name: str
    tags: List[Tag]
    products: str
    product_streams: str
    product_variants: str
    errata: str
    builds: str
    components: List[ComponentList]
    manifest: str
    upstream: str
    ofuri: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    channels: Union[Unset, List[str]] = UNSET
    meta_attr: Union[Unset, ProductVersionMetaAttr] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        link = self.link
        uuid = self.uuid
        name = self.name
        tags: List[Dict[str, Any]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = []
            for tags_item_data in self.tags:
                tags_item: Dict[str, Any] = UNSET
                if not isinstance(tags_item_data, Unset):
                    tags_item = tags_item_data.to_dict()

                tags.append(tags_item)

        products = self.products
        product_streams = self.product_streams
        product_variants = self.product_variants
        errata = self.errata
        builds = self.builds
        components: List[Dict[str, Any]] = UNSET
        if not isinstance(self.components, Unset):
            components = []
            for components_item_data in self.components:
                components_item: Dict[str, Any] = UNSET
                if not isinstance(components_item_data, Unset):
                    components_item = components_item_data.to_dict()

                components.append(components_item)

        manifest = self.manifest
        upstream = self.upstream
        ofuri = self.ofuri
        description = self.description
        channels: Union[Unset, List[str]] = UNSET
        if not isinstance(self.channels, Unset):
            channels = self.channels

        meta_attr: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.meta_attr, Unset):
            meta_attr = self.meta_attr.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if link is not UNSET:
            field_dict["link"] = link
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if name is not UNSET:
            field_dict["name"] = name
        if tags is not UNSET:
            field_dict["tags"] = tags
        if products is not UNSET:
            field_dict["products"] = products
        if product_streams is not UNSET:
            field_dict["product_streams"] = product_streams
        if product_variants is not UNSET:
            field_dict["product_variants"] = product_variants
        if errata is not UNSET:
            field_dict["errata"] = errata
        if builds is not UNSET:
            field_dict["builds"] = builds
        if components is not UNSET:
            field_dict["components"] = components
        if manifest is not UNSET:
            field_dict["manifest"] = manifest
        if upstream is not UNSET:
            field_dict["upstream"] = upstream
        if ofuri is not UNSET:
            field_dict["ofuri"] = ofuri
        if description is not UNSET:
            field_dict["description"] = description
        if channels is not UNSET:
            field_dict["channels"] = channels
        if meta_attr is not UNSET:
            field_dict["meta_attr"] = meta_attr

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy() if isinstance(src_dict, dict) else {}
        link = d.pop("link", UNSET)

        uuid = d.pop("uuid", UNSET)

        name = d.pop("name", UNSET)

        tags = []
        _tags = d.pop("tags", UNSET)
        if _tags is UNSET:
            tags = UNSET
        else:
            for tags_item_data in _tags or []:
                _tags_item = tags_item_data
                tags_item: Tag
                if isinstance(_tags_item, Unset):
                    tags_item = UNSET
                else:
                    tags_item = Tag.from_dict(_tags_item)

                tags.append(tags_item)

        products = d.pop("products", UNSET)

        product_streams = d.pop("product_streams", UNSET)

        product_variants = d.pop("product_variants", UNSET)

        errata = d.pop("errata", UNSET)

        builds = d.pop("builds", UNSET)

        components = []
        _components = d.pop("components", UNSET)
        if _components is UNSET:
            components = UNSET
        else:
            for components_item_data in _components or []:
                _components_item = components_item_data
                components_item: ComponentList
                if isinstance(_components_item, Unset):
                    components_item = UNSET
                else:
                    components_item = ComponentList.from_dict(_components_item)

                components.append(components_item)

        manifest = d.pop("manifest", UNSET)

        upstream = d.pop("upstream", UNSET)

        ofuri = d.pop("ofuri", UNSET)

        description = d.pop("description", UNSET)

        channels = cast(List[str], d.pop("channels", UNSET))

        _meta_attr = d.pop("meta_attr", UNSET)
        meta_attr: Union[Unset, ProductVersionMetaAttr]
        if isinstance(_meta_attr, Unset):
            meta_attr = UNSET
        else:
            meta_attr = ProductVersionMetaAttr.from_dict(_meta_attr)

        product_version = cls(
            link=link,
            uuid=uuid,
            name=name,
            tags=tags,
            products=products,
            product_streams=product_streams,
            product_variants=product_variants,
            errata=errata,
            builds=builds,
            components=components,
            manifest=manifest,
            upstream=upstream,
            ofuri=ofuri,
            description=description,
            channels=channels,
            meta_attr=meta_attr,
        )

        product_version.additional_properties = d
        return product_version

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
