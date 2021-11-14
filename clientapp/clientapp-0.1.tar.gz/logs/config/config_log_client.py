import logging.handlers
import os
import sys

sys.path.append('../')

PATH = os.getcwd()
PATH = os.getcwd()
PATH = os.path.join(PATH, '../log-files/client.log')

CLIENT_FORMATTER = logging.Formatter(
    '%(asctime)-30s %(levelname)-15s %(filename)-15s %(message)s')

CLIENT_HANDLER = logging.handlers.TimedRotatingFileHandler(PATH,
                                                           encoding='utf-8',
                                                           interval=1, when='D')
CLIENT_HANDLER.setFormatter(CLIENT_FORMATTER)

LOGGER = logging.getLogger('client')
LOGGER.addHandler(CLIENT_HANDLER)
LOGGER.setLevel(logging.INFO)

if __name__ == '__main__':
    LOGGER.critical('critical - check')
    LOGGER.error('error - check')
    LOGGER.debug('debug - check')
    LOGGER.info('info - check')
