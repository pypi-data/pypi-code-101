#!/usr/bin/env python3

from dataclasses import dataclass
from dataclasses_json import DataClassJsonMixin
from ew_dsb_client_lib.message.entities.message_entity import Message
from typing import List, AsyncGenerator

@dataclass(frozen=True)
class FindAllMessagesResponseDto(DataClassJsonMixin):
    findAllMessages: List[Message]

@dataclass(frozen=True)
class PublishMessageResponseDto(DataClassJsonMixin):
    publishMessage: bool

@dataclass(frozen=True)
class SubscribeMessageResponseDto(DataClassJsonMixin):
    subscribeMessage: AsyncGenerator[Message, None]

@dataclass(frozen=True)
class SendMessageResponseDto(DataClassJsonMixin):
    sendMessage: bool

@dataclass(frozen=True)
class ReceiveMessageResponseDto(DataClassJsonMixin):
    receiveMessage: AsyncGenerator[Message, None]
