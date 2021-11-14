import logging
import sys
import traceback
import inspect
sys.path.append('../')


if sys.argv[0].find('client') == -1:
    LOGGER = logging.getLogger('server')
if sys.argv[0].find('server') == -1:
    LOGGER = logging.getLogger('client')


class ClassLog:
    '''
    Декоратор, выполняющий логирование вызовов классов.
    Сохраняет события типа debug, содержащие
    информацию о имени вызываемой функиции, параметры с которыми
    вызывается функция, и модуль, вызывающий функцию.
    '''
    def __call__(self, log_to_save):
        def log_saver(*args, **kwargs):
            f = log_to_save(*args, **kwargs)
            LOGGER.debug(
                f'Была вызвана функция {log_to_save.__name__} c параметрами {args}, {kwargs}. '
                f'Вызов из модуля {log_to_save.__module__}. '
                f'Вызов из функции {inspect.stack(0)[1][3]}', stacklevel=2)
            return f

        return log_saver


def func_log(log_to_save):
    '''
    Декоратор, выполняющий логирование вызовов функций.
    Сохраняет события типа debug, содержащие
    информацию о имени вызываемой функиции, параметры с которыми
    вызывается функция, и модуль, вызывающий функцию.
    '''
    def log(*args, **kwargs):
        f = log_to_save(*args, **kwargs)
        LOGGER.debug(
            f'Была вызвана функция {log_to_save.__name__} c параметрами {args}, {kwargs}. '
            f'Вызов из модуля {log_to_save.__module__}. '
            f'Вызов из функции {log_to_save.__name__}')
        return f

    return log
