"""Declares :class:`Identification`."""
from pydantic import BaseModel
from pydantic import Field


class Identification(BaseModel):
    id_token: str = Field(...,
        title="ID Token",
        example="<Open ID identity token>"
    )
