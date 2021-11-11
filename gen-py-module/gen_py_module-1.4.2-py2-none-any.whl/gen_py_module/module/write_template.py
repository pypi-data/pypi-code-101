# -*- coding: UTF-8 -*-

'''
 Module
     write_template.py
 Copyright
     Copyright (C) 2017 Vladimir Roncevic <elektron.ronca@gmail.com>
     gen_py_module is free software: you can redistribute it and/or modify it
     under the terms of the GNU General Public License as published by the
     Free Software Foundation, either version 3 of the License, or
     (at your option) any later version.
     gen_py_module is distributed in the hope that it will be useful, but
     WITHOUT ANY WARRANTY; without even the implied warranty of
     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
     See the GNU General Public License for more details.
     You should have received a copy of the GNU General Public License along
     with this program. If not, see <http://www.gnu.org/licenses/>.
 Info
     Defined class WriteTemplate with atribute(s) and method(s).
     Created API for writing a template content with parameters to a file.
'''

import sys
from datetime import date
from os import getcwd, chmod
from string import Template

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
__copyright__ = 'Copyright 2017, https://vroncevic.github.io/gen_form_model'
__credits__ = ['Vladimir Roncevic']
__license__ = 'https://github.com/vroncevic/gen_py_module/blob/dev/LICENSE'
__version__ = '1.4.2'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class WriteTemplate(FileChecking):
    '''
        Defined class WriteTemplate with atribute(s) and method(s).
        Created API for writing a template content with parameters to a file.
        It defines:

            :attributes:
                | GEN_VERBOSE - console text indicator for process-phase.
                | __check_setup - check setup status.
            :methods:
                | __init__ - initial constructor.
                | get_check_setup - getter for checking status.
                | write - write a template content with parameters to a file.
                | __str__ - dunder method for WriteTemplate.
    '''

    GEN_VERBOSE = 'GEN_PY_MODULE::MODULE::WRITE_TEMPLATE'

    def __init__(self, verbose=False):
        '''
           Initial constructor.

            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :exceptions: None
        '''
        FileChecking.__init__(self, verbose=verbose)
        verbose_message(WriteTemplate.GEN_VERBOSE, verbose, 'init writer')
        self.__check_setup = False

    def get_check_setup(self):
        '''
            Getter for checking status.

            :return: boolean status, True (checked and ok) | False.
            :rtype: <bool>
            :exceptions: None
        '''
        return self.__check_setup

    def write(self, module_content, module_name, verbose=False):
        '''
            Write a template content with parameters to a file.

            :param module_content: template content.
            :type module_content: <str>
            :param module_name: file name.
            :type module_name: <str>
            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :return: boolean status, True (success) | False.
            :rtype: <bool>
            :exceptions: ATSTypeError | ATSBadCallError
        '''
        checker, error, status = ATSChecker(), None, False
        error, status = checker.check_params([
            ('str:module_content', module_content),
            ('str:module_name', module_name)
        ])
        if status == ATSChecker.TYPE_ERROR:
            raise ATSTypeError(error)
        if status == ATSChecker.VALUE_ERROR:
            raise ATSBadCallError(error)
        status, template = False, None
        self.__check_setup = True
        module_file_name = '{0}/{1}.py'.format(getcwd(), module_name)
        template = Template(module_content)
        if template:
            with open(module_file_name, 'w') as module_file:
                module_file.write(
                    template.substitute(
                        {
                            'mod': '{0}'.format(module_name),
                            'modlc': '{0}'.format(module_name.lower()),
                            'date': '{0}'.format(date.today()),
                            'year': '{0}'.format(date.today().year)
                        }
                    )
                )
                chmod(module_file_name, 0o666)
                self.check_path(module_file_name, verbose=verbose)
                self.check_mode('w', verbose=verbose)
                self.check_format(module_file_name, 'py', verbose=verbose)
                if self.is_file_ok():
                    status = True
        return status

    def __str__(self):
        '''
            Dunder method for WriteTemplate.

            :return: object in a human-readable format.
            :rtype: <str>
            :exceptions: None
        '''
        return '{0} ({1}, {2})'.format(
            self.__class__.__name__, FileChecking.__str__(self),
            str(self.__check_setup)
        )
