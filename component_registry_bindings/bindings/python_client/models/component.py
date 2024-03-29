import json
from typing import Any, Dict, List, Tuple, Type, TypeVar, Union, cast

import attr

from ..models.component_channels_item import ComponentChannelsItem
from ..models.component_product_streams_item import ComponentProductStreamsItem
from ..models.component_product_variants_item import ComponentProductVariantsItem
from ..models.component_product_versions_item import ComponentProductVersionsItem
from ..models.component_products_item import ComponentProductsItem
from ..models.component_type_enum import ComponentTypeEnum
from ..models.namespace_enum import NamespaceEnum
from ..models.software_build_summary import SoftwareBuildSummary
from ..models.tag import Tag
from ..types import UNSET, ComponentRegistryModel, Unset

T = TypeVar("T", bound="Component")


@attr.s(auto_attribs=True)
class Component(ComponentRegistryModel):
    """Show detailed information for a Component.
    Add or remove fields using ?include_fields=&exclude_fields="""

    link: str
    download_url: str
    uuid: str
    type: ComponentTypeEnum
    namespace: NamespaceEnum
    purl: str
    name: str
    description: str
    related_url: str
    tags: List[Tag]
    version: str
    release: str
    el_match: List[str]
    arch: str
    nvr: str
    nevra: str
    epoch: int
    copyright_text: str
    license_concluded: str
    license_concluded_list: List[str]
    license_declared: str
    license_declared_list: List[str]
    openlcs_scan_url: str
    openlcs_scan_version: str
    software_build: SoftwareBuildSummary
    errata: List[str]
    products: List[ComponentProductsItem]
    product_versions: List[ComponentProductVersionsItem]
    product_streams: List[ComponentProductStreamsItem]
    product_variants: List[ComponentProductVariantsItem]
    channels: List[ComponentChannelsItem]
    sources: str
    provides: str
    upstreams: str
    manifest: str
    filename: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        link = self.link
        download_url = self.download_url
        uuid = self.uuid
        type: str = UNSET
        if not isinstance(self.type, Unset):

            type = ComponentTypeEnum(self.type).value

        namespace: str = UNSET
        if not isinstance(self.namespace, Unset):

            namespace = NamespaceEnum(self.namespace).value

        purl = self.purl
        name = self.name
        description = self.description
        related_url = self.related_url
        tags: List[Dict[str, Any]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = []
            for tags_item_data in self.tags:
                tags_item: Dict[str, Any] = UNSET
                if not isinstance(tags_item_data, Unset):
                    tags_item = tags_item_data.to_dict()

                tags.append(tags_item)

        version = self.version
        release = self.release
        el_match: List[str] = UNSET
        if not isinstance(self.el_match, Unset):
            el_match = self.el_match

        arch = self.arch
        nvr = self.nvr
        nevra = self.nevra
        epoch = self.epoch
        copyright_text = self.copyright_text
        license_concluded = self.license_concluded
        license_concluded_list: List[str] = UNSET
        if not isinstance(self.license_concluded_list, Unset):
            license_concluded_list = self.license_concluded_list

        license_declared = self.license_declared
        license_declared_list: List[str] = UNSET
        if not isinstance(self.license_declared_list, Unset):
            license_declared_list = self.license_declared_list

        openlcs_scan_url = self.openlcs_scan_url
        openlcs_scan_version = self.openlcs_scan_version
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

        channels: List[Dict[str, Any]] = UNSET
        if not isinstance(self.channels, Unset):
            channels = []
            for channels_item_data in self.channels:
                channels_item: Dict[str, Any] = UNSET
                if not isinstance(channels_item_data, Unset):
                    channels_item = channels_item_data.to_dict()

                channels.append(channels_item)

        sources = self.sources
        provides = self.provides
        upstreams = self.upstreams
        manifest = self.manifest
        filename = self.filename

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if not isinstance(link, Unset):
            field_dict["link"] = link
        if not isinstance(download_url, Unset):
            field_dict["download_url"] = download_url
        if not isinstance(uuid, Unset):
            field_dict["uuid"] = uuid
        if not isinstance(type, Unset):
            field_dict["type"] = type
        if not isinstance(namespace, Unset):
            field_dict["namespace"] = namespace
        if not isinstance(purl, Unset):
            field_dict["purl"] = purl
        if not isinstance(name, Unset):
            field_dict["name"] = name
        if not isinstance(description, Unset):
            field_dict["description"] = description
        if not isinstance(related_url, Unset):
            field_dict["related_url"] = related_url
        if not isinstance(tags, Unset):
            field_dict["tags"] = tags
        if not isinstance(version, Unset):
            field_dict["version"] = version
        if not isinstance(release, Unset):
            field_dict["release"] = release
        if not isinstance(el_match, Unset):
            field_dict["el_match"] = el_match
        if not isinstance(arch, Unset):
            field_dict["arch"] = arch
        if not isinstance(nvr, Unset):
            field_dict["nvr"] = nvr
        if not isinstance(nevra, Unset):
            field_dict["nevra"] = nevra
        if not isinstance(epoch, Unset):
            field_dict["epoch"] = epoch
        if not isinstance(copyright_text, Unset):
            field_dict["copyright_text"] = copyright_text
        if not isinstance(license_concluded, Unset):
            field_dict["license_concluded"] = license_concluded
        if not isinstance(license_concluded_list, Unset):
            field_dict["license_concluded_list"] = license_concluded_list
        if not isinstance(license_declared, Unset):
            field_dict["license_declared"] = license_declared
        if not isinstance(license_declared_list, Unset):
            field_dict["license_declared_list"] = license_declared_list
        if not isinstance(openlcs_scan_url, Unset):
            field_dict["openlcs_scan_url"] = openlcs_scan_url
        if not isinstance(openlcs_scan_version, Unset):
            field_dict["openlcs_scan_version"] = openlcs_scan_version
        if not isinstance(software_build, Unset):
            field_dict["software_build"] = software_build
        if not isinstance(errata, Unset):
            field_dict["errata"] = errata
        if not isinstance(products, Unset):
            field_dict["products"] = products
        if not isinstance(product_versions, Unset):
            field_dict["product_versions"] = product_versions
        if not isinstance(product_streams, Unset):
            field_dict["product_streams"] = product_streams
        if not isinstance(product_variants, Unset):
            field_dict["product_variants"] = product_variants
        if not isinstance(channels, Unset):
            field_dict["channels"] = channels
        if not isinstance(sources, Unset):
            field_dict["sources"] = sources
        if not isinstance(provides, Unset):
            field_dict["provides"] = provides
        if not isinstance(upstreams, Unset):
            field_dict["upstreams"] = upstreams
        if not isinstance(manifest, Unset):
            field_dict["manifest"] = manifest
        if not isinstance(filename, Unset):
            field_dict["filename"] = filename

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        link = self.link if self.link is UNSET else (None, str(self.link), "text/plain")
        download_url = (
            self.download_url
            if self.download_url is UNSET
            else (None, str(self.download_url), "text/plain")
        )
        uuid = self.uuid if self.uuid is UNSET else (None, str(self.uuid), "text/plain")
        type: Union[Unset, Tuple[None, str, str]] = UNSET
        if not isinstance(self.type, Unset):

            type = ComponentTypeEnum(self.type).value

        namespace: Union[Unset, Tuple[None, str, str]] = UNSET
        if not isinstance(self.namespace, Unset):

            namespace = NamespaceEnum(self.namespace).value

        purl = self.purl if self.purl is UNSET else (None, str(self.purl), "text/plain")
        name = self.name if self.name is UNSET else (None, str(self.name), "text/plain")
        description = (
            self.description
            if self.description is UNSET
            else (None, str(self.description), "text/plain")
        )
        related_url = (
            self.related_url
            if self.related_url is UNSET
            else (None, str(self.related_url), "text/plain")
        )
        tags: Union[Unset, Tuple[None, str, str]] = UNSET
        if not isinstance(self.tags, Unset):
            _temp_tags = []
            for tags_item_data in self.tags:
                tags_item: Dict[str, Any] = UNSET
                if not isinstance(tags_item_data, Unset):
                    tags_item = tags_item_data.to_dict()

                _temp_tags.append(tags_item)
            tags = (None, json.dumps(_temp_tags), "application/json")

        version = (
            self.version
            if self.version is UNSET
            else (None, str(self.version), "text/plain")
        )
        release = (
            self.release
            if self.release is UNSET
            else (None, str(self.release), "text/plain")
        )
        el_match: Union[Unset, Tuple[None, str, str]] = UNSET
        if not isinstance(self.el_match, Unset):
            _temp_el_match = self.el_match
            el_match = (None, json.dumps(_temp_el_match), "application/json")

        arch = self.arch if self.arch is UNSET else (None, str(self.arch), "text/plain")
        nvr = self.nvr if self.nvr is UNSET else (None, str(self.nvr), "text/plain")
        nevra = (
            self.nevra if self.nevra is UNSET else (None, str(self.nevra), "text/plain")
        )
        epoch = (
            self.epoch if self.epoch is UNSET else (None, str(self.epoch), "text/plain")
        )
        copyright_text = (
            self.copyright_text
            if self.copyright_text is UNSET
            else (None, str(self.copyright_text), "text/plain")
        )
        license_concluded = (
            self.license_concluded
            if self.license_concluded is UNSET
            else (None, str(self.license_concluded), "text/plain")
        )
        license_concluded_list: Union[Unset, Tuple[None, str, str]] = UNSET
        if not isinstance(self.license_concluded_list, Unset):
            _temp_license_concluded_list = self.license_concluded_list
            license_concluded_list = (
                None,
                json.dumps(_temp_license_concluded_list),
                "application/json",
            )

        license_declared = (
            self.license_declared
            if self.license_declared is UNSET
            else (None, str(self.license_declared), "text/plain")
        )
        license_declared_list: Union[Unset, Tuple[None, str, str]] = UNSET
        if not isinstance(self.license_declared_list, Unset):
            _temp_license_declared_list = self.license_declared_list
            license_declared_list = (
                None,
                json.dumps(_temp_license_declared_list),
                "application/json",
            )

        openlcs_scan_url = (
            self.openlcs_scan_url
            if self.openlcs_scan_url is UNSET
            else (None, str(self.openlcs_scan_url), "text/plain")
        )
        openlcs_scan_version = (
            self.openlcs_scan_version
            if self.openlcs_scan_version is UNSET
            else (None, str(self.openlcs_scan_version), "text/plain")
        )
        software_build: Union[Unset, Tuple[None, str, str]] = UNSET
        if not isinstance(self.software_build, Unset):
            software_build = (
                None,
                json.dumps(self.software_build.to_dict()),
                "application/json",
            )

        errata: Union[Unset, Tuple[None, str, str]] = UNSET
        if not isinstance(self.errata, Unset):
            _temp_errata = self.errata
            errata = (None, json.dumps(_temp_errata), "application/json")

        products: Union[Unset, Tuple[None, str, str]] = UNSET
        if not isinstance(self.products, Unset):
            _temp_products = []
            for products_item_data in self.products:
                products_item: Dict[str, Any] = UNSET
                if not isinstance(products_item_data, Unset):
                    products_item = products_item_data.to_dict()

                _temp_products.append(products_item)
            products = (None, json.dumps(_temp_products), "application/json")

        product_versions: Union[Unset, Tuple[None, str, str]] = UNSET
        if not isinstance(self.product_versions, Unset):
            _temp_product_versions = []
            for product_versions_item_data in self.product_versions:
                product_versions_item: Dict[str, Any] = UNSET
                if not isinstance(product_versions_item_data, Unset):
                    product_versions_item = product_versions_item_data.to_dict()

                _temp_product_versions.append(product_versions_item)
            product_versions = (
                None,
                json.dumps(_temp_product_versions),
                "application/json",
            )

        product_streams: Union[Unset, Tuple[None, str, str]] = UNSET
        if not isinstance(self.product_streams, Unset):
            _temp_product_streams = []
            for product_streams_item_data in self.product_streams:
                product_streams_item: Dict[str, Any] = UNSET
                if not isinstance(product_streams_item_data, Unset):
                    product_streams_item = product_streams_item_data.to_dict()

                _temp_product_streams.append(product_streams_item)
            product_streams = (
                None,
                json.dumps(_temp_product_streams),
                "application/json",
            )

        product_variants: Union[Unset, Tuple[None, str, str]] = UNSET
        if not isinstance(self.product_variants, Unset):
            _temp_product_variants = []
            for product_variants_item_data in self.product_variants:
                product_variants_item: Dict[str, Any] = UNSET
                if not isinstance(product_variants_item_data, Unset):
                    product_variants_item = product_variants_item_data.to_dict()

                _temp_product_variants.append(product_variants_item)
            product_variants = (
                None,
                json.dumps(_temp_product_variants),
                "application/json",
            )

        channels: Union[Unset, Tuple[None, str, str]] = UNSET
        if not isinstance(self.channels, Unset):
            _temp_channels = []
            for channels_item_data in self.channels:
                channels_item: Dict[str, Any] = UNSET
                if not isinstance(channels_item_data, Unset):
                    channels_item = channels_item_data.to_dict()

                _temp_channels.append(channels_item)
            channels = (None, json.dumps(_temp_channels), "application/json")

        sources = (
            self.sources
            if self.sources is UNSET
            else (None, str(self.sources), "text/plain")
        )
        provides = (
            self.provides
            if self.provides is UNSET
            else (None, str(self.provides), "text/plain")
        )
        upstreams = (
            self.upstreams
            if self.upstreams is UNSET
            else (None, str(self.upstreams), "text/plain")
        )
        manifest = (
            self.manifest
            if self.manifest is UNSET
            else (None, str(self.manifest), "text/plain")
        )
        filename = (
            self.filename
            if self.filename is UNSET
            else (None, str(self.filename), "text/plain")
        )

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                key: (None, str(value), "text/plain")
                for key, value in self.additional_properties.items()
            }
        )
        if not isinstance(link, Unset):
            field_dict["link"] = link
        if not isinstance(download_url, Unset):
            field_dict["download_url"] = download_url
        if not isinstance(uuid, Unset):
            field_dict["uuid"] = uuid
        if not isinstance(type, Unset):
            field_dict["type"] = type
        if not isinstance(namespace, Unset):
            field_dict["namespace"] = namespace
        if not isinstance(purl, Unset):
            field_dict["purl"] = purl
        if not isinstance(name, Unset):
            field_dict["name"] = name
        if not isinstance(description, Unset):
            field_dict["description"] = description
        if not isinstance(related_url, Unset):
            field_dict["related_url"] = related_url
        if not isinstance(tags, Unset):
            field_dict["tags"] = tags
        if not isinstance(version, Unset):
            field_dict["version"] = version
        if not isinstance(release, Unset):
            field_dict["release"] = release
        if not isinstance(el_match, Unset):
            field_dict["el_match"] = el_match
        if not isinstance(arch, Unset):
            field_dict["arch"] = arch
        if not isinstance(nvr, Unset):
            field_dict["nvr"] = nvr
        if not isinstance(nevra, Unset):
            field_dict["nevra"] = nevra
        if not isinstance(epoch, Unset):
            field_dict["epoch"] = epoch
        if not isinstance(copyright_text, Unset):
            field_dict["copyright_text"] = copyright_text
        if not isinstance(license_concluded, Unset):
            field_dict["license_concluded"] = license_concluded
        if not isinstance(license_concluded_list, Unset):
            field_dict["license_concluded_list"] = license_concluded_list
        if not isinstance(license_declared, Unset):
            field_dict["license_declared"] = license_declared
        if not isinstance(license_declared_list, Unset):
            field_dict["license_declared_list"] = license_declared_list
        if not isinstance(openlcs_scan_url, Unset):
            field_dict["openlcs_scan_url"] = openlcs_scan_url
        if not isinstance(openlcs_scan_version, Unset):
            field_dict["openlcs_scan_version"] = openlcs_scan_version
        if not isinstance(software_build, Unset):
            field_dict["software_build"] = software_build
        if not isinstance(errata, Unset):
            field_dict["errata"] = errata
        if not isinstance(products, Unset):
            field_dict["products"] = products
        if not isinstance(product_versions, Unset):
            field_dict["product_versions"] = product_versions
        if not isinstance(product_streams, Unset):
            field_dict["product_streams"] = product_streams
        if not isinstance(product_variants, Unset):
            field_dict["product_variants"] = product_variants
        if not isinstance(channels, Unset):
            field_dict["channels"] = channels
        if not isinstance(sources, Unset):
            field_dict["sources"] = sources
        if not isinstance(provides, Unset):
            field_dict["provides"] = provides
        if not isinstance(upstreams, Unset):
            field_dict["upstreams"] = upstreams
        if not isinstance(manifest, Unset):
            field_dict["manifest"] = manifest
        if not isinstance(filename, Unset):
            field_dict["filename"] = filename

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

        _namespace = d.pop("namespace", UNSET)
        namespace: NamespaceEnum
        if isinstance(_namespace, Unset):
            namespace = UNSET
        else:
            namespace = NamespaceEnum(_namespace)

        purl = d.pop("purl", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        related_url = d.pop("related_url", UNSET)

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

        release = d.pop("release", UNSET)

        el_match = cast(List[str], d.pop("el_match", UNSET))

        arch = d.pop("arch", UNSET)

        nvr = d.pop("nvr", UNSET)

        nevra = d.pop("nevra", UNSET)

        epoch = d.pop("epoch", UNSET)

        copyright_text = d.pop("copyright_text", UNSET)

        license_concluded = d.pop("license_concluded", UNSET)

        license_concluded_list = cast(List[str], d.pop("license_concluded_list", UNSET))

        license_declared = d.pop("license_declared", UNSET)

        license_declared_list = cast(List[str], d.pop("license_declared_list", UNSET))

        openlcs_scan_url = d.pop("openlcs_scan_url", UNSET)

        openlcs_scan_version = d.pop("openlcs_scan_version", UNSET)

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
                    product_versions_item = ComponentProductVersionsItem.from_dict(
                        _product_versions_item
                    )

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
                    product_streams_item = ComponentProductStreamsItem.from_dict(
                        _product_streams_item
                    )

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
                    product_variants_item = ComponentProductVariantsItem.from_dict(
                        _product_variants_item
                    )

                product_variants.append(product_variants_item)

        channels = []
        _channels = d.pop("channels", UNSET)
        if _channels is UNSET:
            channels = UNSET
        else:
            for channels_item_data in _channels or []:
                _channels_item = channels_item_data
                channels_item: ComponentChannelsItem
                if isinstance(_channels_item, Unset):
                    channels_item = UNSET
                else:
                    channels_item = ComponentChannelsItem.from_dict(_channels_item)

                channels.append(channels_item)

        sources = d.pop("sources", UNSET)

        provides = d.pop("provides", UNSET)

        upstreams = d.pop("upstreams", UNSET)

        manifest = d.pop("manifest", UNSET)

        filename = d.pop("filename", UNSET)

        component = cls(
            link=link,
            download_url=download_url,
            uuid=uuid,
            type=type,
            namespace=namespace,
            purl=purl,
            name=name,
            description=description,
            related_url=related_url,
            tags=tags,
            version=version,
            release=release,
            el_match=el_match,
            arch=arch,
            nvr=nvr,
            nevra=nevra,
            epoch=epoch,
            copyright_text=copyright_text,
            license_concluded=license_concluded,
            license_concluded_list=license_concluded_list,
            license_declared=license_declared,
            license_declared_list=license_declared_list,
            openlcs_scan_url=openlcs_scan_url,
            openlcs_scan_version=openlcs_scan_version,
            software_build=software_build,
            errata=errata,
            products=products,
            product_versions=product_versions,
            product_streams=product_streams,
            product_variants=product_variants,
            channels=channels,
            sources=sources,
            provides=provides,
            upstreams=upstreams,
            manifest=manifest,
            filename=filename,
        )

        component.additional_properties = d
        return component

    @staticmethod
    def get_fields():
        return {
            "link": str,
            "download_url": str,
            "uuid": str,
            "type": ComponentTypeEnum,
            "namespace": NamespaceEnum,
            "purl": str,
            "name": str,
            "description": str,
            "related_url": str,
            "tags": List[Tag],
            "version": str,
            "release": str,
            "el_match": List[str],
            "arch": str,
            "nvr": str,
            "nevra": str,
            "epoch": int,
            "copyright_text": str,
            "license_concluded": str,
            "license_concluded_list": List[str],
            "license_declared": str,
            "license_declared_list": List[str],
            "openlcs_scan_url": str,
            "openlcs_scan_version": str,
            "software_build": SoftwareBuildSummary,
            "errata": List[str],
            "products": List[ComponentProductsItem],
            "product_versions": List[ComponentProductVersionsItem],
            "product_streams": List[ComponentProductStreamsItem],
            "product_variants": List[ComponentProductVariantsItem],
            "channels": List[ComponentChannelsItem],
            "sources": str,
            "provides": str,
            "upstreams": str,
            "manifest": str,
            "filename": str,
        }

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
