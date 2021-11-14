from typing import Tuple
from easyansi.core import core as _core
from easyansi.common import field_validations as _validator
import shutil

# screen size
DEFAULT_COLS = 80
DEFAULT_ROWS = 24

# clear screen
CLEAR_SCREEN = f"{_core.CSI}2J"
CLEAR = CLEAR_SCREEN
CLEAR_SCREEN_FWD = f"{_core.CSI}0J"
CLEAR_FWD = CLEAR_SCREEN_FWD
CLEAR_SCREEN_BWD = f"{_core.CSI}1J"
CLEAR_BWD = CLEAR_SCREEN_BWD

# clear row
CLEAR_ROW = f"{_core.CSI}2K"
CLEAR_ROW_FWD = f"{_core.CSI}0K"
CLEAR_ROW_BWD = f"{_core.CSI}1K"

# other
BELL = _core.BEL

# reset
RESET = _core.RESET


def size() -> Tuple[int, int]:
    """Return the screen size in (cols, rows).

    This is not an ANSI function, but uses python to retrieve this for you."""
    screen_size = shutil.get_terminal_size()
    return screen_size.columns, screen_size.lines


def sufficient_size(min_cols: int, min_rows: int) -> Tuple[bool, int, int]:
    """Given a minimum number of columns and rows, check that the screen is at least this size.
    Returns True / False if the size meets the minimums, followed by the current number of columns and rows.

    Parameters:
        min_cols: The minimum number of columns for the terminal size.
        min_rows: The minimum number of rows for the terminal size.
    """
    minimum_columns = 1
    minimum_rows = 1
    _validator.check_int_minimum_value(min_cols, minimum_columns, "Minimum number of columns")
    _validator.check_int_minimum_value(min_rows, minimum_rows, "Minimum number of rows")
    cols, rows = size()
    if (cols < min_cols) or (rows < min_rows):
        return False, cols, rows
    return True, cols, rows


def title(text: str, window: bool = True, icon: bool = True, alt: bool = False) -> str:
    """Given text, set the terminal window title.

    Parameters:
        text: The text to set the terminal window to.
        window: True/False if the window title should be set.
        icon: True/False if the window icon text should be set.
        alt: True/False: Generate an alternate code.  Try this if the terminal title is not changing.
    """
    _validator.check_if_string(text, "Screen title text")
    _validator.check_if_boolean(window, "Screen title window indicator")
    _validator.check_if_boolean(icon, "Screen title icon indicator")
    _validator.check_if_boolean(alt, "Screen title alternate code indicator")
    if (not window) and (not icon):
        _validator._raise_error("Screen title indicators", str(False),
                                "No title indicators set to be changed", ValueError)
    end_code = _core.BEL if alt else _core.ST
    operation = "0"
    if (not window) and icon:
        operation = "1"
    elif window and (not icon):
        operation = "2"
    return f"{_core.OSC}{operation};{text}{end_code}"
