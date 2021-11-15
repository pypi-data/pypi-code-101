import webbrowser

import click

from sym.flow.cli.helpers.api import SymAPI


def slack_new(api_url, service_id: str) -> None:
    """Generate a magic link to install the Sym Slack App. This link
    can be opened directly or sent to an administrator with permission to
    install the app into your workspace.
    """

    url = get_magic_url(api_url=api_url, service_id=service_id)
    click.echo("Generated an installation link for the Sym Slack App:\n")
    click.secho(url, fg="white", bold=True)
    click.echo(
        "\nPlease send this URL to an administrator who has permission to install the app.\nOr, if that's you, we can open it now."
    )
    if click.confirm(
        "\nWould you like to open the Slack installation URL in a browser window?",
        default=True,
    ):
        webbrowser.open(url)


def get_magic_url(api_url: str, service_id: str):
    return SymAPI(url=api_url).get_slack_install_url(service_id)
