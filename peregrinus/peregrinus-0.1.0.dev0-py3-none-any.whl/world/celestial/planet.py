"""Data model of a planet."""
from . import base, moon


class Planet(base.ColdCelestialBody[moon.Moon]):
    """Class describing a planet."""
