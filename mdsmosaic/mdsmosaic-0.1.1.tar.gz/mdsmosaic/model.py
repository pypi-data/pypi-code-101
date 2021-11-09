from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass(frozen=True)
class Identity:
    first_name: str
    last_name: str
    gender: str
    birth_date: datetime = field(default_factory=datetime.now)
    birth_place: Optional[str] = None
    civil_status: Optional[str] = None
    degree: Optional[str] = None
    external_date: Optional[datetime] = None
    middle_name: Optional[str] = None
    mother_tongue: Optional[str] = None
    mothers_maiden_name: Optional[str] = None
    nationality: Optional[str] = None
    prefix: Optional[str] = None
    race: Optional[str] = None
    religion: Optional[str] = None
    suffix: Optional[str] = None
