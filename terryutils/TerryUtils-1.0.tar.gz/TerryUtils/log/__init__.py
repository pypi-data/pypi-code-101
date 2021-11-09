import os
import logging
import logging.handlers
import platform


LOG_LEVEL = os.getenv("LOG_LEVEL", logging.DEBUG)
LOG_FMT = '%(asctime)s 线程名:%(threadName)s %(levelname)s [%(filename)s %(funcName)s line:%(lineno)d]: %(message)s'

if platform.system() == 'Windows':
    LOG_SAVE_DIR = "C:/Logs"
elif platform.system() == 'Linux':
    LOG_SAVE_DIR = "~/Logs"
else:
    print('其他')

if not os.path.exists(LOG_SAVE_DIR):
    os.mkdir(LOG_SAVE_DIR)


class MyLog:

    def __init__(self, file_name, interval=1, when="D", backupCount=7, level=LOG_LEVEL):
        self._logger = None
        self.file_name = file_name
        self.file_path = os.path.join(LOG_SAVE_DIR, file_name)
        self._level = level
        self.interval = interval
        self.when = when
        self.backupCount = backupCount

    def get_logger(self, write_log=False):
        self._logger = logging.getLogger(self.file_name)
        self._format = logging.Formatter(LOG_FMT)
        self._logger.setLevel(self._level)

        self._stream_handler = logging.StreamHandler()
        self._stream_handler.setFormatter(self._format)

        self._file_handler = logging.handlers.TimedRotatingFileHandler(filename=self.file_path, interval=self.interval, when=self.when, backupCount=self.backupCount, encoding="utf-8")
        self._file_handler.setFormatter(self._format)

        self._logger.addHandler(self._stream_handler)

        if write_log:
            self._logger.addHandler(self._file_handler)

        return self._logger


if __name__ == '__main__':
    print("124")
    log = MyLog("test").get_logger(True)
    import time
    for i in range(20):
        log.info("I's a test message")
        time.sleep(1)







