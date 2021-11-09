import os
import arc4
import random
import string
import getpass
import termcolor


def gen_key(length: int = 12):
    source = string.ascii_lowercase + string.digits
    return ''.join(random.choice(source) for _ in range(length))


def load_login_info(path: str = '') -> (str, str):
    if not path:
        path = os.path.expanduser('~/.ykps_info')

    if os.path.isfile(path):
        with open(path, 'r') as f:
            info = [i.strip() for i in f.readlines()]

        if len(info) == 3:
            user, pwd, key = info
            stream = bytes.fromhex(pwd)
            return (user, arc4.ARC4(key).decrypt(stream).decode('utf-8'))

        print(termcolor.colored(
            'Info save file has incorrect format. Reloading.',
            'red'
        ))

    user = input('Student ID: ')
    pwd = getpass.getpass()

    encrypted, key = encrypt(pwd)

    with open(path, 'w+') as f:
        f.write('\n'.join([user, encrypted, key]))

    return (user, pwd)


def clear_info_cache(path: str = ''):
    if not path:
        path = os.path.expanduser('.ykps_info')

    if os.path.isfile(path):
        os.remove(path)
        print('User info file removed.')
    else:
        print('There is no user info file.')


def encrypt(pwd: str) -> (str, str):
    key = gen_key()
    return (arc4.ARC4(key).encrypt(pwd).hex(), key)