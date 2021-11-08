from enum import IntEnum
from enum import Enum

from pygame.color import Color


class WinEventType(IntEnum):
    WET_NONE = 0
    WET_KEY = 1
    WET_MOUSE = 2
    WET_BTN = 3
    WET_FORM = 4


class KeySubEvent(IntEnum):
    KEY_NONE = 0
    KEY_PRESS = 1
    KEY_CHAR = 2


class MouseSubEvent(IntEnum):
    MOUSE_NONE = 0
    MOUSE_MOVE = 1
    MOUSE_DOWN = 2
    MOUSE_UP = 3
    MOUSE_WHEEL_UP = 3
    MOUSE_WHEEL_DOWN = 4
    MOUSE_DRAG = 5
    MOUSE_DROP = 6


class ButtonSubEvent(IntEnum):
    BTN_NONE = 0
    BTN_DOWN = 1
    BTN_UP = 2
    BTN_CLICK = 4


class FormSubEvent(IntEnum):
    FORM_NONE = 0
    FORM_CREATE = 1
    FORM_SHOW = 2
    FORM_HIDE = 3
    FORM_CLOSE = 4
    #FORM_RESIZE = 5


class DefaultColor(Enum):
    FORM_BACKGROUND: Color = Color('white')
    BORDER: Color = Color('darkgray')
    TEXT: Color = Color(0, 0, 0)  # black

    BTN_UP: Color = Color('darkgray')
    BTN_OVER: Color = Color('gray')
    BTN_DOWN: Color = Color('lightgray')

    # for Label
    TEXT_UP: Color = Color('darkblue')
    TEXT_OVER: Color = Color('blue')
    TEXT_DOWN: Color = Color('red')

    # for Edit
    EDIT_FOCUS_ON_BG: Color = Color('aliceblue')
    EDIT_FOCUS_OFF_BG: Color = Color('white')
    EDIT_FOCUS_ON_BD: Color = Color('black')
    EDIT_FOCUS_OFF_BD: Color = Color('gray')
    EDIT_FOCUS_ON_TEXT: Color = Color('black')
    EDIT_FOCUS_OFF_TEXT: Color = Color('darkgray')
    EDIT_CURSOR: Color = Color('black')


class MouseOverState(IntEnum):
    MOS_NONE = 0
    MOS_OVER = 1
    MOS_DOWN = 2


class DefaultFont:
    NAME: str = 'msyh.ttc'
    SIZE: int = 20


class DefaultParams(IntEnum):
    # for Frame
    FRAME_TITLE_HEIGHT: int = 32

    # for Edit
    EDIT_TEXT_EDGE: int = 3
    EDIT_CURSOR_THICKNESS: int = 1
