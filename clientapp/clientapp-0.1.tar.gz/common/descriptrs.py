import logging

LOGGER = logging.getLogger('server')


class CheckPort:
    '''
    Класс - дескриптор для номера порта.
    Позволяет использовать только порты с 1023 по 65536.
    При попытке установить неподходящий номер порта генерирует исключение.
    '''
    def __set__(self, instance, value):
        if (value is not int) and (not 1023 < value < 65536):
            LOGGER.critical(
                f'Порт: {value}. Значение порта должно быть целым положительным числом. Введите корректное значение порта.')
            exit(1)
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name


class CheckIP:
    '''
    Класс - дескриптор для IP-адреса.
    Позволяет использовать только значения от 0 до 255.
    При попытке выйти за диапазон допустимого адреса генерирует исключение.
    '''
    def __set__(self, instance, value):
        for i in value.split('.'):
            if not 0 <= int(i) <= 255:
                LOGGER.critical(
                    f'IPv4: {value}. Значение IP-адреса вне допустимого диапазона. Введите корректный IP-адрес.')
                exit(1)
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name
