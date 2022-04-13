import json
from typing import Any, Dict, List, Tuple, Type, TypeVar, Union, cast

import attr

from ..models.component_detail_meta_attr import ComponentDetailMetaAttr
from ..models.component_detail_tags import ComponentDetailTags
from ..types import UNSET, Unset

T = TypeVar("T", bound="ComponentDetail")


@attr.s(auto_attribs=True)
class ComponentDetail:
    """Component detail serializer

    TODO - most of these serialisations are experimental, we may push to the model itself and/or
    generalise."""

    uuid: str
    nvr: str
    epoch: str
    license_: str
    software_build: str
    errata: str
    purl: Union[Unset, None, str] = UNSET
    name: Union[Unset, None, str] = UNSET
    description: Union[Unset, None, str] = UNSET
    tags: Union[Unset, ComponentDetailTags] = UNSET
    version: Union[Unset, None, str] = UNSET
    release: Union[Unset, None, str] = UNSET
    arch: Union[Unset, None, str] = UNSET
    products: Union[Unset, None, List[str]] = UNSET
    product_versions: Union[Unset, None, List[str]] = UNSET
    product_streams: Union[Unset, None, List[str]] = UNSET
    product_variants: Union[Unset, None, List[str]] = UNSET
    sources: Union[Unset, None, List[str]] = UNSET
    provides: Union[Unset, None, List[str]] = UNSET
    upstream: Union[Unset, None, List[str]] = UNSET
    meta_attr: Union[Unset, None, ComponentDetailMetaAttr] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        uuid = self.uuid
        nvr = self.nvr
        epoch = self.epoch
        license_ = self.license_
        software_build = self.software_build
        errata = self.errata
        purl = self.purl
        name = self.name
        description = self.description
        tags: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags.to_dict()

        version = self.version
        release = self.release
        arch = self.arch
        products: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.products, Unset):
            if self.products is None:
                products = None
            else:
                products = self.products

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

        sources: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.sources, Unset):
            if self.sources is None:
                sources = None
            else:
                sources = self.sources

        provides: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.provides, Unset):
            if self.provides is None:
                provides = None
            else:
                provides = self.provides

        upstream: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.upstream, Unset):
            if self.upstream is None:
                upstream = None
            else:
                upstream = self.upstream

        meta_attr: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.meta_attr, Unset):
            meta_attr = self.meta_attr.to_dict() if self.meta_attr else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if nvr is not UNSET:
            field_dict["nvr"] = nvr
        if epoch is not UNSET:
            field_dict["epoch"] = epoch
        if license_ is not UNSET:
            field_dict["license"] = license_
        if software_build is not UNSET:
            field_dict["software_build"] = software_build
        if errata is not UNSET:
            field_dict["errata"] = errata
        if purl is not UNSET:
            field_dict["purl"] = purl
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if tags is not UNSET:
            field_dict["tags"] = tags
        if version is not UNSET:
            field_dict["version"] = version
        if release is not UNSET:
            field_dict["release"] = release
        if arch is not UNSET:
            field_dict["arch"] = arch
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
        if meta_attr is not UNSET:
            field_dict["meta_attr"] = meta_attr

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        uuid = self.uuid if self.uuid is UNSET else (None, str(self.uuid), "text/plain")
        nvr = self.nvr if self.nvr is UNSET else (None, str(self.nvr), "text/plain")
        epoch = self.epoch if self.epoch is UNSET else (None, str(self.epoch), "text/plain")
        license_ = self.license_ if self.license_ is UNSET else (None, str(self.license_), "text/plain")
        software_build = (
            self.software_build if self.software_build is UNSET else (None, str(self.software_build), "text/plain")
        )
        errata = self.errata if self.errata is UNSET else (None, str(self.errata), "text/plain")
        purl = self.purl if self.purl is UNSET else (None, str(self.purl), "text/plain")
        name = self.name if self.name is UNSET else (None, str(self.name), "text/plain")
        description = self.description if self.description is UNSET else (None, str(self.description), "text/plain")
        tags: Union[Unset, Tuple[None, str, str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = (None, json.dumps(self.tags.to_dict()), "application/json")

        version = self.version if self.version is UNSET else (None, str(self.version), "text/plain")
        release = self.release if self.release is UNSET else (None, str(self.release), "text/plain")
        arch = self.arch if self.arch is UNSET else (None, str(self.arch), "text/plain")
        products: Union[Unset, Tuple[None, str, str]] = UNSET
        if not isinstance(self.products, Unset):
            if self.products is None:
                products = None
            else:
                _temp_products = self.products
                products = (None, json.dumps(_temp_products), "application/json")

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

        sources: Union[Unset, Tuple[None, str, str]] = UNSET
        if not isinstance(self.sources, Unset):
            if self.sources is None:
                sources = None
            else:
                _temp_sources = self.sources
                sources = (None, json.dumps(_temp_sources), "application/json")

        provides: Union[Unset, Tuple[None, str, str]] = UNSET
        if not isinstance(self.provides, Unset):
            if self.provides is None:
                provides = None
            else:
                _temp_provides = self.provides
                provides = (None, json.dumps(_temp_provides), "application/json")

        upstream: Union[Unset, Tuple[None, str, str]] = UNSET
        if not isinstance(self.upstream, Unset):
            if self.upstream is None:
                upstream = None
            else:
                _temp_upstream = self.upstream
                upstream = (None, json.dumps(_temp_upstream), "application/json")

        meta_attr: Union[Unset, Tuple[None, str, str]] = UNSET
        if not isinstance(self.meta_attr, Unset):
            meta_attr = (None, json.dumps(self.meta_attr.to_dict()), "application/json") if self.meta_attr else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({key: (None, str(value), "text/plain") for key, value in self.additional_properties.items()})
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if nvr is not UNSET:
            field_dict["nvr"] = nvr
        if epoch is not UNSET:
            field_dict["epoch"] = epoch
        if license_ is not UNSET:
            field_dict["license"] = license_
        if software_build is not UNSET:
            field_dict["software_build"] = software_build
        if errata is not UNSET:
            field_dict["errata"] = errata
        if purl is not UNSET:
            field_dict["purl"] = purl
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if tags is not UNSET:
            field_dict["tags"] = tags
        if version is not UNSET:
            field_dict["version"] = version
        if release is not UNSET:
            field_dict["release"] = release
        if arch is not UNSET:
            field_dict["arch"] = arch
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
        if meta_attr is not UNSET:
            field_dict["meta_attr"] = meta_attr

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        uuid = d.pop("uuid", UNSET)

        nvr = d.pop("nvr", UNSET)

        epoch = d.pop("epoch", UNSET)

        license_ = d.pop("license", UNSET)

        software_build = d.pop("software_build", UNSET)

        errata = d.pop("errata", UNSET)

        purl = d.pop("purl", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        _tags = d.pop("tags", UNSET)
        tags: Union[Unset, ComponentDetailTags]
        if isinstance(_tags, Unset):
            tags = UNSET
        else:
            tags = ComponentDetailTags.from_dict(_tags)

        version = d.pop("version", UNSET)

        release = d.pop("release", UNSET)

        arch = d.pop("arch", UNSET)

        products = cast(List[str], d.pop("products", UNSET))

        product_versions = cast(List[str], d.pop("product_versions", UNSET))

        product_streams = cast(List[str], d.pop("product_streams", UNSET))

        product_variants = cast(List[str], d.pop("product_variants", UNSET))

        sources = cast(List[str], d.pop("sources", UNSET))

        provides = cast(List[str], d.pop("provides", UNSET))

        upstream = cast(List[str], d.pop("upstream", UNSET))

        _meta_attr = d.pop("meta_attr", UNSET)
        meta_attr: Union[Unset, None, ComponentDetailMetaAttr]
        if _meta_attr is None:
            meta_attr = None
        elif isinstance(_meta_attr, Unset):
            meta_attr = UNSET
        else:
            meta_attr = ComponentDetailMetaAttr.from_dict(_meta_attr)

        component_detail = cls(
            uuid=uuid,
            nvr=nvr,
            epoch=epoch,
            license_=license_,
            software_build=software_build,
            errata=errata,
            purl=purl,
            name=name,
            description=description,
            tags=tags,
            version=version,
            release=release,
            arch=arch,
            products=products,
            product_versions=product_versions,
            product_streams=product_streams,
            product_variants=product_variants,
            sources=sources,
            provides=provides,
            upstream=upstream,
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
