from typing import Any, Dict, List, Optional, Type, TypeVar, Union

import attr

from ..extensions import NotPresentError
from ..models.benchling_app_error import BenchlingAppError
from ..models.transform_status import TransformStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="Transform")


@attr.s(auto_attribs=True, repr=False)
class Transform:
    """  """

    _blob_id: Union[Unset, None, str] = UNSET
    _custom_transform_id: Union[Unset, None, str] = UNSET
    _errors: Union[Unset, List[BenchlingAppError]] = UNSET
    _id: Union[Unset, str] = UNSET
    _status: Union[Unset, TransformStatus] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def __repr__(self):
        fields = []
        fields.append("blob_id={}".format(repr(self._blob_id)))
        fields.append("custom_transform_id={}".format(repr(self._custom_transform_id)))
        fields.append("errors={}".format(repr(self._errors)))
        fields.append("id={}".format(repr(self._id)))
        fields.append("status={}".format(repr(self._status)))
        fields.append("additional_properties={}".format(repr(self.additional_properties)))
        return "Transform({})".format(", ".join(fields))

    def to_dict(self) -> Dict[str, Any]:
        blob_id = self._blob_id
        custom_transform_id = self._custom_transform_id
        errors: Union[Unset, List[Any]] = UNSET
        if not isinstance(self._errors, Unset):
            errors = []
            for errors_item_data in self._errors:
                errors_item = errors_item_data.to_dict()

                errors.append(errors_item)

        id = self._id
        status: Union[Unset, int] = UNSET
        if not isinstance(self._status, Unset):
            status = self._status.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if blob_id is not UNSET:
            field_dict["blobId"] = blob_id
        if custom_transform_id is not UNSET:
            field_dict["customTransformId"] = custom_transform_id
        if errors is not UNSET:
            field_dict["errors"] = errors
        if id is not UNSET:
            field_dict["id"] = id
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        blob_id = d.pop("blobId", UNSET)

        custom_transform_id = d.pop("customTransformId", UNSET)

        errors = []
        _errors = d.pop("errors", UNSET)
        for errors_item_data in _errors or []:
            errors_item = BenchlingAppError.from_dict(errors_item_data)

            errors.append(errors_item)

        id = d.pop("id", UNSET)

        status = None
        _status = d.pop("status", UNSET)
        if _status is not None and _status is not UNSET:
            try:
                status = TransformStatus(_status)
            except ValueError:
                status = TransformStatus.of_unknown(_status)

        transform = cls(
            blob_id=blob_id,
            custom_transform_id=custom_transform_id,
            errors=errors,
            id=id,
            status=status,
        )

        transform.additional_properties = d
        return transform

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

    def get(self, key, default=None) -> Optional[Any]:
        return self.additional_properties.get(key, default)

    @property
    def blob_id(self) -> Optional[str]:
        if isinstance(self._blob_id, Unset):
            raise NotPresentError(self, "blob_id")
        return self._blob_id

    @blob_id.setter
    def blob_id(self, value: Optional[str]) -> None:
        self._blob_id = value

    @blob_id.deleter
    def blob_id(self) -> None:
        self._blob_id = UNSET

    @property
    def custom_transform_id(self) -> Optional[str]:
        if isinstance(self._custom_transform_id, Unset):
            raise NotPresentError(self, "custom_transform_id")
        return self._custom_transform_id

    @custom_transform_id.setter
    def custom_transform_id(self, value: Optional[str]) -> None:
        self._custom_transform_id = value

    @custom_transform_id.deleter
    def custom_transform_id(self) -> None:
        self._custom_transform_id = UNSET

    @property
    def errors(self) -> List[BenchlingAppError]:
        if isinstance(self._errors, Unset):
            raise NotPresentError(self, "errors")
        return self._errors

    @errors.setter
    def errors(self, value: List[BenchlingAppError]) -> None:
        self._errors = value

    @errors.deleter
    def errors(self) -> None:
        self._errors = UNSET

    @property
    def id(self) -> str:
        if isinstance(self._id, Unset):
            raise NotPresentError(self, "id")
        return self._id

    @id.setter
    def id(self, value: str) -> None:
        self._id = value

    @id.deleter
    def id(self) -> None:
        self._id = UNSET

    @property
    def status(self) -> TransformStatus:
        if isinstance(self._status, Unset):
            raise NotPresentError(self, "status")
        return self._status

    @status.setter
    def status(self, value: TransformStatus) -> None:
        self._status = value

    @status.deleter
    def status(self) -> None:
        self._status = UNSET
