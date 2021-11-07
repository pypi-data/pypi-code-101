from .base import BaseModel


class Tag(BaseModel):
    id: str
    name: str
    frequency: int = 0
