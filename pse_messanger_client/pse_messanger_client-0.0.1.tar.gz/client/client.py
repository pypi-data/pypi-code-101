import argparse
import logging
import sys
import os

from Cryptodome.PublicKey import RSA
from PyQt5.QtWidgets import QApplication, QMessageBox

sys.path.append('../')
from client.start_dialog import UserNameDialog
from client.main_window import ClientMainWindow
from client.transport import ClientTransport
from db.db_client import ClientDatabase
from common.decos import log
from common.errors import ServerError
from common.variables import *

logger = logging.getLogger('app.client')


@log
def argsParser(arguments=None):
    """Парсер аргументов коммандной строки"""
    """Создаём парсер аргументов коммандной строки
        и читаем параметры, возвращаем 3 параметра
        """
    if arguments is None:
        arguments = []

    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument('-a', default=DEFAULT_IP_ADDRESS, nargs='?')
    argument_parser.add_argument('-port', default=DEFAULT_PORT, type=int, nargs='?')
    argument_parser.add_argument('-n', '--name', default=None, nargs='?')
    argument_parser.add_argument('-p', '--password', default=None, nargs='?')
    namespace = argument_parser.parse_args(sys.argv[1:])
    server_address = namespace.a
    server_port = namespace.port
    client_name = namespace.name
    client_passwd = namespace.password

    return server_address, server_port, client_name, client_passwd


if __name__ == '__main__':
    # Загружаем параметы коммандной строки
    server_address, server_port, client_name, client_passwd = argsParser()

    # Создаём клиентокое приложение
    client_app = QApplication(sys.argv)

    # Если имя пользователя не было указано в командной строке то запросим его

    if not client_name or not client_passwd:
        start_dialog = UserNameDialog()
        client_app.exec_()
        # Если пользователь ввёл имя и нажал ОК, то сохраняем ведённое и
        # удаляем объект, инааче выходим
        if start_dialog.ok_pressed:
            client_name = start_dialog.client_name.text()
            client_passwd = start_dialog.client_passwd.text()
            logger.debug(
                f'Using USERNAME = {client_name}, PASSWD = {client_passwd}.')
        else:
            sys.exit(0)

    # Записываем логи
    logger.info(
        f'Запущен клиент с парамертами: адрес сервера: {server_address} , порт: {server_port}, имя пользователя: {client_name}')

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
    logger.debug("Keys sucsessfully loaded.")
    # Создаём объект базы данных
    database = ClientDatabase(client_name)
    # Создаём объект - транспорт и запускаем транспортный поток
    try:
        transport = ClientTransport(
            server_port,
            server_address,
            database,
            client_name,
            client_passwd,
            keys)
        logger.debug("Transport ready.")
    except ServerError as error:
        message = QMessageBox()
        message.critical(start_dialog, 'Ошибка сервера', error.text)
        sys.exit(1)
    transport.setDaemon(True)
    transport.start()

    # Удалим объект диалога за ненадобностью
    del start_dialog

    # Создаём GUI
    main_window = ClientMainWindow(database, transport, keys)
    main_window.make_connection(transport)
    main_window.setWindowTitle(
        f'Чат Программа testing release - {client_name}')
    client_app.exec_()

    # Раз графическая оболочка закрылась, закрываем транспорт
    transport.transport_shutdown()
    transport.join()
