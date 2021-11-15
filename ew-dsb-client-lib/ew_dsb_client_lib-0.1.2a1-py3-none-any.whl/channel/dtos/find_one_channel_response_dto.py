#!/usr/bin/env python3

from dataclasses import dataclass
from dataclasses_json import DataClassJsonMixin
from ew_dsb_client_lib.channel.entities.channel_entity import Channel

@dataclass(frozen=True)
class FindOneChannelResponseDto(DataClassJsonMixin):
    findOneChannel: Channel