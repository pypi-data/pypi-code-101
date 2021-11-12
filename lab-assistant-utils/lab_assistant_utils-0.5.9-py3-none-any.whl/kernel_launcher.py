#!/usr/bin/env python

import os
from ipykernel import kernelapp as app
import click


@click.command()
@click.option('--home', required=True)
@click.option('--uid', required=True)
@click.option('--gid', required=True)
@click.option('--session-key', required=True)
@click.option('--heartbeat-port', required=True)
@click.option('--shell-port', required=True)
@click.option('--iopub-port', required=True)
@click.option('--stdin-port', required=True)
@click.option('--control-port', required=True)
@click.option('--debug', default=True)
def launch(home, uid, gid, session_key, heartbeat_port, shell_port, iopub_port, stdin_port, control_port, debug: bool):
    os.mkdir(home)
    os.chown(home, uid, gid)
    args = [
        f'--Session.key={session_key}',
        f'--ip=0.0.0.0',
        f'--hb={heartbeat_port}',
        f'--shell={shell_port}',
        f'--iopub={iopub_port}',
        f'--stdin={stdin_port}',
        f'--control={control_port}'
    ]
    if debug:
        args.append('--debug')
    app.launch_new_instance(argv=args)


if __name__ == '__main__':
    launch()
