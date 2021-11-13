"""Метаклассы проверки сервера и клиента"""

import dis


class ServerVerifier(type):
    """
    Метакласс, проверяющий, что в результирующем классе нет клиентского
    вызова connect. Также проверяется, что серверный
    сокет является TCP и работает по IPv4 протоколу.
    """

    def __init__(self, clsname, bases, clsdict):
        # Список методов, которые используются в функциях класса:
        methods = []
        # Атрибуты, вызываемые функциями классов
        attrs = []
        for func in clsdict:
            try:
                ret = dis.get_instructions(clsdict[func])
            except TypeError:
                pass
            else:
                for i in ret:
                    if i.opname == 'LOAD_GLOBAL':
                        if i.argval not in methods:
                            methods.append(i.argval)
                    elif i.opname == 'LOAD_ATTR':
                        if i.argval not in attrs:
                            attrs.append(i.argval)
        # Если обнаружено использование недопустимого метода connect,
        # генерируем исключение:
        if 'connect' in methods:
            raise TypeError(
                'Method connect usage is unacceptable in server class.')
        # Если сокет не инициализировался константами SOCK_STREAM(TCP)
        # AF_INET(IPv4), тоже исключение.
        if not ('SOCK_STREAM' in attrs and 'AF_INET' in attrs):
            raise TypeError('Incorrect socket initialization.')
        super().__init__(clsname, bases, clsdict)


class ClientVerifier(type):
    """
    Метакласс, проверяющий, что в результирующем классе нет серверных
    вызовов таких, как accept, listen. Также проверяется, что сокет не
    создаётся внутри конструктора класса.
    """

    def __init__(self, clsname, bases, clsdict):
        # Список методов, которые используются в функциях класса:
        methods = []
        for func in clsdict:
            try:
                ret = dis.get_instructions(clsdict[func])
            except TypeError:
                pass
            else:
                for i in ret:
                    if i.opname == 'LOAD_GLOBAL':
                        if i.argval not in methods:
                            methods.append(i.argval)
        # Если обнаружено использование недопустимого метода accept, listen,
        # socket бросаем исключение:
        for command in ('accept', 'listen', 'socket'):
            if command in methods:
                raise TypeError('A forbidden method is detected in class')
        # Вызов take_msg или send_msg из utils считаем корректным
        # использованием сокетов
        if 'take_msg' in methods or 'send_msg' in methods:
            pass
        else:
            raise TypeError('Function calls working with sockets are absent.')
        super().__init__(clsname, bases, clsdict)
