from collections import deque
from typing import Optional, Callable
from highwire.signals import Sampler, Tick
from highwire.variables import X
from highwire.events import project, Event


class MovingAverage(Sampler[X]):
    _current: Optional[X]

    def __init__(self, n: int, fn: Callable[[], Optional[X]]):
        super().__init__()
        self._n = n
        self._buffer: deque = deque(maxlen=n)
        self._current = None
        self._fn: Callable[[], Optional[X]] = fn

    def sample(self, tick: Tick) -> None:
        val = self._fn()
        if val is not None:
            self._buffer.append(val)

        if len(self._buffer) == self._n:
            self._current = sum(self._buffer) / self._n  # type: ignore
            event: Event[X] = project(tick, lambda _: self._current)  # type: ignore
            self._notify(event)  # pylint: disable=no-member

    def get(self) -> Optional[X]:
        return self._current
