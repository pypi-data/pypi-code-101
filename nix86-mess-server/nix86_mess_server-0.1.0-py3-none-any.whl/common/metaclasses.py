import dis


class ServerMetaClass(type):
    def __init__(self, class_name, bases, class_dict):
        methods = []
        attributes = []

        for function in class_dict:
            try:
                res = dis.get_instructions(class_dict[function])
            except TypeError:
                pass
            else:
                for item in res:
                    if item.opname == 'LOAD_GLOBAL':
                        if item.argval not in methods:
                            methods.append(item.argval)
                    elif item.opname == 'LOAD_ATTR':
                        if item.argval not in attributes:
                            attributes.append(item.argval)

        if 'connect' in methods:
            raise TypeError('Использование метода connect недопустимо в серверном классе')

        if not ('SOCK_STREAM' in attributes and 'AF_INET' in attributes):
            raise TypeError('Некорректная инициализация сокета.')

        super().__init__(class_name, bases, class_dict)


class ClientMetaClass(type):
    def __init__(self, class_name, bases, class_dict):
        methods = []

        for function in class_dict:
            try:
                res = dis.get_instructions(class_dict[function])
            except TypeError:
                pass
            else:
                for item in res:
                    if item.opname == 'LOAD_GLOBAL':
                        if item.argval not in methods:
                            methods.append(item.argval)

        for method in ('accept', 'listen', 'socket'):
            if method in methods:
                raise TypeError(
                    'Обнаружено использование запрещённого метода'
                )

        if 'get_message' in methods or 'send_message' in methods:
            pass
        else:
            raise TypeError(
                'Отсутствуют вызовы функций, работающих с сокетами.')
        super().__init__(class_name, bases, class_dict)
