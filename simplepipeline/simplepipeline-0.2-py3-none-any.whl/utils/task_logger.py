import logging
from datetime import timedelta
from timeit import default_timer as timer

logger = logging.getLogger("root")


class TaskLogger:

    def __init__(self, func_name):
        self.func_name = func_name
        self._start = None
        self._end = None

    def start(self):
        logger.info(f"Starting: {self.func_name}")
        self._start = timer()

    def stop(self, additional=""):
        self._end = timer()
        logger.info(f"Finished: {self.func_name}. "
                    f"Time elapsed: {str(timedelta(seconds=self._end - self._start)).split('.')[0]}. "
                    f"{additional}")
