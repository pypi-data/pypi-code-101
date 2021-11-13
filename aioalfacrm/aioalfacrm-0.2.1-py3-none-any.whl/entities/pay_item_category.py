from typing import Optional

from .. import fields
from ..core import AlfaEntity


class PayItemCategory(AlfaEntity):
    id: Optional[int] = fields.Integer()
    name: Optional[str] = fields.String()
    weight: Optional[int] = fields.Integer()

    def __init__(
            self,
            id_: Optional[int] = None,
            name: Optional[str] = None,
            weight: Optional[int] = None,
            **kwargs
    ):
        super().__init__(
            id=id_,
            name=name,
            weight=weight,
            **kwargs
        )
