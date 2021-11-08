from typing import List, Tuple

from .point import Point


class Utils:
    def __init__(self) -> None:
        pass

    @staticmethod
    def to_mspoints(
            rawpoints: List[Tuple[float]] = [],
            sort_by_intensity_asc: bool = False,
            sort_by_intensity_desc: bool = False
         ) -> List[Point]:
        """
        Converts a list of tuples that contain floats into
        a list of Points.

        Args:
            rawpoints (List[Tuple[float]], optional): The list of raw data.
            Defaults to [].
            sort_by_intensity_asc (bool, optional): Whether or not to have the
            returned list of points sorted by increasing intensity.
            Defaults to False.
            sort_by_intensity_desc (bool, optional): Whether or not to have the
            returned list of points sorted by decreasing intensity.
            Defaults to False.

        Returns:
            List[Point]: the converted list of Points.
        """

        # TODO: We could have a better sorting/ordering system here

        points = []
        for pt in rawpoints:
            converted = Point(mz=pt[0], rt=pt[1], intensity=pt[2])
            points.append(converted)

        if sort_by_intensity_asc:
            return sorted(points, key=lambda pt: pt.intensity)
        if sort_by_intensity_desc:
            return sorted(points, key=lambda pt: pt.intensity, reverse=True)

        return points

    @staticmethod
    def to_ndarray(
            points: List[Point],
            attributes_to_include: List[str] = ['mz', 'rt', 'intensity']
         ) -> List[List[float]]:
        """
        Converts a list of Points to a two dimensional list of floats.

        Args:
            points (List[Point], optional): [description].
            Defaults to [].
            attributes_to_include (List[str], optional): [description].
            Defaults to ['mz', 'rt', 'intensity'].

        Returns:
            List[List[float]]: The converted ndarray.
        """
        ndarray = []
        for pt in points:
            pt_as_list = pt.to_list(attributes=attributes_to_include)
            ndarray.append(pt_as_list)

        return ndarray

    @staticmethod
    def pluck_dimension(
            points: List[Point],
            dimension: str = 'mz'
         ) -> List[float]:
        """
        Plucks a single dimension from a list of points.

        Args:
            points (List[Point]): The Points you wish to convert.
            dimension (str, optional): The dimension you wish to pluck.
            Can be one of 'mz', 'rt', or 'intensity'. Defaults to 'mz'.

        Returns:
            List[float]: List of float values representing
            the plucked dimension.
        """
        # TODO: Pretty naive, def a better way of doing this.
        plucked = []
        for pt in points:
            if dimension == 'mz':
                plucked.append(pt.mz)
            if dimension == 'rt':
                plucked.append(pt.rt)
            if dimension == 'intensity':
                plucked.append(pt.intensity)

        return plucked
