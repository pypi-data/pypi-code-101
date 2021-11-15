from typing import Callable, Dict, List, Optional, TypeVar

import click
import inquirer

from sym.flow.cli.errors import InvalidChoiceError

KeyT = TypeVar("KeyT")
ValueT = TypeVar("ValueT")


def filter_dict(
    d: Dict[KeyT, ValueT], filter_func: Callable[[ValueT], bool]
) -> Dict[KeyT, ValueT]:
    return {k: v for k, v in d.items() if filter_func(v)}


def get_or_prompt(value: Optional[str], prompt: str, choices: List[str]) -> str:
    sorted_choices = sorted(choices)
    if not value and len(choices) == 1:
        click.echo(f"{prompt}: Using '{choices[0]}'")
        return choices[0]
    elif not value:
        return inquirer.list_input(prompt, choices=sorted_choices)
    elif value not in choices:
        raise InvalidChoiceError(value=value, valid_choices=sorted_choices)

    return value
