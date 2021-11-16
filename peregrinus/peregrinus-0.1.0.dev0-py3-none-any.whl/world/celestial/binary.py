"""Data model of a binary or multiple star system."""
import typing

import pint

from . import base


class BinaryStar(base.CenterOfGravity):
    """A generalized binary star system.

    A generalized binary star system is a hierarchical multi-star system with two components, where each component
    is either a generalized binary star system or a single star.

    :param components: the components of the binary star system
    :type components: typing.Tuple[typing.Union[BinaryStar, base.LuminousCelestialBody],
                                   typing.Union[BinaryStar, base.LuminousCelestialBody]]
    :param orbital_elements: the geometry of the orbit between the two components
    :type orbital_elements: base.OrbitalElements
    """

    def __init__(
        self,
        components: typing.Tuple[
            typing.Union['BinaryStar', 'base.LuminousCelestialBody'],
            typing.Union['BinaryStar', 'base.LuminousCelestialBody'],
        ],
        orbital_elements: base.OrbitalElements,
    ) -> None:
        """Initialize a new instance of this class.

        :param components: the components of the binary star system
        :type components: typing.Tuple[typing.Union[BinaryStar, base.LuminousCelestialBody],
                                       typing.Union[BinaryStar, base.LuminousCelestialBody]]
        :param orbital_elements: the geometry of the orbit between the two components
        :type orbital_elements: base.OrbitalElements
        """
        super().__init__()
        self.satellites.append(BinaryStar._mkorbit(components, orbital_elements))
        self._components: typing.Tuple[
            typing.Union[BinaryStar, base.LuminousCelestialBody], typing.Union[BinaryStar, base.LuminousCelestialBody]
        ] = components

    @property
    def mass(self) -> pint.Quantity:
        """Return the total mass of the binary star system.

        :return: the sum of the masses of the components
        :rtype: pint.Quantity['mass']
        """
        return sum(component.mass for component in self.components)

    @property
    def components(
        self,
    ) -> typing.Tuple[
        typing.Union['BinaryStar', base.LuminousCelestialBody], typing.Union['BinaryStar', base.LuminousCelestialBody]
    ]:
        """Return the components of this binary star system.

        :return: the components of the binary star system
        :rtype: typing.Tuple[typing.Union[BinaryStar, base.LuminousCelestialBody],
                             typing.Union[BinaryStar, base.LuminousCelestialBody]]
        """
        return self._components

    @staticmethod
    def _mkorbit(
        components: typing.Tuple[
            typing.Union['BinaryStar', base.LuminousCelestialBody],
            typing.Union['BinaryStar', base.LuminousCelestialBody],
        ],
        orbital_elements: base.OrbitalElements,
    ) -> base.Orbit[typing.Union['BinaryStar', base.LuminousCelestialBody]]:
        """Create a new orbit object with the components as host and satellite.

        :param components: the components of the binary star system
        :type components: typing.Tuple[typing.Union[BinaryStar, base.LuminousCelestialBody],
                          typing.Union[BinaryStar, base.LuminousCelestialBody]]
        :param orbital_elements: the geometry of the orbit between the two components
        :type orbital_elements: base.OrbitalElements
        :return: a new orbit with the components as host and satellite
        :rtype: base.Orbit[typing.Union[BinaryStar, base.LuminousCelestialBody]]
        """
        _, satellite = components
        return base.Orbit(satellite, orbital_elements)
