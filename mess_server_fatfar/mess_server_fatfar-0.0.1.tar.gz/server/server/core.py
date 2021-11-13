""" Основной класс сервера. Принимает содинения, словари - пакеты
    от клиентов, обрабатывает поступающие сообщения.
"""

import threading
import logging
import select
import socket
import json
import hmac
import binascii
import os

from descriptors import Port
from decos import login_required
from common.variables import *
from common.utils import send_msg, take_msg

# Инициализация логирования сервера.
LOGGER = logging.getLogger('server')


class MessageProcessor(threading.Thread):
    """
    Основной класс сервера. Принимает содинения, словари - пакеты
    от клиентов, обрабатывает поступающие сообщения.
    Работает в качестве отдельного потока.
    """
    port = Port()

    def __init__(self, listen_address, listen_port, database):
        # Параметры подключения
        self.addr = listen_address
        self.port = listen_port

        # База данных сервера
        self.database = database

        # Сокет, через который будет осуществляться работа
        self.sock = None

        # Список подключённых клиентов.
        self.clients = []

        # Сокеты
        self.listen_sockets = None
        self.error_sockets = None

        # Флаг продолжения работы
        self.running = True

        # Словарь, содержащий сопоставленные имена и соответствующие им сокеты.
        self.names = dict()

        # Конструктор предка
        super().__init__()

    def run(self):
        """ Основной цикл потока. """
        # Инициализация сокета
        self.init_socket()

        # Основной цикл программы сервера
        while self.running:
            try:
                client, client_address = self.sock.accept()
            except OSError:
                pass
            else:
                LOGGER.info(
                    f'Connection with PC {client_address} is established')
                client.settimeout(5)
                self.clients.append(client)

            recv_data_lst = []
            send_data_lst = []
            err_lst = []
            # Проверяем на наличие ждущих клиентов
            try:
                if self.clients:
                    recv_data_lst, self.listen_sockets, self.error_sockets = select.select(
                        self.clients, self.clients, [], 0)
            except OSError as err:
                LOGGER.error(f'Error in work with sockets: {err.errno}')

            # принимаем сообщения и, если ошибка, исключаем клиента.
            if recv_data_lst:
                for client_with_message in recv_data_lst:
                    try:
                        self.process_client_message(
                            take_msg(client_with_message), client_with_message)
                    except (OSError, json.JSONDecodeError, TypeError) as err:
                        LOGGER.debug(
                            f'Getting data from client exception.', exc_info=err)
                        self.remove_client(client_with_message)

    def remove_client(self, client):
        """
        Метод-обработчик клиента, с которым прервана связь.
        Ищет клиента и удаляет его из списков и базы:
        """
        LOGGER.info(
            f'Client {client.getpeername()} is switched off from server.')
        for name in self.names:
            if self.names[name] == client:
                self.database.user_logout(name)
                del self.names[name]
                break
        self.clients.remove(client)
        client.close()

    def init_socket(self):
        """ Метод-инициализатор сокета. """
        LOGGER.info(
            f'Server is launched, port for connections: {self.port}, '
            f'Address for connection: {self.addr}. '
            f'If address is not indicated, connections from any addresses are accepted.')

        # Готовим сокет
        sock_prep = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock_prep.bind((self.addr, self.port))
        sock_prep.settimeout(0.5)

        # Начинаем слушать сокет.
        self.sock = sock_prep
        self.sock.listen(MAX_CONNECTIONS)

    def process_message(self, message):
        """
        Метод отправки сообщения клиенту.
        """
        if message[DESTINATION] in self.names and self.names[message[DESTINATION]
                                                             ] in self.listen_sockets:
            try:
                send_msg(self.names[message[DESTINATION]], message)
                LOGGER.info(
                    f'Message is sent to user {message[DESTINATION]} from user {message[SENDER]}.')
            except OSError:
                self.remove_client(message[DESTINATION])
        elif message[DESTINATION] in self.names and self.names[message[DESTINATION]] not in self.listen_sockets:
            LOGGER.error(
                f'Connection with client {message[DESTINATION]} is lost. Connection is closed, delivery is not possible.')
            self.remove_client(self.names[message[DESTINATION]])
        else:
            LOGGER.error(
                f'User {message[DESTINATION]} is not registered on server, message sending is not possible.')

    @login_required
    def process_client_message(self, message, client):
        """Метод-обработчик поступающих сообщений."""
        LOGGER.debug(f"Detailed analysis of client's message: {message}")
        # Если это сообщение о присутствии, принимаем и отвечаем
        if ACTION in message and message[ACTION] == HERE and TIME in message and USER in message:
            # Если сообщение о присутствии, то вызываем функцию авторизации.
            self.authorize_user(message, client)

        # Если это сообщение, то отправляем его получателю.
        elif ACTION in message and message[ACTION] == MESSAGE and DESTINATION in message and TIME in message \
                and SENDER in message and MESSAGE_TEXT in message and self.names[message[SENDER]] == client:
            if message[DESTINATION] in self.names:
                self.database.process_message(
                    message[SENDER], message[DESTINATION])
                self.process_message(message)
                try:
                    send_msg(client, RESPONSE_200)
                except OSError:
                    self.remove_client(client)
            else:
                response = RESPONSE_400
                response[ERROR] = 'User is not registered on server.'
                try:
                    send_msg(client, response)
                except OSError:
                    pass
            return

        # Если клиент выходит
        elif ACTION in message and message[ACTION] == EXIT and ACCOUNT_NAME in message \
                and self.names[message[ACCOUNT_NAME]] == client:
            self.remove_client(client)

        # Если это запрос контакт-листа
        elif ACTION in message and message[ACTION] == GET_CONTACTS and USER in message and \
                self.names[message[USER]] == client:
            response = RESPONSE_202
            response[LIST_INFO] = self.database.get_contacts(message[USER])
            try:
                send_msg(client, response)
            except OSError:
                self.remove_client(client)

        # Если это добавление контакта
        elif ACTION in message and message[ACTION] == ADD_CONTACT and ACCOUNT_NAME in message and USER in message \
                and self.names[message[USER]] == client:
            self.database.add_contact(message[USER], message[ACCOUNT_NAME])
            try:
                send_msg(client, RESPONSE_200)
            except OSError:
                self.remove_client(client)

        # Если это удаление контакта
        elif ACTION in message and message[ACTION] == REMOVE_CONTACT and ACCOUNT_NAME in message and USER in message \
                and self.names[message[USER]] == client:
            self.database.remove_contact(message[USER], message[ACCOUNT_NAME])
            try:
                send_msg(client, RESPONSE_200)
            except OSError:
                self.remove_client(client)

        # Если это запрос известных пользователей
        elif ACTION in message and message[ACTION] == USERS_REQUEST and ACCOUNT_NAME in message \
                and self.names[message[ACCOUNT_NAME]] == client:
            response = RESPONSE_202
            response[LIST_INFO] = [user[0]
                                   for user in self.database.users_list()]
            try:
                send_msg(client, response)
            except OSError:
                self.remove_client(client)

        # Если это запрос публичного ключа пользователя
        elif ACTION in message and message[ACTION] == PUBLIC_KEY_REQUEST and ACCOUNT_NAME in message:
            response = RESPONSE_511
            response[DATA] = self.database.get_pubkey(message[ACCOUNT_NAME])
            # может быть, что ключа ещё нет (пользователь никогда не логинился,
            # тогда шлём 400)
            if response[DATA]:
                try:
                    send_msg(client, response)
                except OSError:
                    self.remove_client(client)
            else:
                response = RESPONSE_400
                response[ERROR] = 'There is no public key for this user'
                try:
                    send_msg(client, response)
                except OSError:
                    self.remove_client(client)

        # Иначе отдаём Bad request
        else:
            response = RESPONSE_400
            response[ERROR] = 'Request is not correct.'
            try:
                send_msg(client, response)
            except OSError:
                self.remove_client(client)

    def authorize_user(self, message, sock):
        """Метод, реализующий авторизацию пользователей."""
        # Если имя пользователя уже занято, то возвращаем 400
        LOGGER.debug(f'Start auth process for {message[USER]}')
        if message[USER][ACCOUNT_NAME] in self.names.keys():
            response = RESPONSE_400
            response[ERROR] = 'Username is already busy.'
            try:
                LOGGER.debug(f'Username is busy, sending {response}')
                send_msg(sock, response)
            except OSError:
                LOGGER.debug('OS Error')
                pass
            self.clients.remove(sock)
            sock.close()

        # Проверяем, что пользователь зарегистрирован на сервере.
        elif not self.database.check_user(message[USER][ACCOUNT_NAME]):
            response = RESPONSE_400
            response[ERROR] = 'User is not registered.'
            try:
                LOGGER.debug(f'Unknown username, sending {response}')
                send_msg(sock, response)
            except OSError:
                pass
            self.clients.remove(sock)
            sock.close()
        else:
            LOGGER.debug('Correct username, starting password check.')
            # Иначе отвечаем 511 и проводим процедуру авторизации
            # Словарь - заготовка
            message_auth = RESPONSE_511
            # Набор байтов в hex представлении
            random_str = binascii.hexlify(os.urandom(64))
            # В словарь байты нельзя, декодируем (json.dumps -> TypeError)
            message_auth[DATA] = random_str.decode('ascii')
            # Создаём хэш пароля и связки с рандомной строкой, сохраняем
            # серверную версию ключа
            hash = hmac.new(
                self.database.get_hash(
                    message[USER][ACCOUNT_NAME]),
                random_str,
                'MD5')
            digest = hash.digest()
            LOGGER.debug(f'Auth message = {message_auth}')
            try:
                # Обмен с клиентом
                send_msg(sock, message_auth)
                ans = take_msg(sock)
            except OSError as err:
                LOGGER.debug('Error in auth, data:', exc_info=err)
                sock.close()
                return
            client_digest = binascii.a2b_base64(ans[DATA])
            # Если ответ клиента корректный, то сохраняем его в список
            # пользователей.
            if FEEDBACK in ans and ans[FEEDBACK] == 511 and hmac.compare_digest(
                    digest, client_digest):
                self.names[message[USER][ACCOUNT_NAME]] = sock
                client_ip, client_port = sock.getpeername()
                try:
                    send_msg(sock, RESPONSE_200)
                except OSError:
                    self.remove_client(message[USER][ACCOUNT_NAME])
                # добавляем пользователя в список активных и если у него изменился открытый ключ
                # сохраняем новый
                self.database.user_login(
                    message[USER][ACCOUNT_NAME],
                    client_ip,
                    client_port,
                    message[USER][PUBLIC_KEY])
            else:
                response = RESPONSE_400
                response[ERROR] = 'Wrong password.'
                try:
                    send_msg(sock, response)
                except OSError:
                    pass
                self.clients.remove(sock)
                sock.close()

    def service_update_lists(self):
        """Метод, реализующий отправку сервисного сообщения 205 клиентам."""
        for client in self.names:
            try:
                send_msg(self.names[client], RESPONSE_205)
            except OSError:
                self.remove_client(self.names[client])
