#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
 Module
     setup.py
 Copyright
     Copyright (C) 2021 Vladimir Roncevic <elektron.ronca@gmail.com>
     gen_gtkmm is free software: you can redistribute it and/or modify it
     under the terms of the GNU General Public License as published by the
     Free Software Foundation, either version 3 of the License, or
     (at your option) any later version.
     gen_gtkmm is distributed in the hope that it will be useful, but
     WITHOUT ANY WARRANTY; without even the implied warranty of
     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
     See the GNU General Public License for more details.
     You should have received a copy of the GNU General Public License along
     with this program. If not, see <http://www.gnu.org/licenses/>.
 Info
     Defined setup for tool gen_gtkmm.
'''

from __future__ import print_function
import sys
from os.path import abspath, dirname, join, exists
from setuptools import setup

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2021, https://electux.github.io/gen_gtkmm'
__credits__ = ['Vladimir Roncevic']
__license__ = 'https://github.com/electux/gen_gtkmm/blob/dev/LICENSE'
__version__ = '1.0.1'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'

def install_directory():
    '''
        Return the installation directory, or None.

        :return: path (success) | None.
        :rtype: <str> | <NoneType>
        :exceptions: None
    '''
    py_version = '{0}.{1}'.format(sys.version_info[0], sys.version_info[1])
    if '--github' in sys.argv:
        index = sys.argv.index('--github')
        sys.argv.pop(index)
        paths = (
            '{0}/lib/python{1}/dist-packages/'.format(sys.prefix, py_version),
            '{0}/lib/python{1}/site-packages/'.format(sys.prefix, py_version)
        )
    else:
        paths = (s for s in (
            '{0}/local/lib/python{1}/dist-packages/'.format(
                sys.prefix, py_version
            ),
            '{0}/local/lib/python{1}/site-packages/'.format(
                sys.prefix, py_version
            )
        ))
    message = None
    for path in paths:
        message = '[setup] check path {0}'.format(path)
        print(message)
        if exists(path):
            message = '[setup] use path {0}'.format(path)
            print(message)
            return path
    message = '[setup] no installation path found, check {0}\n'.format(
        sys.prefix
    )
    print(message)
    return None

INSTALL_DIR = install_directory()
TOOL_DIR = 'gen_gtkmm/'
if not INSTALL_DIR:
    print('[setup] force exit from install process')
    exit(127)
THIS_DIR, LONG_DESCRIPTION = abspath(dirname(__file__)), None
with open(join(THIS_DIR, 'README.md')) as readme:
    LONG_DESCRIPTION = readme.read()
PROGRAMMING_LANG = 'Programming Language :: Python ::'
VERSIONS = ['2.7', '3', '3.2', '3.3', '3.4', '3.5', '3.6', '3.7', '3.8', '3.9']
SUPPORTED_PY_VERSIONS = [
    '{0} {1}'.format(PROGRAMMING_LANG, VERSION) for VERSION in VERSIONS
]
LICENSE_PREFIX = 'License :: OSI Approved ::'
LICENSES = [
    'GNU Lesser General Public License v2 (LGPLv2)',
    'GNU Lesser General Public License v2 or later (LGPLv2+)',
    'GNU Lesser General Public License v3 (LGPLv3)',
    'GNU Lesser General Public License v3 or later (LGPLv3+)',
    'GNU Library or Lesser General Public License (LGPL)'
]
APPROVED_LICENSES = [
    '{0} {1}'.format(LICENSE_PREFIX, LICENSE) for LICENSE in LICENSES
]
PYP_CLASSIFIERS = SUPPORTED_PY_VERSIONS + APPROVED_LICENSES
setup(
    name='gen_gtkmm',
    version='1.0.1',
    description='GTK-- project skeleton generator',
    author='Vladimir Roncevic',
    author_email='elektron.ronca@gmail.com',
    url='https://electux.github.io/gen_gtkmm/',
    license='GPL 2021 Free software to use and distributed it.',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    keywords='GTK--, Project, C++, Gtk, Unix, Linux',
    platforms='POSIX',
    classifiers=PYP_CLASSIFIERS,
    packages=['gen_gtkmm', 'gen_gtkmm.pro', 'gen_gtkmm.pro.config'],
    install_requires=['ats-utilities'],
    package_data = {
        'gen_gtkmm': [
            'conf/gen_gtkmm.cfg',
            'conf/gen_gtkmm_util.cfg',
            'conf/project.yaml',
            'conf/template/Makefile.template',
            'conf/template/ccflags.template',
            'conf/template/ldflags.template',
            'conf/template/objects.template',
            'conf/template/sources.template',
            'conf/template/source_module.template',
            'conf/template/header_module.template',
            'conf/template/main_module.template',
            'log/gen_gtkmm.log'
        ]
    },
    data_files=[(
        '/usr/local/bin/', ['gen_gtkmm/run/gen_gtkmm_run.py']
    )]
)
