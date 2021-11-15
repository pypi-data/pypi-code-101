# -*- coding: utf-8 -*-
import subprocess
import threading
import socket
from pathlib import Path

import cloudpickle

from outflow.core.backends.default import Backend as DefaultBackend
from outflow.core.logging import logger, LogRecordSocketReceiver
from outflow.core.pipeline import context, get_pipeline_states
from outflow.core.tasks import TaskManager


class Backend(DefaultBackend):
    def __init__(self):

        try:
            subprocess.run(["sinfo", "-V"], check=False, capture_output=True)
        except FileNotFoundError:
            raise RuntimeError(
                "Slurm is not installed",
            )

        super().__init__()
        self.name = "slurm"

        context.head_address = socket.gethostbyname(socket.gethostname())

        self.tcpserver = LogRecordSocketReceiver()
        self.server_thread = threading.Thread(target=self.tcpserver.serve_forever)
        self.init_tcp_socket_receiver()

    def run(self, *, workflow, task_returning=None):

        if task_returning is None:
            task_returning = []
        elif not isinstance(task_returning, list):
            task_returning = [task_returning]

        pipeline_states = get_pipeline_states()
        run_dir = Path(f".outflow_tmp/outflow_{context.run_uuid}")

        run_dir.mkdir(exist_ok=True, parents=True)

        with open(run_dir / "pipeline_states", "wb") as pipeline_states_file:
            cloudpickle.dump(pipeline_states, pipeline_states_file)

        task_manager = TaskManager()

        task_manager.compute(workflow)

        execution_return = [
            task_manager.results.resolve(task.id) for task in task_returning
        ]
        # but still return results of task_list, if list is not none

        return execution_return
        # filter_results = False  # TODO parametrize outside
        # if filter_results:
        #     return list(
        #         filter(
        #             lambda el: not any(isinstance(val, Skipped) for val in el.values()),
        #             execution_return,
        #         )
        #     )
        # else:
        #     return execution_return

    def init_tcp_socket_receiver(self):  # TODO move to DefaultBackend
        logger.debug("About to start TCP server...")

        # Exit the server thread when the main thread terminates
        self.server_thread.daemon = True
        self.server_thread.start()
        _, context.logger_port = self.tcpserver.server_address

    def clean(self):
        logger.debug("Cleaning slurm backend")
        self.tcpserver.shutdown()

        while not len(context.running_slurm_job_ids) == 0:
            slurm_id = context.running_slurm_job_ids.pop()
            logger.debug("cancelling slurm id {id}".format(id=slurm_id))
            subprocess.run(["scancel", str(slurm_id), "-b"])
