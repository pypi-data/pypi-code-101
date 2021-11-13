import abc
import numpy as np


class BaseFit(np.ndarray, metaclass=abc.ABCMeta):
    def __new__(cls, kind, x, y, **kwargs):
        x = np.asarray(x, order="F")
        y = np.asarray(y, order="F")

        obj = np.asarray(cls._fit(x, y, **kwargs)).view(cls)

        obj.kind = kind

        return obj

    def __array_finalize__(self, obj):
        if obj is None:
            return

        self.kind = getattr(obj, "kind", None)

    @staticmethod
    @abc.abstractmethod
    def _fit(x, y, **kwargs):
        return []
