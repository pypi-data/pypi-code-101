from typing import Optional, List

from .. import fields
from ..core import AlfaEntity


class PayItem(AlfaEntity):
    id: Optional[int] = fields.Integer()
    branch_ids: Optional[List[int]] = fields.ListField(fields.Integer())
    category_id: Optional[int] = fields.Integer()
    pay_type_ids: Optional[List[int]] = fields.ListField(fields.Integer())
    name: Optional[str] = fields.String()
    weight: Optional[int] = fields.Integer()

    def __init__(
            self,
            id_: Optional[int] = None,
            branch_ids: Optional[List[int]] = None,
            category_id: Optional[int] = None,
            pay_type_ids: Optional[List[int]] = None,
            name: Optional[str] = None,
            weight: Optional[int] = None,
            **kwargs
    ):
        super().__init__(
            id=id_,
            branch_ids=branch_ids,
            category_id=category_id,
            pay_type_ids=pay_type_ids,
            name=name,
            weight=weight,
            **kwargs
        )
