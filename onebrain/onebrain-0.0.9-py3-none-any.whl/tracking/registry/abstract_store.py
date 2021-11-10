from abc import ABCMeta, abstractmethod


class AbstractStore:

    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def log_metric(self, run_id, metric):
        pass