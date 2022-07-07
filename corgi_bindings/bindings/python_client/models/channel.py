import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.channel_meta_attr import ChannelMetaAttr
from ..models.channel_type_enum import ChannelTypeEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="Channel")


@attr.s(auto_attribs=True)
class Channel:
    """ """

    uuid: str
    last_changed: datetime.datetime
    created_at: datetime.datetime
    name: str
    type: ChannelTypeEnum
    description: Union[Unset, str] = UNSET
    meta_attr: Union[Unset, ChannelMetaAttr] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        uuid = self.uuid
        last_changed: str = UNSET
        if not isinstance(self.last_changed, Unset):
            last_changed = self.last_changed.isoformat()

        created_at: str = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        name = self.name
        type: str = UNSET
        if not isinstance(self.type, Unset):

            type = ChannelTypeEnum(self.type).value

        description = self.description
        meta_attr: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.meta_attr, Unset):
            meta_attr = self.meta_attr.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if last_changed is not UNSET:
            field_dict["last_changed"] = last_changed
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if name is not UNSET:
            field_dict["name"] = name
        if type is not UNSET:
            field_dict["type"] = type
        if description is not UNSET:
            field_dict["description"] = description
        if meta_attr is not UNSET:
            field_dict["meta_attr"] = meta_attr

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy() if isinstance(src_dict, dict) else {}
        uuid = d.pop("uuid", UNSET)

        _last_changed = d.pop("last_changed", UNSET)
        last_changed: datetime.datetime
        if isinstance(_last_changed, Unset):
            last_changed = UNSET
        else:
            last_changed = isoparse(_last_changed)

        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        name = d.pop("name", UNSET)

        _type = d.pop("type", UNSET)
        type: ChannelTypeEnum
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = ChannelTypeEnum(_type)

        description = d.pop("description", UNSET)

        _meta_attr = d.pop("meta_attr", UNSET)
        meta_attr: Union[Unset, ChannelMetaAttr]
        if isinstance(_meta_attr, Unset):
            meta_attr = UNSET
        else:
            meta_attr = ChannelMetaAttr.from_dict(_meta_attr)

        channel = cls(
            uuid=uuid,
            last_changed=last_changed,
            created_at=created_at,
            name=name,
            type=type,
            description=description,
            meta_attr=meta_attr,
        )

        channel.additional_properties = d
        return channel

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
