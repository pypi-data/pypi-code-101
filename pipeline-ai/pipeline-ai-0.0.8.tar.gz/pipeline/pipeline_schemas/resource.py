from typing import List, Optional

from .base import BaseModel


class ResourceCreateSchema(BaseModel):
    foreign_id: Optional[str]
    resource_label: str
    resource_type: str


class ResourceGetSchema(BaseModel):
    id: str
    foreign_id: Optional[str]
    resource_label: str
    resource_type: str

    class Config:
        orm_mode = True
