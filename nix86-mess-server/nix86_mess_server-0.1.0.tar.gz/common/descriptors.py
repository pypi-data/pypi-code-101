import logging
import sys


logger = logging.getLogger('server')


class Port:
    def __set__(self, instance, value):
        if not 1023 < value < 65536:
            logger.critical(
                f'Попытка запуска сервера на некорректном порту {value}'
                f'Допустимый порт с 1024 по 65535'
            )
            sys.exit(1)

        # Если подходит, добавляем в список атрибутов экземпляра класса
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name
