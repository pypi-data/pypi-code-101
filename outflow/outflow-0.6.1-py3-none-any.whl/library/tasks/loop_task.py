# -*- coding: utf-8 -*-
from copy import deepcopy

from outflow.core.tasks import TaskManager
from outflow.core.tasks import Task
from outflow.core.workflow import ManagerTask


class LoopTask(Task, ManagerTask):
    def __init__(
        self,
        iterations=0,
        infinite=False,
        name=None,
    ):
        if iterations and infinite:
            raise RuntimeError(
                "You can only set a number of iterations or infinite=True for LoopTask, not both."
            )

        if not iterations and not infinite:
            raise RuntimeError(
                "You must either set a number of iterations or infinite=True for LoopTask"
            )

        self.nb_iterations = iterations
        self.infinite = infinite

        ManagerTask.__init__(self)

        Task.__init__(self, auto_outputs=False)

        if name is not None:
            self.name = name

    def run_subworkflow(self, inputs_copy):

        workflow_copy = deepcopy(self.inner_workflow)
        workflow_copy.start_nodes()[0].bind(
            **inputs_copy,
        )

        # execute subworkflow
        task_manager = TaskManager()
        task_manager.compute(workflow_copy)

        terminating_tasks = list()

        # get outputs of last tasks of workflow
        for task in workflow_copy:
            if task.terminating:
                terminating_tasks.append(task_manager.results[task.id])

    def run(self, **inputs):

        inputs_copy = inputs.copy()

        self.setup_external_edges(self.inner_workflow, self.external_edges, inputs_copy)

        for i in range(self.nb_iterations):
            self.run_subworkflow(inputs_copy)

        if self.infinite:
            while True:
                self.run_subworkflow(inputs_copy)

    def check_inputs(self, task_inputs):
        pass
