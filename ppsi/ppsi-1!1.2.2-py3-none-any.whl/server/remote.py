#!/usr/bin/env python3
# -*- coding:utf-8; mode:python -*-
#
# Copyright 2020-2021 Pradyumna Paranjape
# This file is part of ppsi.
#
# ppsi is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# ppsi is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with ppsi.  If not, see <https://www.gnu.org/licenses/>.
#
"""
Call remote commands through ssh/[waypipe]

Interactive username, server, interface, application
that is temporarily remembered till reboot.

TODO: Offer to ossify temporary information.

"""

import os
from pathlib import Path
from typing import List, Optional, Tuple

import yaml
from launcher_menus import menu  # type: ignore
from ppsi.common import shell
from ppsi.server import CONFIG


def handle_tmp_cfg() -> Tuple[Path, dict]:
    """
    look for temporary configuration file to store learnt remote addresses,
    user-names and graphical applications for the session

    Returns:
        location of temporary library
        configuration from temporary library
    """
    data = {}
    uid = os.environ.get('UID')
    basepath = Path(
        '/tmp') if uid is None else Path('/run') / f'user/{str(uid)}'
    tmp_cfg = Path(os.environ.get('XDG_RUNTIME_DIR',
                                  basepath)) / 'sway/ppsi/remote.yml'
    if tmp_cfg.is_file():
        with open(tmp_cfg, 'r') as config_h:
            data = yaml.safe_load(config_h)
        if not data:
            data = {}
    return tmp_cfg, data


TMP_CFG, DATA = handle_tmp_cfg()


def add_id(identity: str, new: str = 'user') -> None:
    """
    Add identity to temporary library.
        - This library is maintained in yml format.
        - This library gets cleared after system reboot.

    Args:
        identity: new object identity
        new: type of object {'user','host','app'}

    Returns:
        ``None``

    """
    TMP_CFG.parent.mkdir(parents=True, exist_ok=True)
    if 'remote' not in DATA:
        DATA['remote'] = {'hosts': [], 'users': []}
    if 'apps' not in DATA:
        DATA['apps'] = []
    if new == 'user':
        DATA['remote']['users'].append(identity)
    elif new == 'host':
        DATA['remote']['hosts'].append(identity)
    elif new == 'app':
        DATA['apps'].append(identity)
    with open(TMP_CFG, 'w') as config_h:
        yaml.safe_dump(DATA, config_h)


def which_remote() -> Tuple[Optional[str], Optional[str]]:
    """
    Fetch desired remote session details using ``menu``

    Returns:
        username
        host
    """
    # default config
    known_users: List[str] = CONFIG['remote']['users'].copy()
    known_hosts: List[str] = CONFIG['remote']['hosts'].copy()

    # temporary config
    if 'remote' in DATA:
        known_users.extend(DATA['remote']['users'])
        known_hosts.extend(DATA['remote']['hosts'])

    user: str = menu(opts=known_users, prompt='user') or os.environ['USER']
    host: str = menu(opts=known_hosts, prompt='host') or 'localhost'
    if user == os.environ['USER'] and host == 'localhost':
        # user aborted
        return None, None
    if user not in known_users:
        add_id(user)
    if host not in known_hosts:
        add_id(host, new='host')
    return user, host


def graphical() -> bool:
    """
    Get remote interface type: Graphical? Default: False

    Returns:
        Whether graphical interface is demanded [experimental]
    """
    return menu(opts=['No', 'Yes'], prompt='Graphical') == 'Yes'


def remote_app() -> Optional[str]:
    """
    Get remote app, also remember it

    Returns:
        Graphical Remote App
    """
    known_apps: List[str] = []
    if 'apps' in DATA:
        known_apps += DATA['apps']
    app = menu(opts=known_apps, prompt='application name')
    if app is None:
        return None
    if app not in known_apps:
        add_id(app, new='app')
    return app


def call_remote(**_) -> int:
    """
    Call remote ssh and try to set up a connection
    Use menu launcher to learn
        * username
        * host address
        * interface type {GUI,CLI}
        * Application name (if GUI)

    Args:
        all are ignored

    Returns:
        error code

    """
    user, host = which_remote()
    if host is None or user is None:
        return 1
    cmd = ['--', 'ssh', f'{user}@{host}']
    if graphical():
        app = remote_app()
        if app is not None:
            cmd.insert(0, 'waypipe')
            cmd.append(
                f'env XDG_SESSION_TYPE=wayland nohup {app} 1>/dev/null 2>&1 &')
        else:
            cmd.insert(0, os.environ.get('defterm', 'xterm'))
    else:
        cmd.insert(0, os.environ.get('defterm', 'xterm'))
        shell.process_comm(*cmd, p_name='connecting remote', timeout=-1)
    return 0
