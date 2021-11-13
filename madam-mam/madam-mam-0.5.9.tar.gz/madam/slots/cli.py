#!/usr/bin/env python
# Copyright 2021 Vincent Texier
#
# This file is part of MADAM.
#
# MADAM is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# MADAM is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with MADAM.  If not, see <https://www.gnu.org/licenses/>.

import logging
import os

import click
from rich.console import Console
from rich.table import Table

from madam.domains.application import MainApplication
from madam.domains.entities import job as data_job
from madam.domains.entities.constants import MADAM_CONFIG_PATH, MADAM_LOG_LEVEL
from madam.slots.graphql import server as graphql_server


@click.group()
@click.option(
    "--config",
    "-c",
    default=MADAM_CONFIG_PATH,
    type=click.Path(),
    show_default=True,
    help="madam.yaml config path",
)
@click.option(
    "--level",
    "-l",
    default=MADAM_LOG_LEVEL,
    type=str,
    show_default=True,
    help="Log level",
)
@click.pass_context
def cli(context, config, level):
    """
    Madam cli console command
    """
    # configure log level
    if os.getenv("MADAM_LOG_LEVEL", None) is not None:
        # from env var
        logging.basicConfig(level=os.getenv("MADAM_LOG_LEVEL").upper())
    else:
        # from --level option
        logging.basicConfig(level=level.upper())

    # check context
    context.ensure_object(dict)

    if os.getenv("MADAM_CONFIG_PATH", None) is not None:
        # from env var
        config_path = os.getenv("MADAM_CONFIG_PATH")
    else:
        # from --config option
        config_path = config

    # create Application instance
    context.obj["application"] = MainApplication(config_path)


@cli.command()
@click.pass_context
def server(context):
    """
    Run Madam server
    """
    graphql_server.run(context.obj["application"], MADAM_LOG_LEVEL)


@cli.group()
def workflows():
    """
    Manage workflows
    """


@workflows.command("load")
@click.argument("filepath", type=click.Path(exists=True))
@click.pass_context
def workflows_load(context, filepath):
    """
    Load FILEPATH BPMN file and create workflow from it
    """
    click.echo(f"Load a workflow from the file {filepath}")
    with open(filepath, encoding="utf-8") as fh:
        content = fh.read()
    workflow_ = context.obj["application"].workflows.create(content)
    click.echo(
        f'Workflow "{workflow_.name}" ({workflow_.id}) Version {workflow_.version} loaded.'
    )


@workflows.command("list")
@click.pass_context
def workflows_list(context):
    """
    List workflows
    """
    application_ = context.obj["application"]  # type: MainApplication

    table = Table(
        show_header=True,
        header_style="bold blue",
        title="WORKFLOWS",
        title_style="bold blue",
    )
    table.add_column("ID")
    table.add_column("Version", justify="right")
    table.add_column("Name")
    table.add_column("Timer")
    table.add_column("Created At")

    for workflow_ in application_.workflows.list():
        table.add_row(
            workflow_.id,
            str(workflow_.version),
            workflow_.name,
            "None" if workflow_.timer is None else workflow_.timer,
            workflow_.created_at.isoformat(),
        )

    Console().print(table)


@workflows.command("clear_instances")
@click.argument("id", type=str)
@click.option(
    "--version",
    "-v",
    type=int,
    default=None,
    show_default=True,
    help="Workflow version",
)
@click.pass_context
def workflows_clear_instances(
    context, id, version
):  # pylint: disable=redefined-builtin
    """
    Delete instances of workflow ID
    """
    application_ = context.obj["application"]  # type: MainApplication
    try:
        workflow_ = application_.workflows.read(id, version)
    except Exception:
        raise click.ClickException(f"Workflow {id} not found.") from Exception

    application_.workflow_instances.delete_by_workflow(workflow_)
    click.echo(f"Instances of workflow {id} deleted.")


@workflows.command("abort_instances")
@click.argument("id", type=str)
@click.option(
    "--version",
    "-v",
    type=int,
    default=None,
    show_default=True,
    help="Workflow version",
)
@click.pass_context
def workflows_abort_instances(
    context, id, version
):  # pylint: disable=redefined-builtin
    """
    Abort instances of workflow ID
    """
    application_ = context.obj["application"]  # type: MainApplication
    try:
        workflow_ = application_.workflows.read(id, version)
    except Exception:
        raise click.ClickException(f"Workflow {id} not found.") from Exception

    application_.workflow_instances.abort_by_workflow(workflow_)
    click.echo(f"Instances of workflow {id} aborted.")


