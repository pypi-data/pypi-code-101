# -*- coding: utf-8 -*-
from outflow.core.commands import RootCommand, Command
from outflow.library.tasks import IPythonTask
from outflow.core.pipeline import config


@RootCommand.subcommand(invokable=False, db_untracked=True, backend="default")
def Management():
    pass


@Management.subcommand()
def DisplayConfig():
    print(config)


@Management.subcommand(db_untracked=False)
class Shell(Command):
    """
    Run an interactive shell with access to the pipeline context.
    """

    def setup_tasks(self):
        return IPythonTask()


# @Management.subcommand()
# class TestSlurm(Command):
#     """
#     Run slurm test suite. Useful to check if your Slurm cluster is properly configured for use with outflow.
#     """
#
#     def setup_tasks(self):
#         from outflow.core.tasks import Task
#         @Task.as_task
#         def ExampleTask() -> {"value": int}:
#             import os
#             return int(os.getenv("SLURM_JOBID"))
#
#
#         from outflow.slurm.map_task import SlurmMapTask
#         with SlurmMapTask() as map:
