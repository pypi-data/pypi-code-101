"""Функции кодирования/ декодирования данных"""

import json
from common.variables import ENCODING
from decos import Log


def dict_to_bytes(message):
    """ Преобразование из данных в байты """
    if isinstance(message, dict):
        jmsg = json.dumps(message)
        bmsg = jmsg.encode(ENCODING)
        return bmsg
    else:
        raise TypeError


def bytes_to_dict(message):
    """ Преобразование из байт в данные """
    if isinstance(message, bytes):
        conv_msg = message.decode(ENCODING)
        conv_dict_msg = json.loads(conv_msg)
        if isinstance(conv_dict_msg, dict):
            return conv_dict_msg
        else:
            raise TypeError
    else:
        raise TypeError


@Log()
def send_msg(sock, message):
    """
    Функция отправки словарей через сокет.
    Кодирует словарь в формат JSON и отправляет через сокет.
    :param sock: сокет для передачи
    :param message: словарь для передачи
    :return: ничего не возвращает
    """
    bytes_view = dict_to_bytes(message)
    sock.send(bytes_view)


@Log()
def take_msg(sock):
    """
    Функция приёма сообщений от удалённых компьютеров.
    Принимает сообщения JSON, декодирует полученное сообщение
    и проверяет что получен словарь.
    :param sock: сокет для передачи данных.
    :return: словарь - сообщение.
    """
    bytes_response = sock.recv(1024)
    response = bytes_to_dict(bytes_response)
    return response
