from typing import List, Optional

from .base import BaseModel
from .resource import ResourceCreateSchema, ResourceGetSchema


class SlaveCreateSchema(BaseModel):
    slave_ip: str
    slave_name: str
    resources: List[ResourceCreateSchema]


class SlaveGetSchema(BaseModel):
    id: str
    slave_ip: str
    slave_name: str
    resources: List[ResourceGetSchema]

    class Config:
        orm_mode = True
