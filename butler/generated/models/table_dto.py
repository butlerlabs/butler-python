from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.column_dto import ColumnDto

T = TypeVar("T", bound="TableDto")


@attr.s(auto_attribs=True)
class TableDto:
    """
    Attributes:
        name (str): The name of the table
        columns (List[ColumnDto]): The columns of the table
    """

    name: str
    columns: List[ColumnDto]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        columns = []
        for columns_item_data in self.columns:
            columns_item = columns_item_data.to_dict()

            columns.append(columns_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "columns": columns,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        columns = []
        _columns = d.pop("columns")
        for columns_item_data in _columns:
            columns_item = ColumnDto.from_dict(columns_item_data)

            columns.append(columns_item)

        table_dto = cls(
            name=name,
            columns=columns,
        )

        table_dto.additional_properties = d
        return table_dto

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
