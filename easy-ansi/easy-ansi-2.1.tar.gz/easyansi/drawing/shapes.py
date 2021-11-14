from enum import Enum
from easyansi.drawing.line_chars import LineChars
from easyansi.drawing.lines import Lines
from easyansi.common import field_validations as _validator
from easyansi.core import cursor as cur

MIN_WIDTH = 2
MIN_HEIGHT = 2


class Shapes(Enum):

    ASCII = (LineChars.ASCII, Lines.ASCII)
    BLOCK = (LineChars.BLOCK, Lines.BLOCK)
    SINGLE = (LineChars.SINGLE, Lines.SINGLE)
    DOUBLE = (LineChars.DOUBLE, Lines.DOUBLE)

    def __init__(self, char_set: LineChars, line_set: Lines):
        self._char_set = char_set
        self._line_set = line_set

    def rectangle(self, width: int, height: int) -> str:
        """Given a width and height, draw a rectangle.

        Parameters:
            width: The width of the box to draw.
            height: The height of the box to draw.
            """
        _validator.check_int_minimum_value(width, MIN_WIDTH, "Rectangle Width")
        _validator.check_int_minimum_value(height, MIN_HEIGHT, "Rectangle Height")
        between_top_corners = width - 2
        between_side_corners = height - 2
        # Top left corner
        rect = self._char_set.top_left
        # Top side
        if between_top_corners > 0:
            rect += self._line_set.horizontal(between_top_corners)
        # Top right corner
        rect += self._char_set.top_right
        rect += cur.move(-width, 1)
        if between_side_corners > 0:
            # Left side
            rect += self._line_set.vertical(between_side_corners)
            rect += cur.move(between_top_corners, -(between_side_corners - 1))
            # Right side
            rect += self._line_set.vertical(between_side_corners)
            rect += cur.move(-width, 1)
        # Bottom left corner
        rect += self._char_set.bottom_left
        # Bottom side
        if between_top_corners > 0:
            rect += self._line_set.horizontal(between_top_corners)
        # Bottom right corner
        rect += self._char_set.bottom_right
        return rect

    def square(self, size: int) -> str:
        """Given a size, draw a square.
        This is a convenience method that calls rectangle with the same width and height.

        Parameters:
            size: The width and height of the square.
        """
        return self.rectangle(size, size)
