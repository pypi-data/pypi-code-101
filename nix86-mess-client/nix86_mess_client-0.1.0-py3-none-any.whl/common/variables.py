import logging


DEFAULT_PORT = 7777
DEFAULT_IP_ADDRESS = '127.0.0.1'
MAX_CONNECTIONS = 5
MAX_PACKAGE_LENGTH = 1024
ENCODING = 'utf-8'
SERVER_DATABASE = 'sqlite:///server_base.db3'

# Прококол JIM основные ключи:
ACTION = 'action'
SENDER = 'from'
DESTINATION = 'to'
PUBLIC_KEY = 'pubkey'
DATA = 'bin'

# Прочие ключи, используемые в протоколе
PRESENCE = 'presence'
RESPONSE = 'response'
ERROR = 'error'
MESSAGE = 'message'
MESSAGE_TEXT = 'message_text'
EXIT = 'exit'
REMOVE_CONTACT = 'remove_contact'
ADD_CONTACT = 'add_contact'
GET_CONTACTS = 'get_contacts'
LIST_INFO = 'data_list'
CONTACT = 'user_name'
USERS_REQUEST = 'get_users'
PUBLIC_KEY_REQUEST = 'pubkey_need'


RESPONSE_200 = {RESPONSE: 200}
RESPONSE_202 = {
    RESPONSE: 202,
    LIST_INFO: None
}
RESPONSE_205 = {
    RESPONSE: 205
}
RESPONSE_400 = {
    RESPONSE: 400,
    ERROR: None
}
RESPONSE_511 = {
    RESPONSE: 511,
    DATA: None
}

# LOG
LOGGING_LEVEL = logging.DEBUG
