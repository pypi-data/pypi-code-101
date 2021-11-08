import functools
import logging
import multiprocessing
import sys
from logging.handlers import RotatingFileHandler, QueueHandler

import coloredlogs

MSG_TEMPLATE = "[%(asctime)s | %(filename)s:%(funcName)s:%(lineno)d] <%(processName)s:%(process)d:%(threadName)s> %(levelname)s:  %(message)s"

_LOGGING_PROCESS = None

_LOGGER_QUEUE = None

_LOG_LEVEL = logging.INFO


def error_log(function):
    @functools.wraps(function)
    def _wrap(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except BaseException as err:
            if not isinstance(err, KeyboardInterrupt):
                logging.warning('The following error occured: %s', err, exc_info=1)

                raise err

    return _wrap


LOG_LEVEL_IDENTIFIER = "log_level"


def connect():
    global _LOGGER_QUEUE, _LOG_LEVEL

    root = logging.getLogger()
    root.setLevel(_LOG_LEVEL)

    h = QueueHandler(_LOGGER_QUEUE)  # Just the one handler needed
    root.handlers.clear()
    root.addHandler(h)


def _logger_thread(queue, level, filename):
    _initialize_process(level, filename)
    while True:
        try:
            record = queue.get()

            if record is None:  # We send this as a sentinel to tell the listener to quit.
                break
            logger = logging.getLogger(record.name)
            logger.handle(record)  # No level or filter logic applied - just do it!
        except Exception:
            import sys, traceback
            print('Whoops! Problem:', file=sys.stderr)
            traceback.print_exc(file=sys.stderr)


def _initialize_process(level, filename):
    logger = logging.getLogger()

    # remove the default handler
    if logger.handlers:
        logger.removeHandler(logger.handlers[0])

    # create a format for the logging as well for file logging as for
    # logging to stdout
    log_format = logging.Formatter(MSG_TEMPLATE.format(start="", end=""))

    logger.setLevel(logging.ERROR)

    # setup the file logging
    if filename:
        file_handler = RotatingFileHandler(filename, pow(2, 20), 10)
        file_handler.setFormatter(log_format)
        file_handler.setLevel(logging.DEBUG)
        logger.addHandler(file_handler)

    # setup the console logging - log to stdout
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(coloredlogs.ColoredFormatter(fmt=MSG_TEMPLATE))
    console_handler.setLevel(logging.ERROR if filename else level)

    logger.addHandler(console_handler)


def initialize(level, filename=None):
    global _LOGGER_QUEUE, _LOGGING_PROCESS, _LOG_LEVEL

    _LOGGER_QUEUE = multiprocessing.Queue(-1)

    _LOGGING_PROCESS = multiprocessing.Process(target=_logger_thread, args=(_LOGGER_QUEUE, level, filename))

    _LOG_LEVEL = level

    _LOGGING_PROCESS.start()

    connect()


def uninitialize():
    global _LOGGER_QUEUE, _LOGGING_PROCESS

    _LOGGER_QUEUE.put_nowait(None)

    _LOGGING_PROCESS.join()


if __name__ == '__main__':

    from random import random


    def test_func():
        connect()

        for i in range(10):
            logger = logging.getLogger()
            logger.warning('Test %d', int(random() * 10))


    initialize(logging.INFO)

    logging.error('test')
    worker = multiprocessing.Process(target=test_func())
    worker.start()
    worker.join()

    uninitialize()
