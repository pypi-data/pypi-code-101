# -*- coding: utf-8 -*-
"""
日志类。读取配置文件，定义日志级别、日志文件名、日志格式。
一般直接把logger import进去
from utils.log import logger
logger.info('test log')
"""
import logging
import os
from time import strftime
from .config import Config, BASE_PATH

__all__ = [
    "Logger",
    "logger"
]

# default log path and config sample
LOG_PATH = os.path.join(BASE_PATH, 'log')
LOG_CONFIG = {
    "backup": 5,
    "console_level": "INFO",
    "file_level": "INFO",
    "file_name": "test.log",
    "pattern": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    "log_path": LOG_PATH
}


class Logger(object):
    def __init__(self, logger_name='PYTEST-REPORT', config=None, log_path=None):
        self.logger = logging.getLogger(logger_name)
        logging.root.setLevel(logging.NOTSET)

        ConfigLog = None
        try:
            cfg = Config()
            CONFIGS = cfg.get()
            ConfigLog = CONFIGS["log"]
            ConfigLog["log_path"] = cfg.LOG_PATH
        except:
            ConfigLog = None

        if config:
            self.config = config
        elif ConfigLog:
            self.config = ConfigLog
        else:
            self.config = LOG_CONFIG

        self.console_output_level = self.config.get('console_level')  # WARNING
        self.file_output_level = self.config.get('file_level')  # INFO
        self.backup_count = self.config.get('backup')  # 5
        self.formatter = logging.Formatter(self.config.get('pattern'))
        self.log_path = log_path if log_path else self.config.get('log_path')
        self.log_file_name = os.path.join(self.log_path,
                                          '{0}-{1}'.format(strftime('%Y-%m-%d'), self.config.get('file_name')))

        os.makedirs(self.log_path, exist_ok=True)

    def __logger(self, level, message):
        # 创建一个FileHandler，用于写到本地
        file_handler = logging.FileHandler(self.log_file_name, 'a', encoding='utf-8')
        file_handler.setFormatter(self.formatter)
        file_handler.setLevel(self.file_output_level)
        self.logger.addHandler(file_handler)

        # 创建一个StreamHandler,用于输出到控制台
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(self.formatter)
        console_handler.setLevel(self.console_output_level)
        self.logger.addHandler(console_handler)

        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)
        # 这两行代码是为了避免日志输出重复问题
        self.logger.removeHandler(console_handler)
        self.logger.removeHandler(file_handler)
        # 关闭打开的文件
        file_handler.close()

    def debug(self, message):
        self.__logger('debug', message)

    def info(self, message):
        self.__logger('info', message)

    def warning(self, message):
        self.__logger('warning', message)

    def error(self, message):
        self.__logger('error', message)


logger = Logger()
logging.getLogger('faker').setLevel(logging.ERROR)
