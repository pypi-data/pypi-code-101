__version__ = "1.0.0"

from .functional import dic_del, dic_get, dic_has, dic_merge, dic_set, dic_walk
from .wrapper import DictBelt

__all__ = [
    "dic_del",
    "dic_get",
    "dic_has",
    "dic_merge",
    "dic_set",
    "dic_walk",
    "DictBelt",
]
