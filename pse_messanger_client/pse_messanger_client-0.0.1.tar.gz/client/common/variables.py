# Файл констант

DEFAULT_PORT = 8080
DEFAULT_IP_ADDRESS = '127.0.0.1'
MAX_CONNECTIONS = 10
MAX_PACKET_LENGTH = 4096
ENCODING_FIELD = 'encoding'
ENCODING = 'utf-8'

ACTION = 'action'
EXIT = 'exit'
TIME = 'time'
USER = 'user'
ACCOUNT_NAME = 'account_name'

PRESENCE = 'presence'
RESPONSE = 'response'
ERROR = 'error'
DATA = 'data'

AUTHENTICATE = 'authenticate'
QUIT = 'quit'
PROBE = 'probe'
MESSAGE = 'msg'
JOIN_GROUP = 'join'
LEAVE_GROUP = 'leave'
STATUS = 'status'
LOGGING_LEVEL = 'DEBUG'
USERS_REQUEST = 'users_request'

MESSAGE_TEXT = 'message_text'
SENDER = 'sender'
TO = 'to'
FROM = 'from'
GET_CONTACTS = 'get_contacts'
ADD_CONTACT = 'add_contact'
DEL_CONTACT = 'del_contact'
LIST_INFO = 'list_info'
GET_LIST = "get_list"
PUBLIC_KEY = "public_key"
PUBLIC_KEY_REQUEST = "public_key_request"

# Словари - ответы:
# 200
RESPONSE_200 = {RESPONSE: 200}
# 400
RESPONSE_400 = {
    RESPONSE: 400,
    ERROR: None
}

RESPONSE_205 = {RESPONSE: 205}
RESPONSE_511 = {
    RESPONSE: 511,
    DATA: ''}
