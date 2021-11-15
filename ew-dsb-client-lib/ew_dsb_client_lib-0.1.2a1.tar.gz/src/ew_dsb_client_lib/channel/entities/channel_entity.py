#!/usr/bin/env python3

from dataclasses import dataclass
from dataclasses_json import DataClassJsonMixin

@dataclass(frozen=True)
class Channel(DataClassJsonMixin):
    fqcn: str
    description: str
    publicKey: str
    privateKey: str
    maxTimeout: int
    defaultTimeout: int
