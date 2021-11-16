# -*- coding: utf-8 -*-
"""utilities that would clutter the main file"""
from pathlib import Path
import sys
from typing import Union

from rich import print


def check_dir(dir_path: Path) -> bool:
    """Checks if a directory exists and has files

    Args:
        dir_path: The directory to check for runnable scripts

    Returns:
        bool: True for success, False otherwise
    """
    if not dir_path.exists() or is_empty(dir_path):
        dir_path.mkdir(parents=True, exist_ok=True)
        return False
    return True


def clean_input(prompt: str) -> str:
    """Returns user input to a prompt, casefolded and stripped of whitespace

    Args:
        prompt: The prompt to display to the user

    Returns:
        str: The user's input to the prompt
    """
    return input(prompt).casefold().strip()


def confirm(prompt: str = None) -> bool:
    """Confirms a choice made by the user

    Args:
        prompt: The prompt to display to the user (default is None)

    Returns:
        bool: True if the user entered 'y' or 'yes', False otherwise
    """
    if not prompt:
        prompt = "Does this information look correct? [Y/n] "
    return clean_input(prompt) in ("y", "yes")


def is_empty(path: Path) -> bool:
    """Checks if a directory has files

    Args:
        path: The path to the directory to check

    Returns:
        bool: True if the dir is empty, False if it contains any files
    """
    return not any(path.iterdir())


def print_error(msg: Union[str, Exception], header: str = "ERR") -> None:
    """Prints a message to stderr

    Args:
        msg: The message to print to stderr
        header: The string to print before the actual message
    """
    if header == "ERR":
        msg = f"[red][{header}][/red] {msg}"
    else:
        msg = f"[orange1][{header}][/orange1] {msg}"
    print(msg, file=sys.stderr)
