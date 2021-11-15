# -*- coding: utf-8 -*-
from copy import deepcopy
from functools import partial
from multiprocessing import Pool, cpu_count

from outflow.core.pipeline import context
from outflow.library.tasks.base_map_task import BaseMapTask
import cloudpickle
from outflow.core.pipeline.pipeline import set_pipeline_state, get_pipeline_states


class ParallelMapTask(BaseMapTask):
    @staticmethod
    def _run_workflow(index, serialized_pipeline_states, serialized_map_info):

        set_pipeline_state(**cloudpickle.loads(serialized_pipeline_states))
        map_info = cloudpickle.loads(serialized_map_info)

        return map_info["run_workflow"](
            workflow=deepcopy(map_info["inner_workflow"]),
            inputs=map_info["generated_inputs"][index],
            index=index,
            raise_exceptions=map_info["raise_exceptions"],
            external_edges=map_info["external_edges"],
        )

    def run(self, **map_inputs):

        if context.map_uuid:
            raise NotImplementedError(
                "Nested MapTasks are not supported with parallel backend"
            )

        inputs = list(self.generator(**map_inputs))

        # serialize everything needed for parallel execution
        map_info = {
            "generated_inputs": {
                index: generated_inputs for index, generated_inputs in enumerate(inputs)
            },
            "external_edges": {
                parent_task: child_task
                for parent_task, child_task in self.external_edges.items()
            },
            "inner_workflow": self.inner_workflow,
            "raise_exceptions": self.raise_exceptions,
            "run_workflow": self.run_workflow,
        }

        serialized_map_info = cloudpickle.dumps(map_info)

        run = partial(
            self._run_workflow,
            serialized_pipeline_states=cloudpickle.dumps(get_pipeline_states()),
            serialized_map_info=serialized_map_info,
        )

        indices = list(range(len(map_info["generated_inputs"])))

        with Pool(cpu_count()) as pool:
            results = pool.map(run, indices)

        return self.reduce(results)
