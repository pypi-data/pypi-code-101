__desc__ = "A python library for generating beizer curves."
__version__ = "0.0.1"

import math
import random

import numpy as np


def beizer_curve(
    points,
    output_points_count: int,
    destructive: bool = False,
    dtype: np.dtype = np.int32,
):
    """
    Generate a beizer curve.

     - points - Knots in format: [[x1, x2, ..., xn], [y1, y2, ..., yn], [z1, z2, ..., zn]].
     - output_points_count - How many points of the curve to generate.
     - destructive - Allow function to modify points array. Don't set to true, if you want to use
    points array later.
     - dtype - dtype array of returned points of the curve.

    Points of a curve are returned in format: [[x1, x2, ..., xn], [y1, y2, ..., yn], [z1, z2, ..., zn]],
    where n is output_points_count.
    """
    n = len(points[0])
    if not n >= 2:
        raise ValueError(
            "You need at least 2 points to draw a line and at least 3 to draw a curve"
        )
    coordinates_count = len(points)

    # Starting point has to be at (0, 0) for the algorithm to work correctly
    _points = np.array(points, dtype=dtype, copy=not destructive)
    offset = np.vstack(_points[:, 0])

    _points -= offset

    def get_point(t, coordinate):
        nonlocal _points, n
        if not (t >= 0 and t <= 1):
            raise ValueError("t has to belong to [0; 1] interval")

        t_1 = 1 - t

        _t = np.empty(n)  # t in i-th power
        _t[0] = 1
        for i in range(1, n):
            _t[i] = _t[i - 1] * t

        _t_1 = np.empty(n)  # (1 - t) in (n - 1 - i)-th power
        _t_1[-1] = 1
        for i in range(n - 2, 0, -1):
            _t_1[i] = _t_1[i + 1] * t_1

        _res = np.empty(n)
        _res[0] = _t_1[0] * _points[coordinate][0]
        for i in range(1, n - 1):
            _res[i] = _points[coordinate][i] * _t[i] * _t_1[i] * (n - 1)
        _res[-1] = _t[-1] * _points[coordinate][-1]
        return _res.sum()

    out = np.empty((coordinates_count, output_points_count), dtype=dtype)
    ts = np.linspace(0, 1, output_points_count)
    for coordinate in range(coordinates_count):
        for i in range(output_points_count):
            out[coordinate][i] = get_point(ts[i], coordinate)

    out += offset
    return out


def point_distance(start_point, end_point):
    if not isinstance(start_point, np.ndarray):
        start_point = np.array(start_point, copy=False)
    if not isinstance(end_point, np.ndarray):
        end_point = np.array(end_point, copy=False)
    return math.sqrt(np.sum((start_point - end_point) ** 2))


def generate_random_points_in_rectangle(
    start_point,
    end_point,
    random_points_count: int,
    point_spread: float = 1,
    include_start_end: bool = True,
    float_random_numbers: bool = False,
):
    if len(start_point) != len(end_point):
        raise ValueError("Invalid start and end points passed")
    if point_spread <= 0:
        raise ValueError("Point spread has to be greater than 0 ")

    coordinates_count = len(start_point)

    rng = random.uniform if float_random_numbers else random.randrange

    random_lower_bounds = np.empty(coordinates_count)
    random_upper_bounds = np.empty(coordinates_count)
    point_spread -= 1
    for i in range(coordinates_count):
        if start_point[i] < end_point[i]:
            dimension = end_point[i] - start_point[i]
            random_lower_bounds[i] = start_point[i]
            random_upper_bounds[i] = end_point[i]
        else:
            dimension = start_point[i] - end_point[i]
            random_lower_bounds[i] = end_point[i]
            random_upper_bounds[i] = start_point[i]
        bound_offset = dimension * point_spread / 2
        random_lower_bounds[i] -= bound_offset
        random_upper_bounds[i] += bound_offset

    points_count = random_points_count + 2 * include_start_end
    points = np.empty((coordinates_count, points_count))
    if include_start_end:
        for coordinate in range(coordinates_count):
            points[coordinate][0] = start_point[coordinate]
            points[coordinate][-1] = end_point[coordinate]
    for coordinate in range(coordinates_count):
        for i in range(include_start_end, points_count - include_start_end):
            points[coordinate][i] = rng(
                random_lower_bounds[coordinate], random_upper_bounds[coordinate]
            )

    return points


def add_noise_to_curve(points, max_offset, rate, float_random_numbers: bool = False):
    if max_offset == 0:
        return points
    rng = random.uniform if float_random_numbers else random.randrange

    coordinates_count = len(points)
    points_count = len(points[0])
    for coordinate in range(coordinates_count):
        for i in range(points_count):
            if rate > random.random():
                offset = rng(-max_offset, max_offset)
                points[coordinate][i] += offset
    return points


def random_beizer_curve(
    start_point,
    end_point,
    output_points_count: int,
    random_points_count: int = 1,
    point_spread: float = 1,
    noise_max_offset: float = 0,
    noise_rate: float = 0.5,
    dtype=np.int32,
    return_forming_points: bool = False,
):
    """
    Generate a random beizer curve, which starts at start_point and ends at end_point.

     - start_point, end_point - coordinates of start and end points of curve in format [x, y, z, ...].
     - output_points_count - How many points of the curve to generate.
    if output_points_count < 0:
        output_points_count = math.ceil(distance / -output_points_count)
    Where distance is distance between start and end.
     - random_points_count - How many knots to generate.
     - point_spread - A scale of a rectangular figure with corners of start_point and end_point,
    in bounds of which random knots are generated. Has to be > 0.
     - noise_max_offset - Max offset of a curve point if > 0
     - noise_rate - A part of curve points to apply noise offset to. Has to belong to [0; 1].
    if noise_max_offset < 0:
        noise_max_offset = math.ceil(distance / -noise_max_offset)
    Where distance is distance between start and end.
     - dtype - dtype array of returned points of the curve.
     - return_forming_points - return points, curve if return_forming_points else curve, where points are randomly generated knots
    """
    floats = np.issubdtype(dtype, np.integer)
    distance = point_distance(start_point, end_point)
    if output_points_count < 0:
        output_points_count = math.ceil(distance / -output_points_count)
    if noise_max_offset < 0:
        noise_max_offset = math.ceil(distance / -noise_max_offset)
    points = generate_random_points_in_rectangle(
        start_point,
        end_point,
        random_points_count,
        point_spread,
        True,
        float_random_numbers=floats,
    )
    curve = add_noise_to_curve(
        beizer_curve(
            points,
            output_points_count,
            destructive=not return_forming_points,
            dtype=dtype,
        ),
        noise_max_offset,
        noise_rate,
        float_random_numbers=floats,
    )
    return points, curve if return_forming_points else curve
