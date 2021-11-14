import json
import sys
from common.variables import MAX_PACKAGE_LENGTH, ENCODING
from common.decors import func_log


@func_log
def get_msg(client):
    '''
    Функция приёма сообщений от удалённых компьютеров.
    Принимает сообщения JSON, декодирует полученное сообщение
    и проверяет что получен словарь.
    :param client: сокет для передачи данных.
    :return: словарь - сообщение.
    '''
    encoded_response = client.recv(MAX_PACKAGE_LENGTH)
    json_response = encoded_response.decode(ENCODING)
    response = json.loads(json_response)
    if isinstance(response, dict):
       return response
    else:
        raise TypeError

@func_log
def send_msg(sock, msg):
    json_msg = json.dumps(msg)
    enc_msg = json_msg.encode(ENCODING)
    sock.send(enc_msg)
