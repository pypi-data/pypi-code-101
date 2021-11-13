import sys
import socket
import logging
import traceback
import inspect

# check the name 'client' or 'server' in a script
if sys.argv[0].find('client') == -1:
    LOGGER = logging.getLogger('server')
else:
    LOGGER = logging.getLogger('client')


class Log:
    """ Декоратор, выполняющий логирование вызовов функций. """

    def __call__(self, load_to_log):
        def log_catcher(*args, **kwargs):
            res = load_to_log(*args, **kwargs)
            LOGGER.info(
                f'Function was called {load_to_log.__name__} with parameters {args}, {kwargs}. '
                f'Call from {load_to_log.__module__}. Call'
                f' from function {traceback.format_stack()[0].strip().split()[-1]}.'
                f'Call from function {inspect.stack()[1][3]}', stacklevel=2)
            return res
        return log_catcher


def login_required(func):
    """
    Декоратор, проверяющий, что клиент авторизован на сервере.
    Проверяет, что передаваемый объект сокета находится в
    списке авторизованных клиентов.
    За исключением передачи словаря-запроса
    на авторизацию. Если клиент не авторизован,
    генерирует исключение TypeError
    """

    def checker(*args, **kwargs):
        # проверяем, что первый аргумент - экземпляр MessageProcessor
        # Импортить необходимо тут, иначе ошибка рекурсивного импорта.
        from packet_server.server import MessageProcessor
        from common.variables import ACTION, HERE
        if isinstance(args[0], MessageProcessor):
            found = False
            for arg in args:
                if isinstance(arg, socket.socket):
                    # Проверяем, что данный сокет есть в списке names класса
                    # MessageProcessor
                    for client in args[0].names:
                        if args[0].names[client] == arg:
                            found = True

            # Теперь надо проверить, что передаваемые аргументы не here
            # сообщение. Если here, то разрешаем
            for arg in args:
                if isinstance(arg, dict):
                    if ACTION in arg and arg[ACTION] == HERE:
                        found = True
            # Если не авторизован и не сообщение начала авторизации, то
            # вызываем исключение.
            if not found:
                raise TypeError
        return func(*args, **kwargs)

    return checker
