"""Procedural generation of main sequence stars.

For details see :doc:`/star_generation`.
"""
import math
import random
import typing

import pint

from ...util.random import power_distribution
from ...world import CONST_BOLTZMAN_SIGMA, UNITS
from ...world.celestial import base, planet


_LUM_SUN: pint.Quantity = 382.8e24 * UNITS.watt
_TEMP_SUN: pint.Quantity = 5772.0 * UNITS.kelvin
_MASS_SUN: pint.Quantity = 1988500e24 * UNITS.kg


class MainSequenceStar(base.LuminousCelestialBody[planet.Planet]):
    """Class describing a main sequence star.

    For background information about how the properties of the star are
    derived from its mass alone.

    :param mass: the star's mass
    :type mass: pint.Quantity['mass']
    """

    def __init__(
        self,
        mass: pint.Quantity,
    ) -> None:
        """Initialize a new instance of a star."""
        super().__init__()
        self._mass: pint.Quantity = mass
        self._luminosity: typing.Optional[pint.Quantity] = None
        self._temperature: typing.Optional[pint.Quantity] = None
        self._radius: typing.Optional[pint.Quantity] = None

    @property
    def luminosity(self) -> pint.Quantity:
        """Return the luminosity of the star.

        This method uses the mass-luminosity relation to derive the luminosity from the mass.

        :return: the star's luminosity
        :rtype: pint.Quantity['energy']
        """
        if self._luminosity is None:
            m_rel = self._mass / _MASS_SUN
            prefactor: float = 0.0
            exponent: float = 1.0

            if m_rel < 0.43:
                prefactor = 0.23
                exponent = 2.3
            elif m_rel < 2.0:
                prefactor = 1.0
                exponent = 4.0
            elif m_rel < 55.0:
                prefactor = 1.4
                exponent = 3.5
            else:
                prefactor = 32.0e3
                exponent = 1.0
            self._luminosity = _LUM_SUN * prefactor * m_rel ** exponent
        return self._luminosity

    @property
    def temperature(self) -> pint.Quantity:
        """Return the star's temperature.

        This method uses the simple fit from Section 'Surface Temperature' in :doc:`/star_generation`.

        :return: the star's temperature.
        :rtype: pint.Quantity['temperature']
        """
        m_rel = self._mass / _MASS_SUN
        if self._temperature is None:
            self._temperature = 1.089 * _TEMP_SUN * m_rel ** 0.47
        return self._temperature

    @property
    def radius(self) -> pint.Quantity:
        """Return the estimated radius of the star.

        This method uses the star's luminosity and temperature to compute its radius.

        :return: the star's radius
        :rtype: pint.Quantity['length']
        """
        if self._radius is None:
            e_radiated = 4.0 * math.pi * CONST_BOLTZMAN_SIGMA
            self._radius = (self.luminosity / e_radiated) ** 0.5
        return self._radius

    @property
    def mass(self) -> pint.Quantity:
        r"""Return the estimated mass of the star.

        :return: the mass of the star
        :rtype: pint.Quantity['mass']
        """
        return self._mass


def generate_random_star(rng: random.Random, lower_m_rel: float = 0.06, upper_m_rel: float = 120.0) -> MainSequenceStar:
    """Generate a Main-Sequence star randomly according to a fitted distribution.

    :param rng: the random number generator
    :type rng: random.Random
    :param lower_m_rel: the lower bound mass (relative to the solar mass), defaults to 0.06
    :type lower_m_rel: float
    :param upper_m_rel: the upper bound mass (relative to the solar mass), defaults to 120.0
    :type upper_m_rel: float

    :return: the newly generate star
    :rtype: MainSequenceStar
    """
    mass = power_distribution(-2.61, lower_m_rel, upper_m_rel, rng) * _MASS_SUN
    return MainSequenceStar(mass)
