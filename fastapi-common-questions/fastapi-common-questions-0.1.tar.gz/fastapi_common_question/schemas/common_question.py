from datetime import datetime
from typing import Optional

from .base import BaseSchema


class CommonQuestionIn(BaseSchema):
    question: str
    answer: str
    additional_data: Optional[dict]
    is_active: Optional[bool]
    is_archive: Optional[bool]


class CommonQuestionFilter(BaseSchema):
    is_active: Optional[bool]
    is_archive: Optional[bool]
    id: Optional[int]
    updated_at: Optional[datetime]
    created_at: Optional[datetime]


class CommonQuestionOut(CommonQuestionIn):
    id: int
    updated_at: Optional[datetime]
    created_at: Optional[datetime]

    class Config:
        orm_mode = True
