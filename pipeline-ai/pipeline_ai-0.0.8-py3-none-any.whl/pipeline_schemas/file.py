from typing import List, Optional

from .base import BaseModel


class FileBase(BaseModel):
    name: str


class FileSchema(FileBase):
    id: str
    path: str

    data: Optional[str]  # Put a limit of 20kB on the data

    class Config:
        orm_mode = True


class FileGet(FileBase):
    id: str
    size: int

    class Config:
        orm_mode = True


class FileCreate(FileBase):
    name: Optional[str]
    file_bytes: Optional[str]
