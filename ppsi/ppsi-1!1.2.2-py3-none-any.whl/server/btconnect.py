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
'''
bluez api to handle bluetooth connections

calls bluetoothctl for connections
'''

import re
import typing

from launcher_menus import menu
from ppsi.common import shell


def query_known() -> typing.Dict[str, str]:
    '''
    Query bluetoothctl for known bluetooth devices

    Returns:
        name: MAC
    '''
    known_devs = {}
    dev_pat = re.compile(r'Device ?((?:.{2}:){5}.{2}) +?(.*)')
    bt_ctl_out = shell.process_comm('bluetoothctl',
                                    'devices',
                                    p_name='remembering')
    if bt_ctl_out is None:
        # Error in process call. Let the user type
        return {}
    for bt_dev in bt_ctl_out.split("\n"):
        device = dev_pat.findall(bt_dev)
        if device:
            known_devs[device[0][1]] = device[0][0]
    return known_devs


def connect_bluetooth(**_) -> int:
    '''
    ``menu`` offers bluetooth devices to connect.
    connection result is flashed via ``notify``.

    Args:
        all are ignored

    Returns:
        error code
    '''
    known_devs = query_known()
    choice = menu(opts=list(known_devs.keys()), prompt="Connect_to:")
    if choice is None:
        # no selection
        return 0
    if choice in known_devs:
        # connect to known device
        response = shell.process_comm('bluetoothctl',
                                      'connect',
                                      known_devs[choice],
                                      p_name='connecting')
        if response is None:
            shell.notify('`bluetoothctl connect` failed.\
            Is the daemon healthy?')
            return 1
        if any(k in response.lower() for k in ('fail', 'error')):
            shell.notify(f'Connection to {choice} failed')
            return 1
    return 0
