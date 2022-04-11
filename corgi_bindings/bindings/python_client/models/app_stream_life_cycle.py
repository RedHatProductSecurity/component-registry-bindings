import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.app_stream_life_cycle_meta_attr import AppStreamLifeCycleMetaAttr
from ..models.app_stream_life_cycle_type_enum import AppStreamLifeCycleTypeEnum
from ..models.source_enum import SourceEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="AppStreamLifeCycle")


@attr.s(auto_attribs=True)
class AppStreamLifeCycle:
    """lifecycle serializer"""

    id: int
    last_changed: datetime.datetime
    created_at: datetime.datetime
    name: str
    lifecycle: int
    acg: int
    product: str
    initial_product_version: str
    stream: str
    source: SourceEnum
    type: Union[Unset, AppStreamLifeCycleTypeEnum] = UNSET
    start_date: Union[Unset, None, datetime.date] = UNSET
    end_date: Union[Unset, None, datetime.date] = UNSET
    private: Union[Unset, None, bool] = UNSET
    meta_attr: Union[Unset, None, AppStreamLifeCycleMetaAttr] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        last_changed: str = UNSET
        if not isinstance(self.last_changed, Unset):
            last_changed = self.last_changed.isoformat()

        created_at: str = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        name = self.name
        lifecycle = self.lifecycle
        acg = self.acg
        product = self.product
        initial_product_version = self.initial_product_version
        stream = self.stream
        source: str = UNSET
        if not isinstance(self.source, Unset):

            source = SourceEnum(self.source).value

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):

            type = AppStreamLifeCycleTypeEnum(self.type).value

        start_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat() if self.start_date else None

        end_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat() if self.end_date else None

        private = self.private
        meta_attr: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.meta_attr, Unset):
            meta_attr = self.meta_attr.to_dict() if self.meta_attr else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if id is not UNSET:
            field_dict["id"] = id
        if last_changed is not UNSET:
            field_dict["last_changed"] = last_changed
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if name is not UNSET:
            field_dict["name"] = name
        if lifecycle is not UNSET:
            field_dict["lifecycle"] = lifecycle
        if acg is not UNSET:
            field_dict["acg"] = acg
        if product is not UNSET:
            field_dict["product"] = product
        if initial_product_version is not UNSET:
            field_dict["initial_product_version"] = initial_product_version
        if stream is not UNSET:
            field_dict["stream"] = stream
        if source is not UNSET:
            field_dict["source"] = source
        if type is not UNSET:
            field_dict["type"] = type
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if end_date is not UNSET:
            field_dict["end_date"] = end_date
        if private is not UNSET:
            field_dict["private"] = private
        if meta_attr is not UNSET:
            field_dict["meta_attr"] = meta_attr

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

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

        lifecycle = d.pop("lifecycle", UNSET)

        acg = d.pop("acg", UNSET)

        product = d.pop("product", UNSET)

        initial_product_version = d.pop("initial_product_version", UNSET)

        stream = d.pop("stream", UNSET)

        _source = d.pop("source", UNSET)
        source: SourceEnum
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = SourceEnum(_source)

        _type = d.pop("type", UNSET)
        type: Union[Unset, AppStreamLifeCycleTypeEnum]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = AppStreamLifeCycleTypeEnum(_type)

        _start_date = d.pop("start_date", UNSET)
        start_date: Union[Unset, None, datetime.date]
        if _start_date is None:
            start_date = None
        elif isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = isoparse(_start_date).date()

        _end_date = d.pop("end_date", UNSET)
        end_date: Union[Unset, None, datetime.date]
        if _end_date is None:
            end_date = None
        elif isinstance(_end_date, Unset):
            end_date = UNSET
        else:
            end_date = isoparse(_end_date).date()

        private = d.pop("private", UNSET)

        _meta_attr = d.pop("meta_attr", UNSET)
        meta_attr: Union[Unset, None, AppStreamLifeCycleMetaAttr]
        if _meta_attr is None:
            meta_attr = None
        elif isinstance(_meta_attr, Unset):
            meta_attr = UNSET
        else:
            meta_attr = AppStreamLifeCycleMetaAttr.from_dict(_meta_attr)

        app_stream_life_cycle = cls(
            id=id,
            last_changed=last_changed,
            created_at=created_at,
            name=name,
            lifecycle=lifecycle,
            acg=acg,
            product=product,
            initial_product_version=initial_product_version,
            stream=stream,
            source=source,
            type=type,
            start_date=start_date,
            end_date=end_date,
            private=private,
            meta_attr=meta_attr,
        )

        app_stream_life_cycle.additional_properties = d
        return app_stream_life_cycle

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
