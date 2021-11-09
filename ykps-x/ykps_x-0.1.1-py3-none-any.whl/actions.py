import re
import json
import requests
import termcolor

from .info import load_login_info, encrypt
from .utils import Page


QUOTE = re.compile('(?<!\\\\)\'')


def auth():
    user, pwd = load_login_info()
    encrypted, key = encrypt(pwd)

    url = 'http://1.1.1.3/ac_portal/login.php'
    data = {
        'opr': 'pwdLogin',
        'userName': user,
        'pwd': encrypted,
        'rc4Key': key,
        'rememberPwd': 1
    }

    print('Sending Request...')
    response = requests.post(url, data=data)
    text = QUOTE.sub('"', response.text)

    if json.loads(text).get('success', ''):
        print(termcolor.colored('Connected!',  'green'))
    else:
        print(termcolor.colored('Login Failed: ' + response.text, 'red'))