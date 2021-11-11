from typing import List

import typer
from dagster_cloud.api.client import create_cloud_dagit_client
from typer import Option, Typer

from ...cli.utils import CLOUD_DAGIT_CLIENT_OPTIONS, add_options

app = Typer(help="Customize your login settings.")


SET_ALLOWLISTED_DOMAINS_MUTATION = """
    mutation ($allowlistedDomains: [String!]) {
        setAllowlistedDomains(allowlistedDomains: $allowlistedDomains) {
            __typename
            ... on DagsterCloudOrganization {
                name
                allowlistedDomains
            }
            ... on PythonError {
                message
                stack
            }
        }
    }
    """


@app.command(name="set-allowlisted-domains")
@add_options(CLOUD_DAGIT_CLIENT_OPTIONS)
def set_allowlisted_domains_command(
    url: str, api_token: str, domains: List[str] = Option(..., "--domain", "-d")
):
    """
    Configures an organization's allowed domains.

    After running this command, only new users with email addresses from the allowed domains will be
    able to authenticate into their organization's Dagster Cloud instance.

    If a user does not already have a Dagster Cloud account, but their email matches one of the
    allowed domains, an account is created on their behalf.
    """
    client = create_cloud_dagit_client(url, api_token)

    response = client.execute(
        SET_ALLOWLISTED_DOMAINS_MUTATION,
        variable_values={"allowlistedDomains": domains},
    )

    if response["data"]["setAllowlistedDomains"]["__typename"] == "DagsterCloudOrganization":
        typer.echo(
            "Organization '{organization_name}' now has its allowlisted domains set to {domains}. "
            "Only users with email addresses from the allowed domains will be able to log into their "
            "organization's Dagster Cloud instance.".format(
                organization_name=response["data"]["setAllowlistedDomains"]["name"],
                domains=domains,
            )
        )
    else:
        typer.echo(f"Error adding domains to allowlist: {response}")
        raise typer.Exit(code=1)


@app.command(name="clear-allowlisted-domains")
@add_options(CLOUD_DAGIT_CLIENT_OPTIONS)
def clear_allowlisted_domains_command(url: str, api_token: str):
    """
    Removes all the allowed domains from an organization.

    After running this command, only users with email addresses corresponding to an existing
    Dagster Cloud account will be able to authenticate into their organization's
    Dagster Cloud instance.
    """
    client = create_cloud_dagit_client(url, api_token)

    response = client.execute(
        SET_ALLOWLISTED_DOMAINS_MUTATION,
        variable_values={"allowlistedDomains": []},
    )

    if response["data"]["setAllowlistedDomains"]["__typename"] == "DagsterCloudOrganization":
        typer.echo(
            "Organization '{organization_name}' now has its allowlisted domains set to {domains}. "
        )
    else:
        typer.echo(f"Error adding domains to allowlist: {response}")
        raise typer.Exit(code=1)
