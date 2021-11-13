from typing import Union

import pint

SECONDS = "seconds"
MINUTES = "minutes"
HOURS = "hours"
DAYS = "days"
WEEKS = "weeks"
FORTNIGHTS = "fortnights"
YEARS = "years"
MONTHS = "months"
CENTURIES = "centuries"
MILLENNIUMS = "millenniums"


def convert(
        time: Union[int, float],
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
            MILLENNIUMS
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
            MILLENNIUMS
        ]
) -> str:
    """
    Converts a time unit to other different unit

    :param time:
    :param unit:
    :param unit_to:
    :return:
    """

    return pint.Quantity(time, unit).to(unit_to)
