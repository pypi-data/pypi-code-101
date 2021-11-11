import collections
import functools
import inspect
import os
from typing import Any, Dict, Tuple

from typer import Option
from typer.models import OptionInfo


def add_options(options: Dict[str, Tuple[Any, OptionInfo]]):
    """Decorator to add Options to a particular command."""

    def decorator(wrapped):
        # Ensure that the function signature has the correct typer.Option defaults,
        # so that every command need not specify them
        wrapped_sig = inspect.signature(wrapped)
        params = collections.OrderedDict(wrapped_sig.parameters)

        for key, value in options.items():
            annotation, option = value

            params[key] = inspect.Parameter(
                key, inspect.Parameter.POSITIONAL_OR_KEYWORD, default=option, annotation=annotation
            )
        if "kwargs" in params:
            del params["kwargs"]
        sig = wrapped_sig.replace(parameters=list(params.values()))

        @functools.wraps(wrapped)
        def wrap_function(*args, **kwargs):
            return wrapped(*args, **kwargs)

        wrap_function.__signature__ = sig
        return wrap_function

    return decorator


_dagit_url = lambda: os.getenv("DAGSTER_CLOUD_DAGIT_URL")


def _api_token():
    return os.getenv("DAGSTER_CLOUD_API_TOKEN")


def _show_api_token_prompt():
    password_exists = bool(_api_token())
    show_prompt = not password_exists
    return show_prompt


def _show_dagit_url_prompt():
    url_exists = bool(_dagit_url())
    return (
        "Your Dagster Cloud url, in the form of 'https://{ORGANIZATION_NAME}.dagster.cloud/{DEPLOYMENT_NAME}'"
        if not url_exists
        else False
    )


CLOUD_DAGIT_CLIENT_OPTIONS = {
    "url": (
        str,
        Option(
            _dagit_url,
            "--url",
            prompt=_show_dagit_url_prompt(),
            help="Your Dagster Cloud url, in the form of 'https://{ORGANIZATION_NAME}.dagster.cloud/{DEPLOYMENT_NAME}'.",
        ),
    ),
    "api_token": (
        str,
        Option(
            _api_token,
            "--api-token",
            prompt=_show_api_token_prompt(),
            hide_input=True,
            help="API token generated in Dagit",
        ),
    ),
}
