"""Data model of a planet."""


class Planet:
    """
    Interface of a planet.

    :param radius: the radius of the (perfectly spherical) planet in meter
    :type radius: float

    Example
    -------

    >>> from peregrinus.world.celestial.planet import Planet
    >>> earth = Planet(radius = 35.0)
    >>> print(earth.radius)
    35.0

    """

    def __init__(self, radius: float) -> None:
        """Initialize a new instance of the class `Planet`."""
        self._radius: float = radius

    @property
    def radius(self: 'Planet') -> float:
        """Return the radius of the planet.

        :return: radius of the planet in meter.
        :rtype: float
        """
        return self._radius
