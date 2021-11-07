from .file import FileSchema
from typing import List, Optional

from .base import BaseModel


class FunctionBase(BaseModel):
    id: Optional[str]
    name: str


class FunctionSchema(FunctionBase):
    id: str


class FunctionGet(FunctionBase):
    id: str
    hex_file: FileSchema
    # source_file_id: FileSchema
    source_sample: str

    class Config:
        orm_mode = True


class FunctionCreate(BaseModel):
    #: The hex-encoded dill-dump of the function object
    function_hex: str
    #: The source code of the function object
    function_source: str
    inputs: dict
    output: dict
    name: str
    hash: str
