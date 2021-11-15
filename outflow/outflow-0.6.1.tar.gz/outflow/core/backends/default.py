# -*- coding: utf-8 -*-
from outflow.core.logging import logger
from outflow.core.tasks import TaskManager
from outflow.core.types import Skipped


class Backend:
    def __init__(self):
        logger.debug(f"Initialize backend '{self}'")
        self.name = "default"

    def run(self, *, workflow, task_returning=None):

        if task_returning is None:
            task_returning = list()
        elif not isinstance(task_returning, list):
            task_returning = [task_returning]

        task_manager = TaskManager()

        task_manager.compute(workflow)  # todo call on top level workflow instead
        # but still return results of task_list, if list is not none

        execution_return = [
            task_manager.results.resolve(task.id) for task in task_returning
        ]
        filter_results = False  # TODO parametrize outside
        if filter_results:
            return list(
                filter(
                    lambda el: not any(isinstance(val, Skipped) for val in el.values()),
                    execution_return,
                )
            )
        else:
            return execution_return

    def clean(self):
        pass
