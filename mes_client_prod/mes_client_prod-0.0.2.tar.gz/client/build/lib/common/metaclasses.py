import dis


class ServerMaker(type):
    """
    Метакласс, проверяющий что в результирующем классе нет клиентских
    вызовов, таких как: connect.
    Также проверяется, что серверный сокет является TCP и работает по IPv4 протоколу.
    """

    def __init__(cls, clsname, bases, clsdict):
        # Список методов, которые используются в функциях класса:
        methods = []
        # Атрибуты, вызываемые функциями классов
        attrs = []
        for func in clsdict:
            # Пробуем
            try:
                ret = dis.get_instructions(clsdict[func])
                # Если не функция, то ловим исключение
            except TypeError:
                pass
            else:
                # Иначе, разбираем код, получая используемые методы и атрибуты.
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
                'Использование метода connect недопустимо в серверном классе')
        # Если сокет не инициализировался константами SOCK_STREAM(TCP)
        # AF_INET(IPv4), тоже исключение.
        if not ('SOCK_STREAM' in attrs and 'AF_INET' in attrs):
            raise TypeError('Некорректная инициализация сокета.')
        super().__init__(clsname, bases, clsdict)


class ClientMaker(type):
    """
    Метакласс, проверяющий результирующий классе на серверные вызовы (accept, listen).
    Проверяется, что сокет не создаётся внутри конструктора класса.
    """

    def __init__(cls, clsname, bases, clsdict):
        # Список методов, которые используются в функциях класса:
        methods = []
        for func in clsdict:
            try:
                ret = dis.get_instructions(clsdict[func])
                # Если не функция, то ловим исключение
            except TypeError:
                pass
            else:
                # Если функция разбираем код, получая используемые методы.
                for i in ret:
                    if i.opname == 'LOAD_GLOBAL':
                        if i.argval not in methods:
                            methods.append(i.argval)
        # Если обнаружено использование недопустимого метода accept, listen,
        # socket бросаем исключение:
        for command in ('accept', 'listen', 'socket'):
            if command in methods:
                raise TypeError(
                    'В классе обнаружено использование запрещённого метода')
        if 'get_message' in methods or 'send_message' in methods:
            pass
        else:
            raise TypeError(
                'Отсутствуют вызовы функций, работающих с сокетами.')
        super().__init__(clsname, bases, clsdict)
