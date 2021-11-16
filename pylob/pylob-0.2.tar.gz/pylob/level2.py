from sortedcontainers import SortedDict

from pylob.statistics import Statistics
from pylob.output import L2Output


def neg(x: int) -> int:
    return -x


class Level2(Statistics, L2Output):
    def __init__(self, name, *, bids=[], asks=[]) -> None:
        self.name = name
        self._bids = SortedDict(neg)
        self._asks = SortedDict()
        self.tick_size = 1
        self.timestamp = 0

        self.set_snapshot(bids, asks)

    def set_tick_size(self, tick_size) -> None:
        self.tick_size = tick_size

    def set_snapshot(self, bids, asks, timestamp=0):
        """align the order book to a snapshot
        """
        for b in bids:
            self._bids[b[0]] = b[1]
        for a in asks:
            self._asks[a[0]] = a[1]
        self.timestamp = timestamp
