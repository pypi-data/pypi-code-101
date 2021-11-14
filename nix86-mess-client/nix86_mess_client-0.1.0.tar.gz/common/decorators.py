import inspect
import traceback
import logging
import sys

# определяем какой логер вызывать
if sys.argv[0].find('client.py') > -1:
    logger = logging.getLogger('client')
else:
    logger = logging.getLogger('server')


# декоратор в виде функции
def log_decorator(func_to_decor):
    def wrapper(*args, **kwargs):
        res = func_to_decor(*args, **kwargs)
        logger.debug(f'Была вызвана функция {func_to_decor.__name__} '
                     f'c параметрами {args}, {kwargs}. '
                     f'Вызов из модуля {func_to_decor.__module__}.'
                     f'Вызов из функции {inspect.stack()[1][3]}', stacklevel=2)
        return res

    return wrapper


# декоратор в виде класса
class LogDecorator:
    def __call__(self, func_to_decor):
        def wrapper(*args, **kwargs):
            res = func_to_decor(*args, **kwargs)
            logger.debug(f'Была вызвана функция {func_to_decor.__name__} '
                         f'c параметрами {args}, {kwargs}. '
                         f'Вызов из модуля {func_to_decor.__module__}.'
                         f'Вызов из функции {inspect.stack()[1][3]}',
                         stacklevel=2)
            return res

        return wrapper
