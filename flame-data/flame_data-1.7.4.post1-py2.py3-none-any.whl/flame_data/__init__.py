# -*- coding: utf-8 -*-

import pathlib

__name__ == 'flame-data'
__version__ = '1.7.4'
__author__ = 'Tong Zhang <zhangt@frib.msu.edu>'
__doc__ ="""Field data for FLAME (pip install flame-code)"""


CWDIR = pathlib.Path(__file__).parent

def get_data_path():
    """Return the full path of cavity_data.
    """
    return CWDIR.joinpath("cavity_data").resolve()
