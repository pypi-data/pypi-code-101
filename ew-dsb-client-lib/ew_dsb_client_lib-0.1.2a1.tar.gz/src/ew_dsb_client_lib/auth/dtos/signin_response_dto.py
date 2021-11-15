#!/usr/bin/env python3

from dataclasses import dataclass
from dataclasses_json import DataClassJsonMixin
from ew_dsb_client_lib.auth.entities.user_jwt_entity import UserJwt

@dataclass(frozen=True)
class SignInResponseDto(DataClassJsonMixin):
    signIn: UserJwt
