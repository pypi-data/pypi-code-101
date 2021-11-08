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
Common PPSI Errors
"""


class PpsiError(Exception):
    """
    Base Error class for PPSI Errors
    """
    def __init__(self, *args, **kwargs):
        super(Exception, self).__init__(*args, **kwargs)


class ExternalError(PpsiError):
    """
    External program threw error

    Args:
        program: external subprocess called
        retcode: return code of external program
        stderr: standard error from external program
        stdout: standard output from external program
    """
    def __init__(self,
                 *cmd: str,
                 retcode: int = 1,
                 stderr: str = "",
                 stdout: str = ""):
        err_out = f'''
        External process {cmd[0]} exitted with error.
        command: {cmd}

        returned: {retcode}

        Output:

        {stdout}


        Error Message:

        {stderr}
        '''
        super(PpsiError, self).__init__(err_out)
