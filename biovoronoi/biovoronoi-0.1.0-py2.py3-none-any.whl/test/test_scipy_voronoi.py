import numpy as np
from scipy.spatial import Voronoi, ConvexHull
import unittest


class TestVoronoi(unittest.TestCase):
    def setUp(self) -> None:
        self.eight_points_unit_cell = np.array(
            [
                [0, 0, 0],
                [0, 1, 0],
                [1, 0, 0],
                [1, 1, 0],
                [0, 0, 1],
                [0, 1, 1],
                [1, 0, 1],
                [1, 1, 1],
            ],
            dtype=np.float64,
        )
        self.cells_of_3x3x3 = np.array(
            [[x, y, z] for z in [0, 1, 2] for y in [0, 1, 2] for x in [0, 1, 2]]
        )
        return super().setUp()

    # scipy.spatial.Voronoi need 5 or more points
    @unittest.expectedFailure
    def test_two_points(self):
        source = np.array([[1, 1, 1], [0, 0, 0]], dtype=np.float32)
        voronoi_object = Voronoi(source)
        voronoi_vertices = voronoi_object.vertices

        expected = np.array([[0.5, 0.5, 0.5]], dtype=np.float32)
        np.testing.assert_array_equal(expected, voronoi_vertices)

    @unittest.expectedFailure
    def test_six_points_with_two_dimention(self):
        """Test situation
        x mean a point.
        axis_z
        | x   x   x
        |
        | x   x   x
        ----------axis_y

        "0" represent expected point
        axis_z
        | x   x   x
        |   0   0
        | x   x   x
        ----------axis_y
        Failed with Error: QH6013 qhull input error:
            input is less than 4-dimensional since
            all points have the same x coordinate    0
        """
        source = np.array(
            [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [0, 2, 0], [0, 2, 1]],
            dtype=np.float64,
        )
        voronoi_object = Voronoi(source)
        voronoi_vertices = voronoi_object.vertices

        expected = np.array(
            [
                [0, 0.5, 0.5],
                [0, 0.5, 1.5],
            ],
            dtype=np.float64,
        )
        np.testing.assert_array_equal(expected, voronoi_vertices)

    def test_eight_points_with_three_dimention(self):
        """a unit cube input
        Return the center of the cube.

        """
        voronoi_object = Voronoi(self.eight_points_unit_cell)
        voronoi_vertices = voronoi_object.vertices

        expected = np.array([[0.5, 0.5, 0.5]], dtype=np.float64)

        np.testing.assert_array_equal(expected, voronoi_vertices)

    @unittest.expectedFailure
    def test_voronoi_volume_with_2x2_cell(self):
        voronoi_object = Voronoi(self.eight_points_unit_cell)
        convex = ConvexHull(
            voronoi_object.vertices[
                voronoi_object.regions[voronoi_object.point_region[1]]
            ]
        )
        print(convex.volume)

    def test_voronoi_volume_with_3x3x3_cell(self):
        voronoi_object = Voronoi(self.cells_of_3x3x3)
        convex = ConvexHull(
            voronoi_object.vertices[
                voronoi_object.regions[voronoi_object.point_region[13]]
            ]
        )
        expected = float(1.0)
        self.assertEqual(expected, convex.volume)