@workflows.command("delete")
@click.argument("id", type=str)
@click.pass_context
def workflows_delete(context, id):  # pylint: disable=redefined-builtin
    """
    Delete workflow by ID
    """
    application_ = context.obj["application"]  # type: MainApplication
    try:
        workflow_ = application_.workflows.read(id)
    except Exception:
        raise click.ClickException(f"Workflow {id} not found.") from Exception

    application_.workflows.delete(workflow_)
    click.echo(f"Workflow {id} deleted.")


@workflows.command("start")
@click.argument("id", type=str)
@click.argument("variables", type=str, nargs=-1)
@click.option(
    "--version",
    "-v",
    type=int,
    default=None,
    show_default=True,
    help="Workflow version",
)
@click.pass_context
def workflows_start(
    context, id, version, variables
):  # pylint: disable=redefined-builtin
    """
    Start processing workflow

    ID: workflow ID

    VARIABLES: initial variables as key=value
    """
    if len(variables) == 0:
        variables_dict = None
    else:
        variables_dict = {}
        for var in variables:
            key, value = var.split("=")
            variables_dict[key] = value

    application_ = context.obj["application"]  # type: MainApplication
    try:
        application_.workflows.start(id, version, variables_dict)
    except Exception as exception:
        raise click.ClickException(exception) from Exception

    click.echo(f"Workflow {id} started.")


@workflows.command("abort")
@click.argument("id", type=str)
@click.option(
    "--version",
    "-v",
    type=int,
    default=None,
    show_default=True,
    help="Workflow version",
)
@click.pass_context
def workflows_abort(context, id, version):  # pylint: disable=redefined-builtin
    """
    Abort workflow (instances and timers) by ID and optionally version
    """
    application_ = context.obj["application"]  # type: MainApplication
    try:
        workflow_ = application_.workflows.read(id, version)
    except Exception:
        raise click.ClickException(f"Workflow {id} not found.") from Exception

    application_.workflows.abort(workflow_)
    click.echo(
        f"Workflow {workflow_.id},{workflow_.version} instances and timers aborted."
    )


@workflows.command("show")
@click.argument("id", type=str)
@click.option(
    "--version",
    "-v",
    type=int,
    default=None,
    show_default=True,
    help="Workflow version",
)
@click.pass_context
def workflows_show(context, id, version):  # pylint: disable=redefined-builtin
    """
    Show workflow by ID and optionally version
    """
    application_ = context.obj["application"]  # type: MainApplication

    try:
        workflow_ = application_.workflows.read(id, version)
    except Exception:
        raise click.ClickException(f"Workflow {id} not found.") from Exception

    table = Table(
        show_header=True,
        header_style="bold blue",
        title=f"WORKFLOW {workflow_.id} Version {workflow_.version}",
        title_style="bold blue",
    )
    table.add_column("Field")
    table.add_column("Value")

    table.add_row("Name", workflow_.name)
    table.add_row("Sha256", workflow_.sha256)
    table.add_row("Timer", workflow_.timer)
    table.add_row("Created At", workflow_.created_at.isoformat())

    Console().print(table)

    if workflow_.timer is not None:
        table = Table(
            show_header=True,
            header_style="bold blue",
            title="TIMERS",
            title_style="bold blue",
        )
        table.add_column("ID")
        table.add_column("Status")
        table.add_column("Start At")
        table.add_column("End At")
        table.add_column("Input")

        for timer_ in application_.timers.list():
            table.add_row(
                str(timer_.id),
                timer_.status,
                timer_.start_at.isoformat(),
                timer_.end_at.isoformat() if timer_.end_at else None,
                str(timer_.input_),
            )

        Console().print(table)

    table = Table(
        show_header=True,
        header_style="bold blue",
        title="INSTANCES",
        title_style="bold blue",
    )
    table.add_column("ID")
    table.add_column("Status")
    table.add_column("Start At")
    table.add_column("End At")
    table.add_column("Input")
    table.add_column("Output")

    for instance_ in application_.workflow_instances.list():
        table.add_row(
            str(instance_.id),
            instance_.status,
            instance_.start_at.isoformat(),
            instance_.end_at.isoformat() if instance_.end_at else None,
            str(instance_.input_),
            str(instance_.output),
        )

    Console().print(table)


