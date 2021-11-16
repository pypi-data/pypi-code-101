import binascii
import hashlib
import hmac
import json
import logging
import os
import socket
import sys
import threading
import time

from PyQt5.QtCore import pyqtSignal, QObject

sys.path.append('../')
from db.db_client import ClientDatabase
from common.decos import log
from common.errors import ServerError
from common.variables import *
from common.descriptors import Port, Host
from common.utils import Connector, get_message, send_message


# Логер и объект блокировки для работы с сокетом.
socket_lock = threading.Lock()


class ClientTransport(threading.Thread, QObject):
    CLIENT_LOG = logging.getLogger('app.client')

    server_address = Host()
    server_port = Port()

    # Сигналы новое сообщение и потеря соединения
    new_message = pyqtSignal(dict)
    connection_lost = pyqtSignal()
    message_205 = pyqtSignal()

    def __init__(self, port, ip_address, database, username, passwd, keys):

        threading.Thread.__init__(self)
        QObject.__init__(self)

        # Класс База данных - работа с базой
        self.database = database
        # Имя пользователя
        self.username = username
        # Сокет для работы с сервером
        self.transport = None
        # Пароль
        self.password = passwd
        # Набор ключей для шифрования
        self.keys = keys
        # Устанавливаем соединение:
        self.connection_init(port, ip_address)

        # Обновляем таблицы известных пользователей и контактов
        try:
            self.user_list_update()
            self.contacts_list_update()
        except OSError as err:
            if err.errno:
                ClientTransport.CLIENT_LOG.critical(
                    f'Потеряно соединение с сервером.')
                raise ServerError('Потеряно соединение с сервером!')
            ClientTransport.CLIENT_LOG.error(
                'Timeout соединения при обновлении списков пользователей.')
        except json.JSONDecodeError:
            ClientTransport.CLIENT_LOG.critical(
                f'Потеряно соединение с сервером.')
            raise ServerError('Потеряно соединение с сервером!')
            # Флаг продолжения работы транспорта.
        self.running = True

        self.SERVER_SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.SERVER_SOCK.connect((ip_address, port))

        self.connector = Connector(self.SERVER_SOCK)

        ClientTransport.CLIENT_LOG.info(
            f'Запущен клиент с парамертами: адрес сервера: {port}, '
            f'порт: {ip_address}, имя клиента: {username}')

    def connection_init(self, port, ip):
        # Инициализация сокета и сообщение серверу о нашем появлении
        self.transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Таймаут необходим для освобождения сокета.
        self.transport.settimeout(5)

        # Соединяемся, 5 попыток соединения, флаг успеха ставим в True если
        # удалось
        connected = False
        for i in range(5):
            self.CLIENT_LOG.info(f'Попытка подключения №{i + 1}')
            try:
                self.transport.connect((ip, port))
            except (OSError, ConnectionRefusedError):
                pass
            else:
                connected = True
                break
            time.sleep(1)

        # Если соединится не удалось - исключение
        if not connected:
            ClientTransport.CLIENT_LOG.critical(
                'Не удалось установить соединение с сервером')
            raise ServerError('Не удалось установить соединение с сервером')

        ClientTransport.CLIENT_LOG.debug('Установлено соединение с сервером')
        print('Установлено соединение с сервером')

        # Запускаем процедуру авторизации
        print('Запускаем процедуру авторизации')
        # Получаем хэш пароля
        passwd_bytes = self.password.encode('utf-8')
        salt = self.username.lower().encode('utf-8')
        passwd_hash = hashlib.pbkdf2_hmac('sha512', passwd_bytes, salt, 10000)
        passwd_hash_string = binascii.hexlify(passwd_hash)

        ClientTransport.CLIENT_LOG.debug(
            f'Passwd hash ready: {passwd_hash_string}')
        print(f'Passwd hash ready: {passwd_hash_string}')

        # Получаем публичный ключ и декодируем его из байтов
        pubkey = self.keys.publickey().export_key().decode('ascii')

        # Авторизируемся на сервере
        with socket_lock:
            presense = {
                ACTION: PRESENCE,
                TIME: time.time(),
                USER: {
                    ACCOUNT_NAME: self.username,
                    PUBLIC_KEY: pubkey
                }
            }
            ClientTransport.CLIENT_LOG.debug(f"Presense message = {presense}")
            print(f"Presense message = {presense}")
            # Отправляем серверу приветственное сообщение.
            try:
                send_message(self.transport, presense)
                ans = get_message(self.transport)
                ClientTransport.CLIENT_LOG.debug(f'Server response = {ans}.')
                print(f'Server response = {ans}.')
                # Если сервер вернул ошибку, бросаем исключение.
                if RESPONSE in ans:
                    if ans[RESPONSE] == 400:
                        raise ServerError(ans[ERROR])
                    elif ans[RESPONSE] == 511:
                        # Если всё нормально, то продолжаем процедуру
                        # авторизации.
                        ans_data = ans[DATA]
                        hash = hmac.new(
                            passwd_hash_string, ans_data.encode('utf-8'), 'MD5')
                        digest = hash.digest()
                        my_ans = RESPONSE_511
                        my_ans[DATA] = binascii.b2a_base64(
                            digest).decode('ascii')
                        send_message(self.transport, my_ans)
                        self.process_server_ans(get_message(self.transport))
            except (OSError, json.JSONDecodeError) as err:
                ClientTransport.CLIENT_LOG.debug(
                    f'Connection error.', exc_info=err)
                raise ServerError('Сбой соединения в процессе авторизации.')

    def run(self):
        ClientTransport.CLIENT_LOG.debug(
            'Запущен процесс - приёмник собщений с сервера.')
        while self.running:
            # Отдыхаем секунду и снова пробуем захватить сокет.
            # если не сделать тут задержку, то отправка может достаточно долго
            # ждать освобождения сокета.
            time.sleep(1)
            with socket_lock:
                try:
                    self.transport.settimeout(0.5)
                    message = get_message(self.transport)
                except OSError as err:
                    if err.errno:
                        ClientTransport.CLIENT_LOG.critical(
                            f'Потеряно соединение с сервером.')
                        self.running = False
                        self.connection_lost.emit()
                # Проблемы с соединением
                except (ConnectionError, ConnectionAbortedError, ConnectionResetError, json.JSONDecodeError, TypeError):
                    ClientTransport.CLIENT_LOG.debug(
                        f'Потеряно соединение с сервером.')
                    self.running = False
                    self.connection_lost.emit()
                # Если сообщение получено, то вызываем функцию обработчик:
                else:
                    ClientTransport.CLIENT_LOG.debug(
                        f'Принято сообщение с сервера: {message}')
                    print(f'Принято сообщение с сервера: {message}')
                    self.process_server_ans(message)
                finally:
                    self.transport.settimeout(5)

    @log
    def process_server_ans(self, message):
        ClientTransport.CLIENT_LOG.debug(
            f'Разбор сообщения от сервера: {message}')

        # Если это подтверждение чего-либо
        if RESPONSE in message:
            if message[RESPONSE] == 200:
                return
            elif message[RESPONSE] == 400:
                raise ServerError(f'{message[ERROR]}')
            else:
                ClientTransport.CLIENT_LOG.debug(
                    f'Принят неизвестный код подтверждения {message[RESPONSE]}')

        # Если это сообщение от пользователя даём сигнал о новом сообщении
        elif ACTION in message and message[ACTION] == MESSAGE and FROM in message and TO in message \
                and MESSAGE_TEXT in message and message[TO] == self.username:
            ClientTransport.CLIENT_LOG.debug(
                f'Получено сообщение от пользователя {message[FROM]}:{message[MESSAGE_TEXT]}')
            print(
                f'Получено сообщение от пользователя {message[FROM]}:{message[MESSAGE_TEXT]}')
            self.new_message.emit(message)

    @log
    def send_message(self, to_user, message):
        message_dict = {
            ACTION: MESSAGE,
            FROM: self.username,
            TO: to_user,
            TIME: time.time(),
            MESSAGE_TEXT: message
        }
        ClientTransport.CLIENT_LOG.debug(
            f'Сформирован словарь сообщения: {message_dict}')
        print(f'Сформирован словарь сообщения: {message_dict}')

        # Необходимо дождаться освобождения сокета для отправки сообщения
        with socket_lock:
            send_message(self.transport, message_dict)
            print(f'Отправлено сообщение для пользователя {to_user}')
            # self.process_server_ans(get_message(self.transport))
            ClientTransport.CLIENT_LOG.info(
                f'Отправлено сообщение для пользователя {to_user}')

    # Функция обновляющая контакт - лист с сервера
    def contacts_list_update(self):
        ClientTransport.CLIENT_LOG.debug(
            f'Запрос контакт листа для пользователся {self.name}')
        req = {
            ACTION: GET_CONTACTS,
            TIME: time.time(),
            USER: self.username
        }
        ClientTransport.CLIENT_LOG.debug(f'Сформирован запрос {req}')
        print(f'Запрос списка контактов пользователя {self.username}')
        with socket_lock:
            send_message(self.transport, req)
            ans = get_message(self.transport)
        ClientTransport.CLIENT_LOG.debug(f'Получен ответ {ans}')
        print(f'Получен ответ {ans}')
        if RESPONSE in ans and ans[RESPONSE] == 200:
            for contact in ans[LIST_INFO]:
                self.database.add_contact(contact)
        else:
            ClientTransport.CLIENT_LOG.error(
                'Не удалось обновить список контактов.')

    # Функция обновления таблицы известных пользователей.
    def user_list_update(self):
        ClientTransport.CLIENT_LOG.debug(
            f'Запрос списка известных пользователей {self.username}')
        req = {
            ACTION: GET_LIST,
            TIME: time.time(),
            ACCOUNT_NAME: self.username
        }
        print(f'Запрос списка всех известных пользователей')

        with socket_lock:
            print(f'send_message in user_list_update(): {req}) ')
            send_message(self.transport, req)
            ans = get_message(self.transport)
            print(f'Получили {ans}')
        if RESPONSE in ans and ans[RESPONSE] == 200:
            self.database.add_users(ans[LIST_INFO])
        else:
            ClientTransport.CLIENT_LOG.error(
                'Не удалось обновить список известных пользователей.')

    def key_request(self, user):
        '''Метод запрашивающий с сервера публичный ключ пользователя.'''
        ClientTransport.CLIENT_LOG.debug(f'Запрос публичного ключа для {user}')
        req = {
            ACTION: PUBLIC_KEY_REQUEST,
            TIME: time.time(),
            ACCOUNT_NAME: user
        }
        with socket_lock:
            send_message(self.transport, req)
            ans = get_message(self.transport)
        if RESPONSE in ans and ans[RESPONSE] == 511:
            return ans[DATA]
        else:
            ClientTransport.CLIENT_LOG.error(
                f'Не удалось получить ключ собеседника{user}.')

    # Функция сообщающая на сервер о добавлении нового контакта
    def add_contact(self, contact):
        ClientTransport.CLIENT_LOG.debug(f'Создание контакта {contact}')
        req = {
            ACTION: ADD_CONTACT,
            TIME: time.time(),
            USER: self.username,
            ACCOUNT_NAME: contact
        }
        with socket_lock:
            send_message(self.transport, req)
            self.process_server_ans(get_message(self.transport))

    # Функция удаления клиента на сервере
    def remove_contact(self, contact):
        ClientTransport.CLIENT_LOG.debug(f'Удаление контакта {contact}')
        req = {
            ACTION: DEL_CONTACT,
            TIME: time.time(),
            USER: self.username,
            ACCOUNT_NAME: contact
        }
        with socket_lock:
            send_message(self.transport, req)
            self.process_server_ans(get_message(self.transport))

    # Функция закрытия соединения, отправляет сообщение о выходе.
    def transport_shutdown(self):
        self.running = False
        message = {
            ACTION: EXIT,
            TIME: time.time(),
            ACCOUNT_NAME: self.username
        }
        with socket_lock:
            try:
                send_message(self.transport, message)
            except OSError:
                pass
        ClientTransport.CLIENT_LOG.debug('Транспорт завершает работу.')
        time.sleep(0.5)


if __name__ == '__main__':
    print(sys.argv)

    ClientTransport(8080, '127.0.0.1', ClientDatabase("test"), "test")
