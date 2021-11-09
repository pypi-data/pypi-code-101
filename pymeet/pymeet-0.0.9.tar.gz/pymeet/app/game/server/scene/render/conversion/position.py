from typing import Tuple


def unit_to_pixel(position: Tuple[float, float]) -> Tuple[float, float]:
    return position[0]*10, position[1]*10


def pixel_to_unit(position: Tuple[float, float]) -> Tuple[float, float]:
    return position[0]/10, position[1]/10
