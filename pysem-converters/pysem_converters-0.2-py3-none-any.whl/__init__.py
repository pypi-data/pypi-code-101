from .objects import *

from .distance import METER, CENTIMETER, MILLIMETER, KILOMETER, INCH, HAND, FOOT, YARD, MILE, LIGHT_YEAR, ASTRONOMICAL_UNIT, PARSEC, NAUTICAL_MILE, ANGSTROM, MICRON, PLANCK_LENGTH
from .temperature import CELSIUS, FAHRENHEIT, KELVIN
from .time import SECONDS, MINUTES, HOURS, DAYS, WEEKS, FORTNIGHTS, YEARS, MONTHS, CENTURIES, MILLENNIUMS


def converter(
        value: Union[int, float],
        unit: Union[
            SECONDS,
            MINUTES,
            HOURS,
            DAYS,
            WEEKS,
            FORTNIGHTS,
            YEARS,
            MONTHS,
            CENTURIES,
            MILLENNIUMS,
            CELSIUS,
            FAHRENHEIT,
            KELVIN,
            'METER',
            'CENTIMETER',
            'MILLIMETER',
            'KILOMETER',
            'INCH',
            'HAND',
            'FOOT',
            'YARD',
            'MILE',
            'LIGHT_YEAR',
            'ASTRONOMICAL_UNIT',
            'PARSEC',
            'NAUTICAL_MILE',
            'ANGSTROM',
            'MICRON',
            'PLANCK_LENGTH'
        ],
        unit_to: Union[
            SECONDS,
            MINUTES,
            HOURS,
            DAYS,
            WEEKS,
            FORTNIGHTS,
            YEARS,
            MONTHS,
            CENTURIES,
            MILLENNIUMS,
            CELSIUS,
            FAHRENHEIT,
            KELVIN,
            'METER',
            'CENTIMETER',
            'MILLIMETER',
            'KILOMETER',
            'INCH',
            'HAND',
            'FOOT',
            'YARD',
            'MILE',
            'LIGHT_YEAR',
            'ASTRONOMICAL_UNIT',
            'PARSEC',
            'NAUTICAL_MILE',
            'ANGSTROM',
            'MICRON',
            'PLANCK_LENGTH'
        ]
) -> str:
    """
    Converts a time, temperature or distance unit to other different unit

    :param value:
    :param unit:
    :param unit_to:
    :return:
    """

    return pint.Quantity(value, unit).to(unit_to)
