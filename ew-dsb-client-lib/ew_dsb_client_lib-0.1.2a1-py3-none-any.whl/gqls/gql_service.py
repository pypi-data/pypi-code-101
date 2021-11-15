#!/usr/bin/env python3

import os
from typing import Dict

from ew_dsb_client_lib.gqls.entities.headers_entity import Headers
from py_dotenv import read_dotenv

from gql import Client, gql
from gql.transport.aiohttp import AIOHTTPTransport
from gql.transport.websockets import WebsocketsTransport

# Read dotenv
dotenv_path = os.path.join(os.path.abspath('./'), '.env')
read_dotenv(dotenv_path)
DEBUG:bool = (os.getenv('DEBUG', 'False') == 'True')
SERVER_HOST:str = os.getenv('SERVER_HOST')
SERVER_PORT:str = os.getenv('SERVER_PORT')

class GQLService:
    http_url:str 
    ws_url:str
    headers:Headers
    http_client: Client
    ws_client: Client

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

        if DEBUG is True:
            self.http_url = 'http://localhost:3000/graphql'
            self.ws_url = 'ws://localhost:3000/graphql'
        else:
            self.http_url = 'http://{}:{}/graphql'.format(SERVER_HOST, SERVER_PORT)
            self.ws_url = 'ws://{}:{}/graphql'.format(SERVER_HOST, SERVER_PORT)

        self.headers = Headers( Authorization='' ).to_dict()

        http_transport = AIOHTTPTransport( url=self.http_url, headers=self.headers )
        self.http_client = Client(transport=http_transport, fetch_schema_from_transport=True)

        ws_transport = WebsocketsTransport( url=self.ws_url , init_payload=self.headers )
        self.ws_client = Client(transport=ws_transport, fetch_schema_from_transport=True)

    def update(self, **kwargs):
        self.__dict__.update(kwargs)

        for key, value in self.__dict__.items():
            if key == 'bearer_token':
                self.headers = Headers( Authorization="".join(['Bearer ', value]) ).to_dict()

        http_transport = AIOHTTPTransport( url=self.http_url, headers=self.headers )
        self.http_client = Client(transport=http_transport, fetch_schema_from_transport=True)

        ws_transport = WebsocketsTransport( url=self.ws_url , init_payload=self.headers )
        self.ws_client = Client(transport=ws_transport, fetch_schema_from_transport=True)        
