"""Base classes for celestial objects and their properties."""
import abc
import dataclasses
import typing

import pint


@dataclasses.dataclass
class OrbitalElements:
    """A class representing the orbital elements of a Kepler orbit.

    :param parameter: the trajectory parameter, typically called 'p'
    :type parameter: pint.Quantity['length']
    :param numeric_eccentricity: numeric eccentricity
    :type numeric_eccentricity: float
    :param inclination: inclination angle
    :type inclination: pint.Quantity[]
    :param longitude_ascending: longitude of the ascending node
    :type longitude_ascending: pint.Quantity[]
    :param arg_periapsis: the argument of the periapsis
    :type arg_periapsis: pint.Quantity[]
    :param true_anomaly: the true anomaly at a globally given epoch time 't0'.
    :type true_anomaly: pint.Quantity[]
    """

    parameter: pint.Quantity
    """the trajectory parameter, typically called 'p'."""

    numeric_eccentricity: float
    """the numeric eccentricity."""

    inclination: pint.Quantity
    """the inclination angle."""

    longitude_ascending: pint.Quantity
    """the longitude of the ascending node."""

    arg_periapsis: pint.Quantity
    """the argument of the periapsis."""

    true_anomaly: pint.Quantity
    """the true anomaly at epoch time."""


SatelliteType = typing.TypeVar('SatelliteType', bound='CenterOfGravity')


class Orbit(typing.Generic[SatelliteType]):
    """A class representing satellites orbiting around a center of gravity.

    The properties include orbital parameters as well as a reference to the
    two gravitationally bound partners, i.e. the central mass and the satellite.

    :param satellite: the satellite surrounding its host
    :type satellite: SatelliteType
    :param orbital_elements: the orbital parameters
    :type orbital_elements: OrbitalElements
    """

    def __init__(
        self,
        satellite: SatelliteType,
        orbital_elements: OrbitalElements,
    ) -> None:
        """Initialize a new instance of the `Orbit` class."""
        self._satellite: SatelliteType = satellite
        self._orbital_elements: OrbitalElements = orbital_elements

    @property
    def satellite(self) -> SatelliteType:
        """Return the satellite.

        :return: the satellite object
        :rtype: SatelliteType
        """
        return self._satellite

    @property
    def orbital_elements(self) -> OrbitalElements:
        """Return the orbital parameters.

        :return: the orbital parameters
        :rtype: OrbitalElements
        """
        return self._orbital_elements


class CenterOfGravity(abc.ABC, typing.Generic[SatelliteType]):
    """A class representing a center of gravity.

    Subclasses of this class include condensed physical objects like planets or stars
    but also composite objects like binary stars.
    """

    def __init__(self) -> None:
        """Initialize a new instance."""
        self._satellites: typing.Sequence[Orbit[SatelliteType]] = []

    @property
    @abc.abstractmethod
    def mass(self) -> pint.Quantity:
        """Return the total mass causing the gravitational attraction.

        This might be the mass of a star, of a binary star system, of a planet
        (attracting a moon).

        :rtype: pint.Quantity['mass']
        """

    @property
    def satellites(self) -> typing.List[Orbit]:
        """Return a sequence of orbits describing the satellites orbiting around this center of gravity.

        The sequence is sorted by the closest distance between the center and the satellite
        from the innermost to the outermost satellite.

        :return: a sequence of orbits describing the satellites orbiting around this center of gravity.
        :rtype: typing.List[Orbit]
        """
        return self._satellites


ColdCelestialBodyType = typing.TypeVar('ColdCelestialBodyType', bound='ColdCelestialBody')


class CelestialBody(CenterOfGravity[ColdCelestialBodyType], typing.Generic[ColdCelestialBodyType]):
    """Physical, roughly spherical celestial body.

    This is the base class of all celestial bodies such as stars, planets or moons.
    """

    @property
    @abc.abstractmethod
    def radius(self) -> pint.Quantity:
        """Return he radius of the object.

        :rtype: pint.Quantity['length']
        """


class LuminousCelestialBody(CelestialBody[ColdCelestialBodyType], typing.Generic[ColdCelestialBodyType]):
    """Celestial bodies which are sources of electromagnetic radiation.

    Purely phenomenological model of a luminous celestial body, defined
    by luminosity and temperature.
    """

    @property
    @abc.abstractmethod
    def luminosity(self) -> pint.Quantity:
        """Return the body's luminosity.

        :rtype: pint.Quantity['energy']
        """

    @property
    @abc.abstractmethod
    def temperature(self) -> pint.Quantity:
        """Return the body's temperature.

        :rtype: pint.Quantity['temperature']
        """


class ColdCelestialBody(CelestialBody[ColdCelestialBodyType], typing.Generic[ColdCelestialBodyType]):
    """Celestial bodies which are cold.

    This class is mainly used as base class of planets and moons.

    :param mass: the mass of the planet
    :type mass: pint.Quantity['mass']
    :param radius: the radius of the planet
    :type mass: pint.Quantity['radius']
    """

    def __init__(
        self,
        mass: pint.Quantity,
        radius: pint.Quantity,
    ) -> None:
        """Initialize an instance of this class."""
        super().__init__()
        self._mass: pint.Quantity = mass
        self._radius: pint.Quantity = radius

    @property
    def radius(self) -> pint.Quantity:
        """Return the radius of the body."""
        return self._radius

    @property
    def mass(self) -> pint.Quantity:
        """Return the mass of the body."""
        return self._mass
