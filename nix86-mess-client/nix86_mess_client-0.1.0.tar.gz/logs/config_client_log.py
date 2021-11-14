import sys
import os
import logging
from common.variables import LOGGING_LEVEL
sys.path.append('../')

logger_formatter = logging.Formatter('%(asctime)s %(levelname)s %(filename)s %(message)s')

PATH = os.getcwd()
path_to_file_log = os.path.join(PATH, 'client/client.log')

log_file_handler = logging.FileHandler(path_to_file_log, encoding='utf8')
log_file_handler.setFormatter(logger_formatter)

logger = logging.getLogger('client')
logger.addHandler(log_file_handler)
logger.setLevel(LOGGING_LEVEL)

if __name__ == '__main__':
    logger.critical('Критическая ошибка')
    logger.error('Ошибка')
    logger.debug('Отладочная информация')
    logger.info('Информационное сообщение')
