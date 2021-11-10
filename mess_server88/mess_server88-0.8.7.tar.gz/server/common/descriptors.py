import logging
import ipaddress

class Port:

    def __set__(self, instance, value):
        if not 1023 < value < 65536:
            logging.getLogger('server').critical(
                        f'Попытка запуска сервера с указанием неподходящего порта {value}. '
                        f'Допустимы адреса с 1024 до 65535.')
            exit(1)
        instance.__dict__[self.my_attr] = value

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr

class Address:

    def __set__(self, instance, value):
        try:
            ipaddress.ip_address(value)
        except ValueError:
            logging.getLogger('server').critical(f'Введен некорректный адрес {value}')
            exit(1)
        instance.__dict__[self.my_attr] = value

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr