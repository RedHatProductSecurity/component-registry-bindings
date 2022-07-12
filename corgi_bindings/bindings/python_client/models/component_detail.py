from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.component_detail_meta_attr import ComponentDetailMetaAttr
from ..models.software_build_summary import SoftwareBuildSummary
from ..models.tag import Tag
from ..models.type_1b3_enum import Type1B3Enum
from ..types import UNSET, Unset

T = TypeVar("T", bound="ComponentDetail")


@attr.s(auto_attribs=True)
class ComponentDetail:
    """ """

    link: str
    uuid: str
    type: Type1B3Enum
    name: str
    description: str
    tags: List[Tag]
    version: str
    epoch: str
    license_list: List[str]
    software_build: SoftwareBuildSummary
    errata: List[str]
    products: str
    product_versions: str
    product_streams: str
    product_variants: str
    sources: str
    provides: str
    upstream: str
    purl: Union[Unset, str] = UNSET
    related_url: Union[Unset, None, str] = UNSET
    release: Union[Unset, str] = UNSET
    arch: Union[Unset, str] = UNSET
    nvr: Union[Unset, str] = UNSET
    nevra: Union[Unset, str] = UNSET
    license_: Union[Unset, str] = UNSET
    meta_attr: Union[Unset, ComponentDetailMetaAttr] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        link = self.link
        uuid = self.uuid
        type: str = UNSET
        if not isinstance(self.type, Unset):

            type = Type1B3Enum(self.type).value

        name = self.name
        description = self.description
        tags: List[Dict[str, Any]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = []
            for tags_item_data in self.tags:
                tags_item: Dict[str, Any] = UNSET
                if not isinstance(tags_item_data, Unset):
                    tags_item = tags_item_data.to_dict()

                tags.append(tags_item)

        version = self.version
        epoch = self.epoch
        license_list: List[str] = UNSET
        if not isinstance(self.license_list, Unset):
            license_list = self.license_list

        software_build: Dict[str, Any] = UNSET
        if not isinstance(self.software_build, Unset):
            software_build = self.software_build.to_dict()

        errata: List[str] = UNSET
        if not isinstance(self.errata, Unset):
            errata = self.errata

        products = self.products
        product_versions = self.product_versions
        product_streams = self.product_streams
        product_variants = self.product_variants
        sources = self.sources
        provides = self.provides
        upstream = self.upstream
        purl = self.purl
        related_url = self.related_url
        release = self.release
        arch = self.arch
        nvr = self.nvr
        nevra = self.nevra
        license_ = self.license_
        meta_attr: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.meta_attr, Unset):
            meta_attr = self.meta_attr.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if link is not UNSET:
            field_dict["link"] = link
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if type is not UNSET:
            field_dict["type"] = type
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if tags is not UNSET:
            field_dict["tags"] = tags
        if version is not UNSET:
            field_dict["version"] = version
        if epoch is not UNSET:
            field_dict["epoch"] = epoch
        if license_list is not UNSET:
            field_dict["license_list"] = license_list
        if software_build is not UNSET:
            field_dict["software_build"] = software_build
        if errata is not UNSET:
            field_dict["errata"] = errata
        if products is not UNSET:
            field_dict["products"] = products
        if product_versions is not UNSET:
            field_dict["product_versions"] = product_versions
        if product_streams is not UNSET:
            field_dict["product_streams"] = product_streams
        if product_variants is not UNSET:
            field_dict["product_variants"] = product_variants
        if sources is not UNSET:
            field_dict["sources"] = sources
        if provides is not UNSET:
            field_dict["provides"] = provides
        if upstream is not UNSET:
            field_dict["upstream"] = upstream
        if purl is not UNSET:
            field_dict["purl"] = purl
        if related_url is not UNSET:
            field_dict["related_url"] = related_url
        if release is not UNSET:
            field_dict["release"] = release
        if arch is not UNSET:
            field_dict["arch"] = arch
        if nvr is not UNSET:
            field_dict["nvr"] = nvr
        if nevra is not UNSET:
            field_dict["nevra"] = nevra
        if license_ is not UNSET:
            field_dict["license"] = license_
        if meta_attr is not UNSET:
            field_dict["meta_attr"] = meta_attr

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy() if isinstance(src_dict, dict) else {}
        link = d.pop("link", UNSET)

        uuid = d.pop("uuid", UNSET)

        _type = d.pop("type", UNSET)
        type: Type1B3Enum
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = Type1B3Enum(_type)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

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

        version = d.pop("version", UNSET)

        epoch = d.pop("epoch", UNSET)

        license_list = cast(List[str], d.pop("license_list", UNSET))

        _software_build = d.pop("software_build", UNSET)
        software_build: SoftwareBuildSummary
        if isinstance(_software_build, Unset):
            software_build = UNSET
        else:
            software_build = SoftwareBuildSummary.from_dict(_software_build)

        errata = cast(List[str], d.pop("errata", UNSET))

        products = d.pop("products", UNSET)

        product_versions = d.pop("product_versions", UNSET)

        product_streams = d.pop("product_streams", UNSET)

        product_variants = d.pop("product_variants", UNSET)

        sources = d.pop("sources", UNSET)

        provides = d.pop("provides", UNSET)

        upstream = d.pop("upstream", UNSET)

        purl = d.pop("purl", UNSET)

        related_url = d.pop("related_url", UNSET)

        release = d.pop("release", UNSET)

        arch = d.pop("arch", UNSET)

        nvr = d.pop("nvr", UNSET)

        nevra = d.pop("nevra", UNSET)

        license_ = d.pop("license", UNSET)

        _meta_attr = d.pop("meta_attr", UNSET)
        meta_attr: Union[Unset, ComponentDetailMetaAttr]
        if isinstance(_meta_attr, Unset):
            meta_attr = UNSET
        else:
            meta_attr = ComponentDetailMetaAttr.from_dict(_meta_attr)

        component_detail = cls(
            link=link,
            uuid=uuid,
            type=type,
            name=name,
            description=description,
            tags=tags,
            version=version,
            epoch=epoch,
            license_list=license_list,
            software_build=software_build,
            errata=errata,
            products=products,
            product_versions=product_versions,
            product_streams=product_streams,
            product_variants=product_variants,
            sources=sources,
            provides=provides,
            upstream=upstream,
            purl=purl,
            related_url=related_url,
            release=release,
            arch=arch,
            nvr=nvr,
            nevra=nevra,
            license_=license_,
            meta_attr=meta_attr,
        )

        component_detail.additional_properties = d
        return component_detail

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
