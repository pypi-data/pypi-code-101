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
common shell calls functions
"""

import os
import subprocess
from pathlib import Path
from typing import List, Optional, Tuple

from ppsi.common.errors import ExternalError


def notify(info: str,
           timeout: int = 5,
           send_args: Tuple[str, ...] = None) -> None:
    """
    Push ``info`` to notify-send for ``timeout`` seconds

    Args:
        info: str = information to notify
        timeout: int = remove notification after seconds. [0 => permament]
        send_args: arguments passed to notify-send command

    Returns:
        None

    """
    if os.environ.get("READTHEDOCS"):
        # RTD virutal environment
        return None
    icon = Path(__file__).parent.joinpath('icon.jpg')
    timeout *= 1000  # miliseconds
    cmd = ['notify-send', '--icon', str(icon)]
    if send_args is not None:
        cmd.extend(send_args)
    if timeout > 0:
        cmd += ['-t', f'{timeout}']
    cmd.append(info)
    subprocess.Popen(
        cmd,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    return None


def process_comm(*cmd: str,
                 p_name: str = 'processing',
                 timeout: int = None,
                 fail: str = 'silent',
                 **kwargs) -> Optional[str]:
    """
    Generic process definition and communication

    Args:
        *cmd: list(args) passed to subprocess.Popen as first argument
        p_name: notified as 'Error {p_name}: {stderr}
        timeout: communicatoin timeout. If -1, 'communicate' isn't called
        fail: on fail, perform the following:
            - notify: send stderr to notify-send, return``None``
            - silent: return ``None``
            - raise: raise ExternalError
        **kwargs: passed on to subprocess.Popen

    Returns:
        ``stdout`` from command's communication if process exits without error
        ``None`` if process exits with error and fail is not raise

    Raises:
        ExternalError: if `fail` == "raise"

    """
    if os.environ.get("READTHEDOCS"):
        # RTD virutal environment
        return None
    cmd_l: List[str] = list(cmd)
    if timeout is not None and timeout < 0:
        process = subprocess.Popen(cmd_l, **kwargs)  # DONT: *cmd_l here
        return None
    process = subprocess.Popen(cmd_l,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE,
                               text=True,
                               **kwargs)
    stdout, stderr = process.communicate(timeout=timeout)
    if not process.returncode:
        return stdout  # type: ignore
    if fail == 'raise':
        raise ExternalError(*cmd,
                            retcode=process.returncode,
                            stderr=stderr,
                            stdout=stdout)
    if fail == "notify":
        notify(info=f'Error: {p_name}: Error Message: {stderr}')
    return None
