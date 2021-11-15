#!/usr/bin/env python3

from dataclasses import dataclass
from typing import Any, AsyncGenerator, Dict, List

from dataclasses_json import DataClassJsonMixin
from ew_dsb_client_lib.gqls.gql_service import GQLService
from ew_dsb_client_lib.message.dtos.operation_message_dto import (
    FindAllMessagesDto, PublishMessageDto, ReceiveMessageDto, SendMessageDto,
    SubscribeMessageDto)
from ew_dsb_client_lib.message.dtos.response_message_dto import (
    FindAllMessagesResponseDto, PublishMessageResponseDto,
    ReceiveMessageResponseDto, SendMessageResponseDto,
    SubscribeMessageResponseDto)
from ew_dsb_client_lib.message.entities.message_entity import Message
from ew_dsb_client_lib.message.operations.mutation_message_operation import (
    PublishMessageMutation, SendMessageMutation)
from ew_dsb_client_lib.message.operations.query_message_operation import \
    FindAllMessagesQuery
from ew_dsb_client_lib.message.operations.subscription_message_operation import (
    ReceiveMessageSubscription, SubscribeMessageSubscription)
from gql import Client, gql


class MessageService:
    http_client: Client
    ws_client: Client

    def __init__(self, gql_service:GQLService):
        self.http_client = gql_service.http_client
        self.ws_client = gql_service.ws_client

    async def find_all(self, find_all_messages_dto: FindAllMessagesDto) -> List[Message]:
        """Gets a list of historical messages

        Parameters
        ----------
        find_all_messages_dto : FindAllMessagesDto

        Returns
        -------
        List[Message]
        """
        query = gql("".join(set(FindAllMessagesQuery)))
        variables: Dict[str, Any] = {
            'findAllMessagesDto': find_all_messages_dto.to_dict()
        }
        response_text = await self.http_client.execute_async(
            query, 
            variable_values=variables
        )
        res = FindAllMessagesResponseDto.from_dict(response_text)
        return res.findAllMessages

    async def publish(self, publish_message_dto: PublishMessageDto) -> bool:
        """Broadcast a message to a channel

        Parameters
        ----------
        publish_message_dto : PublishMessageDto

        Returns
        -------
        bool
        """
        query = gql("".join(set(PublishMessageMutation)))
        variables: Dict[str, Any] = {
            'publishMessageDto': publish_message_dto.to_dict()
        }
        response_text = await self.http_client.execute_async(
            query, 
            variable_values=variables
        )
        res = PublishMessageResponseDto.from_dict(response_text)
        return res.publishMessage

    async def subscribe(self, subscribe_message_dto: SubscribeMessageDto) -> AsyncGenerator[Message, None]:
        """Subscribe to a channel

        Parameters
        ----------
        subscribe_message_dto : SubscribeMessageDto

        Returns
        -------
        AsyncGenerator[Message, None]

        Yields
        -------
        Iterator[AsyncGenerator[Message, None]]
        """
        query = gql("".join(set(SubscribeMessageSubscription)))
        variables: Dict[str, Any] = {
            'subscribeMessageDto': subscribe_message_dto.to_dict()
        }
        async with self.ws_client as session:
            subscription = session.subscribe(
                query, 
                variable_values=variables
            )
            async for response_text in subscription:
                res = SubscribeMessageResponseDto.from_dict(response_text)
                yield res.subscribeMessage

    async def send(self, send_message_dto: SendMessageDto) -> bool:
        """Send a message to a recipient_DID

        Parameters
        ----------
        send_message_dto : SendMessageDto

        Returns
        -------
        bool
        """
        query = gql("".join(set(SendMessageMutation)))
        variables: Dict[str, Any] = {
            'sendMessageDto': send_message_dto.to_dict()
        }
        response_text = await self.http_client.execute_async(
            query, 
            variable_values=variables
        )
        res = SendMessageResponseDto.from_dict(response_text)
        return res.sendMessage

    async def receive(self, receive_message_dto: ReceiveMessageDto) -> AsyncGenerator[Message, None]:
        """Receive a message from a sender_DID

        Parameters
        ----------
        receive_message_dto : ReceiveMessageDto

        Returns
        -------
        AsyncGenerator[Message, None]
            [description]

        Yields
        -------
        Iterator[AsyncGenerator[Message, None]]
            [description]
        """
        query = gql("".join(set(ReceiveMessageSubscription)))
        variables: Dict[str, Any] = {
            'receiveMessageDto': receive_message_dto.to_dict()
        }
        async with self.ws_client as session:
            subscription = session.subscribe(
                query, 
                variable_values=variables
            )
            async for response_text in subscription:
                res = ReceiveMessageResponseDto.from_dict(response_text)
                yield res.receiveMessage
