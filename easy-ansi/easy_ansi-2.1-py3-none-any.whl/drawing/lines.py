from enum import Enum
from easyansi.drawing.line_chars import LineChars
from easyansi.common import field_validations as _validator
from easyansi.core import cursor as cur

MIN_LENGTH = 1


class Lines(Enum):

    ASCII = LineChars.ASCII
    BLOCK = LineChars.BLOCK
    SINGLE = LineChars.SINGLE
    DOUBLE = LineChars.DOUBLE

    def __init__(self, char_set: LineChars):
        self._char_set = char_set

    def horizontal(self, length: int) -> str:
        """Return a line of horizontal characters.

        Parameters:
            length: The length of the line to draw.
        """
        _validator.check_int_minimum_value(length, MIN_LENGTH, "Horizontal Line Length")
        return self._char_set.horizontal * length

    def vertical(self, length: int) -> str:
        """Return a line of vertical characters.

        Parameters:
            length: The length of the line to draw.
        """
        _validator.check_int_minimum_value(length, MIN_LENGTH, "Vertical Line Length")
        return (self._char_set.vertical + cur.move(-1, 1)) * (length - 1) + self._char_set.vertical
