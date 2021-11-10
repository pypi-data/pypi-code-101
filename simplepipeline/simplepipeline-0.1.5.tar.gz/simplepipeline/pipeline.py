import logging

logger = logging.getLogger("root")


class Pipeline:

    def __init__(self, name=None):
        self.name = name
        self._tasks = []

    def register(self, task_name):
        self._tasks.append(task_name)

    def executed_tasks(self):
        logger.info(f"Pipeline: {'Not Specified' if self.name is None else self.name}")
        _ = [logger.info(f"\t Task: {task}") for task in self._tasks]
        logger.info("hallo")
        return self._tasks
