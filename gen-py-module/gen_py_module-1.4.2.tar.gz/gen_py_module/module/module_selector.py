# -*- coding: UTF-8 -*-

'''
 Module
     module_selector.py
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
     Definedd class ModuleSelector with attribute(s) and method(s).
     Selecting python template module for generating process.
'''

import sys

try:
    from ats_utilities.console_io.error import error_message
    from ats_utilities.console_io.verbose import verbose_message
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


class ModuleSelector:
    '''
        Defined class ModuleSelector with attribute(s) and method(s).
        Selecting python template module for generating process.
        It defines:

            :attributes:
                | GEN_VERBOSE - console text indicator for process-phase.
            :methods:
                | choose_module - selecting type of module.
                | format_name - formatting name for file module.
                | __str__ - dunder method for ModuleSelector.
    '''

    GEN_VERBOSE = 'GEN_PY_MODULE::MODULE::MODULE_SELECTOR'

    @classmethod
    def choose_module(self, config, verbose=False):
        '''
            Select module type.

            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :return: project template selected | None.
            :rtype: <str> | <NoneType>
            :exceptions: None
        '''
        template_target = None
        if bool(config):
            types = config['py_module']
            pro_types_len = len(types)
            for pro_type in types:
                for project_type, project_info in pro_type.items():
                    if project_type != 'cancel':
                        print(
                            '{0} {1}'.format(
                                types.index(pro_type) + 1,
                                project_info[0]['info']
                            )
                        )
                        verbose_message(
                            ModuleSelector.GEN_VERBOSE, verbose,
                            'to be processed template',
                            project_info[1]['template']
                        )
                    else:
                        print(
                            '{0} {1}'.format(
                                types.index(pro_type) + 1, 'Cancel'
                            )
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
                            if target == 'cancel':
                                template_target = 'cancel'
                            else:
                                template_target = types[
                                    int(input_type) - 1
                                ][target][1]['template']
                        break
                    else:
                        raise ValueError
                except ValueError:
                    error_message(
                        ModuleSelector.GEN_VERBOSE, 'not an appropriate choice'
                    )
            verbose_message(
                ModuleSelector.GEN_VERBOSE, verbose,
                'selected', template_target
            )
        return template_target

    def __str__(self):
        '''
            Dunder method for ModuleSelector.

            :return: object in a human-readable format.
            :rtype: <str>
            :exceptions: None
        '''
        return '{0} ()'.format(self.__class__.__name__)
