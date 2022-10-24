from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.product_stream_brew_tags import ProductStreamBrewTags
from ..models.product_stream_composes import ProductStreamComposes
from ..models.product_stream_product_variants_item import ProductStreamProductVariantsItem
from ..models.product_stream_product_versions_item import ProductStreamProductVersionsItem
from ..models.product_stream_products_item import ProductStreamProductsItem
from ..models.product_stream_relations_item import ProductStreamRelationsItem
from ..models.tag import Tag
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProductStream")


@attr.s(auto_attribs=True)
class ProductStream:
    """ """

    link: str
    uuid: str
    name: str
    build_count: int
    builds: str
    manifest: str
    components: str
    upstreams: str
    relations: List[ProductStreamRelationsItem]
    tags: List[Tag]
    products: List[ProductStreamProductsItem]
    product_versions: List[ProductStreamProductVersionsItem]
    product_variants: List[ProductStreamProductVariantsItem]
    ofuri: Union[Unset, str] = UNSET
    cpe: Union[Unset, str] = UNSET
    active: Union[Unset, bool] = UNSET
    brew_tags: Union[Unset, ProductStreamBrewTags] = UNSET
    yum_repositories: Union[Unset, List[str]] = UNSET
    composes: Union[Unset, ProductStreamComposes] = UNSET
    et_product_versions: Union[Unset, List[str]] = UNSET
    description: Union[Unset, str] = UNSET
    channels: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        link = self.link
        uuid = self.uuid
        name = self.name
        build_count = self.build_count
        builds = self.builds
        manifest = self.manifest
        components = self.components
        upstreams = self.upstreams
        relations: List[Dict[str, Any]] = UNSET
        if not isinstance(self.relations, Unset):
            relations = []
            for relations_item_data in self.relations:
                relations_item: Dict[str, Any] = UNSET
                if not isinstance(relations_item_data, Unset):
                    relations_item = relations_item_data.to_dict()

                relations.append(relations_item)

        tags: List[Dict[str, Any]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = []
            for tags_item_data in self.tags:
                tags_item: Dict[str, Any] = UNSET
                if not isinstance(tags_item_data, Unset):
                    tags_item = tags_item_data.to_dict()

                tags.append(tags_item)

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

        product_variants: List[Dict[str, Any]] = UNSET
        if not isinstance(self.product_variants, Unset):
            product_variants = []
            for product_variants_item_data in self.product_variants:
                product_variants_item: Dict[str, Any] = UNSET
                if not isinstance(product_variants_item_data, Unset):
                    product_variants_item = product_variants_item_data.to_dict()

                product_variants.append(product_variants_item)

        ofuri = self.ofuri
        cpe = self.cpe
        active = self.active
        brew_tags: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.brew_tags, Unset):
            brew_tags = self.brew_tags.to_dict()

        yum_repositories: Union[Unset, List[str]] = UNSET
        if not isinstance(self.yum_repositories, Unset):
            yum_repositories = self.yum_repositories

        composes: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.composes, Unset):
            composes = self.composes.to_dict()

        et_product_versions: Union[Unset, List[str]] = UNSET
        if not isinstance(self.et_product_versions, Unset):
            et_product_versions = self.et_product_versions

        description = self.description
        channels: Union[Unset, List[str]] = UNSET
        if not isinstance(self.channels, Unset):
            channels = self.channels

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if link is not UNSET:
            field_dict["link"] = link
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if name is not UNSET:
            field_dict["name"] = name
        if build_count is not UNSET:
            field_dict["build_count"] = build_count
        if builds is not UNSET:
            field_dict["builds"] = builds
        if manifest is not UNSET:
            field_dict["manifest"] = manifest
        if components is not UNSET:
            field_dict["components"] = components
        if upstreams is not UNSET:
            field_dict["upstreams"] = upstreams
        if relations is not UNSET:
            field_dict["relations"] = relations
        if tags is not UNSET:
            field_dict["tags"] = tags
        if products is not UNSET:
            field_dict["products"] = products
        if product_versions is not UNSET:
            field_dict["product_versions"] = product_versions
        if product_variants is not UNSET:
            field_dict["product_variants"] = product_variants
        if ofuri is not UNSET:
            field_dict["ofuri"] = ofuri
        if cpe is not UNSET:
            field_dict["cpe"] = cpe
        if active is not UNSET:
            field_dict["active"] = active
        if brew_tags is not UNSET:
            field_dict["brew_tags"] = brew_tags
        if yum_repositories is not UNSET:
            field_dict["yum_repositories"] = yum_repositories
        if composes is not UNSET:
            field_dict["composes"] = composes
        if et_product_versions is not UNSET:
            field_dict["et_product_versions"] = et_product_versions
        if description is not UNSET:
            field_dict["description"] = description
        if channels is not UNSET:
            field_dict["channels"] = channels

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy() if isinstance(src_dict, dict) else {}
        link = d.pop("link", UNSET)

        uuid = d.pop("uuid", UNSET)

        name = d.pop("name", UNSET)

        build_count = d.pop("build_count", UNSET)

        builds = d.pop("builds", UNSET)

        manifest = d.pop("manifest", UNSET)

        components = d.pop("components", UNSET)

        upstreams = d.pop("upstreams", UNSET)

        relations = []
        _relations = d.pop("relations", UNSET)
        if _relations is UNSET:
            relations = UNSET
        else:
            for relations_item_data in _relations or []:
                _relations_item = relations_item_data
                relations_item: ProductStreamRelationsItem
                if isinstance(_relations_item, Unset):
                    relations_item = UNSET
                else:
                    relations_item = ProductStreamRelationsItem.from_dict(_relations_item)

                relations.append(relations_item)

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

        products = []
        _products = d.pop("products", UNSET)
        if _products is UNSET:
            products = UNSET
        else:
            for products_item_data in _products or []:
                _products_item = products_item_data
                products_item: ProductStreamProductsItem
                if isinstance(_products_item, Unset):
                    products_item = UNSET
                else:
                    products_item = ProductStreamProductsItem.from_dict(_products_item)

                products.append(products_item)

        product_versions = []
        _product_versions = d.pop("product_versions", UNSET)
        if _product_versions is UNSET:
            product_versions = UNSET
        else:
            for product_versions_item_data in _product_versions or []:
                _product_versions_item = product_versions_item_data
                product_versions_item: ProductStreamProductVersionsItem
                if isinstance(_product_versions_item, Unset):
                    product_versions_item = UNSET
                else:
                    product_versions_item = ProductStreamProductVersionsItem.from_dict(_product_versions_item)

                product_versions.append(product_versions_item)

        product_variants = []
        _product_variants = d.pop("product_variants", UNSET)
        if _product_variants is UNSET:
            product_variants = UNSET
        else:
            for product_variants_item_data in _product_variants or []:
                _product_variants_item = product_variants_item_data
                product_variants_item: ProductStreamProductVariantsItem
                if isinstance(_product_variants_item, Unset):
                    product_variants_item = UNSET
                else:
                    product_variants_item = ProductStreamProductVariantsItem.from_dict(_product_variants_item)

                product_variants.append(product_variants_item)

        ofuri = d.pop("ofuri", UNSET)

        cpe = d.pop("cpe", UNSET)

        active = d.pop("active", UNSET)

        _brew_tags = d.pop("brew_tags", UNSET)
        brew_tags: Union[Unset, ProductStreamBrewTags]
        if isinstance(_brew_tags, Unset):
            brew_tags = UNSET
        else:
            brew_tags = ProductStreamBrewTags.from_dict(_brew_tags)

        yum_repositories = cast(List[str], d.pop("yum_repositories", UNSET))

        _composes = d.pop("composes", UNSET)
        composes: Union[Unset, ProductStreamComposes]
        if isinstance(_composes, Unset):
            composes = UNSET
        else:
            composes = ProductStreamComposes.from_dict(_composes)

        et_product_versions = cast(List[str], d.pop("et_product_versions", UNSET))

        description = d.pop("description", UNSET)

        channels = cast(List[str], d.pop("channels", UNSET))

        product_stream = cls(
            link=link,
            uuid=uuid,
            name=name,
            build_count=build_count,
            builds=builds,
            manifest=manifest,
            components=components,
            upstreams=upstreams,
            relations=relations,
            tags=tags,
            products=products,
            product_versions=product_versions,
            product_variants=product_variants,
            ofuri=ofuri,
            cpe=cpe,
            active=active,
            brew_tags=brew_tags,
            yum_repositories=yum_repositories,
            composes=composes,
            et_product_versions=et_product_versions,
            description=description,
            channels=channels,
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
