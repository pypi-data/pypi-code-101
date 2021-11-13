# encoding: utf-8
import os
import time
import socket
import inspect
import aiohttp
import asyncio
import requests
from flask import request
from functools import wraps
from dotenv import load_dotenv

# load_dotenv()
# loop = asyncio.get_event_loop()

# TOKEN = os.environ.get('ACTION_LOGGER_TOKEN')
# SERVICE_ID = int(os.environ.get('ACTION_LOGGER_SERVICE_ID'))
# API_ACTION_POST = os.environ.get('ACTION_LOGGER_API_ACTION_POST')


class ActionClient:

    def __init__(self, token, service_id, api_action_post_address):
        self.TOKEN = token
        self.SERVICE_ID = int(service_id)
        self.API_ACTION_POST = api_action_post_address

    def get_client_info(self):
        """
        Get client details.
        """
        client_ip = request.environ['REMOTE_ADDR']
        client_port = request.environ['REMOTE_PORT']
        client_UA = request.headers['User-Agent']
        data = {
            'client_ip': client_ip,
            'client_port': client_port,
            'hostname': None,
            'client_UA': client_UA
        }
        return data

    async def push(self, session, url, data):
        async with session.post(url, json=data, timeout=0.5) as response:
            await response.text()

    def sync_push(self, url, data):
        response = requests.post(url, json=data, timeout=0.5, verify=False)
        return response.text

    async def async_post(self, event_detail, event_start_time, event_end_time, use_time):
        """
        Push to the action logger server.
        :param event_detail:
        :param event_start_time:
        :param event_end_time:
        :param use_time:
        :return:
        """
        async with aiohttp.ClientSession() as session:
            data = {}
            client_info = self.get_client_info()

            data['service_id'] = self.SERVICE_ID
            data['event_start_time'] = event_start_time
            data['event_end_time'] = event_end_time
            data['use_time'] = use_time

            data['event_detail'] = event_detail
            data['event_detail']['user_ip'] = client_info.get('client_ip')
            data['event_detail']['user_port'] = client_info.get('client_port')
            data['event_detail']['user_hostname'] = client_info.get('hostname')
            data['event_detail']['user_UA'] = client_info.get('client_UA')
            data['event_detail']['user_email'] = ''
            data['token'] = self.TOKEN
            await self.push(session, self.API_ACTION_POST, data)

    def sync_post(self, event_detail, event_start_time, event_end_time, use_time):
        """
        Push to the action logger server.
        :param event_detail:
        :param event_start_time:
        :param event_end_time:
        :param use_time:
        :return:
        """
        data = {}
        client_info = self.get_client_info()

        data['service_id'] = self.SERVICE_ID
        data['event_start_time'] = event_start_time
        data['event_end_time'] = event_end_time
        data['use_time'] = use_time

        data['event_detail'] = event_detail
        data['event_detail']['user_ip'] = client_info.get('client_ip')
        data['event_detail']['user_port'] = client_info.get('client_port')
        data['event_detail']['user_hostname'] = client_info.get('hostname')
        data['event_detail']['user_UA'] = client_info.get('client_UA')
        data['event_detail']['user_email'] = ''
        data['token'] = self.TOKEN
        self.sync_push(self.API_ACTION_POST, data)

    def action_post(self, function_to_protect):
        """
        Record the details of the event, client information, event time, etc.
        :param function_to_protect:
        :return:
        """
        @wraps(function_to_protect)
        def wrapper(*args, **kwargs):
            start = time.time()
            event_start_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start))
            ans = function_to_protect(*args, **kwargs)  # call func
            end = time.time()
            event_end_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(end))
            use_time = end - start
            event_detail = {
                'func_name': function_to_protect.__name__,
                'func_parameters': [args, kwargs],
                'func_source_code': inspect.getsource(function_to_protect),
                'func_module_name': function_to_protect.__module__,
                'func_doc': function_to_protect.__doc__,
            }
            try:
                self.sync_post(event_detail, event_start_time, event_end_time, use_time)
                # loop.run_until_complete(async_post(event_detail, event_start_time, event_end_time, use_time))
            except Exception as e:
                print(f'Action logger: {e}')
            return ans

        return wrapper
