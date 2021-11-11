from __future__ import annotations

import threading
from typing import TYPE_CHECKING

import requests
from requests.adapters import HTTPAdapter
from urllib3 import Retry
from urllib3.exceptions import MaxRetryError

from botco.methods.base import TelegramType, TelegramMethod

if TYPE_CHECKING:
    from botco import Bot

API_URL = "https://api.telegram.org"

thread_local = threading.local()


class Session:
    def __init__(self, api_url=API_URL):
        self._api_url = api_url

    def api_url(self, token: str, method: str):
        return f"{self._api_url}/bot{token}/{method}"

    @staticmethod
    def get_session(reset: bool = False, close: bool = False) -> requests.Session:
        if reset is True:
            setattr(thread_local, 'session', requests.Session())
        elif not hasattr(thread_local, 'session'):
            if not close:
                setattr(thread_local, 'session', requests.Session())
        return getattr(thread_local, 'session', None)

    def close(self):
        session = self.get_session(close=True)
        if session:
            session.close()
            del thread_local.session

    def __call__(self, bot: Bot, method: TelegramMethod[TelegramType]):
        request = method.build_request(bot)
        try:
            session = self.get_session()
            if bot.retry_on_error:
                retries = Retry(total=bot.max_retries,
                                backoff_factor=1,
                                status_forcelist=[500, 502, 503, 504])
                session.mount('https://', HTTPAdapter(max_retries=retries))
            response = session.post(
                self.api_url(bot.token, request.method),
                data=request.data,
                timeout=(bot.connect_timeout, bot.read_timeout)
            )
            data = response.json()
            data['method'] = method
            return method.build_response(data)
        except ConnectionError as e:
            print(e)
        except MaxRetryError as e:
            print('maxretry error', e)
        except TimeoutError as e:
            print(e)
