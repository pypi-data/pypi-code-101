# -*- coding: UTF-8 -*-

'''
 Module
     __init__.py
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
     Defined class GenModule with attribute(s) and method(s).
     Generate python module by template and parameters.
'''

import sys

try:
    from pathlib import Path
    from gen_py_module.module.read_template import ReadTemplate
    from gen_py_module.module.write_template import WriteTemplate
    from gen_py_module.module.module_selector import ModuleSelector
    from ats_utilities.checker import ATSChecker
    from ats_utilities.config_io.base_check import FileChecking
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.config_io.yaml.yaml2object import Yaml2Object
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


class GenModule(FileChecking):
    '''
        Defined class GenModule with attribute(s) and method(s).
        Generate python module by template and parameters.
        It defines:

            :attributes:
                | GEN_VERBOSE - console text indicator for process-phase.
                | PRO_STRUCTURE - project setup (templates).
                | __reader - reader API.
                | __writer - writer API.
                | __config - project setup in dict format.
            :methods:
                | __init__ - initial constructor.
                | get_reader - getter for reader object.
                | get_writer - getter for writer object.
                | gen_module - generate file python module.
                | __str__ - dunder method for GenModule.
    '''

    GEN_VERBOSE = 'GEN_PY_MODULE::MODULE::GEN_MODULE'
    PRO_STRUCTURE = '/../conf/project.yaml'

    def __init__(self, verbose=False):
        '''
            Initial constructor.

            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :exceptions: None
        '''
        FileChecking.__init__(self, verbose=verbose)
        verbose_message(GenModule.GEN_VERBOSE, verbose, 'init generator')
        self.__reader = ReadTemplate(verbose=verbose)
        self.__writer = WriteTemplate(verbose=verbose)
        project = '{0}{1}'.format(
            Path(__file__).parent, GenModule.PRO_STRUCTURE
        )
        self.check_path(file_path=project, verbose=verbose)
        self.check_mode(file_mode='r', verbose=verbose)
        self.check_format(
            file_path=project, file_format='yaml', verbose=verbose
        )
        if self.is_file_ok():
            yml2obj = Yaml2Object(project)
            self.__config = yml2obj.read_configuration()
        else:
            self.__config = None

    def get_reader(self):
        '''
            Getter for reader object.

            :return: read template object.
            :rtype: <ReadTemplate>
            :exceptions: None
        '''
        return self.__reader

    def get_writer(self):
        '''
            Getter for writer object.

            :return: write template object.
            :rtype: <WriteTemplate>
            :exceptions: None
        '''
        return self.__writer

    def gen_module(self, module_name, verbose=False):
        '''
            Generate file python module.

            :param module_name: parameter module name.
            :type module_name: <str>
            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :return: boolean status, True (success) | False.
            :rtype: <bool>
            :exceptions: ATSTypeError | ATSBadCallError
        '''
        checker, error, status = ATSChecker(), None, False
        error, status = checker.check_params([
            ('str:module_name', module_name)
        ])
        if status == ATSChecker.TYPE_ERROR:
            raise ATSTypeError(error)
        if status == ATSChecker.VALUE_ERROR:
            raise ATSBadCallError(error)
        verbose_message(
            GenModule.GEN_VERBOSE, verbose, 'generating module', module_name
        )
        template_name = ModuleSelector.choose_module(
            self.__config, verbose=verbose
        )
        if template_name != 'cancel':
            module_content = self.__reader.read(template_name, verbose=verbose)
            if module_content:
                status = self.__writer.write(
                    module_content, module_name, verbose=verbose
                )
        elif template_name == 'cancel':
            status = True
        return status

    def __str__(self):
        '''
            Dunder method for GenModule.

            :return: object in a human-readable format.
            :rtype: <str>
            :exceptions: None
        '''
        return '{0} ({1}, {2})'.format(
            self.__class__.__name__, str(self.__reader), str(self.__writer)
        )