@cli.group()
def instances():
    """
    Manage workflow instances
    """


@instances.command("list")
@click.pass_context
def instances_list(context):
    """
    List workflow instances
    """
    application_ = context.obj["application"]  # type: MainApplication

    table = Table(
        show_header=True,
        header_style="bold blue",
        title="WORKFLOW INSTANCES",
        title_style="bold blue",
    )
    table.add_column("ID")
    table.add_column("Workflow")
    table.add_column("Version")
    table.add_column("Status")
    table.add_column("Start At")
    table.add_column("End At")

    for instance_ in application_.workflow_instances.list():
        table.add_row(
            str(instance_.id),
            instance_.workflow.id,
            str(instance_.workflow.version),
            instance_.status,
            instance_.start_at.isoformat(),
            instance_.end_at.isoformat() if instance_.end_at else None,
        )

    Console().print(table)


@instances.command("abort")
@click.argument("id", type=str)
@click.pass_context
def instances_abort(context, id):  # pylint: disable=redefined-builtin
    """
    Abort workflow instance by ID
    """
    application_ = context.obj["application"]  # type: MainApplication
    try:
        instance_ = application_.workflow_instances.read(id)
    except Exception:
        raise click.ClickException(f"Instance {id} not found.") from Exception

    application_.workflow_instances.abort(instance_)
    click.echo(f"Workflow instance {id} aborted.")


@instances.command("delete")
@click.argument("id", type=str)
@click.pass_context
def instances_delete(context, id):  # pylint: disable=redefined-builtin
    """
    Delete workflow instance by ID
    """
    application_ = context.obj["application"]  # type: MainApplication
    try:
        instance_ = application_.workflow_instances.read(id)
    except Exception:
        raise click.ClickException(f"Instance {id} not found.") from Exception

    application_.workflow_instances.delete(instance_)
    click.echo(f"Workflow instance {id} deleted.")


@instances.command("show")
@click.argument("id", type=str)
@click.pass_context
def instances_show(context, id):  # pylint: disable=redefined-builtin
    """
    Show workflow instance by ID
    """
    application_ = context.obj["application"]  # type: MainApplication
    try:
        instance_ = application_.workflow_instances.read(id)
    except Exception:
        raise click.ClickException(f"Instance {id} not found.") from Exception

    table = Table(
        show_header=True,
        header_style="bold blue",
        title=f"WORKFLOW INSTANCE {instance_.id}",
        title_style="bold blue",
    )
    table.add_column("Field")
    table.add_column("Value")

    table.add_row("Workflow ID", str(instance_.workflow.id))
    table.add_row("Workflow Version", str(instance_.workflow.version))
    table.add_row("Status", instance_.status)
    table.add_row("Input", str(instance_.input_))
    table.add_row("Output", str(instance_.output))
    table.add_row("Start At", instance_.start_at.isoformat())
    table.add_row("End At", instance_.end_at.isoformat() if instance_.end_at else None)

    Console().print(table)

    table = Table(
        show_header=True,
        header_style="bold blue",
        title="JOBS",
        title_style="bold blue",
    )
    table.add_column("ID")
    table.add_column("Agent ID")
    table.add_column("Agent Type")
    table.add_column("Status")
    table.add_column("Error")
    table.add_column("Start At")
    table.add_column("End At")

    for job_ in application_.jobs.list(workflow_instance_id=instance_.id):
        table.add_row(
            str(job_.id),
            job_.agent_id,
            job_.agent_type,
            job_.status,
            job_.error,
            job_.start_at.isoformat(),
            job_.end_at.isoformat() if job_.end_at else None,
        )

    Console().print(table)

    # list of job with status error
    for job_ in application_.jobs.list(
        status=data_job.STATUS_ERROR, workflow_instance_id=instance_.id
    ):
        table = Table(
            show_header=True,
            header_style="bold blue",
            title=f"JOB {job_.id}",
            title_style="bold blue",
        )
        table.add_column("Field")
        table.add_column("Value")

        table.add_row("Agent ID", job_.agent_id)
        table.add_row("Agent Type", job_.agent_type)
        table.add_row("Status", job_.status)
        table.add_row("Error", job_.error)
        table.add_row("Headers", str(job_.headers))
        table.add_row("Input", str(job_.input_))
        table.add_row("Output", str(job_.output))
        table.add_row("Start At", job_.start_at.isoformat())
        table.add_row("End At", job_.end_at.isoformat() if job_.end_at else None)

        Console().print(table)

        for job_application_ in application_.applications.list():
            table = Table(
                show_header=True,
                header_style="bold blue",
                title=f"JOB APPLICATION {job_application_.id}",
                title_style="bold blue",
            )
            table.add_column("Field")
            table.add_column("Value")

            table.add_row("ID", str(job_application_.id))
            table.add_row("Name", job_application_.name)
            table.add_row("Status", job_application_.status)
            table.add_row("Arguments", job_application_.arguments)
            table.add_row("Logs", job_application_.logs)
            table.add_row("Container ID", job_application_.container_id)
            table.add_row("Container Name", job_application_.container_name)
            table.add_row("Container Error", job_application_.container_error)
            table.add_row("Start At", job_application_.start_at.isoformat())
            table.add_row(
                "End At",
                job_application_.end_at.isoformat()
                if job_application_.end_at
                else None,
            )

            Console().print(table)


