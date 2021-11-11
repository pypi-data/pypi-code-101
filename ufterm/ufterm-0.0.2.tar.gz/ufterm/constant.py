from typing import Union, Tuple, Callable, TypeVar, Type
from enum import Enum


ValueType = TypeVar('ValueType', str, int, float, bool)
InputDef = Union[Tuple[str, Type[ValueType]],
                 Tuple[str, Type[ValueType], ValueType],
                 Tuple[str, Type[ValueType], ValueType, Callable[[ValueType], bool]]]
FormInputDefTuple = InputDef[Union[str, int, float, bool]]


class MsgType(Enum):
    INFO = 1
    WARNING = 2
    ERROR = 3
# Reassign the enum variable to for more convenient naming
INFO_MSG = MsgType.INFO
WARNING_MSG = MsgType.WARNING
ERROR_MSG = MsgType.ERROR

CMD_ASK = "ask"
CMD_SHOW = "show"
CMD_SHOW_ERR = "show_err"

PROGRAM_FINISH = 'program_stopped'
GUI_MAINLOOP_STARTED = 'mainloop_started'
GUI_MAINLOOP_FINISH = 'mainloop_finish'

