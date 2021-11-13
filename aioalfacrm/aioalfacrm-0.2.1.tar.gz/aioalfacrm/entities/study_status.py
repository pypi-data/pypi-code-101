from typing import Optional

from .. import fields
from ..core import AlfaEntity


class StudyStatus(AlfaEntity):
    id: Optional[int] = fields.Integer()
    name: Optional[str] = fields.String()
    is_enabled: Optional[bool] = fields.Bool()
    weight: Optional[int] = fields.Integer()

    def __init__(
            self,
            id_: Optional[int] = None,
            name: Optional[str] = None,
            is_enabled: Optional[bool] = None,
            weight: Optional[int] = None,
            **kwargs,
    ):
        super(StudyStatus, self).__init__(
            id=id_,
            name=name,
            is_enabled=is_enabled,
            weight=weight,
            **kwargs,
        )
