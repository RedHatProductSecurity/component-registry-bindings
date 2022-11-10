from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.type_111_enum import Type111Enum
from ..types import UNSET, Unset

T = TypeVar("T", bound="SoftwareBuildSummary")


@attr.s(auto_attribs=True)
class SoftwareBuildSummary:
    """ """

    link: str
    build_id: int
    type: Type111Enum
    name: str
    source: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        link = self.link
        build_id = self.build_id
        type: str = UNSET
        if not isinstance(self.type, Unset):

            type = Type111Enum(self.type).value

        name = self.name
        source = self.source

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

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy() if isinstance(src_dict, dict) else {}
        link = d.pop("link", UNSET)

        build_id = d.pop("build_id", UNSET)

        _type = d.pop("type", UNSET)
        type: Type111Enum
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = Type111Enum(_type)

        name = d.pop("name", UNSET)

        source = d.pop("source", UNSET)

        software_build_summary = cls(
            link=link,
            build_id=build_id,
            type=type,
            name=name,
            source=source,
        )

        software_build_summary.additional_properties = d
        return software_build_summary

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
