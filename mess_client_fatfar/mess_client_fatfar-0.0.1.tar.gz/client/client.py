""" Основная функция клиента """

import sys
import os
import logging
import argparse

from Cryptodome.PublicKey import RSA
from PyQt5.QtWidgets import QApplication, QMessageBox

from errors import ServerError
from common.variables import *
from decos import Log
from packet_client.client import ClientDB
from packet_client.client import ClientTransport
from packet_client.client import ClientMainWindow
from packet_client.client import UserNameDialog

# Инициализация клиентского логера
LOGGER = logging.getLogger('client')


# Парсим аргументы командной строки
@Log()
def arg_parser():
    """
    Парсер аргументов командной строки, возвращает кортеж из 4 элементов:
    адрес сервера, порт, имя пользователя, пароль.
    Выполняет проверку на корректность номера порта.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('addr', default=DEFAULT_IP_ADDR, nargs='?')
    parser.add_argument('port', default=DEFAULT_PORT, type=int, nargs='?')
    parser.add_argument('-n', '--name', default=None, nargs='?')
    parser.add_argument('-p', '--password', default='', nargs='?')
    namespace = parser.parse_args(sys.argv[1:])
    server_address = namespace.addr
    server_port = namespace.port
    client_name = namespace.name
    client_passwd = namespace.password

    # проверим подходящий номер порта
    if not 1023 < server_port < 65536:
        LOGGER.critical(
            f'Attempt to launch a client with inappropriate port number: {server_port}. '
            f'The only addresses from 1024 to 65535 are acceptable. Client is closing.')
        sys.exit(1)

    return server_address, server_port, client_name, client_passwd


# Основная функция клиента
if __name__ == '__main__':
    # Загружаем параметры командной строки
    server_address, server_port, client_name, client_passwd = arg_parser()
    LOGGER.debug('Args loaded')
    client_app = QApplication(sys.argv)

    # Если имя пользователя не было указано в командной строке, запрашиваем его
    start_dialog = UserNameDialog()
    if not client_name or not client_passwd:
        client_app.exec_()
        # Если пользователь ввёл имя и нажал ОК, то сохраняем введённое и
        # удаляем объект, иначе выходим
        if start_dialog.ok_pressed:
            client_name = start_dialog.client_name.text()
            client_passwd = start_dialog.client_passwd.text()
            LOGGER.debug(
                f'Using USERNAME = {client_name}, PASSWD = {client_passwd}.')
        else:
            sys.exit(0)

    # Записываем логи
    LOGGER.info(
        f'Client is launched with parameters: server addr: {server_address}, port: {server_port},\
         user name: {client_name}')

    # Загружаем ключи с файла, если же файла нет, то генерируем новую пару.
    dir_path = os.getcwd()
    key_file = os.path.join(dir_path, f'{client_name}.key')
    if not os.path.exists(key_file):
        keys = RSA.generate(2048, os.urandom)
        with open(key_file, 'wb') as key:
            key.write(keys.export_key())
    else:
        with open(key_file, 'rb') as key:
            keys = RSA.import_key(key.read())

    # !!!keys.publickey().export_key()
    LOGGER.debug("Keys are successfully loaded.")
    # Создаём объект базы данных

    database = ClientDB(client_name)

    # Создаём объект - транспорт и запускаем транспортный поток
    try:
        transport = ClientTransport(
            server_port,
            server_address,
            database,
            client_name,
            client_passwd,
            keys)
        LOGGER.debug('Transport is ready.')
    except ServerError as error:
        message = QMessageBox()
        message.critical(start_dialog, 'Server error', error.text)
        sys.exit(1)
    transport.setDaemon(True)
    transport.start()

    # Удалим объект диалога за ненадобностью
    del start_dialog

    # Создаём GUI
    main_window = ClientMainWindow(database, transport, keys)
    main_window.make_connection(transport)
    main_window.setWindowTitle(f'Chat Program alpha release - {client_name}')
    client_app.exec_()

    # Если графическая оболочка закрылась, закрываем транспорт
    transport.transport_shutdown()
    transport.join()
