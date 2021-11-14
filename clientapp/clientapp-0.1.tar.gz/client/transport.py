import sys
import time
import logging
import json
import threading
import binascii
import hashlib
import hmac
from PyQt5.QtCore import pyqtSignal, QObject
from socket import socket, AF_INET, SOCK_STREAM

sys.path.append('../')
from common.utils import get_msg, send_msg
from common.variables import ACTION, PRESENCE, TIME, USER, \
    ACCOUNT_NAME, RESPONSE, ERROR, PORT, IP_ADDRESS, TEXT, \
    MESSAGE, EXIT, HELP, FROM_USER, TO_USER, ADD_CONTACT, USERS_REQUEST, \
    LIST_INFO, GET_CONTACTS, REMOVE_CONTACT, \
    PUBLIC_KEY, PUBLIC_KEY_REQUEST, DATA, RESPONSE_511

LOGGER = logging.getLogger('client')
socket_lock = threading.Lock()


class ClientTransport(threading.Thread, QObject):
    '''
    Класс реализующий транспортную подсистему клиентского
    модуля. Отвечает за взаимодействие с сервером.
    '''
    new_msg = pyqtSignal(dict)
    msg_205 = pyqtSignal()
    connection_lost = pyqtSignal()

    def __init__(self, port, ip_address, database, username, user_pass, keys):
        threading.Thread.__init__(self)
        QObject.__init__(self)

        self.database = database
        self.username = username
        self.password = user_pass
        self.transport = None
        self.keys = keys
        self.connection_init(port, ip_address)

        try:
            self.user_list_upd()
            self.contacts_list_upd()
        except OSError as err:
            if err.errno:
                LOGGER.critical(f'Потеряно соединение с сервером.')
            LOGGER.error(
                'Timeout соединения при обновлении списков пользователей.')
        except json.JSONDecodeError:
            LOGGER.critical(f'Потеряно соединение с сервером.')
        self.running = True

    def connection_init(self, port, ip):
        '''Устанновку соединения с сервером.'''
        self.transport = socket(AF_INET, SOCK_STREAM)
        self.transport.settimeout(5)
        connected = False

        # Попытки подключения к серверу
        for i in range(5):
            LOGGER.info(f'Попытка подключения №{i + 1}')
            try:
                self.transport.connect((ip, port))
            except (OSError, ConnectionRefusedError) as err:
                LOGGER.error(f'OSError or ConnectionRefusedError = {err}')
            else:
                connected = True
                LOGGER.debug("Соединение установлено. Функция connection_init")
                break
            time.sleep(1)

        if not connected:
            LOGGER.critical('Не удалось установить соединение с сервером')
            raise LOGGER.critical('Не удалось установить соединение с сервером')

        LOGGER.info('Старт диалога аутентификации.')

        pass_bytes = self.password.encode('utf-8')
        salt = self.username.lower().encode('utf-8')
        pass_hash = hashlib.pbkdf2_hmac('sha512', pass_bytes, salt, 10000)
        pass_hash_string = binascii.hexlify(pass_hash)

        LOGGER.debug(f'Pass hash ready: {pass_hash_string}')

        pubkey = self.keys.publickey().export_key().decode('ascii')

        with socket_lock:
            presense = {
                ACTION: PRESENCE,
                TIME: time.time(),
                USER: {
                    ACCOUNT_NAME: self.username,
                    PUBLIC_KEY: pubkey
                }
            }
            LOGGER.debug(f"Сообщение для сервера - {presense}")
            try:
                send_msg(self.transport, presense)
                ans = get_msg(self.transport)
                LOGGER.debug(f'Ответ сервера - {ans}.')
                if RESPONSE in ans:
                    if ans[RESPONSE] == 400:
                        LOGGER.error(f'Сервер вернул ошибку: {(ans[ERROR])}')
                    elif ans[RESPONSE] == 511:
                        # Если всё нормально, то продолжаем процедуру
                        # авторизации.
                        ans_data = ans[DATA]
                        hash = hmac.new(pass_hash_string,
                                        ans_data.encode('utf-8'), 'MD5')
                        digest = hash.digest()
                        my_ans = RESPONSE_511
                        my_ans[DATA] = binascii.b2a_base64(
                            digest).decode('ascii')
                        send_msg(self.transport, my_ans)
                        self.proc_ans(get_msg(self.transport))
            except (OSError, json.JSONDecodeError) as err:
                LOGGER.debug(f'Ошибка соединения в процессе авторизации.',
                             exc_info=err)

    def create_presence(self):
        '''
        Отправка серверу сообщения о подключении
        '''
        out = {
            ACTION: PRESENCE,
            TIME: time.time(),
            USER: {
                ACCOUNT_NAME: self.username
            }
        }
        LOGGER.debug(
            f'Сформировано {PRESENCE} сообщение для пользователя {self.username}')
        return out

    def proc_ans(self, msg):
        '''Обработка сообщений с сервера.'''
        LOGGER.debug(f'Разбор приветственного сообщения от сервера: {msg}')
        if RESPONSE in msg:
            if msg[RESPONSE] == 200:
                return
            elif msg[RESPONSE] == 400:
                LOGGER.error(
                    f'{msg[RESPONSE]}. Ошибка обработки сообщения сервера: {msg[ERROR]}')
            elif msg[RESPONSE] == 205:
                self.user_list_upd()
                self.contacts_list_upd()
                self.msg_205.emit()
            else:
                LOGGER.debug(
                    f'Принят неизвестный код подтверждения {msg[RESPONSE]}')

        # Если это сообщение от пользователя добавляем в базу, даём сигнал о новом сообщении
        elif ACTION in msg and msg[
            ACTION] == MESSAGE and FROM_USER in msg and TO_USER in msg \
                and TEXT in msg and msg[TO_USER] == self.username:
            LOGGER.debug(
                f'Получено сообщение от пользователя {msg[FROM_USER]}:{msg[TEXT]}')
            self.new_msg.emit(msg)

    def contacts_list_upd(self):
        '''Получение списка клиентов от сервера и
        обновляющий аналогичный список клиента.'''
        self.database.contacts_clear()
        LOGGER.debug(f'Запрос контакт листа для пользователся {self.username}')
        req = {
            ACTION: GET_CONTACTS,
            TIME: time.time(),
            USER: self.username
        }
        LOGGER.debug(f'Сформирован запрос {req}')
        with socket_lock:
            send_msg(self.transport, req)
            ans = get_msg(self.transport)
        LOGGER.debug(f'Получен ответ {ans}')
        if RESPONSE in ans and ans[RESPONSE] == 202:
            for contact in ans[LIST_INFO]:
                self.database.add_contact(contact)
        else:
            raise LOGGER.error('Не удалось обновить список клиентов.')

    def user_list_upd(self):
        '''
        Обновление списка известных пользователей
        '''
        LOGGER.debug(f'Запрос списка известных пользователей {self.username}')
        req = {
            ACTION: USERS_REQUEST,
            TIME: time.time(),
            ACCOUNT_NAME: self.username
        }
        LOGGER.debug(f'Сформирован запрос {req}')
        with socket_lock:
            send_msg(self.transport, req)
            ans = get_msg(self.transport)
        if RESPONSE in ans and ans[RESPONSE] == 202:
            self.database.add_users(ans[LIST_INFO])
        else:
            LOGGER.error('Не удалось обновить список известных пользователей.')

    def key_request(self, user):
        '''Метод запрашивающий с сервера публичный ключ пользователя.'''
        LOGGER.debug(f'Запрос публичного ключа для {user}')
        req = {
            ACTION: PUBLIC_KEY_REQUEST,
            TIME: time.time(),
            ACCOUNT_NAME: user
        }
        with socket_lock:
            send_msg(self.transport, req)
            ans = get_msg(self.transport)
        if RESPONSE in ans and ans[RESPONSE] == 511:
            return ans[DATA]
        else:
            LOGGER.error(f'Не удалось получить ключ собеседника{user}.')

    # Добавление нового контакта
    def add_contact(self, contact):
        '''Отправка на сервер сведений о добавлении контакта.'''
        LOGGER.debug(f'Создание контакта {contact}')
        req = {
            ACTION: ADD_CONTACT,
            TIME: time.time(),
            USER: self.username,
            ACCOUNT_NAME: contact
        }
        with socket_lock:
            send_msg(self.transport, req)
            self.proc_ans(get_msg(self.transport))

    def remove_contact(self, contact):
        '''Отправка на сервер сведений о удалении контакта.'''
        LOGGER.debug(f'Удаление контакта {contact}')
        req = {
            ACTION: REMOVE_CONTACT,
            TIME: time.time(),
            USER: self.username,
            ACCOUNT_NAME: contact
        }
        with socket_lock:
            send_msg(self.transport, req)
            self.proc_ans(get_msg(self.transport))

    def create_exit_message(self):
        '''
        Создание сообщения о выходе из приложения
        '''
        msg = {
            ACTION: EXIT,
            TIME: time.time(),
            ACCOUNT_NAME: self.username
        }

        with socket_lock:
            try:
                send_msg(self.transport, msg)
            except OSError:
                pass
        LOGGER.debug(
            'Совершен выход из клиентского приложения. Соединение разорвано')
        time.sleep(0.5)

    def create_msg(self, to, msg):
        '''
        Создание сообщения сервера для отправки сообщения другому клиенту.
        '''
        msg_dict = {
            ACTION: MESSAGE,
            FROM_USER: self.username,
            TO_USER: to,
            TIME: time.time(),
            TEXT: msg
        }
        LOGGER.info(f'Сообщение для отправки сформировано. {msg_dict}')

        with socket_lock:
            try:
                send_msg(self.transport, msg_dict)
                self.proc_ans(get_msg(self.transport))
                LOGGER.info(f'Отправлено сообщение для пользователя {to}')
            except OSError as err:
                if err.errno:
                    LOGGER.critical('Потеряно соединение с сервером.')
                    exit(1)
                else:
                    LOGGER.error(
                        'Не удалось передать сообщение. Таймаут соединения')

    def transport_shutdown(self):
        '''Метод уведомляющий сервер о завершении работы клиента.'''
        self.running = False
        msg = {
            ACTION: EXIT,
            TIME: time.time(),
            ACCOUNT_NAME: self.username
        }
        with socket_lock:
            try:
                send_msg(self.transport, msg)
            except OSError:
                pass
        LOGGER.debug('Транспорт завершает работу.')
        time.sleep(0.5)

    def run(self):
        '''Метод содержащий основной цикл работы транспортного потока.'''
        LOGGER.debug('Запущен процесс обмена сообщениями с сервером.')
        while self.running:
            time.sleep(1)
            with socket_lock:
                try:
                    self.transport.settimeout(1)
                    msg = get_msg(self.transport)
                except OSError as err:
                    if err.errno:
                        LOGGER.critical(f'Потеряно соединение с сервером.')
                        self.running = False
                        self.connection_lost.emit()
                except (OSError, ConnectionError, ConnectionAbortedError,
                        ConnectionResetError, json.JSONDecodeError):
                    LOGGER.critical(f'Потеряно соединение с сервером.')
                    self.running = False
                    self.connection_lost.emit()
                else:
                    LOGGER.debug(f'Принято сообшение от сервера: {msg}')
                    self.proc_ans(msg)
                finally:
                    self.transport.settimeout(5)
