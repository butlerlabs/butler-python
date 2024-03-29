from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.block_dto import BlockDto
from ..models.bounding_box_dto import BoundingBoxDto
from ..models.doc_ex_confidence import DocExConfidence
from ..types import UNSET, Unset

T = TypeVar("T", bound="TrainingCellWithConfidenceLabeledResultDto")


@attr.s(auto_attribs=True)
class TrainingCellWithConfidenceLabeledResultDto:
    """
    Attributes:
        column_id (str): The id of the column for this cell.
        confidence_score (DocExConfidence):
        blocks (List[BlockDto]): The blocks for this cell.
        region (Union[Unset, BoundingBoxDto]):
        value (Union[Unset, str]): The text value for this cell.
    """

    column_id: str
    confidence_score: DocExConfidence
    blocks: List[BlockDto]
    region: Union[Unset, BoundingBoxDto] = UNSET
    value: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        column_id = self.column_id
        confidence_score = self.confidence_score.value

        blocks = []
        for blocks_item_data in self.blocks:
            blocks_item = blocks_item_data.to_dict()

            blocks.append(blocks_item)

        region: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.region, Unset):
            region = self.region.to_dict()

        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "columnId": column_id,
                "confidenceScore": confidence_score,
                "blocks": blocks,
            }
        )
        if region is not UNSET:
            field_dict["region"] = region
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        column_id = d.pop("columnId")

        confidence_score = DocExConfidence(d.pop("confidenceScore"))

        blocks = []
        _blocks = d.pop("blocks")
        for blocks_item_data in _blocks:
            blocks_item = BlockDto.from_dict(blocks_item_data)

            blocks.append(blocks_item)

        _region = d.pop("region", UNSET)
        region: Union[Unset, BoundingBoxDto]
        if isinstance(_region, Unset):
            region = UNSET
        else:
            region = BoundingBoxDto.from_dict(_region)

        value = d.pop("value", UNSET)

        training_cell_with_confidence_labeled_result_dto = cls(
            column_id=column_id,
            confidence_score=confidence_score,
            blocks=blocks,
            region=region,
            value=value,
        )

        training_cell_with_confidence_labeled_result_dto.additional_properties = d
        return training_cell_with_confidence_labeled_result_dto

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
