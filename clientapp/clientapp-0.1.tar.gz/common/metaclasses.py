import dis


class ClientVerifier(type):
    '''
    Метакласс, проверяющий что в результирующем классе нет серверных
    вызовов таких как: accept, listen. Также проверяется, что сокет не
    создаётся внутри конструктора класса.
    '''
    def __init__(self, clsname, bases, clsdict):
        methods = []
        for fnc in clsdict:
            try:
                ret = dis.get_instructions(clsdict[fnc])
            except TypeError:
                pass
            else:
                for i in ret:
                    if i.opname == 'LOAD_GLOBAL':
                        if i.argval not in methods:
                            methods.append(i.argval)
        for command in ('accept', 'listen', 'socket'):
            if command in methods:
                raise TypeError(
                    'В классе обнаружено использование запрещённого метода')
        if ('get_msg' not in methods) and ('send_msg' not in methods):
            raise TypeError(
                'Отсутствуют вызовы функций, работающих с сокетами.')

        super().__init__(clsname, bases, clsdict)


class ServerVerifier(type):
    '''
    Метакласс, проверяющий что в результирующем классе нет клиентских
    вызовов таких как: connect. Также проверяется, что серверный
    сокет является TCP и работает по IPv4 протоколу.
    '''
    def __init__(self, clsname, bases, clsdict):
        methods = []
        for fnc in clsdict:
            try:
                ret = dis.get_instructions(clsdict[fnc])
            except TypeError:
                pass
            else:
                for i in ret:
                    if i.opname == 'LOAD_GLOBAL':
                        if i.argval not in methods:
                            methods.append(i.argval)
        if 'connect' in methods:
            raise TypeError(
                'Использование метода connect недопустимо в серверном классе')
        if not ('SOCK_STREAM' in methods and 'AF_INET' in methods):
            raise TypeError('Некорректная инициализация сокета.')
        super().__init__(clsname, bases, clsdict)
