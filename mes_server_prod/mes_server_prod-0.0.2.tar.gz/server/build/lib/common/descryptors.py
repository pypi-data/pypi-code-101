import logging
import sys
import re

# Проверяем откуда запущено:
if sys.argv[0].find('client') == -1:
    # сервер
    logger = logging.getLogger('server')
else:
    # клиент
    logger = logging.getLogger('client')


class Port:
    '''
    Класс - дескриптор для номера порта.
    Позволяет использовать только порты с 1023 по 65536.
    При попытке установить неподходящий номер порта генерирует исключение.
    '''

    def __set__(self, instance, value):
        if not 1023 < value < 65536:
            logger.critical(
                f'Попытка запуска с указанием неподходящего порта {value}. Допустимы адреса с 1024 до 65535.')
            raise TypeError('Некорректрый номер порта')
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name


class Host:
    '''
    Класс - дескриптор для имени хоста.
    При попытке установить неподходящий хост, генерирует исключение.
    '''

    def __set__(self, instance, value):
        # Вариант 1. Проверяет только ip
        # try:
        #     ip_address(value)
        # except ValueError:
        #     logger.critical(
        #         f'Неверно указан хост: {value}')
        #     sys.exit(1)

        # Вариант 2. Работает только с ip. localhost не проходит
        # try:
        #     host = ip_address(value)
        # except ValueError:
        #     pass
        # ping = Popen(f"ping {host} -w 500 -n 1", shell=False, stdout=PIPE)
        # ping.wait()
        # if ping.returncode != 0:
        #     logger.critical(f'Неверно указан хост: {value}')
        #     sys.exit(1)

        # Вариант 3. Регулярки
        check_ipv4 = re.match(
            "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$",
            value)
        check_host = re.match(
            "^(([a-zA-Z]|[a-zA-Z][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z]|[A-Za-z][A-Za-z0-9\-]*[A-Za-z0-9])$",
            value)
        if not (check_ipv4 or check_host):
            logger.critical(f'Указан недопустимый хост: {value}')
            raise TypeError('Некорректрый хост')
        # Если хост прошел проверку, добавляем его в список атрибутов экземпляра
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name
