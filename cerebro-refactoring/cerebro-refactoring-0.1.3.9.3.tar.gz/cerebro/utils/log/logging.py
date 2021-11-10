# ------------------------------------------------------------------------------
#  MIT License
#
#  Copyright (c) 2021 Hieu Pham. All rights reserved.
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.
# ------------------------------------------------------------------------------

import os
import logging
import matplotlib.pyplot as plt
from cerebro.utils.io import Path
from cerebro.refactoring.designs import Singleton


# Log levels.
LOG_LEVELS = {'DEBUG': logging.DEBUG, 'INFO': logging.INFO, 'ERROR': logging.ERROR, 'CRITICAL': logging.CRITICAL}


class Log(metaclass=Singleton):
    """
    This class help us to write debug logs easily.
    ---------
    @author:    Hieu Pham.
    @created:   17.10.2021.
    @updated:   18.10.2021.
    """

    def __init__(self, **kwargs):
        """
        Create new instance.
        :param kwargs:  keyword arguments.
        """
        super().__init__()
        # Default log level.
        self._level = logging.DEBUG
        # Default log directory.
        self._dir = os.path.join(os.getcwd(), 'logs')
        self.config()

    def config(self, log_dir: str = os.path.join(os.getcwd(), 'logs'), logfile: str = None):
        """
        Configure logging object.
        :param log_dir:     directory to store logs.
        :param logfile:     file to save logs.
        :return:            the log itself.
        """
        self._dir = log_dir if log_dir is not None else self._dir
        # Log level will be set though ENV.
        self._level = os.environ.get('DEBUG', '').upper()
        self._level = logging.NOTSET if self._level not in LOG_LEVELS else LOG_LEVELS[self._level]
        logging.basicConfig(level=self._level)
        # Make logging format.
        _format = logging.Formatter('%(levelname)s:%(asctime)s: %(message)s')
        # Reset log handler.
        logger = logging.getLogger()
        logger.handlers.clear()
        # Make stream handler.
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(_format)
        logger.addHandler(console_handler)
        # Make file handler.
        if logfile is not None:
            file = os.path.join(log_dir, logfile)
            os.makedirs(os.path.dirname(file), exist_ok=True)
            file_handler = logging.FileHandler(file)
            file_handler.setFormatter(_format)
            logger.addHandler(file_handler)
        # Make console handler.
        return self

    def debug(self, msg):
        """
        Write log message.
        :param msg: log message.
        :return:    log itself.
        """
        logging.debug(msg)
        return self

    def info(self, msg):
        """
        Write log message.
        :param msg: log message.
        :return:    log itself.
        """
        logging.info(msg)
        return self

    def error(self, msg):
        """
        Write log message.
        :param msg: log message.
        :return:    log itself.
        """
        logging.error(msg)
        return self

    def critical(self, msg):
        """
        Write log message.
        :param msg: log message.
        :return:    log itself.
        """
        logging.critical(msg)
        return self

    def plot(self, figure=None, filename: str = None, **kwargs):
        """
        Write plot.
        :param figure:      figure to be write.
        :param filename:    filename to save.
        """
        if self._level != logging.NOTSET:
            plt.show()
            if filename is not None:
                file = os.path.join(self._dir, filename)
                file = Path(file).unique_suffix().path
                os.makedirs(os.path.dirname(file), exist_ok=True)
                figure.savefig(file)
        return self
