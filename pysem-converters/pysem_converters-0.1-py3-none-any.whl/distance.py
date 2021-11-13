from typing import Union

import pint

METER = 'meter'
CENTIMETER = 'centimeter'
MILLIMETER = 'millimeter'
KILOMETER = 'kilometer'
INCH = 'inch'
HAND = 'hand'
FOOT = 'foot'
YARD = 'yard'
MILE = 'mile'
LIGHT_YEAR = 'light_year'
ASTRONOMICAL_UNIT = 'astronomical_unit'
PARSEC = 'parsec'
NAUTICAL_MILE = 'nautical_mile'
ANGSTROM = 'angstrom'
MICRON = 'micron'
PLANCK_LENGTH = 'planck_length'


def convert(
        distance: Union[int, float],
        unit: Union[
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
    Converts a distance unit to other different unit

    :param distance:
    :param unit:
    :param unit_to:
    :return:
    """

    return pint.Quantity(distance, unit).to(unit_to)
