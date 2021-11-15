#!/usr/bin/env python3

from dataclasses import dataclass
from dataclasses_json import DataClassJsonMixin
from ew_dsb_client_lib.auth.entities.user_entity import User

@dataclass(frozen=True)
class GetUserResponseDto(DataClassJsonMixin):
    getUser: User
