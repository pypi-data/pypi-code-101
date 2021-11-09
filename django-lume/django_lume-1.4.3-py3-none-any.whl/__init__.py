# -*- coding: utf-8 -*-
# pylint: disable=unused-import

import inspect

from django.db import models

from .kentta import EI_ASETETTU, Lumekentta
from . import puukko

# Periytä lumeversio kustakin Djangon kenttätyypistä.
for nimi, luokka in inspect.getmembers(
  models, lambda x: inspect.isclass(x) and issubclass(x, models.Field)
):
  globals()[nimi] = type(nimi, (Lumekentta, luokka), {})
del inspect
del models


def __dir__():
  ''' PEP 562: dynaaminen luettelo moduulin tarjoamasta sisällöstä. '''
  return [
    nimi
    for nimi, luokka in inspect.getmembers(
      models, lambda x: inspect.isclass(x) and issubclass(x, models.Field)
    )
  ]
  # def __dir__
