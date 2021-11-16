import dis
import logging

SERVER_LOG = logging.getLogger('app.server')
CLIENT_LOG = logging.getLogger('app.client')


class ServerVerifier(type):
    def __init__(self, clsname, bases, clsdict):
        """
        clsname - экземпляр класса
        bases - кортеж предков
        clsdict - словарь атрибутов и методов
        """
        methods = []  # Пустой список методов
        attributes = []  # Пустой список атрибутов

        for function in clsdict:
            try:
                returns = dis.get_instructions(clsdict[function])
            except TypeError:  # exception if not a function in dis
                pass
            else:  # if function
                for i in returns:
                    if i.opname == 'LOAD_GLOBAL':
                        if i.argval not in methods:  # заполняем список методами, использующимися в функциях класса
                            methods.append(i.argval)
                    elif i.opname == 'LOAD_ATTR':
                        if i.argval not in attributes:  # заполняем список атрибутами, использующимися в функциях класса
                            attributes.append(i.argval)
        # Если обнаружено использование недопустимого метода connect, бросаем
        # исключение:
        SERVER_LOG.debug(
            f"Нашли методы при инициализации фабрикой классов: {methods}")
        SERVER_LOG.debug(
            f"Нашли атрибуты при инициализации фабрикой классов: {attributes}")

        if 'connect' in methods:
            raise TypeError(
                'Использование метода connect недопустимо в серверном классе')
        # Если сокет не инициализировался константами SOCK_STREAM(TCP)
        # AF_INET(IPv4), тоже исключение.
        if not ('SOCK_STREAM' in attributes and 'AF_INET' in attributes):
            raise TypeError('Некорректная инициализация сокета.')

        super().__init__(clsname, bases, clsdict)


class ClientVerifier(type):
    def __init__(self, clsname, bases, clsdict):
        methods = []  # Пустой список методов
        attributes = []  # Пустой список атрибутов
        print(clsdict)
        for function in clsdict:
            try:
                returns = dis.get_instructions(clsdict[function])
            except TypeError:
                pass
            else:
                for i in returns:
                    if i.opname == 'LOAD_GLOBAL':
                        if i.argval not in methods:
                            methods.append(i.argval)
                    elif i.opname == 'LOAD_ATTR':
                        if i.argval not in attributes:  # заполняем список атрибутами, использующимися в функциях класса
                            attributes.append(i.argval)
        CLIENT_LOG.debug(
            f"Нашли методы при инициализации фабрикой классов: {methods}")
        CLIENT_LOG.debug(
            f"Нашли атрибуты при инициализации фабрикой классов: {attributes}")

        # Если обнаружено использование недопустимого метода accept, listen,
        # socket бросаем исключение:
        for command in ('accept', 'listen', 'socket'):
            if command in methods:
                raise TypeError(
                    'В классе обнаружено использование запрещённого метода')
        # Наличие поле connector, который является объектом с методами работы с
        # сокетами считаем корректным использованием сокетов
        if 'connector' in attributes:
            pass
        else:
            raise TypeError('Отсутствует поле, работающее с сокетами.')
        super().__init__(clsname, bases, clsdict)
