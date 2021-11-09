import os
import time
import hmac
import hashlib
import base64
import urllib.parse
import json

import requests


class ConfigNotFound(Exception):
    pass


class TokenError(Exception):
    pass


class URLError(Exception):
    pass


class SecretError(Exception):
    pass


class Dingbot:
    def __init__(self, webhook, secret):
        self.webhook = webhook
        self.secret = secret

    @property
    def sign(self):
        timestamp = str(round(time.time() * 1000))
        secret_enc = self.secret.encode('utf-8')
        string_to_sign = '{}\n{}'.format(timestamp, self.secret)
        string_to_sign_enc = string_to_sign.encode('utf-8')
        hmac_code = hmac.new(secret_enc, string_to_sign_enc,
                             digestmod=hashlib.sha256).digest()
        sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
        self.signstring = sign
        self.timestamp = timestamp

    @property
    def url(self):
        self.sign
        url = '&'.join([self.webhook,
                        '&'.join([f'timestamp={self.timestamp}',
                                  f'sign={self.signstring}'])])
        return url

    def send_msg(self, title, text, at_mobiles=None, at_all=False):
        content = '### {0}\n\n{1}'.format(title, text)
        if at_mobiles:
            at_string = ' '.join([f'@{mobile}' for mobile in at_mobiles])
            all_text = f'{content}\n\n{at_string}'
        else:
            all_text = content
        data = {
            'msgtype': 'markdown',
            'markdown': {
                'title': title,
                'text': all_text
            },
            'at': {
                'atMobiles': at_mobiles,
                'isAtAll': at_all
            }
        }
        print(f'url: {self.url}')
        return requests.post(url=self.url, headers={
            'Content-Type': 'application/json'
        }, data=json.dumps(data)).text


def inform(webhook,
           secret,
           title='TASK NAME',
           text='TEXT',
           at_mobiles=None,
           at_all=False):
    """Send message to dingbot

    Args:
        dingbot_id (str, optional): Dingbot id that you setted in config, 
                                    if you don't know, use the command line "pydingbot-ls-dingbot" to list all dingbots ids.
                                    Defaults to 'default'.
        title (str, optional): The title showing in dingbot. Defaults to 'TASK NAME'.
        text (str, optional): The text showing in dingbot, it support markdown syntax. Defaults to 'TEXT'.
    """
    dingbot = Dingbot(webhook, secret)
    return dingbot.send_msg(title, text, at_mobiles=at_mobiles, at_all=at_all)


if __name__ == '__main__':
    pass
