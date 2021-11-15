from simplepipeline.utils.task_logger import TaskLogger


class Map:

    def __init__(self, partial_func, task):
        self.partial_func = partial_func
        self.task = task()

    def run(self):
        task_logger = TaskLogger(self.task.func_name)
        task_logger.start()
        result = self.partial_func()
        task_logger.stop()
        return result


class MultiMap:

    def __init__(self, func):
        self.func = func

    def run(self):
        return map(list, zip(*self.func.run()))
