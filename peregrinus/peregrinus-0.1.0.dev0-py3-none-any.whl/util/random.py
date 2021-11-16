"""Additional functions for random numbers."""

import random


def power_distribution(alpha: float, lower_bound: float, upper_bound: float, rng: random.Random) -> float:
    r"""Draw a random number according to a power law distribution.

    This method draws a single random number within the given interval
    according to a probability
    density function that is proportional to :math:`x^\alpha`.

    :param alpha: the exponent of the probability density function, must not be equal to -1
    :type alpha: float
    :param lower_bound: lower bound of the interval from which the random number is chosen
    :type lower_bound: float
    :param upper_bound: upper bound of the interval from which the random number is chosen
    :type upper_bound: float
    :param rng: the random number generator to be used
    :type rng: random.Random

    :return: the random number
    :rtype: float
    :raises ValueError: if the exponent is set to -1
    """
    if alpha == -1.0:
        raise ValueError('Exponent alpha must not be equal to -1')

    alpha_1 = alpha + 1.0
    rnd_p = rng.random()
    rnd_q = 1.0 - rnd_p
    return (upper_bound ** alpha_1 * rnd_p + lower_bound ** alpha_1 * rnd_q) ** (1.0 / alpha_1)
