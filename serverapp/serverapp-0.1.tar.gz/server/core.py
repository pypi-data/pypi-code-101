import threading
import binascii
import hmac
import json
import logging
import os
import sys
import select
import threading
from socket import socket, AF_INET, SOCK_STREAM

sys.path.append('../')
from common.descriptrs import CheckPort, CheckIP
from common.utils import send_msg, get_msg
from common.variables import MAX_CONNECTIONS, TO_USER, FROM_USER, \
    ACCOUNT_NAME, EXIT, RESPONSE_200, RESPONSE_202, \
    RESPONSE_400, PRESENCE, USER, ERROR, MESSAGE, TEXT, ACTION, GET_CONTACTS, \
    USERS_REQUEST, REMOVE_CONTACT, ADD_CONTACT, \
    LIST_INFO, TIME, PUBLIC_KEY_REQUEST, RESPONSE_511, RESPONSE_205, DATA, \
    RESPONSE, PUBLIC_KEY

LOGGER = logging.getLogger('server')

class MsgProc(threading.Thread):
    '''
    Основной класс сервера. Принимает содинения, словари - пакеты
    от клиентов, обрабатывает поступающие сообщения.
    Работает в качестве отдельного потока.
    '''
    ip = CheckIP()
    port = CheckPort()

    def __init__(self, ip, port, database):
        super().__init__()
        self.ip = ip
        self.port = port
        self.database = database
        self.sock = None
        self.clients = []
        self.listen_sockets = None
        self.error_sockets = None
        self.running = True
        self.names = dict()

    def init_socket(self):
        '''Метод инициализатор сокета.'''
        LOGGER.info(f'Запущен сервер. Порт: {self.port} , IP-адрес: {self.ip}. Если адрес не указан, принимаются '
                    f'соединения с любых адресов.')
        transport = socket(AF_INET, SOCK_STREAM)
        transport.bind((self.ip, self.port))
        transport.settimeout(0.5)

        self.sock = transport
        self.sock.listen(MAX_CONNECTIONS)

    def remove_client(self, client):
        '''
        Метод обработчик клиента с которым прервана связь.
        Ищет клиента и удаляет его из списков и базы:
        '''
        LOGGER.info(f'Клиент {client.getpeername()} отключился от сервера.')
        for name in self.names:
            if self.names[name] == client:
                self.database.user_logout(name)
                del self.names[name]
                break
        self.clients.remove(client)
        client.close()

    def process_msg(self, msg):
        '''
        Метод отправки сообщения клиенту.
        '''
        if msg[TO_USER] in self.names and self.names[msg[TO_USER]] in self.listen_sockets:
            try:
                send_msg(self.names[msg[TO_USER]], msg)
                LOGGER.info(f'Отправлено сообщение пользователю {msg[TO_USER]} '
                        f'от пользователя {msg[FROM_USER]}.')
            except OSError:
                self.remove_client(msg[TO_USER])
        elif msg[TO_USER] in self.names and self.names[msg[TO_USER]] not in self.listen_sockets:
            LOGGER.error(f'Связь с клиентом {msg[TO_USER]} была потеряна. Соединение закрыто, доставка невозможна.')
            self.remove_client(self.names[msg[TO_USER]])
        else:
            LOGGER.error(
                f'Пользователь {msg[TO_USER]} не зарегистрирован на сервере, '
                f'отправка сообщения невозможна.')

    def process_client_msg(self, msg, client):
        '''Метод отбработчик поступающих сообщений.'''
        LOGGER.debug(f'Разбор сообщения от клиента : {msg}')
        if ACTION in msg and msg[ACTION] == MESSAGE and \
                TO_USER in msg and TIME in msg \
                and FROM_USER in msg and TEXT in msg and self.names[msg[FROM_USER]] == client:
            if msg[TO_USER] in self.names:
                self.database.process_msg(
                    msg[FROM_USER], msg[TO_USER])
                self.process_msg(msg)
                try:
                    send_msg(client, RESPONSE_200)
                except OSError:
                    self.remove_client(client)
            else:
                response = RESPONSE_400
                response[ERROR] = 'Пользователь не зарегистрирован на сервере.'
                try:
                    send_msg(client, response)
                except OSError:
                    pass
            return
        elif ACTION in msg and msg[ACTION] == PRESENCE and TIME in msg and USER in msg:
            self.autorize_user(msg, client)
        elif ACTION in msg and msg[ACTION] == EXIT and ACCOUNT_NAME in msg and self.names[
            msg[ACCOUNT_NAME]] == client:
            self.remove_client(client)
            LOGGER.info(
                f'Клиент {msg[ACCOUNT_NAME]} корректно отключился от сервера.')
            return
        elif ACTION in msg and msg[ACTION] == GET_CONTACTS and USER in msg and \
                self.names[msg[USER]] == client:
            response = RESPONSE_202
            response[LIST_INFO] = self.database.get_contacts(msg[USER])
            try:
                send_msg(client, response)
            except OSError:
                self.remove_client(client)
        elif ACTION in msg and msg[ACTION] == REMOVE_CONTACT and ACCOUNT_NAME in msg and USER in msg \
                and self.names[msg[USER]] == client:
            self.database.remove_contact(msg[USER], msg[ACCOUNT_NAME])
            try:
                send_msg(client, RESPONSE_200)
            except OSError:
                self.remove_client(client)
        elif ACTION in msg and msg[ACTION] == ADD_CONTACT and ACCOUNT_NAME in msg and USER in msg \
                and self.names[msg[USER]] == client:
            self.database.add_contact(msg[USER], msg[ACCOUNT_NAME])
            try:
                send_msg(client, RESPONSE_200)
            except OSError:
                self.remove_client(client)
        elif ACTION in msg and msg[ACTION] == USERS_REQUEST and ACCOUNT_NAME in msg \
                and self.names[msg[ACCOUNT_NAME]] == client:
            response = RESPONSE_202
            response[LIST_INFO] = [user[0] for user in self.database.users_list()]
            try:
                send_msg(client, response)
            except OSError:
                self.remove_client(client)
        elif ACTION in msg and msg[ACTION] == PUBLIC_KEY_REQUEST and ACCOUNT_NAME in msg:
            response = RESPONSE_511
            response[DATA] = self.database.get_pubkey(msg[ACCOUNT_NAME])
            if response[DATA]:
                try:
                    send_msg(client, response)
                except OSError:
                    self.remove_client(client)
            else:
                response = RESPONSE_400
                response[ERROR] = 'Нет публичного ключа для данного пользователя'
                try:
                    send_msg(client, response)
                except OSError:
                    self.remove_client(client)
        else:
            response = RESPONSE_400
            response[ERROR] = 'Запрос некорректен.'
            try:
                send_msg(client, response)
            except OSError:
                self.remove_client(client)

    def service_upd_lists(self):
        '''Метод реализующий отправки сервисного сообщения 205 клиентам.'''
        for client in self.names:
            try:
                send_msg(self.names[client], RESPONSE_205)
            except OSError:
                self.remove_client(self.names[client])

    def autorize_user(self, msg, sock):
        '''Метод реализующий авторизцию пользователей.'''
        LOGGER.debug(f'Старт авторизации пользователя - {msg[USER]}')
        if msg[USER][ACCOUNT_NAME] in self.names.keys():
            response = RESPONSE_400
            response[ERROR] = 'Имя пользователя уже занято.'
            try:
                LOGGER.debug(f'Username busy, sending {response}')
                send_msg(sock, response)
            except OSError:
                LOGGER.debug('OS Error')
                pass
            self.clients.remove(sock)
            sock.close()
        # Проверяем что пользователь зарегистрирован на сервере.
        elif not self.database.check_user(msg[USER][ACCOUNT_NAME]):
            response = RESPONSE_400
            response[ERROR] = 'Пользователь не зарегистрирован.'
            try:
                LOGGER.debug(f'Неизвестное имя пользователя {response}')
                send_msg(sock, response)
            except OSError:
                pass
            self.clients.remove(sock)
            sock.close()
        else:
            LOGGER.debug('Correct username, starting passwd check.')
            msg_auth = RESPONSE_511
            random_str = binascii.hexlify(os.urandom(64))
            msg_auth[DATA] = random_str.decode('ascii')
            hash = hmac.new(self.database.get_hash(msg[USER][ACCOUNT_NAME]), random_str, 'MD5')
            digest = hash.digest()
            LOGGER.debug(f'Сообщение аутентификации = {msg_auth}')
            try:
                send_msg(sock, msg_auth)
                ans = get_msg(sock)
            except OSError as err:
                LOGGER.debug('Ошибка аутентификации', exc_info=err)
                sock.close()
                return
            client_dig = binascii.a2b_base64(ans[DATA])
            if RESPONSE in ans and ans[RESPONSE] == 511 and hmac.compare_digest(digest, client_dig):
                self.names[msg[USER][ACCOUNT_NAME]] = sock
                client_ip, client_port = sock.getpeername()
                try:
                    send_msg(sock, RESPONSE_200)
                except OSError:
                    self.remove_client(msg[USER][ACCOUNT_NAME])
                self.database.user_login(
                    msg[USER][ACCOUNT_NAME],
                    client_ip,
                    client_port,
                    msg[USER][PUBLIC_KEY])
            else:
                response = RESPONSE_400
                response[ERROR] = 'Неверный пароль.'
                try:
                    send_msg(sock, response)
                except OSError:
                    pass
                self.clients.remove(sock)
                sock.close()

    def run(self):
        '''Главный цикл потока.'''
        self.init_socket()
        while self.running:
            try:
                client, client_address = self.sock.accept()
            except OSError:
                pass
            else:
                LOGGER.info(f'Установлено соедение с ПК {client_address}')
                client.settimeout(5)
                self.clients.append(client)

            recv_data_lst = []
            send_data_lst = []
            err_lst = []
            try:
                if self.clients:
                    recv_data_lst, self.listen_sockets, self.error_sockets = select.select(
                        self.clients, self.clients, [], 0)
            except OSError as err:
                LOGGER.error(f'Ошибка работы с сокетами: {err.errno}')
            if recv_data_lst:
                for client_with_msg in recv_data_lst:
                    try:
                        self.process_client_msg(get_msg(client_with_msg), client_with_msg)
                    except (OSError, json.JSONDecodeError, TypeError) as err:
                        LOGGER.debug(f'Getting data from client exception.', exc_info=err)
                        self.remove_client(client_with_msg)