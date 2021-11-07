from .base import AvatarHolder


class ProjectBase(AvatarHolder):
    name: str


class ProjectGet(ProjectBase):
    id: str

    class Config:
        orm_mode = True
