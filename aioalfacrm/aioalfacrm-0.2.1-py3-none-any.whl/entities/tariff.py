import datetime
from typing import Optional, List

from .. import fields
from ..core import AlfaEntity


class Tariff(AlfaEntity):
    id: Optional[int] = fields.Integer()
    tariff_type: Optional[int] = fields.Integer(alias='type')
    name: Optional[str] = fields.String()
    price: Optional[float] = fields.Float()
    lesson_count: Optional[int] = fields.Integer()
    duration: Optional[int] = fields.Integer()
    added: Optional[datetime.datetime] = fields.DateTimeField()
    branch_ids: Optional[List[int]] = fields.ListField(fields.Integer())

    def __init__(
            self,
            id_: Optional[int] = None,
            tariff_type: Optional[int] = None,
            name: Optional[str] = None,
            price: Optional[float] = None,
            lesson_count: Optional[int] = None,
            duration: Optional[int] = None,
            added: Optional[datetime.datetime] = None,
            branch_ids: Optional[List[int]] = None,
            **kwargs,
    ):
        super().__init__(
            id=id_,
            tariff_type=tariff_type,
            name=name,
            price=price,
            lesson_count=lesson_count,
            duration=duration,
            added=added,
            branch_ids=branch_ids,
            **kwargs,
        )
