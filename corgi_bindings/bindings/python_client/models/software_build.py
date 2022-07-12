import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.software_build_meta_attr import SoftwareBuildMetaAttr
from ..models.tag import Tag
from ..models.type_f2c_enum import TypeF2CEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="SoftwareBuild")


@attr.s(auto_attribs=True)
class SoftwareBuild:
    """ """

    link: str
    build_id: int
    type: TypeF2CEnum
    name: str
    source: str
    tags: List[Tag]
    created_at: datetime.datetime
    last_changed: datetime.datetime
    components: str
    meta_attr: Union[Unset, SoftwareBuildMetaAttr] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        link = self.link
        build_id = self.build_id
        type: str = UNSET
        if not isinstance(self.type, Unset):

            type = TypeF2CEnum(self.type).value

        name = self.name
        source = self.source
        tags: List[Dict[str, Any]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = []
            for tags_item_data in self.tags:
                tags_item: Dict[str, Any] = UNSET
                if not isinstance(tags_item_data, Unset):
                    tags_item = tags_item_data.to_dict()

                tags.append(tags_item)

        created_at: str = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        last_changed: str = UNSET
        if not isinstance(self.last_changed, Unset):
            last_changed = self.last_changed.isoformat()

        components = self.components
        meta_attr: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.meta_attr, Unset):
            meta_attr = self.meta_attr.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if link is not UNSET:
            field_dict["link"] = link
        if build_id is not UNSET:
            field_dict["build_id"] = build_id
        if type is not UNSET:
            field_dict["type"] = type
        if name is not UNSET:
            field_dict["name"] = name
        if source is not UNSET:
            field_dict["source"] = source
        if tags is not UNSET:
            field_dict["tags"] = tags
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if last_changed is not UNSET:
            field_dict["last_changed"] = last_changed
        if components is not UNSET:
            field_dict["components"] = components
        if meta_attr is not UNSET:
            field_dict["meta_attr"] = meta_attr

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy() if isinstance(src_dict, dict) else {}
        link = d.pop("link", UNSET)

        build_id = d.pop("build_id", UNSET)

        _type = d.pop("type", UNSET)
        type: TypeF2CEnum
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = TypeF2CEnum(_type)

        name = d.pop("name", UNSET)

        source = d.pop("source", UNSET)

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

        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _last_changed = d.pop("last_changed", UNSET)
        last_changed: datetime.datetime
        if isinstance(_last_changed, Unset):
            last_changed = UNSET
        else:
            last_changed = isoparse(_last_changed)

        components = d.pop("components", UNSET)

        _meta_attr = d.pop("meta_attr", UNSET)
        meta_attr: Union[Unset, SoftwareBuildMetaAttr]
        if isinstance(_meta_attr, Unset):
            meta_attr = UNSET
        else:
            meta_attr = SoftwareBuildMetaAttr.from_dict(_meta_attr)

        software_build = cls(
            link=link,
            build_id=build_id,
            type=type,
            name=name,
            source=source,
            tags=tags,
            created_at=created_at,
            last_changed=last_changed,
            components=components,
            meta_attr=meta_attr,
        )

        software_build.additional_properties = d
        return software_build

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
