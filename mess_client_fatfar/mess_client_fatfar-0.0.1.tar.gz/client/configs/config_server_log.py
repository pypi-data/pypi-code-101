"""Конфигурация логирования серверной части"""

import sys
import os
import logging
import logging.handlers

from common.variables import LOGGING_LEVEL


# создаём формировщик логов (formatter):
SERVER_FORMATTER = logging.Formatter(
    '%(asctime)s %(levelname)s %(filename)s %(message)s')

# указываем путь для сохранения файла-лога
PATH = os.getcwd()
PATH = os.path.join(PATH, '../project-logs/server.log')

# создаём потоки вывода логов
STREAM_HANDLER = logging.StreamHandler(sys.stderr)
STREAM_HANDLER.setFormatter(SERVER_FORMATTER)
STREAM_HANDLER.setLevel(logging.ERROR)
LOG_FILE = logging.handlers.TimedRotatingFileHandler(
    PATH, encoding='utf8', interval=1, when='D')
LOG_FILE.setFormatter(SERVER_FORMATTER)

# создаём регистратор и настраиваем его
LOGGER = logging.getLogger('server')
LOGGER.addHandler(STREAM_HANDLER)
LOGGER.addHandler(LOG_FILE)
LOGGER.setLevel(LOGGING_LEVEL)


# проверка перед импортом к клиенту и серверу
if __name__ == '__main__':
    LOGGER.critical('Alarm!')
    LOGGER.error('Error')
    LOGGER.debug('Debug information')
    LOGGER.info('Info')
