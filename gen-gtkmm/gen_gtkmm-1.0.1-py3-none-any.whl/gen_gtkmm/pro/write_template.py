# -*- coding: UTF-8 -*-

'''
 Module
     write_template.py
 Copyright
     Copyright (C) 2018 Vladimir Roncevic <elektron.ronca@gmail.com>
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
     Defined class WriteTemplate with attribute(s) and method(s).
     Created API for writing templates content with parameters.
'''

import sys
from os import getcwd, chmod, mkdir
from os.path import exists
from string import Template
from time import strftime

try:
    from ats_utilities.checker import ATSChecker
    from ats_utilities.config_io.base_check import FileChecking
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
except ImportError as ats_error_message:
    MESSAGE = '\n{0}\n{1}\n'.format(__file__, ats_error_message)
    sys.exit(MESSAGE)  # Force close python ATS ##############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2021, https://electux.github.io/gen_gtkmm'
__credits__ = ['Vladimir Roncevic']
__license__ = 'https://github.com/electux/gen_gtkmm/blob/dev/LICENSE'
__version__ = '1.0.1'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class WriteTemplate(FileChecking):
    '''
        Defined class WriteTemplate with attribute(s) and method(s).
        Created API for writing templates content with parameters.
        It defines:

            :attributes:
                | GEN_VERBOSE - console text indicator for process-phase.
            :methods:
                | __init__ - initial constructor.
                | write - write a template content to a project setup.
                | __str__ - dunder method for WriteTemplate.
    '''

    GEN_VERBOSE = 'GEN_GTKMM::PRO::WRITE_TEMPLATE'

    def __init__(self, verbose=False):
        '''
            Initial constructor.

            :param verbose: enable/disable verbose option
            :type verbose: <bool>
            :exceptions: None
        '''
        FileChecking.__init__(self, verbose=verbose)
        verbose_message(WriteTemplate.GEN_VERBOSE, verbose, 'init writer')

    def write(self, templates, project_name, verbose=False):
        '''
            Write setup content to file.

            :param templates: project templates.
            :type templates: <list>
            :param project_name: project name.
            :type project_name: <str>
            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :return: boolean status, True (success) | False.
            :rtype: <bool>
            :exception: ATSBadCallError | ATSTypeError
        '''
        checker, error, status = ATSChecker(), None, False
        error, status = checker.check_params([
            ('list:templates', templates), ('str:project_name', project_name)
        ])
        if status == ATSChecker.TYPE_ERROR:
            raise ATSTypeError(error)
        if status == ATSChecker.VALUE_ERROR:
            raise ATSBadCallError(error)
        pro_dir, statuses = '{0}/{1}'.format(getcwd(), project_name), []
        status, build_dir = False, '{0}/{1}'.format(pro_dir, 'build')
        expected_num_of_modules = len(templates)
        if not exists(pro_dir):
            mkdir(pro_dir)
            mkdir(build_dir)
        for pro_item in templates:
            module_name = list(pro_item.keys())[0]
            is_build_config = any([
                'makefile'.capitalize() in module_name,
                '.mk' in module_name
            ])
            if is_build_config:
                module_path = '{0}/{1}'.format(build_dir, module_name)
            else:
                if 'main' in module_name:
                    module_path = '{0}/{1}'.format(pro_dir, module_name)
                else:
                    module_content = pro_item[module_name]
                    pro_item.pop(module_name)
                    module_name = '{0}.{1}'.format(
                        project_name, module_name.split('.')[1]
                    )
                    pro_item[module_name] = module_content
                    module_path = '{0}/{1}'.format(pro_dir, module_name)
            template = Template(pro_item[module_name])
            if bool(template):
                with open(module_path, 'w') as module_file:
                    module_content = template.substitute(
                        {
                            'PRO': project_name,
                            'PRO_UP': project_name.upper(),
                            'PRO_CLASS': project_name.capitalize(),
                            'DATE': strftime("%m/%d/%Y"),
                            'YEAR': strftime("%Y")
                        }
                    )
                    module_file.write(module_content)
                    chmod(module_path, 0o666)
                    self.check_path(module_path, verbose=verbose)
                    self.check_mode('w', verbose=verbose)
                    if 'makefile'.capitalize() in module_path:
                        self.check_format(
                            module_path, 'makefile', verbose=verbose
                        )
                    else:
                        self.check_format(
                            module_path, module_path.split('.')[1],
                            verbose=verbose
                        )
                    if self.is_file_ok():
                        statuses.append(True)
                    else:
                        statuses.append(False)
        if all(statuses) and len(statuses) == expected_num_of_modules:
            status = True
        return status

    def __str__(self):
        '''
            Dunder method for WriteTemplate.

            :return: object in a human-readable format.
            :rtype: <str>
            :exceptions: None
        '''
        return '{0} ({1})'.format(
            self.__class__.__name__, FileChecking.__str__(self)
        )
