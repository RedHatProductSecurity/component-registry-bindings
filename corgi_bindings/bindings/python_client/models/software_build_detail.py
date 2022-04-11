import json
from typing import Any, Dict, List, Tuple, Type, TypeVar, Union

import attr

from ..models.software_build_detail_meta_attr import SoftwareBuildDetailMetaAttr
from ..models.software_build_detail_tags import SoftwareBuildDetailTags
from ..models.software_build_detail_type_enum import SoftwareBuildDetailTypeEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="SoftwareBuildDetail")


@attr.s(auto_attribs=True)
class SoftwareBuildDetail:
    """software build detail serializer"""

    build_id: int
    name: str
    brew_tags: str
    components: str
    tags: Union[Unset, SoftwareBuildDetailTags] = UNSET
    type: Union[Unset, SoftwareBuildDetailTypeEnum] = UNSET
    meta_attr: Union[Unset, None, SoftwareBuildDetailMetaAttr] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        build_id = self.build_id
        name = self.name
        brew_tags = self.brew_tags
        components = self.components
        tags: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags.to_dict()

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):

            type = SoftwareBuildDetailTypeEnum(self.type).value

        meta_attr: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.meta_attr, Unset):
            meta_attr = self.meta_attr.to_dict() if self.meta_attr else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if build_id is not UNSET:
            field_dict["build_id"] = build_id
        if name is not UNSET:
            field_dict["name"] = name
        if brew_tags is not UNSET:
            field_dict["brew_tags"] = brew_tags
        if components is not UNSET:
            field_dict["components"] = components
        if tags is not UNSET:
            field_dict["tags"] = tags
        if type is not UNSET:
            field_dict["type"] = type
        if meta_attr is not UNSET:
            field_dict["meta_attr"] = meta_attr

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        build_id = self.build_id if self.build_id is UNSET else (None, str(self.build_id), "text/plain")
        name = self.name if self.name is UNSET else (None, str(self.name), "text/plain")
        brew_tags = self.brew_tags if self.brew_tags is UNSET else (None, str(self.brew_tags), "text/plain")
        components = self.components if self.components is UNSET else (None, str(self.components), "text/plain")
        tags: Union[Unset, Tuple[None, str, str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = (None, json.dumps(self.tags.to_dict()), "application/json")

        type: Union[Unset, Tuple[None, str, str]] = UNSET
        if not isinstance(self.type, Unset):

            type = SoftwareBuildDetailTypeEnum(self.type).value

        meta_attr: Union[Unset, Tuple[None, str, str]] = UNSET
        if not isinstance(self.meta_attr, Unset):
            meta_attr = (None, json.dumps(self.meta_attr.to_dict()), "application/json") if self.meta_attr else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({key: (None, str(value), "text/plain") for key, value in self.additional_properties.items()})
        if build_id is not UNSET:
            field_dict["build_id"] = build_id
        if name is not UNSET:
            field_dict["name"] = name
        if brew_tags is not UNSET:
            field_dict["brew_tags"] = brew_tags
        if components is not UNSET:
            field_dict["components"] = components
        if tags is not UNSET:
            field_dict["tags"] = tags
        if type is not UNSET:
            field_dict["type"] = type
        if meta_attr is not UNSET:
            field_dict["meta_attr"] = meta_attr

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        build_id = d.pop("build_id", UNSET)

        name = d.pop("name", UNSET)

        brew_tags = d.pop("brew_tags", UNSET)

        components = d.pop("components", UNSET)

        _tags = d.pop("tags", UNSET)
        tags: Union[Unset, SoftwareBuildDetailTags]
        if isinstance(_tags, Unset):
            tags = UNSET
        else:
            tags = SoftwareBuildDetailTags.from_dict(_tags)

        _type = d.pop("type", UNSET)
        type: Union[Unset, SoftwareBuildDetailTypeEnum]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = SoftwareBuildDetailTypeEnum(_type)

        _meta_attr = d.pop("meta_attr", UNSET)
        meta_attr: Union[Unset, None, SoftwareBuildDetailMetaAttr]
        if _meta_attr is None:
            meta_attr = None
        elif isinstance(_meta_attr, Unset):
            meta_attr = UNSET
        else:
            meta_attr = SoftwareBuildDetailMetaAttr.from_dict(_meta_attr)

        software_build_detail = cls(
            build_id=build_id,
            name=name,
            brew_tags=brew_tags,
            components=components,
            tags=tags,
            type=type,
            meta_attr=meta_attr,
        )

        software_build_detail.additional_properties = d
        return software_build_detail

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
