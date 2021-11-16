"""Data model of the simulated world."""
import math

import pint


UNITS: pint.UnitRegistry = pint.UnitRegistry(system='mks')

CONST_PLANK_H: pint.Quantity = 6.62607015e-34 * UNITS.joule * UNITS.second
CONST_SPEED_OF_LIGHT: pint.Quantity = 2.99792458e8 * UNITS.meter / UNITS.second
CONST_BOLTZMANN_K: pint.Quantity = 1.380649e-23 * UNITS.joule / UNITS.kelvin
CONST_BOLTZMAN_SIGMA: pint.Quantity = (
    2.0 * math.pi ** 5 * CONST_BOLTZMANN_K ** 4 / (15 * CONST_PLANK_H ** 3 * CONST_SPEED_OF_LIGHT ** 2)
)
