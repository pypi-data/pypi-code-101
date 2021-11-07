from datetime import datetime
import re
from typing import Optional

from pydantic import BaseModel as PydanticModel, validator


class BaseModel(PydanticModel):
    """Base model for all schemas."""

    class Config:
        # Encode datetime objects to JSON as integer timestamps
        json_encoders = {datetime: datetime.timestamp}


class AvatarHolder(BaseModel):
    """Schema mixin for models which may hold avatars.

    See the associated database model `database.models.Base.AvatarHolder`.
    """

    avatar_colour: Optional[str]
    avatar_image_url: Optional[str]

    @validator("avatar_colour")
    def validate_avatar_colour(cls, value: Optional[str]):
        if value is not None and not re.match(r"#[0-9a-f]{6}", value.lower()):
            raise ValueError("not a valid #rrggbb colour")
        return value
