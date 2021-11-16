import json

from .decos import log
from .variables import *


class Connector:
    def __init__(self, sock):
        self.sock = sock

    def get_message(self):
        encoded_response = self.sock.recv(MAX_PACKET_LENGTH)
        if isinstance(encoded_response, bytes):
            json_response = encoded_response.decode(ENCODING)
            response = json.loads(json_response)
            if isinstance(response, dict):
                return response
            raise ValueError
        raise ValueError

    def send_message(self, message):
        js_message = json.dumps(message, ensure_ascii=False)
        encoded_message = js_message.encode(ENCODING)
        self.sock.send(encoded_message)


# if __name__ == "__main__":
#     message = {
#         "test": [('client_2', '192.168.1.5', 7777, datetime.datetime(2021, 10, 28, 15, 5, 49, 716620)), ('client_3', '192.168.1.6', 6666, datetime.datetime(2021, 10, 28, 15, 5, 49, 763465)), ('client_4', '192.168.1.7', 5555, datetime.datetime(2021, 10, 28, 15, 5, 49, 810328))]
#     }
#     js_message = json.dumps(message, ensure_ascii=False)

@log
def get_message(client):
    encoded_response = client.recv(MAX_PACKET_LENGTH)
    json_response = encoded_response.decode(ENCODING)
    response = json.loads(json_response)
    if isinstance(response, dict):
        return response
    else:
        raise TypeError


# Утилита кодирования и отправки сообщения
# принимает словарь и отправляет его
@log
def send_message(sock, message):
    js_message = json.dumps(message, ensure_ascii=False)
    encoded_message = js_message.encode(ENCODING)
    sock.send(encoded_message)
