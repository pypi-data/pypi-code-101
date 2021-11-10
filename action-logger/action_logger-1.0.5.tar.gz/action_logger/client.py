# encoding: utf-8
import os
import time
import socket
import inspect
import aiohttp
import asyncio
from functools import wraps
from dotenv import load_dotenv

load_dotenv()
loop = asyncio.get_event_loop()

TOKEN = os.environ.get('ACTION_LOGGER_TOKEN')
SERVICE_ID = int(os.environ.get('ACTION_LOGGER_SERVICE_ID'))
API_ACTION_POST = os.environ.get('ACTION_LOGGER_API_ACTION_POST')


def get_client_info():
    """
    Get information from client.
    """
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    data = {
        'ip': ip,
        'hostname': hostname
    }
    return data


async def push(session, url, data):
    async with session.post(url, json=data, timeout=0.2) as response:
        await response.text()


async def async_post(event_detail):
    async with aiohttp.ClientSession() as session:
        data = {}
        client_info = get_client_info()

        data['service_id'] = SERVICE_ID
        data['event_start_time'] = time.strftime('%Y-%m-%d %H:%M:%S')
        data['event_detail'] = event_detail
        data['event_detail']['user_ip'] = client_info.get('ip')
        data['event_detail']['user_port'] = None
        data['event_detail']['user_hostname'] = client_info.get('hostname')
        data['event_detail']['user_email'] = ''
        data['token'] = TOKEN
        await push(session, API_ACTION_POST, data)


def action_post(function_to_protect):
    @wraps(function_to_protect)
    def wrapper(*args, **kwargs):
        event_detail = {
            'func_name': function_to_protect.__name__,
            'func_parameters': [args, kwargs],
            'func_source_code': inspect.getsource(function_to_protect),
            'func_module_name': function_to_protect.__module__,
            'func_doc': function_to_protect.__doc__,
        }
        try:
            loop.run_until_complete(async_post(event_detail))
        except Exception as e:
            print(f'Action logger: {e}')
        return function_to_protect(*args, **kwargs)

    return wrapper
