from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.component_product_streams_item import ComponentProductStreamsItem
from ..models.component_product_variants_item import ComponentProductVariantsItem
from ..models.component_product_versions_item import ComponentProductVersionsItem
from ..models.component_products_item import ComponentProductsItem
from ..models.component_provides_item import ComponentProvidesItem
from ..models.component_sources_item import ComponentSourcesItem
from ..models.component_type_enum import ComponentTypeEnum
from ..models.component_upstreams_item import ComponentUpstreamsItem
from ..models.software_build_summary import SoftwareBuildSummary
from ..models.tag import Tag
from ..types import UNSET, Unset

T = TypeVar("T", bound="Component")


@attr.s(auto_attribs=True)
class Component:
    """ """

    link: str
    download_url: str
    uuid: str
    type: ComponentTypeEnum
    name: str
    description: str
    tags: List[Tag]
    version: str
    epoch: str
    license_list: List[str]
    software_build: SoftwareBuildSummary
    errata: List[str]
    products: List[ComponentProductsItem]
    product_versions: List[ComponentProductVersionsItem]
    product_streams: List[ComponentProductStreamsItem]
    product_variants: List[ComponentProductVariantsItem]
    sources: List[ComponentSourcesItem]
    provides: List[ComponentProvidesItem]
    upstreams: List[ComponentUpstreamsItem]
    purl: Union[Unset, str] = UNSET
    related_url: Union[Unset, None, str] = UNSET
    release: Union[Unset, str] = UNSET
    arch: Union[Unset, str] = UNSET
    nvr: Union[Unset, str] = UNSET
    nevra: Union[Unset, str] = UNSET
    license_: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        link = self.link
        download_url = self.download_url
        uuid = self.uuid
        type: str = UNSET
        if not isinstance(self.type, Unset):

            type = ComponentTypeEnum(self.type).value

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

        products: List[Dict[str, Any]] = UNSET
        if not isinstance(self.products, Unset):
            products = []
            for products_item_data in self.products:
                products_item: Dict[str, Any] = UNSET
                if not isinstance(products_item_data, Unset):
                    products_item = products_item_data.to_dict()

                products.append(products_item)

        product_versions: List[Dict[str, Any]] = UNSET
        if not isinstance(self.product_versions, Unset):
            product_versions = []
            for product_versions_item_data in self.product_versions:
                product_versions_item: Dict[str, Any] = UNSET
                if not isinstance(product_versions_item_data, Unset):
                    product_versions_item = product_versions_item_data.to_dict()

                product_versions.append(product_versions_item)

        product_streams: List[Dict[str, Any]] = UNSET
        if not isinstance(self.product_streams, Unset):
            product_streams = []
            for product_streams_item_data in self.product_streams:
                product_streams_item: Dict[str, Any] = UNSET
                if not isinstance(product_streams_item_data, Unset):
                    product_streams_item = product_streams_item_data.to_dict()

                product_streams.append(product_streams_item)

        product_variants: List[Dict[str, Any]] = UNSET
        if not isinstance(self.product_variants, Unset):
            product_variants = []
            for product_variants_item_data in self.product_variants:
                product_variants_item: Dict[str, Any] = UNSET
                if not isinstance(product_variants_item_data, Unset):
                    product_variants_item = product_variants_item_data.to_dict()

                product_variants.append(product_variants_item)

        sources: List[Dict[str, Any]] = UNSET
        if not isinstance(self.sources, Unset):
            sources = []
            for sources_item_data in self.sources:
                sources_item: Dict[str, Any] = UNSET
                if not isinstance(sources_item_data, Unset):
                    sources_item = sources_item_data.to_dict()

                sources.append(sources_item)

        provides: List[Dict[str, Any]] = UNSET
        if not isinstance(self.provides, Unset):
            provides = []
            for provides_item_data in self.provides:
                provides_item: Dict[str, Any] = UNSET
                if not isinstance(provides_item_data, Unset):
                    provides_item = provides_item_data.to_dict()

                provides.append(provides_item)

        upstreams: List[Dict[str, Any]] = UNSET
        if not isinstance(self.upstreams, Unset):
            upstreams = []
            for upstreams_item_data in self.upstreams:
                upstreams_item: Dict[str, Any] = UNSET
                if not isinstance(upstreams_item_data, Unset):
                    upstreams_item = upstreams_item_data.to_dict()

                upstreams.append(upstreams_item)

        purl = self.purl
        related_url = self.related_url
        release = self.release
        arch = self.arch
        nvr = self.nvr
        nevra = self.nevra
        license_ = self.license_

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if link is not UNSET:
            field_dict["link"] = link
        if download_url is not UNSET:
            field_dict["download_url"] = download_url
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
        if upstreams is not UNSET:
            field_dict["upstreams"] = upstreams
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

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy() if isinstance(src_dict, dict) else {}
        link = d.pop("link", UNSET)

        download_url = d.pop("download_url", UNSET)

        uuid = d.pop("uuid", UNSET)

        _type = d.pop("type", UNSET)
        type: ComponentTypeEnum
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = ComponentTypeEnum(_type)

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

        products = []
        _products = d.pop("products", UNSET)
        if _products is UNSET:
            products = UNSET
        else:
            for products_item_data in _products or []:
                _products_item = products_item_data
                products_item: ComponentProductsItem
                if isinstance(_products_item, Unset):
                    products_item = UNSET
                else:
                    products_item = ComponentProductsItem.from_dict(_products_item)

                products.append(products_item)

        product_versions = []
        _product_versions = d.pop("product_versions", UNSET)
        if _product_versions is UNSET:
            product_versions = UNSET
        else:
            for product_versions_item_data in _product_versions or []:
                _product_versions_item = product_versions_item_data
                product_versions_item: ComponentProductVersionsItem
                if isinstance(_product_versions_item, Unset):
                    product_versions_item = UNSET
                else:
                    product_versions_item = ComponentProductVersionsItem.from_dict(_product_versions_item)

                product_versions.append(product_versions_item)

        product_streams = []
        _product_streams = d.pop("product_streams", UNSET)
        if _product_streams is UNSET:
            product_streams = UNSET
        else:
            for product_streams_item_data in _product_streams or []:
                _product_streams_item = product_streams_item_data
                product_streams_item: ComponentProductStreamsItem
                if isinstance(_product_streams_item, Unset):
                    product_streams_item = UNSET
                else:
                    product_streams_item = ComponentProductStreamsItem.from_dict(_product_streams_item)

                product_streams.append(product_streams_item)

        product_variants = []
        _product_variants = d.pop("product_variants", UNSET)
        if _product_variants is UNSET:
            product_variants = UNSET
        else:
            for product_variants_item_data in _product_variants or []:
                _product_variants_item = product_variants_item_data
                product_variants_item: ComponentProductVariantsItem
                if isinstance(_product_variants_item, Unset):
                    product_variants_item = UNSET
                else:
                    product_variants_item = ComponentProductVariantsItem.from_dict(_product_variants_item)

                product_variants.append(product_variants_item)

        sources = []
        _sources = d.pop("sources", UNSET)
        if _sources is UNSET:
            sources = UNSET
        else:
            for sources_item_data in _sources or []:
                _sources_item = sources_item_data
                sources_item: ComponentSourcesItem
                if isinstance(_sources_item, Unset):
                    sources_item = UNSET
                else:
                    sources_item = ComponentSourcesItem.from_dict(_sources_item)

                sources.append(sources_item)

        provides = []
        _provides = d.pop("provides", UNSET)
        if _provides is UNSET:
            provides = UNSET
        else:
            for provides_item_data in _provides or []:
                _provides_item = provides_item_data
                provides_item: ComponentProvidesItem
                if isinstance(_provides_item, Unset):
                    provides_item = UNSET
                else:
                    provides_item = ComponentProvidesItem.from_dict(_provides_item)

                provides.append(provides_item)

        upstreams = []
        _upstreams = d.pop("upstreams", UNSET)
        if _upstreams is UNSET:
            upstreams = UNSET
        else:
            for upstreams_item_data in _upstreams or []:
                _upstreams_item = upstreams_item_data
                upstreams_item: ComponentUpstreamsItem
                if isinstance(_upstreams_item, Unset):
                    upstreams_item = UNSET
                else:
                    upstreams_item = ComponentUpstreamsItem.from_dict(_upstreams_item)

                upstreams.append(upstreams_item)

        purl = d.pop("purl", UNSET)

        related_url = d.pop("related_url", UNSET)

        release = d.pop("release", UNSET)

        arch = d.pop("arch", UNSET)

        nvr = d.pop("nvr", UNSET)

        nevra = d.pop("nevra", UNSET)

        license_ = d.pop("license", UNSET)

        component = cls(
            link=link,
            download_url=download_url,
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
            upstreams=upstreams,
            purl=purl,
            related_url=related_url,
            release=release,
            arch=arch,
            nvr=nvr,
            nevra=nevra,
            license_=license_,
        )

        component.additional_properties = d
        return component

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
