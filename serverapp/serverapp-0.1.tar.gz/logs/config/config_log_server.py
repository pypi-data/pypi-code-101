import logging.handlers
import os
import sys

sys.path.append('../')

PATH = os.getcwd()
PATH = os.path.join(PATH, '../log-files/server.log')

SERVER_FORMATTER = logging.Formatter(
    '%(asctime)-30s %(levelname)-15s %(filename)-15s %(message)s')

SERVER_HANDLER = logging.StreamHandler(sys.stderr)
SERVER_HANDLER.setFormatter(SERVER_FORMATTER)

LOGGER = logging.getLogger('server')
LOGGER.addHandler(SERVER_HANDLER)
LOGGER.setLevel(logging.DEBUG)

if __name__ == '__main__':
    LOGGER.critical('critical - check')
    LOGGER.error('error - check')
    LOGGER.debug('debug - check')
    LOGGER.info('info - check')
