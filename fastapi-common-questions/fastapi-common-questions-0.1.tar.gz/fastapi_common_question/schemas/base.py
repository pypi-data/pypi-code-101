from typing import Optional
import pytz
from datetime import datetime
from pydantic import BaseModel, validator


class BaseSchema(BaseModel):

    # id: int = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    @validator('created_at')
    def convert_to_local(cls, value):
        return value.astimezone(pytz.timezone('Asia/Tehran')) if isinstance(value, datetime) else value

    @validator('updated_at')
    def convert_update_to_local(cls, value):
        return value.astimezone(pytz.timezone('Asia/Tehran')) if isinstance(value, datetime) else value
