# system modules
import logging
import re

# internal modules
from openrepos.client import Client

# external modules
import click
from xvfbwrapper import Xvfb

logger = logging.getLogger(__name__)


@click.group(
    help="OpenRepos.net web client",
    context_settings={
        "help_option_names": ["-h", "--help"],
        "auto_envvar_prefix": "OPENREPOS",
    },
    chain=True,
    invoke_without_command=True,
)
@click.option(
    "-v",
    "--verbose",
    "verbosity",
    help="increase the loglevel. "
    "Specifying this option more than 3 times "
    "enables all log messages. More than 4 times doesn't limit "
    "logging to only this package.",
    show_envvar=True,
    count=True,
)
@click.option(
    "-q",
    "--quiet",
    "quietness",
    help="decrease the loglevel",
    show_envvar=True,
    count=True,
)
@click.option(
    "-u",
    "--username",
    metavar="USERNAME",
    help="OpenRepos.net username",
    show_envvar=True,
)
@click.option(
    "-p",
    "--password",
    metavar="PASSWORD",
    help="OpenRepos.net password",
    show_envvar=True,
)
@click.option(
    "--xvfb/--no-xvfb",
    "use_xvfb",
    help="Whether to execute Xvfb",
    show_envvar=True,
)
@click.option(
    "-i/--interactive", "interactive", is_flag=True, help="Ask before "
)
@click.option(
    "-w",
    "--webdriver",
    help="Which selenium WebDriver to use",
    default=next(Client.matching_webdriver(), ("?", None))[0],
    show_default=True,
    show_envvar=True,
)
@click.version_option(help="show version and exit")
@click.pass_context
def cli(
    ctx,
    quietness,
    verbosity,
    username,
    password,
    use_xvfb,
    webdriver,
    interactive,
):
    # set up logging
    loglevel_choices = dict(
        enumerate(
            (
                logging.CRITICAL + 1,
                logging.CRITICAL,
                logging.WARNING,
                logging.INFO,
                logging.DEBUG,
            ),
            -2,
        )
    )
    loglevel = loglevel_choices.get(
        min(
            max(loglevel_choices),
            max(min(loglevel_choices), verbosity - quietness),
        )
    )
    logging.basicConfig(
        level=loglevel,
        format="[%(asctime)s] %(levelname)-8s"
        + (" (%(name)s)" if verbosity >= 3 else "")
        + " %(message)s",
    )
    for n, l in logger.manager.loggerDict.items():
        if (
            not re.match(
                r"openrepos\." if verbosity >= 3 else r"openrepos.cli(?!\w)", n
            )
            and not verbosity > 4
        ):
            l.propagate = False
            if hasattr(l, "setLevel"):
                l.setLevel(logging.CRITICAL + 1)
    ctx.ensure_object(dict)
    if use_xvfb:
        xvfb = Xvfb()
        logger.info("Starting Xvfb...")
        xvfb.start()
        logger.debug("Xvfb is running")

        def stop_xvfb():
            logger.info("Stopping Xvfb...")
            xvfb.stop()
            logger.debug("Xvfb stopped")

        ctx.obj["xvfb"] = xvfb
    client = Client(
        username=username, password=password, interactive=interactive
    )
    ctx.obj["client"] = client
    # explicitly cause the webdriver to be loaded
    logger.info("Opening the webdriver")
    client.webdriver
    # proper teardown order: webdriver needs to be closed before Xvfb
    ctx.call_on_close(client.close)
    if use_xvfb:
        ctx.call_on_close(stop_xvfb)
