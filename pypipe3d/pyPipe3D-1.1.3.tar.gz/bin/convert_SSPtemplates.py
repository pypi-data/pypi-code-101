#!/usr/bin/env python3
import sys
from os.path import basename
from pyFIT3D.common.io import ReadArguments
from auto_ssp_new import new_SSPModels

class ReadArgumentsLocal(ReadArguments):
    """
    Argument parser for the emission-lines fit scripts.

    To add an argument to the script:
        Argument name in `__mandatory__` or `__optional__` list.
        Argument conversion function in `__mandatory_conv_func___` or `__optional_conv_func___` list.
        Argument default value (if not mandatory) in `__def_optional__`
    """
    # class static configuration:
    # arguments names and conversion string to number functions
    __script_name__ = basename(sys.argv[0])
    __mandatory__ = ['filename']
    __optional__ = ['label', 'output_path']
    __arg_names__ = __mandatory__ + __optional__
    __N_tot_args__ = len(__arg_names__)
    # default values of optional arguments with __optional__ as keys
    __def_optional__ = {'label': 'new', 'output_path': '.'}

    # parse functions
    __conv_func_mandatory__ = {'filename': str}
    __conv_func_optional__ = {'n': int, 'extlaw': str, 'label': str, 'output_path': str}
    __conv_func__ = __conv_func_mandatory__.copy()
    __conv_func__.update(__conv_func_optional__)

    # usage message
    __usage_msg__ = 'usage: {} SSP_FILENAME'.format(__script_name__)
    __usage_msg__ += ' [OUTPUT_LABEL={}]'.format(__def_optional__['label'])
    __usage_msg__ += ' [OUTPUT_PATH={}]'.format(__def_optional__['output_path'])

    def __init__(self, args_list=None, verbose=False):
        ReadArguments.__init__(self, args_list, verbose=verbose)

if __name__ == '__main__':
    pa = ReadArgumentsLocal()
    ssp = new_SSPModels(pa.filename)
    ssp.output_new_FITS(label=pa.label, path=pa.output_path)
