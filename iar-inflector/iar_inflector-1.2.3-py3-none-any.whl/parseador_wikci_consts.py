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


DEBUG = False
# SÓLO ARTÍCULOS ESPAÑOLES
# Los artículos con contenido de palabras españolas tienen dos tipos de marca:
# - "Nueva": == {{lengua|es}} ==
MARCA_ESPANOLA_NUEVA_REGEX = u'== ?\{\{lengua\|es\}\} ?=='
# - "Antigua": {{ES}}, {{ES|palabra}}, {{ES||2}}. También hay traducciones {{ES-PT}} y otras cosas,
# pero no interesan.
MARCA_ESPANOLA_ANTIGUA_REGEX = u'\{\{ES(\|[^\}\|]*){0,2}\}\}'
MARCA_ESPANOLA_REGEX = u'(' + MARCA_ESPANOLA_NUEVA_REGEX + u')|(' + MARCA_ESPANOLA_ANTIGUA_REGEX + u')'

# Marca el inicio de acepción de cualquier idioma
MARCA_ENTRADA_REGEX = u'((== ?\{\{lengua(\|[^\}]+)?\}\} ?==)|' \
                      u'(((?<=^)|(?<=\n)|(?<=^\s)|(?<=\n\s)|(?<=^\s\s)|(?<=\n\s\s))' \
                      u'\{\{((([A-ZÑ]{2,3})(-([A-ZÑ]{2,})){0,2})|(TRANSLIT))(\|[^\}]*)?\}\}))'

