#!/usr/bin/env python3

from dataclasses import dataclass
from dataclasses_json import DataClassJsonMixin

@dataclass(frozen=True)
class CreateChannelDto(DataClassJsonMixin):
    fqcn: str
    description: str
    publisherRole: str
    subscriberRole: str
