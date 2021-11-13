""" Реализация транспортной подсистемы клиента """

import socket
import psutil
import time
import logging
import json
import threading
import hashlib
import hmac
import binascii
from PyQt5.QtCore import pyqtSignal, QObject

from common.utils import *
from common.variables import *
from errors import ServerError

# Логер и объект блокировки для работы с сокетом.
LOGGER = logging.getLogger('client')
socket_lock = threading.Lock()


class ClientTransport(threading.Thread, QObject):
    """ Класс, реализующий транспортную подсистему клиентского модуля."""
    # Сигналы, новое сообщение и потеря соединения
    new_message = pyqtSignal(dict)
    message_205 = pyqtSignal()
    connection_lost = pyqtSignal()

    def __init__(self, port, ip_address, database, username, passwd, keys):
        # Вызываем конструктор предка
        threading.Thread.__init__(self)
        QObject.__init__(self)

        # Класс База данных - работа с базой
        self.database = database
        # Имя пользователя
        self.username = username
        # Пароль
        self.password = passwd
        # Сокет для работы с сервером
        self.transport = None
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
                LOGGER.critical(f'Server connection is lost.')
                raise ServerError('Server connection is lost')
            LOGGER.error('Timeout connection during the update of users list.')
        except json.JSONDecodeError:
            LOGGER.critical(f'Server connection is lost')
            raise ServerError('It is impossible to connect with server')
            # Флаг продолжения работы транспорта.
        self.running = True

    def connection_init(self, port, ip):
        """  Метод инициализации соединения с сервером """
        # Инициализация сокета и сообщение серверу о нашем появлении
        self.transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Таймаут необходим для освобождения сокета.
        self.transport.settimeout(5)

        # Соединяемся, 5 попыток соединения, флаг успеха ставим в True если
        # удалось
        connected = False
        for i in range(5):
            LOGGER.info(f'Attempt to connect №{i + 1}')
            try:
                self.transport.connect((ip, port))
            except (OSError, ConnectionRefusedError):
                pass
            else:
                connected = True
                LOGGER.debug("Connection established.")
                break
            time.sleep(1)

        # Если соединиться не удалось - исключение
        if not connected:
            LOGGER.critical('Connection with server is not provided')
            raise ServerError('Connection with server is not provided')

        LOGGER.debug('Starting auth dialog.')

        # Запускаем процедуру авторизации
        # Получаем хэш пароля
        passwd_bytes = self.password.encode('utf-8')
        salt = self.username.lower().encode('utf-8')
        passwd_hash = hashlib.pbkdf2_hmac('sha512', passwd_bytes, salt, 10000)
        passwd_hash_string = binascii.hexlify(passwd_hash)

        LOGGER.debug(f'Passwd hash ready: {passwd_hash_string}')

        # Получаем публичный ключ и декодируем его из байтов
        pubkey = self.keys.publickey().export_key().decode('ascii')

        # Авторизируемся на сервере
        with socket_lock:
            presense = {
                ACTION: HERE,
                TIME: time.time(),
                CPU_CONSUMPTION: psutil.virtual_memory().available,
                USER: {
                    ACCOUNT_NAME: self.username,
                    PUBLIC_KEY: pubkey
                }
            }
            LOGGER.debug(f"Presence message = {presense}")
            # Отправляем серверу приветственное сообщение.
            try:
                send_msg(self.transport, presense)
                ans = take_msg(self.transport)
                LOGGER.debug(f'Server response = {ans}.')
                # Если сервер вернул ошибку, бросаем исключение.
                if FEEDBACK in ans:
                    if ans[FEEDBACK] == 400:
                        raise ServerError(ans[ERROR])
                    elif ans[FEEDBACK] == 511:
                        # Если всё нормально, то продолжаем процедуру
                        # авторизации.
                        ans_data = ans[DATA]
                        hash = hmac.new(
                            passwd_hash_string, ans_data.encode('utf-8'), 'MD5')
                        digest = hash.digest()
                        my_ans = RESPONSE_511
                        my_ans[DATA] = binascii.b2a_base64(
                            digest).decode('ascii')
                        send_msg(self.transport, my_ans)
                        self.process_server_ans(take_msg(self.transport))
            except (OSError, json.JSONDecodeError) as err:
                LOGGER.debug(f'Connection error.', exc_info=err)
                raise ServerError(
                    'Connection problem during the process of authorization.')

    def process_server_ans(self, message):
        """ Метод-обработчик поступающих сообщений с сервера. """
        LOGGER.debug(f'Analysis of incoming message from server: {message}')
        if FEEDBACK in message:
            if message[FEEDBACK] == 200:
                return
            elif message[FEEDBACK] == 400:
                raise ServerError(f'{message[ERROR]}')
            elif message[FEEDBACK] == 205:
                self.user_list_update()
                self.contacts_list_update()
                self.message_205.emit()
            else:
                LOGGER.debug(
                    f'Unknown approval code is accepted {message[FEEDBACK]}')

        # Если это сообщение от пользователя, добавляем в базу, даём сигнал о
        # новом сообщении
        elif ACTION in message and message[ACTION] == MESSAGE and SENDER in message and DESTINATION in message \
                and MESSAGE_TEXT in message and message[DESTINATION] == self.username:
            LOGGER.debug(
                f'Message is taken from user {message[SENDER]}:{message[MESSAGE_TEXT]}')
            self.new_message.emit(message)

    def contacts_list_update(self):
        """ Метод, обновляющий контакт-лист с сервера """
        self.database.contacts_clear()
        LOGGER.debug(f"Request to get user's contact list {self.name}")
        req = {
            ACTION: GET_CONTACTS,
            TIME: time.time(),
            USER: self.username
        }
        LOGGER.debug(f'Request is formed {req}')
        with socket_lock:
            send_msg(self.transport, req)
            ans = take_msg(self.transport)
        LOGGER.debug(f'Answer is received {ans}')
        if FEEDBACK in ans and ans[FEEDBACK] == 202:
            for contact in ans[LIST_INFO]:
                self.database.add_contact(contact)
        else:
            LOGGER.error('It is impossible to update users list.')

    def user_list_update(self):
        """ Метод, обновляющий с сервера список пользователей. """
        LOGGER.debug(f'Request for a list of known users {self.username}')
        req = {
            ACTION: USERS_REQUEST,
            TIME: time.time(),
            ACCOUNT_NAME: self.username
        }
        with socket_lock:
            send_msg(self.transport, req)
            ans = take_msg(self.transport)
        if FEEDBACK in ans and ans[FEEDBACK] == 202:
            self.database.add_users(ans[LIST_INFO])
        else:
            LOGGER.error('It is impossible to update known users list.')

    def key_request(self, user):
        """Метод, запрашивающий с сервера публичный ключ пользователя."""
        LOGGER.debug(f'Public key request for {user}')
        req = {
            ACTION: PUBLIC_KEY_REQUEST,
            TIME: time.time(),
            ACCOUNT_NAME: user
        }
        with socket_lock:
            send_msg(self.transport, req)
            ans = take_msg(self.transport)
        if FEEDBACK in ans and ans[FEEDBACK] == 511:
            return ans[DATA]
        else:
            LOGGER.error(f'failed to get the key of {user}.')

    def add_contact(self, contact):
        """ Метод, сообщающий на сервер о добавлении нового контакта """
        LOGGER.debug(f'Contact creature {contact}')
        req = {
            ACTION: ADD_CONTACT,
            TIME: time.time(),
            USER: self.username,
            ACCOUNT_NAME: contact
        }
        with socket_lock:
            send_msg(self.transport, req)
            self.process_server_ans(take_msg(self.transport))

    def remove_contact(self, contact):
        """ Метод, отправляющий на сервер сведения об удалении контакта. """
        LOGGER.debug(f'Contact delete {contact}')
        req = {
            ACTION: REMOVE_CONTACT,
            TIME: time.time(),
            USER: self.username,
            ACCOUNT_NAME: contact
        }
        with socket_lock:
            send_msg(self.transport, req)
            self.process_server_ans(take_msg(self.transport))

    def transport_shutdown(self):
        """ Метод, уведомляющий сервер о завершении работы клиента. """
        self.running = False
        message = {
            ACTION: EXIT,
            TIME: time.time(),
            ACCOUNT_NAME: self.username
        }
        with socket_lock:
            try:
                send_msg(self.transport, message)
            except OSError:
                pass
        LOGGER.debug('Transport is completing the work.')
        time.sleep(0.5)

    def send_msg(self, to, message):
        """ Метод, отправляющий на сервер сообщения для пользователя. """
        message_dict = {
            ACTION: MESSAGE,
            SENDER: self.username,
            DESTINATION: to,
            TIME: time.time(),
            MESSAGE_TEXT: message
        }
        LOGGER.debug(f'Message dict is formed: {message_dict}')

        # Необходимо дождаться освобождения сокета для отправки сообщения
        with socket_lock:
            send_msg(self.transport, message_dict)
            self.process_server_ans(take_msg(self.transport))
            LOGGER.info(f'Message to user {to} is sent')

    def run(self):
        """Метод, содержащий основной цикл работы транспортного потока."""
        LOGGER.debug('Process is launched - messages receiver from server.')
        while self.running:
            # Отдыхаем секунду и снова пробуем захватить сокет.
            # если не сделать тут задержку, то отправка может достаточно долго
            # ждать освобождения сокета.
            time.sleep(1)
            message = None
            with socket_lock:
                try:
                    self.transport.settimeout(0.5)
                    message = take_msg(self.transport)
                except OSError as err:
                    if err.errno:
                        LOGGER.critical(f'Server connection is lost.')
                        self.running = False
                        self.connection_lost.emit()
                # Проблемы с соединением
                except (ConnectionError, ConnectionAbortedError, ConnectionResetError, json.JSONDecodeError, TypeError):
                    LOGGER.debug(f'Server connection is lost.')
                    self.running = False
                    self.connection_lost.emit()
                finally:
                    self.transport.settimeout(5)

            # Если сообщение получено, то вызываем функцию-обработчик:
            if message:
                LOGGER.debug(f'Server message is received: {message}')
                self.process_server_ans(message)
