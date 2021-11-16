import logging
import argparse
import configparser
import select
import socket
import sys
import os
import threading
import hmac
import binascii

from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QMessageBox

sys.path.append('../')
from common.variables import *
from common.utils import Connector, get_message, send_message
from db.db_server import ServerDB
from common.metaclasses import ServerVerifier
from common.descriptors import Port, Host
from server.gui_server import MainWindow, HistoryWindow, ConfigWindow, RegisterUser, DelUserDialog


# Флаг что был подключён новый пользователь, нужен чтобы не мучать BD
# постоянными запросами на обновление
new_connection = False
conflag_lock = threading.Lock()


class Server(threading.Thread, metaclass=ServerVerifier):
    listen_port = Port()
    listen_address = Host()

    def argsParser(self, arguments=None):
        """Парсер аргументов коммандной строки"""
        if arguments is None:
            arguments = []

        argument_parser = argparse.ArgumentParser()
        argument_parser.add_argument('-a', default='', nargs='?')
        argument_parser.add_argument(
            '-p', default=DEFAULT_PORT, type=int, nargs='?')
        namespace = argument_parser.parse_args(sys.argv[1:])
        self.listen_address = namespace.a
        self.listen_port = namespace.p

    def __init__(self, db, arguments=None):
        if arguments is None:
            arguments = []

        self.SERVER_LOG = logging.getLogger('app.server')
        # список клиентов , очередь сообщений
        self.clients = []
        self.messages = []
        self.names = dict()
        self.database = db
        self.argsParser()
        self.active_users = []
        self.history_users = self.database.message_history()

        super().__init__()

    def process_client_message(self, message, client):
        """
        Обработка входящего сообщения
        @param message: сообщение
        @param client: от кого пришло
        @return:
        """
        global new_connection
        # Проверяем, если это сообщение о присутствии, принимаем и отвечаем,
        # если успех
        if ACTION in message and message[ACTION] == PRESENCE and USER in message:
            # Если сообщение о присутствии то вызываем функцию авторизации.
            self.autorize_user(message, client)

        # Если это сообщение, то добавляем его в очередь сообщений. Ответ не
        # требуется.
        elif ACTION in message and message[ACTION] == MESSAGE and MESSAGE_TEXT in message and \
                TO in message and FROM in message:
            self.database.process_message(message[FROM], message[TO])
            self.history_users = self.database.message_history()
            self.messages.append(message)
            return

        # Запрос контакт листа пользователей с сервера:
        elif ACTION in message and message[ACTION] == GET_CONTACTS and USER in message:
            query = self.database.get_contacts(message[USER])
            response_contacts_list = []
            for user in query:
                response_contacts_list.append(user)
            response = {
                RESPONSE: 200,
                LIST_INFO: response_contacts_list
            }
            Connector(client).send_message(response)

        elif ACTION in message and message[ACTION] == ADD_CONTACT \
                and ACCOUNT_NAME in message and USER in message:
            self.database.add_contact(message[ACCOUNT_NAME], message[USER])
            Connector(client).send_message(RESPONSE_200)

        elif ACTION in message and message[ACTION] == DEL_CONTACT and ACCOUNT_NAME in message \
                and USER in message:
            self.database.remove_contact(message[ACCOUNT_NAME], message[USER])
            Connector(client).send_message(RESPONSE_200)

        # Если клиент выходит
        elif ACTION in message and message[ACTION] == EXIT and ACCOUNT_NAME in message:
            self.database.user_logout(message[ACCOUNT_NAME])
            self.active_users = self.database.active_users_list()
            self.clients.remove(self.names[message[ACCOUNT_NAME]])
            self.names[message[ACCOUNT_NAME]].close()
            del self.names[message[ACCOUNT_NAME]]
            with conflag_lock:
                new_connection = True
            return

        elif ACTION in message and message[ACTION] == GET_LIST:
            query = self.database.users_list()
            print(f'We get message: {message}')
            response_temp = []
            for user in query:
                response_temp.append(user[0])
            response = {
                RESPONSE: 200,
                LIST_INFO: response_temp
            }
            Connector(client).send_message(response)

        elif ACTION in message and message[ACTION] == "GET_HISTORY" and "history_name" in message:
            query = self.database.login_history(message["history_name"])
            response_temp = []
            for user in query:
                response_temp.append(
                    (user[0], user[1].strftime("%m/%d/%Y, %H:%M:%S")))
            response = {
                ACTION: "GET_HISTORY",
                MESSAGE_TEXT: response_temp
            }
            Connector(client).send_message(response)
        elif ACTION in message and message[ACTION] == "GET_CONNLIST":
            query = self.database.active_users_list()
            response_temp = []
            for user in query:
                response_temp.append(user[0])
            print(response_temp)
            response = {
                ACTION: "GET_CONNLIST",
                MESSAGE_TEXT: response_temp
            }
            Connector(client).send_message(response)
        elif ACTION in message and message[ACTION] == PUBLIC_KEY_REQUEST and ACCOUNT_NAME in message:
            response = RESPONSE_511
            response[DATA] = self.database.get_pubkey(message[ACCOUNT_NAME])
            # может быть, что ключа ещё нет (пользователь никогда не логинился,
            # тогда шлём 400)
            if response[DATA]:
                try:
                    send_message(client, response)
                except OSError:
                    self.remove_client(client)
            else:
                response = RESPONSE_400
                response[ERROR] = 'Нет публичного ключа для данного пользователя'
                try:
                    send_message(client, response)
                except OSError:
                    self.remove_client(client)

        # Иначе отдаём Bad request
        else:
            response = RESPONSE_400
            response[ERROR] = 'Запрос некорректен.'
            Connector(client).send_message(response)
            return

    def process_message(self, message, listen_socks):
        """
        Функция адресной отправки сообщения определённому клиенту. Принимает словарь сообщение,
        список зарегистрированых пользователей и слушающие сокеты. Ничего не возвращает.
        """
        if message[TO] in self.names and self.names[message[TO]] in listen_socks:
            Connector(self.names[message[TO]]).send_message(message)
            self.SERVER_LOG.info(
                f'Отправлено сообщение пользователю {message[TO]} '
                f'от пользователя {message[FROM]}.')
        elif message[TO] in self.names.keys() and self.names[message[TO]] not in listen_socks:
            raise ConnectionError
        else:
            self.SERVER_LOG.error(
                f'Пользователь {message[TO]} не зарегистрирован на сервере, '
                f'отправка сообщения невозможна.')

    def init_socket(self):
        '''Метод инициализатор сокета.'''
        self.SERVER_LOG.debug(
            (f'Запущен сервер, порт для подключений: {self.listen_port}, '
             f'адрес с которого принимаются подключения: {self.listen_address}. '
             f'Если адрес не указан, принимаются соединения с любых адресов.'))
        transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        transport.bind((self.listen_address, self.listen_port))
        transport.settimeout(0.5)

        # Начинаем слушать сокет.
        self.SERV_SOCK = transport
        self.SERV_SOCK.listen()

    def run(self):
        """
        Функция потока
        @return:
        """
        self.init_socket()
        while True:
            try:
                CLIENT_SOCK, CLIENT_ADDR = self.SERV_SOCK.accept()
            except OSError:
                pass
            else:
                self.SERVER_LOG.debug(
                    f'Установлено соединение с ПК по адресу: {CLIENT_ADDR}')
                self.clients.append(CLIENT_SOCK)

            # Начинаем работать с несколькими клиентами и информацией от них
            received_data_lst = []
            send_data_lst = []
            error_lst = []
            # Словарь, содержащий имена пользователей и соответствующие им сокеты.
            # Проверяем на наличие ждущих клиентов
            try:
                if self.clients:
                    received_data_lst, send_data_lst, error_lst = select.select(
                        self.clients, self.clients, [], 0)
            except OSError:
                pass
            # принимаем сообщения и если там есть сообщения,
            # кладём в словарь, если ошибка, исключаем клиента.
            if received_data_lst:
                print(f"received_data_lst in server: {received_data_lst}")
                for client_with_message in received_data_lst:
                    print(
                        f"client_with_message in received_data_lst: {client_with_message}")
                    try:
                        message_from_client = get_message(client_with_message)
                        print(f"message_from_client: {message_from_client}")
                        self.process_client_message(
                            message_from_client, client_with_message)
                        self.SERVER_LOG.info(
                            f'Список принятых сообщений: {self.messages}')
                    except BaseException:
                        self.SERVER_LOG.info(
                            f'Клиент {client_with_message.getpeername()} '
                            f'отключился от сервера.')
                        self.clients.remove(client_with_message)
            # Если есть сообщения для отправки и ожидающие клиенты, отправляем
            # им сообщение.
            for message in self.messages:
                try:
                    self.process_message(message, send_data_lst)
                except Exception:
                    self.SERVER_LOG.info(
                        f'Клиент {message[TO]} отключился от сервера.')
                    self.clients.remove(self.names[message[TO]])
                    del self.names[message[TO]]
            self.messages.clear()

    # GUI - Создание таблицы QModel, для отображения в окне программы.
    def gui_create_model(self):
        list = QStandardItemModel()
        list.setHorizontalHeaderLabels(
            ['Имя Клиента', 'IP Адрес', 'Порт', 'Время подключения'])
        for row in self.active_users:
            user, ip, port, time = row
            user = QStandardItem(user)
            user.setEditable(False)
            ip = QStandardItem(ip)
            ip.setEditable(False)
            port = QStandardItem(str(port))
            port.setEditable(False)
            time = QStandardItem(str(time.replace(microsecond=0)))
            time.setEditable(False)
            list.appendRow([user, ip, port, time])
        return list

    # GUI - Функция реализующая заполнение таблицы историей сообщений.
    def gui_create_stat_model(self):
        list = QStandardItemModel()
        list.setHorizontalHeaderLabels(
            ['Имя Клиента', 'Последний раз входил', 'Сообщений отправлено', 'Сообщений получено'])
        for row in self.history_users:
            user, last_seen, sent, recvd = row
            user = QStandardItem(user)
            user.setEditable(False)
            last_seen = QStandardItem(str(last_seen.replace(microsecond=0)))
            last_seen.setEditable(False)
            sent = QStandardItem(str(sent))
            sent.setEditable(False)
            recvd = QStandardItem(str(recvd))
            recvd.setEditable(False)
            list.appendRow([user, last_seen, sent, recvd])
        return list

    def autorize_user(self, message, sock):
        '''Метод реализующий авторизцию пользователей.'''
        global new_connection
        # Если имя пользователя уже занято то возвращаем 400
        self.SERVER_LOG.debug(f'Start auth process for {message[USER]}')
        print(f'Start auth process for {message[USER]}')
        if message[USER][ACCOUNT_NAME] in self.names.keys():
            response = RESPONSE_400
            response[ERROR] = 'Имя пользователя уже занято.'
            try:
                self.SERVER_LOG.debug(f'Username busy, sending {response}')
                send_message(sock, response)
            except OSError:
                self.SERVER_LOG.debug('OS Error')
                pass
            self.clients.remove(sock)
            sock.close()
        # Проверяем что пользователь зарегистрирован на сервере.
        elif not self.database.check_user(message[USER][ACCOUNT_NAME]):
            response = RESPONSE_400
            response[ERROR] = 'Пользователь не зарегистрирован.'
            try:
                self.SERVER_LOG.debug(f'Unknown username, sending {response}')
                send_message(sock, response)
            except OSError:
                pass
            self.clients.remove(sock)
            sock.close()
        else:
            self.SERVER_LOG.debug('Correct username, starting passwd check.')
            # Иначе отвечаем 511 и проводим процедуру авторизации
            # Словарь - заготовка
            message_auth = RESPONSE_511
            print(f"message_auth = RESPONSE_511: {message_auth}")
            # Набор байтов в hex представлении
            random_str = binascii.hexlify(os.urandom(64))
            print(f"random_str: {random_str}")
            # В словарь байты нельзя, декодируем (json.dumps -> TypeError)
            message_auth[DATA] = random_str.decode('ascii')
            print(f"message_auth = RESPONSE_511: {message_auth}")
            # Создаём хэш пароля и связки с рандомной строкой, сохраняем
            # серверную версию ключа
            hash = hmac.new(
                self.database.get_hash(
                    message[USER][ACCOUNT_NAME]),
                random_str,
                'MD5')
            digest = hash.digest()
            self.SERVER_LOG.debug(f'Auth message = {message_auth}')
            print(f'Auth message = {message_auth}')
            try:
                # Обмен с клиентом
                send_message(sock, message_auth)
                ans = get_message(sock)
            except OSError as err:
                self.SERVER_LOG.debug('Error in auth, data:', exc_info=err)
                sock.close()
                return
            client_digest = binascii.a2b_base64(ans[DATA])
            # Если ответ клиента корректный, то сохраняем его в список
            # пользователей.
            if RESPONSE in ans and ans[RESPONSE] == 511 and hmac.compare_digest(
                    digest, client_digest):
                self.names[message[USER][ACCOUNT_NAME]] = sock
                client_ip, client_port = sock.getpeername()
                try:
                    send_message(sock, RESPONSE_200)
                except OSError:
                    self.remove_client(message[USER][ACCOUNT_NAME])
                # добавляем пользователя в список активных и если у него изменился открытый ключ
                # сохраняем новый
                self.database.user_login(
                    message[USER][ACCOUNT_NAME],
                    client_ip,
                    client_port,
                    message[USER][PUBLIC_KEY])
                self.active_users = self.database.active_users_list()
                new_connection = True
            else:
                response = RESPONSE_400
                response[ERROR] = 'Неверный пароль.'
                try:
                    send_message(sock, response)
                except OSError:
                    pass
                self.clients.remove(sock)
                sock.close()

    def service_update_lists(self):
        '''Метод реализующий отправки сервисного сообщения 205 клиентам.'''
        for client in self.clients:
            try:
                Connector(client).send_message(RESPONSE_205)
            except OSError:
                self.clients.remove(client)


