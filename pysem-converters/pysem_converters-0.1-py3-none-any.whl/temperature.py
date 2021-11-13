from typing import Union

import pint

CELSIUS = "degC"
FAHRENHEIT = "degF"
KELVIN = "kelvin"


def convert(
        temperature: Union[int, float],
        unit: Union[
            CELSIUS,
            FAHRENHEIT,
            KELVIN
        ],
        unit_to: Union[
            CELSIUS,
            FAHRENHEIT,
            KELVIN
        ]
) -> str:
    """
    Converts a temperature unit to other different unit

    :param temperature:
    :param unit:
    :param unit_to:
    :return:
    """

    return pint.Quantity(temperature, unit).to(unit_to)
