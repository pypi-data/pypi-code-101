from enum import Enum
from typing import Dict

LINE_CHARS_KEYS = ("top_left", "top_right", "bottom_left", "bottom_right",
                   "center_cross", "left_cross", "right_cross", "top_cross", "bottom_cross",
                   "horizontal", "vertical",
                   "diagonal_fwd", "diagonal_bwd", "diagonal_cross")


class LineChars(Enum):

    ASCII = {"top_left": "+",
             "top_right": "+",
             "bottom_left": "+",
             "bottom_right": "+",
             "center_cross": "+",
             "left_cross": "+",
             "right_cross": "+",
             "top_cross": "+",
             "bottom_cross": "+",
             "horizontal": "-",
             "vertical": "|",
             "diagonal_fwd": "/",
             "diagonal_bwd": "\\",
             "diagonal_cross": "X"}

    BLOCK = {"top_left": "\u2588",
             "top_right": "\u2588",
             "bottom_left": "\u2588",
             "bottom_right": "\u2588",
             "center_cross": "\u2588",
             "left_cross": "\u2588",
             "right_cross": "\u2588",
             "top_cross": "\u2588",
             "bottom_cross": "\u2588",
             "horizontal": "\u2588",
             "vertical": "\u2588",
             "diagonal_fwd": "\u2588",
             "diagonal_bwd": "\u2588",
             "diagonal_cross": "\u2588"}

    SINGLE = {"top_left": "\u250C",
              "top_right": "\u2510",
              "bottom_left": "\u2514",
              "bottom_right": "\u2518",
              "center_cross": "\u253C",
              "left_cross": "\u251C",
              "right_cross": "\u2524",
              "top_cross": "\u252C",
              "bottom_cross": "\u2534",
              "horizontal": "\u2500",
              "vertical": "\u2502",
              "diagonal_fwd": "\u2571",
              "diagonal_bwd": "\u2572",
              "diagonal_cross": "\u2573"}

    DOUBLE = {"top_left": "\u2554",
              "top_right": "\u2557",
              "bottom_left": "\u255A",
              "bottom_right": "\u255D",
              "center_cross": "\u256C",
              "left_cross": "\u2560",
              "right_cross": "\u2563",
              "top_cross": "\u2566",
              "bottom_cross": "\u2569",
              "horizontal": "\u2550",
              "vertical": "\u2551",
              "diagonal_fwd": "\u2571",
              "diagonal_bwd": "\u2572",
              "diagonal_cross": "\u2573"}

    def __init__(self, char_set: Dict[str, str]):
        self._char_set = char_set

    @property
    def all_chars(self) -> Dict[str, str]:
        """Returns the full character dictionary."""
        return self._char_set

    @property
    def top_left(self) -> str:
        """Return the top left corner character."""
        return self._char_set["top_left"]

    @property
    def top_right(self) -> str:
        """Return the top right corner character."""
        return self._char_set["top_right"]

    @property
    def bottom_left(self) -> str:
        """Return the bottom left corner character."""
        return self._char_set["bottom_left"]

    @property
    def bottom_right(self) -> str:
        """Return the bottom right corner character."""
        return self._char_set["bottom_right"]

    @property
    def center_cross(self) -> str:
        """Return the intersection of horizontal and vertical character."""
        return self._char_set["center_cross"]

    @property
    def left_cross(self) -> str:
        """Return the intersection of the left side and horizontal character."""
        return self._char_set["left_cross"]

    @property
    def right_cross(self) -> str:
        """Return the intersection of the horizontal and right side character."""
        return self._char_set["right_cross"]

    @property
    def top_cross(self) -> str:
        """Return the intersection of the top side and vertical character."""
        return self._char_set["top_cross"]

    @property
    def bottom_cross(self) -> str:
        """Return the intersection of the vertical and bottom side character."""
        return self._char_set["bottom_cross"]

    @property
    def horizontal(self) -> str:
        """Return the horizontal character."""
        return self._char_set["horizontal"]

    @property
    def vertical(self) -> str:
        """Return the vertical character."""
        return self._char_set["vertical"]

    @property
    def diagonal_fwd(self) -> str:
        """Return a 'forward slash' (/) character."""
        return self._char_set["diagonal_fwd"]

    @property
    def diagonal_bwd(self) -> str:
        """Return a 'backward slash' (\\) character."""
        return self._char_set["diagonal_bwd"]

    @property
    def diagonal_cross(self) -> str:
        """Return the intersection of a 'forward slash' and 'backward slash' (X) character."""
        return self._char_set["diagonal_cross"]