def main():
    config = configparser.ConfigParser()

    dir_path = os.getcwd()
    config.read(f"{dir_path}/{'server.ini'}")

    database = ServerDB(
        os.path.join(
            config['SETTINGS']['Database_path'],
            config['SETTINGS']['Database_file']))

    server = Server(database, f"- a {config['SETTINGS']['Default_port']}"
                              f" - p {config['SETTINGS']['Listen_Address']}")

    server.daemon = True
    server.start()

    server_app = QApplication(sys.argv)
    main_window = MainWindow()

    main_window.statusBar().showMessage('Server Working')

    main_window.active_clients_table.setModel(server.gui_create_model())
    main_window.active_clients_table.resizeColumnsToContents()
    main_window.active_clients_table.resizeRowsToContents()

    def list_update():
        global new_connection
        if new_connection:
            main_window.active_clients_table.setModel(
                server.gui_create_model())
            main_window.active_clients_table.resizeColumnsToContents()
            main_window.active_clients_table.resizeRowsToContents()
            with conflag_lock:
                new_connection = False

    # Функция создающяя окно со статистикой клиентов
    def show_statistics():
        global stat_window
        stat_window = HistoryWindow()
        stat_window.history_table.setModel(server.gui_create_stat_model())
        stat_window.history_table.resizeColumnsToContents()
        stat_window.history_table.resizeRowsToContents()
        stat_window.show()

    # Функция создающяя окно с настройками сервера.
    def server_config():
        global config_window
        # Создаём окно и заносим в него текущие параметры
        config_window = ConfigWindow()
        config_window.db_path.insert(config['SETTINGS']['Database_path'])
        config_window.db_file.insert(config['SETTINGS']['Database_file'])
        config_window.port.insert(config['SETTINGS']['Default_port'])
        config_window.ip.insert(config['SETTINGS']['Listen_Address'])
        config_window.save_btn.clicked.connect(save_server_config)

    # Функция сохранения настроек
    def save_server_config():
        global config_window
        message = QMessageBox()
        config['SETTINGS']['Database_path'] = config_window.db_path.text()
        config['SETTINGS']['Database_file'] = config_window.db_file.text()
        try:
            port = int(config_window.port.text())
        except ValueError:
            message.warning(config_window, 'Ошибка', 'Порт должен быть числом')
        else:
            config['SETTINGS']['Listen_Address'] = config_window.ip.text()
            if 1023 < port < 65536:
                config['SETTINGS']['Default_port'] = str(port)
                print(port)
                with open('server.ini', 'w') as conf:
                    config.write(conf)
                    message.information(
                        config_window, 'OK', 'Настройки успешно сохранены!')
            else:
                message.warning(
                    config_window,
                    'Ошибка',
                    'Порт должен быть от 1024 до 65536')

    def reg_user():
        '''Метод создающий окно регистрации пользователя.'''
        global reg_window
        reg_window = RegisterUser(database, server)
        reg_window.show()

    def rem_user():
        '''Метод создающий окно удаления пользователя.'''
        global rem_window
        rem_window = DelUserDialog(database, server)
        rem_window.show()

    # Таймер, обновляющий список клиентов 1 раз в секунду
    timer = QTimer()
    timer.timeout.connect(list_update)
    timer.start(1000)

    # Связываем кнопки с процедурами
    main_window.refresh_button.triggered.connect(list_update)
    main_window.show_history_button.triggered.connect(show_statistics)
    main_window.config_btn.triggered.connect(server_config)
    main_window.register_btn.triggered.connect(reg_user)
    main_window.remove_btn.triggered.connect(rem_user)

    # Запускаем GUI
    server_app.exec_()


if __name__ == '__main__':
    main()
