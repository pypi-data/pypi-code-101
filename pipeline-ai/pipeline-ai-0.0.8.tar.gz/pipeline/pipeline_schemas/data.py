from datetime import datetime
import enum
from typing import Optional

from .base import BaseModel
from .file import FileSchema
from .token import Token


class FileType(enum.Enum):
    text = "text"
    image = "image"


class DataGet(BaseModel):
    id: str
    hex_file: FileSchema
    created_at: datetime
    modified_at: Optional[datetime]
    name: Optional[str]
    size: Optional[int]
    file_type: Optional[FileType]
    token_created_by: Optional[Token]
    token_modified_by: Optional[Token]
    url: Optional[str]
    preview: Optional[str]

    class Config:
        orm_mode = True
