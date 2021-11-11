# -*- coding: UTF-8 -*-

'''
 Module
     read_template.py
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
     Defined class ReadTemplate with attribute(s) and method(s).
     Created API for read a template file and return in string format.
'''

import sys
from os.path import exists

try:
    from pathlib import Path
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


class ReadTemplate(FileChecking):
    '''
        Defined class ReadTemplate with attribute(s) and method(s).
        Created API for read a template file and return in string format.
        It defines:

            :attributes:
                | GEN_VERBOSE - console text indicator for process-phase.
                | TEMPLATE_DIR - prefix path to templates.
                | __template - absolute template file path.
            :methods:
                | __init__ - initial constructor.
                | get_template - getter for template object.
                | read - read a template and return a string representation.
                | __str__ - dunder method for ReadTemplate.
    '''

    GEN_VERBOSE = 'GEN_FORM_MODEL::PRO::READ_TEMPLATE'
    TEMPLATE_DIR = '/../conf/template/'

    def __init__(self, verbose=False):
        '''
            Initial constructor.

            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :exceptions: None
        '''
        FileChecking.__init__(self, verbose=verbose)
        verbose_message(ReadTemplate.GEN_VERBOSE, verbose, 'init template')
        self.__template = '{0}{1}'.format(
            Path(__file__).resolve().parent, ReadTemplate.TEMPLATE_DIR
        )

    def get_template(self):
        '''
            Getter for template object.

            :return: template object.
            :rtype: <str>
            :exceptions: None
        '''
        return self.__template

    def read(self, form_template, verbose=False):
        '''
            Read a template and return a string representation.

            :param form_template: form template file.
            :type form_template: <str>
            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :return: form content | None.
            :rtype: <str> | <NoneType>
            :exception: ATSTypeError | ATSBadCallError
        '''
        checker, error, status = ATSChecker(), None, False
        error, status = checker.check_params([
            ('str:form_template', form_template)
        ])
        if status == ATSChecker.TYPE_ERROR:
            raise ATSTypeError(error)
        if status == ATSChecker.VALUE_ERROR:
            raise ATSBadCallError(error)
        template_file, form_content = '{0}{1}'.format(
            self.__template, form_template
        ), None
        verbose_message(
            ReadTemplate.GEN_VERBOSE, verbose,
            'loading template', template_file
        )
        if bool(template_file) and exists(template_file):
            self.check_path(template_file, verbose=verbose)
            self.check_mode('r', verbose=verbose)
            self.check_format(template_file, 'template',verbose=verbose)
            if self.is_file_ok():
                with open(template_file, 'r') as form_file:
                    form_content = form_file.read()
        else:
            error_message(
                ReadTemplate.GEN_VERBOSE,
                'check file {0}'.format(template_file)
            )
        return form_content

    def __str__(self):
        '''
            Dunder method for ReadTemplate.

            :return: object in a human-readable format.
            :rtype: <str>
            :exceptions: None
        '''
        return '{0} ({1}, {2})'.format(
            self.__class__.__name__, FileChecking.__str__(self),
            str(self.__template)
        )
