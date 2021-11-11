import atexit
import sys
import textwrap

from os import path
from datetime import datetime
from typing import Tuple, Callable, Type

from .register import Register
from .exception import *
from .utils import convert_str_to_type, is_empty_str, get_digit_number
from .constant import ValueType, InputDef, FormInputDefTuple, MsgType, INFO_MSG, WARNING_MSG, ERROR_MSG
from . import gui, terminal


__all__ = ["INFO_MSG", "WARNING_MSG", "ERROR_MSG",
           "show", "ask", "form", "get_file_path",
           "done", "is_done",
           "add_command", "run_command",
           "start_gui",
           "init_register"]


_g_commands = {}
_g_selected_command = None
_g_done = False
_g_started = False


def show(text: str, msg_type: MsgType = MsgType.INFO):
    """
    Display a message to the user.
    The warning and error message are display on the error output with the terminal.py mode.

    :param      text:  Message to display
    :param  msg_type:  Type of message. The warning will be orange and error red.
    """
    text = textwrap.indent(text, '           ')
    text = text.replace('          ', datetime.now().strftime('[%H:%M:%S]'), 1)

    if gui.is_started():
        gui.show(text, msg_type.name)
    else:
        if msg_type != INFO_MSG:
            print(text, file=sys.stderr)
        else:
            print(text)


def _get_default_default_value(type_: Type[ValueType]) -> ValueType:
    if type_ is int:
        return 0
    elif type_ is float:
        return 0.
    elif type_ is bool:
        return False
    elif type_ is str:
        return ""
    raise TypeError("Unsupported type")


def ask(label: str = "",
        history_id: str = None,
        type_: Type[ValueType] = str,
        default_value: ValueType = None,
        validator: Callable[[ValueType], bool] = lambda s: True) -> ValueType:
    """
    Ask users to enter some data. Then convert and check the value before returning it.

    :param          label:  The prompt (text displayed right before the area where the user is going write).
    :param     history_id:  Optional id to record values entered to create a history.
    :param          type_:  The type of the value that have to be converted to.
    :param  default_value:  Optional pre-set value inside the area where the user enter the data
                            (This only work on Linux terminal.py and GUI interface)
    :param      validator:  Function that will validate the data entered

    :return: The value entered by the user checked and converted to the right type.
    """
    if default_value is None:
        default_value = _get_default_default_value(type_)
    if gui.is_started():
        return gui.ask(label, history_id, type_, default_value, validator)
    else:
        return terminal.ask(label, type_, default_value, history_id, validator)


def get_file_path(label: str = "Please select the file path: ",
                  history_id: str = None,
                  default_value: str = "",
                  have_to_exist: bool = False):
    """
    Ask users to select a file path. The function can check if the file exist before returning.

    :param          label:  The prompt (text displayed right before the area where the user is going write).
    :param     history_id:  Optional id to record values entered to create a history.
    :param  default_value:  Optional pre-set value inside the area where the user enter the data
                            (This only work on Linux terminal.py and GUI interface)
    :param  have_to_exist:  Define if the file have to exist or not.

    :return:  The file path as a string.
    """
    if gui.is_started():
        result = gui.get_file_path(label, history_id, default_value, have_to_exist)
    else:
        result = terminal.get_file_path(label, history_id, default_value, have_to_exist)

    if have_to_exist:
        if not path.isfile(result):
            print("The file '%s' doesn't exist" % result, file=sys.stderr)
            return get_file_path(label, history_id, result, have_to_exist)
    return result


def _enumerate_input_def(form_definition, form_id):
    def generate_input_label(pos):
        return "%s_input_%0*d" % (form_id, number_of_zero, pos)

    number_of_zero = get_digit_number(len(form_definition))

    for i, input_definition in enumerate(form_definition):
        default = input_definition[2] if len(input_definition) >= 3 else None
        validator = input_definition[3] if len(input_definition) == 4 else lambda s: True
        yield input_definition[0], generate_input_label(i + 1), input_definition[1], default, validator


def form(form_definition: Tuple[FormInputDefTuple, ...], form_history_id: str = None) -> Tuple[ValueType, ...]:
    """
    Ask users to enter multiple values.

    :param  form_definition:  See the input_ parameter definition.
                              The only parameter to omit is the history_id.
    :param  form_history_id:  Optional id to record values entered to create a history.

    :return:
    """
    result = []
    for label, input_id, type_, default, validator in _enumerate_input_def(form_definition, form_history_id):
        result.append(ask(label, input_id, type_, default, validator))

    return tuple(result)


def done():
    """
    Set the program as done. That mean it is going to stop at the next loop
    """
    global _g_done
    _g_done = True


def is_done():
    """
    :return:  The value to know if the current program is finish or not
    """
    return _g_done


def is_started():
    """
    :return:  The value to know if the current program is already started or not
    """
    return _g_started


def reset():
    """
    Reset the module to its original state
    """
    global _g_commands
    global _g_selected_command
    global _g_done
    global _g_started

    _g_commands = {}
    _g_selected_command = None
    _g_done = False
    _g_started = False

def add_command(command: callable, custom_name: str = None):
    """
    Add a command to the module.

    :param      command:  Command to be add to the choice
    :param  custom_name:
    """
    global _g_commands

    if is_started():
        raise RuntimeError("The program was already started")
    if command in _g_commands.values():
        raise CommandAlreadyPresentError(command.__name__)
    if custom_name is None:
        custom_name = command.__name__
    if custom_name in _g_commands:
        raise CommandNameAlreadyUsedError(custom_name)
    _g_commands[custom_name] = command


def run_command():
    global _g_commands
    global _g_selected_command

    if len(_g_commands) == 1:
        _g_selected_command = _g_commands[list(_g_commands.keys())[0]]
    if _g_selected_command is None:
        raise NoCommandSelectedError()
    _g_selected_command()


def loop():
    global _g_started
    global _g_commands
    global _g_selected_command

    _g_started = True
    if len(_g_commands) == 1:
        _g_selected_command = _g_commands[list(_g_commands.keys())[0]]
    while not is_done():
        if _g_selected_command is None:
            try:
                display_menu()
            except MenuExitException:
                done()
                break
        else:
            _g_selected_command()
            _g_selected_command = None


def display_menu():
    global _g_selected_command

    if gui.is_started():
        _g_selected_command = gui.display_menu(_g_commands)
    else:
        _g_selected_command = terminal.display_menu(_g_commands)


def start_gui(title: str):
    """
    start a graphical interface in a back process for the user to interact with

    :param title:
    :return:
    """
    gui.start(title)


def init_register(file_name: str):
    def commit_at_exit():
        Register.commit()
        Register.wait_commit_to_finish()
    Register.record_in_file(file_name)
    atexit.register(commit_at_exit)
