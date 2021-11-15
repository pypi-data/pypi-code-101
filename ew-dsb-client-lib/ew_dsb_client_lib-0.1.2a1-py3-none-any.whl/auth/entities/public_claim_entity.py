#!/usr/bin/env python3

from dataclasses import dataclass
from dataclasses_json import DataClassJsonMixin
from ew_dsb_client_lib.auth.entities.claim_data_entity import ClaimData

@dataclass(frozen=True)
class PublicClaim(DataClassJsonMixin):
    claimData: ClaimData
    iss: str