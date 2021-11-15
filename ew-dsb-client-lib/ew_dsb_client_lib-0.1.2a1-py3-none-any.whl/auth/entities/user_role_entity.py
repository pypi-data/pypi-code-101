#!/usr/bin/env python3

from dataclasses import dataclass
from dataclasses_json import DataClassJsonMixin

@dataclass(frozen=True)
class UserRole(DataClassJsonMixin):
    name: str
    namespace: str
