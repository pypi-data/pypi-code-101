#!/usr/bin/env python3

from dataclasses import dataclass
from dataclasses_json import DataClassJsonMixin

@dataclass(frozen=True)
class FindAllMessagesDto(DataClassJsonMixin):
    fqcn: str
    take: int
    skip: int
    startDate: int
    endDate: int
  
@dataclass(frozen=True)
class PublishMessageDto(DataClassJsonMixin):
    fqcn: str
    payload: str
    signature: str

@dataclass(frozen=True)
class SubscribeMessageDto(DataClassJsonMixin):
    fqcn: str

@dataclass(frozen=True)
class SendMessageDto(DataClassJsonMixin):
    recipientDID: str
    payload: str
    signature: str

@dataclass(frozen=True)
class ReceiveMessageDto(DataClassJsonMixin):
    recipientDID: str
