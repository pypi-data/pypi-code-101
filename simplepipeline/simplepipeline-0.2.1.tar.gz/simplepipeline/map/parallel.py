from functools import partial

import ray

from simplepipeline.map.base_map import Map, MultiMap


@ray.remote
def run(obj, *args, **kwargs):
    return obj.run_map(*args, **kwargs)


def par_map_(func, iterable, **kwargs):
    """
    Lot of overhead because of multiprocessing. Should only be used for processing intensive tasks.
    Args:
        func: Function to be executed
        iterable: Iterable to be looped over
        **kwargs: Arguments of the function
    Returns:
        Result of the function
    """
    ray.init()
    futures = [run.remote(func(), i, **kwargs) for i in iterable]
    results = ray.get(futures)
    ray.shutdown()
    return results


def par_map(func, iterable, **kwargs):
    return Map(partial(par_map_, func, iterable, **kwargs), func)


def par_map_unpack(func, iterable, **kwargs):
    """
    Used for funcs that return several values (or a tuple of values). Note that any return
    value is a list.
    """
    return MultiMap(par_map(func, iterable, **kwargs))
