# -*- coding: utf-8 -*-
import pathlib
import re
import signal
import subprocess
import sys
import time
from pathlib import Path

import cloudpickle
from simple_slurm import Slurm

from outflow.core.logging import logger
from outflow.core.pipeline import context
from outflow.library.tasks.base_map_task import BaseMapTask, SigTerm
from outflow.management.models.mixins import StateEnum
from outflow.management.models.workflow import Workflow
from outflow.management.models.task import Task as TaskModel


class SignalHandler:
    term_received = False

    def __init__(self):
        signal.signal(signal.SIGTERM, self.handle_sigterm)

    def handle_sigterm(self, *args):
        self.term_received = True


class SlurmMapTask(BaseMapTask):
    def __init__(self, simultaneous_tasks=None, **kwargs):

        super().__init__(**kwargs)

        # all other kwargs should be sbatch directives
        for kw in ["name", "no_outputs", "output_name", "raise_exceptions"]:
            if kw in kwargs:
                del kwargs[kw]

        self.sbatch_directives = kwargs
        self.simultaneous_tasks = simultaneous_tasks

    def run(self, **map_inputs):

        inputs = list(self.generator(**map_inputs))

        # serialize everything needed for remote execution
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

        run_dir = Path(f".outflow_tmp/outflow_{context.run_uuid}")
        with open(run_dir / f"map_info_{self.uuid}.pickle", "wb") as map_info_file:
            cloudpickle.dump(map_info, map_info_file)

        # Sbatch slurm array
        nb_slurm_tasks = len(map_info["generated_inputs"])

        if nb_slurm_tasks == 0:
            return self.reduce([])

        array_directive = f"0-{nb_slurm_tasks-1}"

        if self.simultaneous_tasks:
            array_directive += f"%{self.simultaneous_tasks}"

        pathlib.Path("slurm_out").mkdir(exist_ok=True)

        map_slurm_array = Slurm(
            array=array_directive,
            job_name=f"outflow_{self.name}_{self.uuid}",
            error="slurm_out/slurm-%A_%a.err",
            output="slurm_out/slurm-%A_%a.out",
            **self.sbatch_directives,
        )

        job_id = map_slurm_array.sbatch(
            f"srun {sys.executable} manage.py --run-uuid {context.run_uuid} --map-uuid {self.uuid}",
            verbose=False,
        )

        context.running_slurm_job_ids.append(job_id)

        results = list()

        timeout = 60000  # seconds
        start = time.time()

        slurm_end_states = [
            "BOOT_FAIL",
            "CANCELLED",
            "COMPLETED",
            "DEADLINE",
            "FAILED",
            "NODE_FAIL",
            "OUT_OF_MEMORY",
            "PREEMPTED",
            "TIMEOUT",
        ]

        array_jobs = [f"{str(job_id)}_{i}" for i in range(nb_slurm_tasks)]

        signal_handler = SignalHandler()

        while True:
            time.sleep(1)
            now = time.time()
            states = []

            if signal_handler.term_received:
                raise SigTerm()

            if now - start > timeout:
                raise RuntimeError("timeout on slurm map")

            for job in array_jobs:
                try:
                    output = subprocess.run(
                        ["scontrol", "show", "job", job, "-o"],
                        capture_output=True,
                        text=True,
                        check=True,
                    ).stdout
                    state = re.findall(r"JobState=(\S*)", output)[0]

                except Exception:
                    state = "COMPLETED"

                finally:
                    states.append(state)

            if all([state in slurm_end_states for state in states]):
                break  # job array has ended

        all_mapped_tasks = (
            context.session.query(TaskModel)
            .filter(TaskModel.workflow.has(Workflow.manager_task_id == self.db_task.id))
            .all()
        )

        if any(task.state == StateEnum.failed for task in all_mapped_tasks):
            error_msg = f"One or more task has failed in mapped workflows of MapTask {self.name}"
            if self.raise_exceptions:
                raise RuntimeError(error_msg)
            else:
                logger.warning(error_msg)

        try:
            for task_id in range(nb_slurm_tasks):
                with open(
                    run_dir / f"map_result_{task_id}_{self.uuid}",
                    "rb",
                ) as map_result_file:
                    results.append(cloudpickle.load(map_result_file))
        except FileNotFoundError as fe:
            logger.error("One or more map output files could not be found")
            raise fe

        context.running_slurm_job_ids.remove(job_id)

        return self.reduce(results)
