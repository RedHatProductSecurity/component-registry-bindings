from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ComponentList")


@attr.s(auto_attribs=True)
class ComponentList:
    """ """

    link: str
    purl: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        link = self.link
        purl = self.purl

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if link is not UNSET:
            field_dict["link"] = link
        if purl is not UNSET:
            field_dict["purl"] = purl

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy() if isinstance(src_dict, dict) else {}
        link = d.pop("link", UNSET)

        purl = d.pop("purl", UNSET)

        component_list = cls(
            link=link,
            purl=purl,
        )

        component_list.additional_properties = d
        return component_list

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
