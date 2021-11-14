from typing import Tuple, Optional
from easyansi.core import core as _core
from easyansi.common import field_validations as _validator
import sys
_WINDOWS = False
try:
    import tty
    import termios
except ModuleNotFoundError:
    import msvcrt
    _WINDOWS = True

MIN_MOVEMENT = 1
MIN_COL = 0
MIN_ROW = 0


def up(rows: int = 1) -> str:
    """Given a number of rows, move the cursor up."""
    _validator.check_int_minimum_value(rows, MIN_MOVEMENT, "Cursor up row count")
    return f"{_core.CSI}{rows}A"


def down(rows: int = 1) -> str:
    """Given a number of rows, move the cursor down."""
    _validator.check_int_minimum_value(rows, MIN_MOVEMENT, "Cursor down row count")
    return f"{_core.CSI}{rows}B"


def left(cols: int = 1) -> str:
    """Given a number of columns, move the cursor left."""
    _validator.check_int_minimum_value(cols, MIN_MOVEMENT, "Cursor left column count")
    return f"{_core.CSI}{cols}D"


def right(cols: int = 1) -> str:
    """Given a number of columns, move the cursor right."""
    _validator.check_int_minimum_value(cols, MIN_MOVEMENT, "Cursor right column count")
    return f"{_core.CSI}{cols}C"


def move(cols: Optional[int] = None, rows: Optional[int] = None) -> str:
    """Given a number of columns and/or rows, move the cursor relative to its current position.
    If a value is zero, this is the same as setting it to None.

    Parameters:
        cols: Negative number = left movement, Positive number = right movement
        rows: Negative number = up movement, Positive number = down movement
    """
    _validator.check_if_any_have_value("Cursor move values", cols, rows, zero_int_no_value=True)
    move_code = ""
    if cols is not None:
        if isinstance(cols, int):
            if cols < 0:
                move_code += left(cols * -1)
            elif cols > 0:
                move_code += right(cols)
            # else:
                # if cols == 0, skip left/right code like it was None
        else:
            # let the right() function throw an error
            right(cols)
    if rows is not None:
        if isinstance(rows, int):
            if rows < 0:
                move_code += up(rows * -1)
            elif rows > 0:
                move_code += down(rows)
            # else:
                # if rows == 0, skip up/down code like it was None
        else:
            # let the down() function throw an error
            move_code += down(rows)
    return move_code


def next_line(rows: int = 1) -> str:
    """Given a number of rows, move cursor down and to the first column."""
    _validator.check_int_minimum_value(rows, MIN_MOVEMENT, "Cursor next line row count")
    return f"{_core.CSI}{rows}E"


def previous_line(rows: int = 1) -> str:
    """Given a number of rows, move cursor up and to the first column."""
    _validator.check_int_minimum_value(rows, MIN_MOVEMENT, "Cursor previous line row count")
    return f"{_core.CSI}{rows}F"


def locate(col: int, row: int) -> str:
    """Given a column and row, move the cursor to this location."""
    _validator.check_int_minimum_value(col, MIN_COL, "Cursor locate column value")
    _validator.check_int_minimum_value(row, MIN_ROW, "Cursor locate row value")
    return f"{_core.CSI}{row + 1};{col + 1}H"


def locate_col(col: int) -> str:
    """Given a column, move the cursor to this column on the current row."""
    _validator.check_int_minimum_value(col, MIN_COL, "Cursor locate_col column value")
    return f"{_core.CSI}{col + 1}G"


def position() -> Tuple[int, int]:
    """Return the col, row coordinates of the cursor."""
    response = _get_position_response()
    loc = response.split(";")
    col = int(loc[1]) - 1
    row = int(loc[0]) - 1
    return col, row


def _get_position_response() -> str:
    """Make the actual ANSI call for the cursor position.
    This code is separated out to make it easy to mock in unit tests."""
    from easyansi.core import utils
    response = ""
    utils.prnt(f"{_core.CSI}6n")  # Send ANSI request for cursor location
    if _WINDOWS:
        while msvcrt.kbhit():  # type: ignore
            char_in = msvcrt.getch()  # type: ignore
            response += char_in.decode("utf-8")
        response = response[2:-1]  # We do not need the first 2 bytes or the last byte
    else:
        f = sys.stdin.fileno()
        terminal_settings = termios.tcgetattr(f)  # Save terminal settings
        try:
            tty.setraw(f)
            sys.stdin.read(2)  # We do not need the first 2 bytes
            char_in = sys.stdin.read(1)
            while char_in != "R":  # R will be the last character of the ANSI response, and we don't need it
                response += char_in
                char_in = sys.stdin.read(1)  # Read a single character
        finally:
            termios.tcsetattr(f, termios.TCSADRAIN, terminal_settings)  # Restore terminal settings
    return response


###########################################################################
# Convenience Constants
###########################################################################

UP = up(1)
DOWN = down(1)
LEFT = left(1)
RIGHT = right(1)

NEXT_LINE = next_line(1)
PREVIOUS_LINE = previous_line(1)

HOME = locate(0, 0)
HOME_ON_SCREEN = HOME
HOME_ON_ROW = locate_col(0)

HIDE = f"{_core.CSI}?25l"
HIDE_ON = HIDE
SHOW = f"{_core.CSI}?25h"
SHOW_ON = SHOW
HIDE_OFF = SHOW
SHOW_OFF = HIDE
