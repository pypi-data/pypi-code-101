import readline
import sys
import os

from os import path
from typing import Type, Callable

from .constant import ValueType
from .register import Register
from .utils import is_empty_str, convert_str_to_type
from .exception import ValidationError, MenuExitException


def ask(label: str,
        type_: Type[ValueType],
        default_value: ValueType,
        history_id: str,
        validator: Callable[[ValueType], bool]) -> ValueType:
    readline.set_completer(None)
    return input_(label, type_, default_value, history_id, validator)


def get_file_path(label: str, history_id: str, default_value: str, have_to_exist: bool):
    def my_completer(text: str, state: int):
        """
        auto-complete override function for the readline library.
        """
        # We replace the slash by the correct path separator depending on the platform.
        text = text.replace("/", path.sep)
        competing_folder, completing_file = path.split(text)
        working_path = path.join(os.getcwd(), competing_folder)
        try:
            results = [f for f in os.listdir(working_path) if f.startswith(completing_file) and not f.startswith(".")]
        except FileNotFoundError:
            results = []

        # If they are only 1 solution and the text completed is a folder ...
        if len(results) == 1 and path.isdir(path.join(os.getcwd(), completing_file)):
            # ... we add the path separator at the end.
            results = [path.join(competing_folder, completing_file, '')]
        else:
            # ... otherwise we re-merge the completing_folder part.
            results = [path.join(competing_folder, f) for f in results]
            # For each propositions ...
            for i, tmp in enumerate(results):
                if path.isdir(path.join(os.getcwd(), tmp)):
                    # ... we add a the path separator to the one which are folder.
                    results[i] = path.join(tmp, '')

        # The library require a list ending by None.
        # results.append(None)  # The code work even without
        return results[state]

    readline.parse_and_bind("tab: complete")
    readline.set_completer_delims('\n')
    readline.set_completer(my_completer)
    return input_(label, str, default_value, history_id, lambda s: True)


def input_(label: str,
           type_: Type[ValueType],
           default_value: ValueType,
           history_id: str,
           validator: Callable[[ValueType], bool]) -> ValueType:

    readline.clear_history()
    readline.set_startup_hook(lambda: readline.insert_text(str(default_value)))
    while True:
        print("\r", end="")
        sys.stdout.flush()
        sys.stderr.flush()
        last_value = ""
        if history_id is not None:
            for previous_value in Register.get("input_history", {}).get(history_id, []):
                readline.add_history(previous_value)
                last_value = previous_value
        result = input(label)
        if history_id is not None and result != last_value and not is_empty_str(result):
            Register["input_history"][history_id].append(result)
        try:
            res = convert_str_to_type(result, type_)
            if validator(res):
                return res
            else:
                print("The value isn't right", file=sys.stderr)
        except ValidationError as error:
            print(error, file=sys.stderr)


def display_menu(commands):
    for i, (name, command) in enumerate(commands.items()):
        print("[%3d]: %s" % (i, name))

    done = False
    while not done:
        try:
            result = input("Select the command (or 'exit' to exit program): ")
            result = result.upper()
            if result == "EXIT":
                raise MenuExitException
            result = int(result)
            if 0 <= result < len(commands):
                return commands[list(commands.keys())[result]]
            else:
                print(f"This command is not define. Please select one in the range [0-{len(commands) - 1}%d]",
                      sys.stderr)
        except EOFError:
            raise MenuExitException
        except ValueError:
            print("Use exit/quit/cancel or Ctrl-D to exit")
