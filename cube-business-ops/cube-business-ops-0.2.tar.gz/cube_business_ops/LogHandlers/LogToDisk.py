from logging.handlers import RotatingFileHandler
import logging

import os

class LogToDisk(RotatingFileHandler):

    def __init__(self, app_address, config):

        self.__address=app_address

        verbose = config["logging-level"]
        log_file=os.path.join(config["logging-dir"], app_address+"-"+str(verbose)+".log")
        max_log_count=config["max-log-count"]
        max_log_size_bytes=config["max-log-size"]*1048576

        RotatingFileHandler.__init__(self,log_file, maxBytes=max_log_size_bytes, backupCount=max_log_count)


        if verbose == "DEBUG":
            level = logging.DEBUG
        elif verbose == "CRITICAL":
            level = logging.CRITICAL
        elif verbose == "ERROR":
            level = logging.ERROR
        elif verbose == "WARNING":
            level = logging.WARNING
        elif verbose == "INFO":
            level = logging.INFO
        else:
            level = logging.DEBUG

        self.setLevel(level)
        formatter = logging.Formatter(config["logging-format"])
        self.setFormatter(formatter)


