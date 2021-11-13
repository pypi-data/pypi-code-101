"""Конфигурация логирования клиента"""

import sys
import os
import logging
import logging.handlers

from common.variables import LOGGING_LEVEL


# создаём формировщик логов (formatter):
CLIENT_FORMATTER = logging.Formatter(
    '%(asctime)s %(levelname)s %(filename)s %(message)s')

# указываем путь для сохранения файла-лога
PATH = os.getcwd()
PATH = os.path.join(PATH, '../project-logs/client.log')


# создаём потоки вывода логов
STREAM_HANDLER = logging.StreamHandler(sys.stderr)
STREAM_HANDLER.setFormatter(CLIENT_FORMATTER)
STREAM_HANDLER.setLevel(logging.ERROR)
LOG_FILE = logging.FileHandler(PATH, encoding='utf8')
LOG_FILE.setFormatter(CLIENT_FORMATTER)

# создаём регистратор и настраиваем его
LOGGER = logging.getLogger('client')
LOGGER.addHandler(STREAM_HANDLER)
LOGGER.addHandler(LOG_FILE)
LOGGER.setLevel(LOGGING_LEVEL)


# проверка перед импортом к клиенту и серверу
if __name__ == '__main__':
    LOGGER.critical('Alarm!')
    LOGGER.error('Error')
    LOGGER.debug('Debug information')
    LOGGER.info('Info')
