#!/usr/bin/env python3
# -*- coding: utf-8 -*-
u"""
"""


__author__ = "Iván Arias Rodríguez"
__copyright__ = "Copyright 2017, Iván Arias Rodríguez"
__credits__ = [""]
__license__ = "GPL"  # No estoy seguro
__version__ = "1.0.1"
__maintainer__ = "Iván Arias Rodríguez"
__email__ = "ivan.arias.rodriguez@gmail.com"
__status__ = "Development"  # "Prototype", "Production"


class Lema:
    u"""

    """

    def __init__(self, lema_txt, entradas):
        self._lema_txt = lema_txt
        self._entradas = entradas

    def get_lema_txt(self):
        return self._lema_txt

    def get_entradas(self):
        return self._entradas

    def append_entradas(self, entradas):
        self._entradas = sorted(self._entradas + entradas, key=lambda e: e.get_n_entrada())
