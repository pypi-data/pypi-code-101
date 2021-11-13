import json
import os
from pathlib import PurePath
from collections import namedtuple
import click
from datetime import datetime
from pytz import timezone
from typing import List

from .docker import DockerRunOptionsBuilder


eastern = timezone('US/Eastern')
NETWORK_NAME = os.environ.get('NETWORK_NAME')
DISPLAY = os.environ.get('DISPLAY')
TRACING_HOST = os.environ.get('TRACING_HOST')
TRACING_PORT = os.environ.get('TRACING_PORT')
USER = os.environ.get('USER')
UID = int(os.environ.get('UID'))
GID = int(os.environ.get('GID'))
DOCKER_GID = int(os.environ.get('DOCKER_GID'))

# The kernel image where this will be used is supplied by the user so
# we need to use /tmp for the HOME path because it will be writable
home_path_parts = list(PurePath(os.environ.get('HOME')).parts)
HOME = str(PurePath('/tmp').joinpath(*home_path_parts[2:]))


KernelConnection = namedtuple('KernelConnection', ['key', 'control_port', 'shell_port', 'stdin_port', 'hb_port', 'iopub_port'])


__all__ = ['lab_start_kernel', 'lab_start_kernel_image']


def parse_kernel_connection(connection: str) -> KernelConnection:
    with open(connection, 'r') as cxn_fp:
        connection_params = json.load(cxn_fp)

    return KernelConnection(
        key=connection_params['key'].encode('utf-8'),
        control_port=connection_params['control_port'],
        shell_port=connection_params['shell_port'],
        stdin_port=connection_params['stdin_port'],
        hb_port=connection_params['hb_port'],
        iopub_port=connection_params['iopub_port']
    )


def lab_start_kernel_image(ctx, connection, kernel_image, project_name, project_path):
    options = DockerRunOptionsBuilder()\
        .with_gpu()\
        .with_privileged()\
        .with_add_devices()\
        .with_display(DISPLAY)\
        .with_shared_memory()\
        .with_project_volumes(project_path)\
        .with_user(UID, GID)\
        .with_tracing(TRACING_HOST, TRACING_PORT)\
        .build()
    cxn = parse_kernel_connection(connection)

    cmd = f'docker run --init \
            {options} \
            --network=container:jupyter \
            --name {project_name}-kernel-{ datetime.now(eastern).strftime("%Y-%m-%d__%H-%M-%S") } \
            {kernel_image} \
            launch-kernel \
                --home={HOME} \
                --uid={UID} \
                --gid={GID} \
                --session-key={cxn.key} \
                --heartbeat-port={cxn.hb_port} \
                --shell-port={cxn.shell_port} \
                --iopub-port={cxn.iopub_port} \
                --stdin-port={cxn.stdin_port} \
                --control-port={cxn.control_port}'.split()
            # python -m ipykernel_launcher \
            #     --debug \
            #     --Session.key={cxn.key} \
            #     --ip=0.0.0.0 \
            #     --hb={cxn.hb_port} \
            #     --shell={cxn.shell_port} \
            #     --iopub={cxn.iopub_port} \
            #     --stdin={cxn.stdin_port} \
            #     --control={cxn.control_port}'.split()
    click.echo(f'About to run command: {cmd}')
    os.execvp(cmd[0], cmd)


def lab_start_kernel(ctx, connection, image_name_prefix: List):
    pass


