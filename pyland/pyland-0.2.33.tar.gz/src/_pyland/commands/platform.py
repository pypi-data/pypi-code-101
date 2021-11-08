import argparse
import os
import json
from typing import List
from ..utils.file_reader import JsonReader


def platform(key, value):
    if key == "list":
        from pyland import list_case
        list_case(value)
    elif key == "import":
        from pyland import update_case
        update_case(value)
    elif key == "run":
        from pyland import run_case
        run_case(value)
    else:
        raise ValueError("only chose from {list, import, run}")


def is_json(val):
    try:
        json.loads(val)
    except ValueError:
        return False
    return True


def main(args: List[str]) -> bool:
    parser = argparse.ArgumentParser(prog='pyland platform')
    platOpt = parser.add_mutually_exclusive_group(required=True)
    platOpt.add_argument('--import', help='import cases to platform')
    platOpt.add_argument('--list', help='list cases to platform')
    platOpt.add_argument('--run', help='run cases with platform')

    parsed_args = parser.parse_args(args)
    key, value = [(k, v) for k, v in vars(parsed_args).items() if v][0]

    # capture error input
    try:
        if is_json(value):
            value = json.loads(value)
        else:
            if os.path.isfile(value):
                value = JsonReader(value).data
            else:
                raise FileNotFoundError
    except FileNotFoundError as e:
        return f"FileNotFoundError: {value} not found"
    except Exception as e:
        return f"JSONDecodeError: {e}"

    # call platform command with json input
    return platform(key=key, value=value)
