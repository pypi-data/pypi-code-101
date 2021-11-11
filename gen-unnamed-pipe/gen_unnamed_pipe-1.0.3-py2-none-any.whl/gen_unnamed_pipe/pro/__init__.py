# -*- coding: UTF-8 -*-

'''
 Module
     __init__.py
 Copyright
     Copyright (C) 2020 Vladimir Roncevic <elektron.ronca@gmail.com>
     gen_unnamed_pipe is free software: you can redistribute it and/or modify
     it under the terms of the GNU General Public License as published by the
     Free Software Foundation, either version 3 of the License, or
     (at your option) any later version.
     gen_unnamed_pipe is distributed in the hope that it will be useful, but
     WITHOUT ANY WARRANTY; without even the implied warranty of
     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
     See the GNU General Public License for more details.
     You should have received a copy of the GNU General Public License along
     with this program. If not, see <http://www.gnu.org/licenses/>.
 Info
     Defined class UnnamedPipe with attribute(s) and method(s).
     Generate module file generator_test.py by template and parameters.
'''

import sys

try:
    from pathlib import Path
    from gen_unnamed_pipe.pro.config import ProConfig
    from gen_unnamed_pipe.pro.config.pro_name import ProName
    from gen_unnamed_pipe.pro.read_template import ReadTemplate
    from gen_unnamed_pipe.pro.write_template import WriteTemplate
    from ats_utilities.checker import ATSChecker
    from ats_utilities.config_io.base_check import FileChecking
    from ats_utilities.console_io.error import error_message
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.config_io.yaml.yaml2object import Yaml2Object
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
except ImportError as ats_error_message:
    MESSAGE = '\n{0}\n{1}\n'.format(__file__, ats_error_message)
    sys.exit(MESSAGE)  # Force close python ATS ##############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2020, https://vroncevic.github.io/gen_unnamed_pipe'
__credits__ = ['Vladimir Roncevic']
__license__ = 'https://github.com/vroncevic/gen_unnamed_pipe/blob/dev/LICENSE'
__version__ = '1.0.3'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class UnnamedPipe(FileChecking, ProConfig, ProName):
    '''
        Defined class UnnamedPipe with attribute(s) and method(s).
        Generate module file generator_test.py by template and parameters.
        It defines:

            :attributes:
                | GEN_VERBOSE - console text indicator for process-phase.
                | PRO_STRUCTURE - project setup (template, module).
                | __reader - reader API.
                | __writer - writer API.
            :methods:
                | __init__ - initial constructor.
                | get_reader - getter for template reader.
                | get_writer - getter for template writer.
                | gen_setup - generate module file setup.py.
                | __str__ - dunder method for UnnamedPipe.
    '''

    GEN_VERBOSE = 'GEN_UNNAMED_PIPE::PRO::GEN_SETUP'
    PRO_STRUCTURE = '/../conf/project.yaml'

    def __init__(self, verbose=False):
        '''
            Initial constructor.

            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :exceptions: None
        '''
        FileChecking.__init__(self, verbose=verbose)
        ProConfig.__init__(self, verbose=verbose)
        ProName.__init__(self, verbose=verbose)
        verbose_message(
            UnnamedPipe.GEN_VERBOSE, verbose, 'init generator'
        )
        self.__reader = ReadTemplate(verbose=verbose)
        self.__writer = WriteTemplate(verbose=verbose)
        project_structure = '{0}{1}'.format(
            Path(__file__).parent, UnnamedPipe.PRO_STRUCTURE
        )
        self.check_path(file_path=project_structure, verbose=verbose)
        self.check_mode(file_mode='r', verbose=verbose)
        self.check_format(
            file_path=project_structure, file_format='yaml', verbose=verbose
        )
        if self.is_file_ok():
            yml2obj = Yaml2Object(project_structure)
            self.config = yml2obj.read_configuration()

    def get_reader(self):
        '''
            Getter for template reader.

            :return: template reader object.
            :rtype: <ReadTemplate>
            :exceptions: None
        '''
        return self.__reader

    def get_writer(self):
        '''
            Getter for template writer.

            :return: template writer object.
            :rtype: <WriteTemplate>
            :exceptions: None
        '''
        return self.__writer

    def select_pro_type(self, verbose=False):
        '''
            Select project type.

            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :return: template type | None.
            :rtype: <str> | <NoneType>
            :exceptions: None
        '''
        template_selected = None
        if bool(self.config):
            types = self.config['templates']
            pro_types_len = len(types)
            for index, pro_type in enumerate(types):
                for project_type, template_file in pro_type.items():
                    if project_type == 'cancel':
                        print(
                            '{0} {1}'.format(
                                index + 1, project_type.capitalize()
                            )
                        )
                    else:
                        print(
                            '{0} {1}'.format(
                                index + 1,
                                project_type.upper().replace('_',' ')
                            )
                        )
                    verbose_message(
                        UnnamedPipe.GEN_VERBOSE, verbose,
                        'to be processed template', template_file
                    )
            while True:
                try:
                    try:
                        input_type = raw_input(' select project type: ')
                    except NameError:
                        input_type = input(' select project type: ')
                    options = xrange(1, pro_types_len + 1, 1)
                except NameError:
                    options = range(1, pro_types_len + 1, 1)
                try:
                    if int(input_type) in list(options):
                        for target in types[int(input_type) - 1].keys():
                            if target is None:
                                template_selected = 'cancel'
                            else:
                                template_selected = target
                        break
                    else:
                        raise ValueError
                except ValueError:
                    error_message(
                        UnnamedPipe.GEN_VERBOSE,
                        'not an appropriate choice'
                    )
            verbose_message(
                UnnamedPipe.GEN_VERBOSE, verbose,
                'selected', template_selected
            )
        return template_selected

    def gen_setup(self, pro_name, verbose=False):
        '''
            Generate unnamed pipe modules.

            :param pro_name: project name.
            :type pro_name: <str>
            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :return: boolean status, True (success) | False.
            :rtype: <bool>
            :exceptions: ATSTypeError | ATSBadCallError
        '''
        checker, error, status = ATSChecker(), None, False
        error, status = checker.check_params([('str:pro_name', pro_name)])
        if status == ATSChecker.TYPE_ERROR:
            raise ATSTypeError(error)
        if status == ATSChecker.VALUE_ERROR:
            raise ATSBadCallError(error)
        status = False
        verbose_message(
            UnnamedPipe.GEN_VERBOSE, verbose,
            'generating unnamed pipe modules for', pro_name
        )
        if bool(self.config):
            uds_type = self.select_pro_type(verbose=verbose)
            if uds_type != 'cancel':
                templates = self.__reader.read(
                    self.config, uds_type, verbose=verbose
                )
                if bool(templates):
                    status = self.__writer.write(
                        templates, pro_name, verbose=verbose
                    )
            else:
                status = True
        return status

    def __str__(self):
        '''
            Dunder method for UnnamedPipe.

            :return: object in a human-readable format.
            :rtype: <str>
            :exceptions: None
        '''
        return '{0} ({1}, {2}, {3}, {4}, {5})'.format(
            self.__class__.__name__, FileChecking.__str__(self),
            ProConfig.__str__(self), ProName.__str__(self),
            str(self.__reader), str(self.__writer)
        )
