import logging
import os
from getpass import getpass

logger = logging.Logger(__name__)

SLIDE_CONFIG = {
    'AUTH_URL': os.getenv('AUTH_URL', 'http://trial.omnipath.cc:9802'),
    'APP_API_URL': os.getenv('APP_API_URL', 'http://trial.omnipath.cc:9801'),
    'MICRON_PER_PIXEL_X': float(os.getenv('MICRON_PER_PIXEL_X', 0.35093510)),
    'MICRON_PER_PIXEL_Y': float(os.getenv('MICRON_PER_PIXEL_Y', 0.35150376)),
    'TILE_CACHE_MAX_SIZE': int(os.getenv('TILE_CACHE_MAX_SIZE', 1024))
}


def update_config(**kwargs):
    new_config = SLIDE_CONFIG.update(kwargs)
    logger.info(f"new config is {SLIDE_CONFIG}")
    return new_config


def use_password_grant(username=None, password=None):
    if username:
        USERNAME = username
    else:
        USERNAME = input("Please enter the user name of coriander: ")

    if password:
        PASSWORD = password
    else:
        PASSWORD = getpass(f"Please enter the password of {USERNAME}: ")

    logger.info(f"use password grant type to access private cloud.")
    new_config = SLIDE_CONFIG.update(
        USERNAME=USERNAME,
        PASSWORD=PASSWORD,
        SCOPE=os.getenv('SCOPE', 'App'),
        CLIENT_ID=os.getenv('CLIENT_ID', 'App_App'),
        CLIENT_SECRET=os.getenv('CLIENT_SECRET', '123456'),
        GRANT_TYPE=os.getenv('GRANT_TYPE', 'password'))
    logger.info(f"new config is {SLIDE_CONFIG}")
    return new_config


def use_client_grant():
    new_config = SLIDE_CONFIG.update(
        GRANT_TYPE=os.getenv('GRANT_TYPE', 'client_credentials'),
        SCOPE=os.getenv('SCOPE', 'App'),
        CLIENT_SECRET=os.getenv('CLIENT_SECRET', '123456'),
        CLIENT_ID=os.getenv('CLIENT_ID', 'App_App'))
    logger.info(f"new config is {SLIDE_CONFIG}")
    return new_config


def is_client_grant():
    return SLIDE_CONFIG['GRANT_TYPE'] == 'client_credentials'


def get_grant_data():
    if is_client_grant():
        return {
            "grant_type": SLIDE_CONFIG['GRANT_TYPE'],
            "scope": SLIDE_CONFIG['SCOPE'],
            "client_id": SLIDE_CONFIG['CLIENT_ID'],
            "client_secret": SLIDE_CONFIG['CLIENT_SECRET']
        }
    return {
        "grant_type": SLIDE_CONFIG['GRANT_TYPE'],
        "scope": SLIDE_CONFIG['SCOPE'],
        "client_id": SLIDE_CONFIG['CLIENT_ID'],
        "client_secret": SLIDE_CONFIG['CLIENT_SECRET'],
        "username": SLIDE_CONFIG['USERNAME'],
        "password": SLIDE_CONFIG['PASSWORD']
    }


def get_config(key: str):
    return SLIDE_CONFIG[key]


use_client_grant()
