import logging
import re
import sys

SERVER_LOG = logging.getLogger('app.server')


class Port:
    def __set__(self, instance, value):
        if not 1023 < value < 65536:
            SERVER_LOG.critical(
                f'Попытка запуска сервера с указанием неподходящего порта '
                f'{value}. Допустимы адреса с 1024 до 65535.')
            sys.exit(1)
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]


class Host:
    def __set__(self, instance, value):
        regex = "^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
        if re.match(regex, value) is False and value != "":
            SERVER_LOG.critical(
                f'Попытка запуска сервера с указанием неподходящего хоста '
                f'{value}. Допустимы адреса IPV4.')
            sys.exit(1)
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]
