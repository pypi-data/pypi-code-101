#!/usr/bin/env python3

from typing import List
from dataclasses import dataclass
from dataclasses_json import DataClassJsonMixin
from ew_dsb_client_lib.auth.entities.user_role_entity import UserRole

@dataclass(frozen=True)
class User(DataClassJsonMixin):
    did: str
    verifiedRoles: List[UserRole]
