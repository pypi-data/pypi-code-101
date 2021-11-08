"""Command line options."""
import os
import sys
import py
import argparse
from typing import Any, Optional, Sequence, Union, List
from importlib_metadata import entry_points
import requests
import colorama
import http
import json
import pyland
from importlib_metadata import version

args = argparse.Namespace()


def main(argv: Optional[Union[py.path.local, List[str]]] = None) -> Any:
    if argv is None:
        argv = sys.argv[1:]
    elif isinstance(argv, py.path.local):
        argv = [str(argv)]
    elif not isinstance(argv, list):
        msg = "`argv` parameter expected to be a list of strings, got: {!r} (type: {})"
        raise TypeError(msg.format(argv, type(argv)))

    try:
        result = dispatch(argv)
    except requests.HTTPError as exc:
        status_code = exc.response.status_code
        status_phrase = http.HTTPStatus(status_code).phrase
        result = (
            f"{exc.__class__.__name__}: {status_code} {status_phrase} "
            f"from {exc.response.url}\n"
            f"{exc.response.reason}"
        )
    except pyland.exceptions.PylandException as exc:
        result = f"{exc.__class__.__name__}: {exc.args[0]}"

    return _format_error(result) if isinstance(result, str) else result


def console_main() -> int:
    """The CLI entry point of pyland.

    This function is not meant for programmable use; use `main()` instead.
    """
    # https://docs.python.org/3/library/signal.html#note-on-sigpipe
    try:
        code = main()
        sys.stdout.flush()
        return code
    except BrokenPipeError:
        # Python flushes standard streams on exit; redirect remaining output
        # to devnull to avoid another BrokenPipeError at shutdown
        devnull = os.open(os.devnull, os.O_WRONLY)
        os.dup2(devnull, sys.stdout.fileno())
        return 1  # Python exits with error code 1 on EPIPE


def dispatch(argv: List[str]) -> Any:
    registered_commands = entry_points(group="pyland.registered_commands")
    parser = argparse.ArgumentParser(prog="pyland")
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s version {} ".format(pyland.__version__),
    )
    parser.add_argument(
        "--no-color",
        default=False,
        required=False,
        action="store_true",
        help="disable colored output",
    )
    parser.add_argument(
        "command",
        choices=registered_commands.names,
    )
    parser.add_argument(
        "args",
        help=argparse.SUPPRESS,
        nargs=argparse.REMAINDER,
    )

    parser.parse_args(argv, namespace=args)

    main = registered_commands[args.command].load()

    return main(args.args)


class EnvironmentDefault(argparse.Action):
    """Get values from environment variable."""

    def __init__(
            self,
            env: str,
            required: bool = True,
            default: Optional[str] = None,
            **kwargs: Any,
    ) -> None:
        default = os.environ.get(env, default)
        self.env = env
        if default:
            required = False
        super().__init__(default=default, required=required, **kwargs)

    def __call__(
            self,
            parser: argparse.ArgumentParser,
            namespace: argparse.Namespace,
            values: Union[str, Sequence[Any], None],
            option_string: Optional[str] = None,
    ) -> None:
        setattr(namespace, self.dest, values)


class EnvironmentFlag(argparse.Action):
    """Set boolean flag from environment variable."""

    def __init__(self, env: str, **kwargs: Any) -> None:
        default = self.bool_from_env(os.environ.get(env))
        self.env = env
        super().__init__(default=default, nargs=0, **kwargs)

    def __call__(
            self,
            parser: argparse.ArgumentParser,
            namespace: argparse.Namespace,
            values: Union[str, Sequence[Any], None],
            option_string: Optional[str] = None,
    ) -> None:
        setattr(namespace, self.dest, True)

    @staticmethod
    def bool_from_env(val: Optional[str]) -> bool:
        """Allow '0' and 'false' and 'no' to be False."""
        falsey = {"0", "false", "no"}
        return bool(val and val.lower() not in falsey)


def _format_error(message: str) -> str:
    pre_style, post_style = "", ""
    if not args.no_color:
        colorama.init()
        pre_style, post_style = colorama.Fore.RED, colorama.Style.RESET_ALL

    return f"{pre_style}{message}{post_style}"
