#!/usr/bin/env python3

from dataclasses import dataclass
from typing import Any, AsyncGenerator, Dict, List

from dataclasses_json import DataClassJsonMixin
from ew_dsb_client_lib.channel.dtos.create_channel_dto import CreateChannelDto
from ew_dsb_client_lib.channel.dtos.create_channel_response_dto import \
    CreateChannelResponseDto
from ew_dsb_client_lib.channel.dtos.find_one_channel_dto import \
    FindOneChannelDto
from ew_dsb_client_lib.channel.dtos.find_one_channel_response_dto import \
    FindOneChannelResponseDto
from ew_dsb_client_lib.channel.dtos.remove_channel_dto import RemoveChannelDto
from ew_dsb_client_lib.channel.dtos.remove_channel_response_dto import \
    RemoveChannelResponseDto
from ew_dsb_client_lib.channel.entities.channel_entity import Channel
from ew_dsb_client_lib.channel.operations.mutation_channel_operation import (
    CreateChannelMutation, RemoveChannelMutation)
from ew_dsb_client_lib.channel.operations.query_channel_operation import \
    FindOneChannelQuery
from ew_dsb_client_lib.gqls.gql_service import GQLService
from gql import Client, gql


class ChannelService:
    http_client: Client
    ws_client: Client

    def __init__(self, gql_service:GQLService):
        self.http_client = gql_service.http_client
        self.ws_client = gql_service.ws_client
            
    async def find_one(self, find_one_channel_dto: FindOneChannelDto) -> Channel:
        """Get a channel metadata

        Parameters
        ----------
        find_one_channel_dto : FindOneChannelDto

        Returns
        -------
        Channel
        """
        query = gql("".join(set(FindOneChannelQuery)))
        variables: Dict[str, Any] = {
            'findOneChannelDto': find_one_channel_dto.to_dict()
        }
        response_text = await self.http_client.execute_async(
            query, 
            variable_values=variables
        )
        res = FindOneChannelResponseDto.from_dict(response_text)
        return res.findOneChannel

    async def create(self, create_channel_dto: CreateChannelDto) -> Channel:
        """Create a new channel

        Parameters
        ----------
        create_channel_dto : CreateChannelDto

        Returns
        -------
        Channel
        """
        query = gql("".join(set(CreateChannelMutation)))
        variables: Dict[str, Any] = {
            'createChannelDto': create_channel_dto.to_dict()
        }
        response_text = await self.http_client.execute_async(
            query, 
            variable_values=variables
        )
        res = CreateChannelResponseDto.from_dict(response_text)
        return res.createChannel

    async def remove(self, remove_channel_dto: RemoveChannelDto) -> str:
        """Remove an existing channel

        Parameters
        ----------
        remove_channel_dto : RemoveChannelDto

        Returns
        -------
        str
        """
        query = gql("".join(set(RemoveChannelMutation)))
        variables: Dict[str, Any] = {
            'removeChannelDto': remove_channel_dto.to_dict()
        }
        response_text = await self.http_client.execute_async(
            query, 
            variable_values=variables
        )
        res = RemoveChannelResponseDto.from_dict(response_text)
        return res.removeChannel

    async def find_public_key(self, fqcn: str) -> str:
        """Get channel's public key

        Parameters
        ----------
        fqcn : str

        Returns
        -------
        str
        """
        find_one_channel_dto: FindOneChannelDto = FindOneChannelDto(
            fqcn
        )
        channel:Channel = await self.find_one(find_one_channel_dto)
        public_key:str = channel.publicKey
        return public_key

    async def find_private_key(self, fqcn: str) -> str:
        """Get channel's private key

        Parameters
        ----------
        fqcn : str

        Returns
        -------
        str
        """
        find_one_channel_dto: FindOneChannelDto = FindOneChannelDto(
            fqcn
        )
        channel:Channel = await self.find_one(find_one_channel_dto)
        private_key:str = channel.privateKey
        return private_key
