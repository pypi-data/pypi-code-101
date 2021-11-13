from typing import Optional

from .. import fields
from ..core import AlfaEntity


class LessonType(AlfaEntity):
    id: Optional[int] = fields.Integer()
    name: Optional[str] = fields.String()
    lesson_type: Optional[int] = fields.Integer(alias='type')
    icon: Optional[str] = fields.String()
    is_active: Optional[bool] = fields.Bool()
    sort: Optional[int] = fields.Integer()

    def __init__(
            self,
            id_: Optional[int] = None,
            name: Optional[str] = None,
            lesson_type: Optional[str] = None,
            icon: Optional[str] = None,
            is_active: Optional[bool] = None,
            sort: Optional[int] = None,
            **kwargs
    ):
        super().__init__(
            id=id_,
            name=name,
            lesson_type=lesson_type,
            icon=icon,
            is_active=is_active,
            sort=sort,
            **kwargs
        )
