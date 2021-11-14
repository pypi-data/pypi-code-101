import logging

# Порт по умолчанию
PORT = 7777
# IP адрес по умолчанию
IP_ADDRESS = '127.0.0.1'
# Максимальная очередь подключений
MAX_CONNECTIONS = 10
# Максимальная длинна сообщения в байтах
MAX_PACKAGE_LENGTH = 1024000
# Кодировка
ENCODING = 'utf-8'
# База данных
DB = 'sqlite:///server_base.db3'

# Основные ключи:
ACTION = 'action'
TIME = 'time'
USER = 'user'
ACCOUNT_NAME = 'account_name'
FROM_USER = 'from_user'
TO_USER = 'to_user'
PUBLIC_KEY = 'pubkey'
DATA = 'bin'

# Прочие ключи
AUTHOR = 'author'
PRESENCE = 'presence'
RESPONSE = 'response'
ERROR = 'error'
MESSAGE = 'message'
ADD_CONTACT = 'add'
GET_CONTACTS = 'get_contacts'
USERS_REQUEST = 'get_users'
LIST_INFO = 'data_list'
REMOVE_CONTACT = 'remove'
TEXT = 'text'
EXIT = 'exit'
PUBLIC_KEY_REQUEST = 'pubkey_need'
HELP = [
    'Доступные комманды:',
    {
        'msg': 'отправка сообщения',
        'clear': 'очистить терминал',
        'exit': 'выход из клиента',
        'help': 'доступные команды',
        'contacts': 'список контактов',
        'edit': 'редактирование контактов',
        'history': 'история сообщений'
    }
]

# Логгирование
LOGGING_LEVEL = logging.DEBUG

RESPONSE_200 = {RESPONSE: 200}
RESPONSE_202 = {RESPONSE: 202, LIST_INFO: None}
RESPONSE_400 = {RESPONSE: 400, ERROR: None}
RESPONSE_205 = {RESPONSE: 205}
RESPONSE_511 = {RESPONSE: 511, DATA: None}