@cli.group()
def jobs():
    """
    Manage jobs
    """


@jobs.command("list")
@click.pass_context
def jobs_list(context):
    """
    List jobs
    """
    application_ = context.obj["application"]  # type: MainApplication

    table = Table(
        show_header=True,
        header_style="bold blue",
        title="JOBS",
        title_style="bold blue",
    )
    table.add_column("ID")
    table.add_column("Instance")
    table.add_column("Workflow")
    table.add_column("Version")
    table.add_column("Status")
    table.add_column("Error")
    table.add_column("Start At")
    table.add_column("End At")

    for job_ in application_.jobs.list():
        table.add_row(
            str(job_.id),
            str(job_.workflow_instance.id),
            job_.workflow_instance.workflow.id,
            str(job_.workflow_instance.workflow.version),
            job_.status,
            job_.error,
            job_.start_at.isoformat(),
            job_.end_at.isoformat() if job_.end_at else None,
        )

    Console().print(table)


@cli.group()
def timers():
    """
    Manage timers
    """


@timers.command("list")
@click.pass_context
def timers_list(context):
    """
    List timers
    """
    application_ = context.obj["application"]  # type: MainApplication

    table = Table(
        show_header=True,
        header_style="bold blue",
        title="TIMERS",
        title_style="bold blue",
    )
    table.add_column("ID")
    table.add_column("Workflow")
    table.add_column("Version")
    table.add_column("Status")
    table.add_column("Start At")
    table.add_column("End At")
    table.add_column("Input")

    for timer_ in application_.timers.list():
        table.add_row(
            str(timer_.id),
            timer_.workflow.id,
            str(timer_.workflow.version),
            timer_.status,
            timer_.start_at.isoformat(),
            timer_.end_at.isoformat() if timer_.end_at else None,
            str(timer_.input_),
        )

    Console().print(table)


@timers.command("abort")
@click.argument("id", type=str)
@click.pass_context
def timers_abort(context, id):  # pylint: disable=redefined-builtin
    """
    Abort timer by ID
    """
    application_ = context.obj["application"]  # type: MainApplication

    try:
        timer_ = application_.timers.read(id)
    except Exception:
        raise click.ClickException(f"Timer {id} not found.") from Exception

    application_.timers.abort(timer_)
    click.echo(f"Timer {id} aborted.")


@timers.command("delete")
@click.argument("id", type=str)
@click.pass_context
def timers_delete(context, id):  # pylint: disable=redefined-builtin
    """
    Delete workflow instance by ID
    """
    application_ = context.obj["application"]  # type: MainApplication
    try:
        timer_ = application_.timers.read(id)
    except Exception:
        raise click.ClickException(f"Timer {id} not found.") from Exception

    application_.timers.delete(timer_)
    click.echo(f"Timer {id} deleted.")


if __name__ == "__main__":
    cli(obj={})  # pylint: disable=unexpected-keyword-arg,no-value-for-parameter
