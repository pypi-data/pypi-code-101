# -*- coding: utf-8 -*-
from outflow.core.generic.lazy_object_proxy import LazyObjectProxy
from outflow.core.logging import logger
from outflow.core.pipeline import context


def determine_map_class():
    logger.debug(f"Generic MapTask initializing a {context.backend_name} MapTask")

    if context.backend_name == "default":
        from outflow.library.tasks.sequential_map_task import SequentialMapTask

        return SequentialMapTask

    elif context.backend_name == "parallel":
        from outflow.library.tasks.parallel_map_task import ParallelMapTask

        return ParallelMapTask

    elif context.backend_name == "slurm":
        from outflow.slurm.map_task import SlurmMapTask

        return SlurmMapTask

    else:
        raise AttributeError("Could not determine backend for generic MapTask")


MapTask = LazyObjectProxy(determine_map_class)
