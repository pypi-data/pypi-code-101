# -*- coding: UTF-8 -*-

'''
 Module
     write_template.py
 Copyright
     Copyright (C) 2017 Vladimir Roncevic <elektron.ronca@gmail.com>
     gen_form_model is free software: you can redistribute it and/or modify it
     under the terms of the GNU General Public License as published by the
     Free Software Foundation, either version 3 of the License, or
     (at your option) any later version.
     gen_form_model is distributed in the hope that it will be useful, but
     WITHOUT ANY WARRANTY; without even the implied warranty of
     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
     See the GNU General Public License for more details.
     You should have received a copy of the GNU General Public License along
     with this program. If not, see <http://www.gnu.org/licenses/>.
 Info
     Defined class WriteTemplate with attribute(s) and method(s).
     Created API for write a template content with parameters to a file.
'''

import sys
from datetime import date
from os import getcwd, chmod
from string import Template

try:
    from ats_utilities.checker import ATSChecker
    from ats_utilities.console_io.error import error_message
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
__license__ = 'https://github.com/vroncevic/gen_form_model/blob/dev/LICENSE'
__version__ = '1.5.3'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class WriteTemplate(FileChecking):
    '''
        Defined class WriteTemplate with attribute(s) and method(s).
        Created API for write a template content with parameters to a file.
        It defines:

            :attributes:
                | GEN_VERBOSE - console text for current process-phase.
                | __file_name - file name.
            :methods:
                | __init__ - initial constructor.
                | get_file_name - getter for file name.
                | write - write a template content with parameters to a file.
                | __str__ - dunder method for WriteTemplate.
    '''

    GEN_VERBOSE = 'GEN_FORM_MODEL::PRO::WRITE_TEMPLATE'

    def __init__(self, verbose=False):
        '''
            Initial constructor.

            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :exceptions: None
        '''
        FileChecking.__init__(self, verbose=verbose)
        verbose_message(WriteTemplate.GEN_VERBOSE, verbose, 'init writter')
        self.__file_name = None

    def get_file_name(self):
        '''
            Getter for file name.

            :return: file name | None.
            :rtype: <str> | <NoneType>
            :exceptions: None
        '''
        return self.__file_name

    def write(self, form_content, form_name, verbose=False):
        '''
            Write a template content with parameters to a file.

            :param form_content: template form content.
            :type form_content: <str>
            :param form_name: parameter form name.
            :type form_name: <str>
            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :return: boolean status, True (success) | False.
            :rtype: <bool>
            :exception: ATSTypeError | ATSBadCallError
        '''
        checker, error, status = ATSChecker(), None, False
        error, status = checker.check_params([
            ('str:form_content', form_content), ('str:form_name', form_name)
        ])
        if status == ATSChecker.TYPE_ERROR:
            raise ATSTypeError(error)
        if status == ATSChecker.VALUE_ERROR:
            raise ATSBadCallError(error)
        self.__file_name = '{0}.py'.format(form_name)
        status = False
        if all([bool(self.__file_name), bool(form_content)]):
            verbose_message(
                WriteTemplate.GEN_VERBOSE, verbose, 'generating form model'
            )
            current_dir = getcwd()
            module_file = '{0}/{1}'.format(current_dir, self.__file_name)
            module_info = {
                'mod': '{0}'.format(form_name),
                'modlc': '{0}'.format(form_name.lower()),
                'date': '{0}'.format(date.today()),
                'year': '{0}'.format(date.today().year)
            }
            template = Template(form_content)
            with open(module_file, 'w') as form_file:
                form_file.write(template.substitute(module_info))
                chmod(module_file, 0o666)
                self.check_path(module_file, verbose=verbose)
                self.check_mode('w', verbose=verbose)
                self.check_format(module_file, 'py',verbose=verbose)
                if self.is_file_ok():
                    status = True
        else:
            error_message(
                WriteTemplate.GEN_VERBOSE, 'failed to write module', form_name
            )
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
            self.__file_name
        )
