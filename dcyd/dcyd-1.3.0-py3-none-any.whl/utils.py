#!/usr/bin/env python3

import base64
import json
import logging
import os
import pathlib
import pickle
import random


DEFAULT_DCYD_CONFIG_FILE = 'dcyd.json'

def generate_uid() -> str:
    '''
    Generate a sha1-like random hex string, 10 times faster than uuid.uuid4()

    The below illustrate the performance of similar solutions
    ```
    print(timeit.timeit(stmt=lambda: uuid.uuid4()))
    print(timeit.timeit(stmt=lambda: secrets.token_hex(16)))
    print(timeit.timeit(stmt=lambda: hashlib.sha1(random.getrandbits(64).to_bytes(8, 'big')).hexdigest()))
    print(timeit.timeit(stmt=lambda: random.getrandbits(160).to_bytes(20, 'big').hex()))
    ```
    '''
    return random.getrandbits(160).to_bytes(20, 'big').hex()


def get_project_id() -> str:
    '''Returns project_id from either env var or config file'''

    project_id = get_project_credentials()['project_id']

    if not project_id:
        report_client_error("Please set either DCYD_PROJECT_ID or DCYD_CONFIG_FILE env var")
        return ''

    return project_id


def get_config_from_file() -> dict:
    """
    If DCYD_CONFIG_FILE is set, return file's contents. (Assume file exists.)
    Else if the DEFAULT_DCYD_CONFIG_FILE exists as a file, return its contents.
    Else return {}.
    """

    config_file_path = pathlib.Path(os.getenv('DCYD_CONFIG_FILE', DEFAULT_DCYD_CONFIG_FILE))

    if config_file_path.exists():
        config = json.loads(config_file_path.read_text())
    else:
        config = {}

    return config


def get_project_credentials(
    *,
    config_from_file: dict = get_config_from_file(),
) -> dict:
    '''
    Returns project_access_token from either env var or config file

    >>> 'project_id' in get_project_credentials()
    True
    >>> 'project_access_token' in get_project_credentials()
    True
    '''

    project_id = os.getenv('DCYD_PROJECT_ID') or config_from_file.get('project_id')
    project_access_token = os.getenv('DCYD_PROJECT_ACCESS_TOKEN') or config_from_file.get('project_access_token')

    return {
        'project_id': project_id,
        'project_access_token': project_access_token,
    }


CLIENT_ERROR_MODE = os.getenv('DCYD_CLIENT_ERROR_MODE', 'log')


def report_client_error(message: str):
    if CLIENT_ERROR_MODE == 'raise_error':
        raise RuntimeError(message)
    elif CLIENT_ERROR_MODE == 'silent':
        return
    else:
        logging.error(message)


def base64_pickle(obj):
    '''To ensure obj is JSON-serializable, pickle and base64-encode it.

    arg obj: object to be tested for JSON-serializability
    type obj: any Python object

    returns: a transformation of obj that is JSON-serializable.
    '''
    try:
        encoded_obj = base64.b64encode(  # encode byte string into bytes
            pickle.dumps(obj)  # convert object into a byte string
        ).decode('ascii')
        success = True
    except Exception as e:
        encoded_obj = base64.b64encode(
            pickle.dumps(e)
        ).decode('ascii')
        success = False
    return encoded_obj, success


def api_url(path='') -> str:
    return os.getenv('DCYD_API_BASE', 'https://api.dcyd.io') + path
