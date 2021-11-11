# -*- coding: UTF-8 -*-

'''
 Module
     gen_form_model.py
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
     Defined class GenFormModel with attribute(s) and method(s).
     Load a base info, create an CLI interface and run operation(s).
'''

import sys
from os import getcwd

try:
    from six import add_metaclass
    from pathlib import Path
    from gen_form_model.pro import GenForm
    from ats_utilities.logging import ATSLogger
    from ats_utilities.cli.cfg_cli import CfgCLI
    from ats_utilities.cooperative import CooperativeMeta
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.console_io.error import error_message
    from ats_utilities.console_io.success import success_message
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


@add_metaclass(CooperativeMeta)
class GenFormModel(CfgCLI):
    '''
        Defined class GenFormModel with attribute(s) and method(s).
        Load a base info, create an CLI interface and run operation(s).
        It defines:

            :attributes:
                | GEN_VERBOSE - console text indicator for process-phase.
                | CONFIG - tool info file path.
                | LOG - tool log file path.
                | OPS - list of tool options.
                | logger - logger object API.
            :methods:
                | __init__ - initial constructor.
                | process - process and generate module setup.py.
                | __str__ - dunder method for DistPyModule.
    '''

    GEN_VERBOSE = 'GEN_FORM_MODEL'
    CONFIG = '/conf/gen_form_model.cfg'
    LOG = '/log/gen_form_model.log'
    OPS = ['-g', '--gen', '-v', '--verbose', '--version']

    def __init__(self, verbose=False):
        '''
            Loading configuration and setting argument options.

            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :exceptions: None
        '''
        current_dir = Path(__file__).resolve().parent
        base_info = '{0}{1}'.format(current_dir, GenFormModel.CONFIG)
        CfgCLI.__init__(self, base_info, verbose=verbose)
        verbose_message(GenFormModel.GEN_VERBOSE, verbose, 'init tool info')
        self.logger = ATSLogger(
            GenFormModel.GEN_VERBOSE.lower(),
            '{0}{1}'.format(current_dir, GenFormModel.LOG),
            verbose=verbose
        )
        if self.tool_operational:
            self.add_new_option(
                GenFormModel.OPS[0], GenFormModel.OPS[1], dest='gen',
                help='generate form model'
            )
            self.add_new_option(
                GenFormModel.OPS[2], GenFormModel.OPS[3],
                action='store_true', default=False,
                help='activate verbose mode for generation'
            )
            self.add_new_option(
                GenFormModel.OPS[4], action='version', version=__version__
            )

    def process(self, verbose=False):
        '''
            Process and run operation.

            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :return: boolean status, True (success) | False.
            :rtype: <bool>
            :exceptions: None
        '''
        status = False
        if self.tool_operational:
            num_of_args_sys = len(sys.argv)
            if num_of_args_sys > 1:
                operation = sys.argv[1]
                if operation not in GenFormModel.OPS:
                    sys.argv.append('-h')
            else:
                sys.argv.append('-h')
            args = self.parse_args(sys.argv[1:])
            current_dir = Path(__file__).resolve().parent
            form_file = '{0}/{1}{2}'.format(
                current_dir, getattr(args, 'gen'), '.py'
            )
            form_file_exist = Path(form_file).exists()
            if not form_file_exist:
                if bool(getattr(args, 'gen')):
                    print(
                        '{0} {1} [{2}]'.format(
                            '[{0}]'.format(GenFormModel.GEN_VERBOSE.lower()),
                            'generating form', getattr(args, 'gen')
                        )
                    )
                    generator = GenForm(
                        verbose=getattr(args, 'verbose') or verbose
                    )
                    status = generator.gen_form(
                        '{0}'.format(getattr(args, 'gen')),
                        verbose=getattr(args, 'verbose') or verbose
                    )
                    if status:
                        success_message(GenFormModel.GEN_VERBOSE, 'done\n')
                        self.logger.write_log(
                            '{0} {1} done'.format(
                                'generating form', getattr(args, 'gen')
                            ), ATSLogger.ATS_INFO
                        )
                    else:
                        error_message(
                            GenFormModel.GEN_VERBOSE, 'generation failed'
                        )
                        self.logger.write_log(
                            'generation failed', ATSLogger.ATS_ERROR
                        )
                else:
                    error_message(
                        GenFormModel.GEN_VERBOSE, 'provide form name'
                    )
                    self.logger.write_log(
                        'provide form name', ATSLogger.ATS_ERROR
                    )
            else:
                error_message(
                    GenFormModel.GEN_VERBOSE, 'form already exists'
                )
                self.logger.write_log(
                    'form already exist', ATSLogger.ATS_ERROR
                )
        else:
            error_message(
                GenFormModel.GEN_VERBOSE, 'tool is not operational'
            )
            self.logger.write_log(
                'tool is not operational', ATSLogger.ATS_ERROR
            )
        return status

    def __str__(self):
        '''
            Dunder method for GenFormModel.

            :return: object in a human-readable format.
            :rtype: <str>
            :exceptions: None
        '''
        return '{0} ({1}, {2})'.format(
            self.__class__.__name__, CfgCLI.__str__(self), str(self.logger)
        )
