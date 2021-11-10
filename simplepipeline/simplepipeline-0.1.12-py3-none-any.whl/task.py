from functools import partial

from simplepipeline.pipeline import Pipeline
from simplepipeline.utils.task_logger import TaskLogger


class Task:
    PIPELINE = None

    def __init__(self, func, func_name, args, kwargs):
        self.func = func
        self.func_name = func_name
        self.func_partial = partial(func, *args, **kwargs)

        self.register()

    def run_map(self, *args, **kwargs):
        result = self.func(*args, **kwargs)
        return result

    def run(self):
        task_logger = TaskLogger(self.func_name)
        task_logger.start()
        result = self.func_partial()
        task_logger.stop()
        return result

    def register(self):
        if self.PIPELINE is not None:
            self.PIPELINE.register(self.func_name)


class FilterTask(Task):

    def __init__(self, func, func_name, args, kwargs):
        super().__init__(func, func_name, args, kwargs)
        self.in_len = len(args[0])

    def run(self):
        task_logger = TaskLogger(self.func_name)
        task_logger.start()
        result = self.func_partial()

        if isinstance(result, tuple):
            out_len = len(result[0])
        else:
            out_len = len(result)

        task_logger.stop(f"Dropped {self.in_len - out_len} items.")
        return result


def task(func):
    def wrapper(*args, **kwargs):
        return Task(func, func.__name__, args, kwargs)

    return wrapper


def filter_task(func):
    def wrapper(*args, **kwargs):
        return FilterTask(func, func.__name__, args, kwargs)

    return wrapper


def set_pipeline(pipeline: Pipeline):
    Task.PIPELINE = pipeline


def get_pipeline():
    return Task.PIPELINE


def delete_pipeline():
    Task.PIPELINE = None
