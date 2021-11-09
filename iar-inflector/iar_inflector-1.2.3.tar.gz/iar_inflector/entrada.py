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


class Entrada:
    u"""

    """

    def __init__(self, acepciones, locuciones, n_entrada):
        self._acepciones = acepciones
        self._locuciones = locuciones
        self._n_entrada = n_entrada

    def get_entrada(self):
        return {"acepciones": self._acepciones,
                "locuciones": self._locuciones,
                "n_entrada": self._n_entrada}

    def get_acepciones(self):
        return self._acepciones

    def set_acepciones(self, acepciones):
        self._acepciones = acepciones

    def append_acepcion(self, acepcion):
        self._acepciones.append(acepcion)

    def get_locuciones(self):
        return self._locuciones

    def set_locuciones(self, locuciones):
        self._locuciones = locuciones

    def get_n_entrada(self):
        return self._n_entrada

    def set_n_entrada(self, n_entrada):
        self._n_entrada = n_entrada
