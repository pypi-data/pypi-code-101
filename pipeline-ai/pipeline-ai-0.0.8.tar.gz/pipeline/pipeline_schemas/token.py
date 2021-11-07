from .base import BaseModel


class TokenAssignRole(BaseModel):
    role_id: str
    permission_object_id: str


class Token(BaseModel):
    """API token representation when returned from an API call."""

    id: str
    #: Token value, used when authenticating with the API
    value: str
    name: str

    class Config:
        orm_mode = True
