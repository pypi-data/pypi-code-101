"""
Custom Containers for Metric results
"""
from numbers import Real
from typing import NamedTuple


class AverageElement(NamedTuple):
    """
    Represents an element of an averageable Value
    Enables calculating incremental average (mean) values
    """
    sum: Real
    no_of_elements: int = 1

    def __add__(self, other):
        if isinstance(other, AverageElement):
            return AverageElement(self.sum + other.sum, self.no_of_elements + other.no_of_elements)
        if not other:
            return self
        else:
            raise TypeError

    def avg(self) -> float:
        """
        calculates the concrete value

        @return: the concrete float value of the average
        """
        return self.sum * 1.0 / self.no_of_elements

    def __float__(self):
        return self.avg()


AVERAGE_NEUTRAL: AverageElement = AverageElement(0, 0)
"""Neutral element of average element addition"""
