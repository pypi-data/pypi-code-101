from functools import partial

from tqdm import tqdm

from simplepipeline.map.base_map import Map, MultiMap


def seq_map_(func, iterable, **kwargs):
    """
        Args:
        func: Function to be executed
        iterable: Iterable to be looped over
        **kwargs: Arguments of the function
    Returns:
        Result of the function
    """
    return [func().run_map(x, **kwargs) for x in tqdm(iterable)]


def seq_map(func, iterable, **kwargs):
    return Map(partial(seq_map_, func, iterable, **kwargs), func)


def seq_map_unpack(func, iterable, **kwargs):
    """
    Used for funcs that return several values (or a tuple of values). Note that any return
    value is a list.
    """
    return MultiMap(seq_map(func, iterable, **kwargs))
