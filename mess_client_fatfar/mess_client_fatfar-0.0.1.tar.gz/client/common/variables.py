""" Константы """

import logging

# Порт по умолчанию для сетевого ваимодействия
DEFAULT_PORT = 7777
# IP адрес по умолчанию для подключения клиента
DEFAULT_IP_ADDR = '127.0.0.1'
# Максимальная очередь подключений
MAX_CONNECTIONS = 5
# Максимальная длина сообщения в байтах
MAX_PACKAGE_LENGTH = 10240
# Кодировка проекта
ENCODING = 'utf-8'
# Текущий уровень логирования
LOGGING_LEVEL = logging.DEBUG
# База данных для хранения данных сервера:
SERVER_CONFIG = 'server.ini'

# Протокол JIM основные ключи:
ACTION = 'action'
TIME = 'time'
CPU_CONSUMPTION = 'cpu_consumption'
USER = 'user'
ACCOUNT_NAME = 'account_name'
SENDER = 'from'
DESTINATION = 'to'
DATA = 'bin'
PUBLIC_KEY = 'pubkey'

HERE = 'here'
FEEDBACK = 'feedback'
ERROR = 'error'
MESSAGE = 'message'
MESSAGE_TEXT = 'message_text'
EXIT = 'exit'
GET_CONTACTS = 'get_contacts'
LIST_INFO = 'data_list'
REMOVE_CONTACT = 'remove'
ADD_CONTACT = 'add'
USERS_REQUEST = 'get_users'
PUBLIC_KEY_REQUEST = 'pubkey_need'


# Словари - ответы:
# 200
RESPONSE_200 = {FEEDBACK: 200}
# 202
RESPONSE_202 = {FEEDBACK: 202,
                LIST_INFO: None
                }
# 400
RESPONSE_400 = {
    FEEDBACK: 400,
    ERROR: None
}
# 205
RESPONSE_205 = {
    FEEDBACK: 205
}

# 511
RESPONSE_511 = {
    FEEDBACK: 511,
    DATA: None
}
