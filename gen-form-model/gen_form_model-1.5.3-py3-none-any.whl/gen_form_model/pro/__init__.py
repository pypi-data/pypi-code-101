# -*- coding: UTF-8 -*-

'''
 Module
     __init__.py
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
     Defined class GenForm with attribute(s) and method(s).
     Generate form model by template and parameters.
'''

import sys

try:
    from pathlib import Path
    from gen_form_model.pro.read_template import ReadTemplate
    from gen_form_model.pro.write_template import WriteTemplate
    from ats_utilities.checker import ATSChecker
    from ats_utilities.console_io.error import error_message
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
__license__ = 'https://github.com/vroncevic/gen_form_model/blob/dev/LICENSE'
__version__ = '1.5.3'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class GenForm(FileChecking):
    '''
        Defined class GenForm with attribute(s) and method(s).
        Generate form model by template and parameters.
        It defines:

            :attributes:
                | GEN_VERBOSE - console text indicator for process-phase.
                | PRO_STRUCTURE - project setup (templates).
                | __reader - reader API.
                | __writter - writer API.
                | __config - project setup in dict format.
            :methods:
                | __init__ - initial constructor.
                | get_reader - getter for reader object.
                | get_writer - getter for writer object.
                | gen_form - generate form module file.
                | select_pro_type - select form type.
                | __str__ - dunder method for GenForm.
    '''

    GEN_VERBOSE = 'GEN_FORM_MODEL::PRO'
    PRO_STRUCTURE = '/../conf/project.yaml'

    def __init__(self, verbose=False):
        '''
            Initial constructor.

            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :exceptions: None
        '''
        FileChecking.__init__(self, verbose=verbose)
        verbose_message(GenForm.GEN_VERBOSE, verbose, 'init form generator')
        self.__reader = ReadTemplate(verbose=verbose)
        self.__writer = WriteTemplate(verbose=verbose)
        project = '{0}/{1}'.format(
            Path(__file__).parent, GenForm.PRO_STRUCTURE
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

            :return: read template object | None.
            :rtype: <ReadTemplate> | <NoneType>
            :exceptions: None
        '''
        return self.__reader

    def get_writer(self):
        '''
            Getter for writer object.

            :return: write template object | None.
            :rtype: <WriteTemplate> | <NoneType>
            :exceptions: None
        '''
        return self.__writer

    def gen_form(self, form_name, verbose=False):
        '''
            Generate form module file.

            :param form_name: parameter form class name.
            :type: <str>
            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :return: boolean status, True (success) | False.
            :rtype: <bool>
            :exceptions: ATSTypeError | ATSBadCallError
        '''
        checker, error, status = ATSChecker(), None, False
        error, status = checker.check_params([('str:form_name', form_name)])
        if status == ATSChecker.TYPE_ERROR:
            raise ATSTypeError(error)
        if status == ATSChecker.VALUE_ERROR:
            raise ATSBadCallError(error)
        form_content, template_file, status = None, None, False
        template_file = self.select_pro_type(verbose=verbose)
        if bool(template_file):
            if template_file == 'cancel':
                status = True
            else:
                form_content = self.__reader.read(
                    template_file, verbose=verbose
                )
                if form_content:
                    status = self.__writer.write(
                        form_content, form_name, verbose=verbose
                    )
        return status

    def select_pro_type(self, verbose=False):
        '''
            Select form type.

            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :return: project template selected | None.
            :rtype: <str> | <NoneType>
            :exceptions: None
        '''
        template_selected = None
        if bool(self.__config):
            types = self.__config['templates']
            pro_types_len = len(types)
            for index, pro_type in enumerate(types):
                for project_type, template_file in pro_type.items():
                    print(
                        '{0} {1}'.format(index + 1, project_type.capitalize())
                    )
                    verbose_message(
                        GenForm.GEN_VERBOSE, verbose,
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
                        for target in types[int(input_type) - 1].values():
                            if target is None:
                                template_selected = 'cancel'
                            else:
                                template_selected = target
                        break
                    else:
                        raise ValueError
                except ValueError:
                    error_message(
                        GenForm.GEN_VERBOSE, 'not an appropriate choice'
                    )
            verbose_message(
                GenForm.GEN_VERBOSE, verbose, 'selected', template_selected
            )
        return template_selected

    def __str__(self):
        '''
            Dunder method for GenForm.

            :return: object in a human-readable format.
            :rtype: <str>
            :exceptions: None
        '''
        return '{0} ({1}, {2}, {3}, {4})'.format(
            self.__class__.__name__, FileChecking.__str__(self),
            str(self.__reader), str(self.__writer), str(self.__config)
        )
