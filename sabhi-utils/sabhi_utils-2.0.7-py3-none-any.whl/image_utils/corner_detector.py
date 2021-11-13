from .utils import get_aspect_ratio_check

from sklearn.cluster import KMeans

import numpy as np

import cv2

from collections import defaultdict

import itertools

from .utils import get_bounding_box_points


def get_hough_lines(
    image,
    rho_acc=1,
    theta_acc=180,
    thresh=70,
):
    """
    Extract straight lines from image using Hough Transform.

    Returns
    ----------
    array containing rho and theta of lines (Hess Norm formulation)
    """
    lines = cv2.HoughLines(
        image,
        rho_acc,
        np.pi / theta_acc,
        thresh
    )

    return lines


def segment_by_angle_kmeans(
    lines=None,
    k=2,
    **kwargs
):
    """Groups lines based on angle with k-means.

    Uses k-means on the coordinates of the angle on the unit circle
    to segment `k` angles inside `lines`.
    """
# Define criteria = (type, max_iter, epsilon)
    default_criteria_type = (
        cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER
    )

    criteria = kwargs.get("criteria", (default_criteria_type, 10, 1.0))
    flags = kwargs.get("flags", cv2.KMEANS_RANDOM_CENTERS)
    attempts = kwargs.get("attempts", 5)

    # returns angles in [0, pi] in radians
    angles = np.array(
        [line[0][1] for line in lines]
    )
# multiply the angles by two and find coordinates of that angle
    pts = np.array(
        [[np.cos(2 * angle), np.sin(2 * angle)] for angle in angles],
        dtype=np.float32,
    )

    # run kmeans on the coords
    labels, centers = cv2.kmeans(
        pts, k, None, criteria, attempts, flags)[1:]
    labels = labels.reshape(-1)  # transpose to row vec

    # segment lines based on their kmeans label
    # segmented = list()
    # for i, line in zip(range(len(lines)), lines):
    #    segmented.append(line)
    segmented = defaultdict(list)
    for i, line in zip(range(len(lines)), lines):
        segmented[labels[i]].append(line)

    segmented = list(segmented.values())
    return segmented


def intersection(
    line1,
    line2
):
    """Finds the intersection of two lines given in Hesse normal form.

    Returns closest integer pixel locations.
    See https://stackoverflow.com/a/383527/5087436
    """
    rho1, theta1 = line1[0]
    rho2, theta2 = line2[0]

    A = np.array(
        [[np.cos(theta1), np.sin(theta1)], [
            np.cos(theta2), np.sin(theta2)]]
    )

    b = np.array([[rho1], [rho2]])
    x0, y0 = np.linalg.solve(A, b)
    x0, y0 = int(np.round(x0)), int(np.round(y0))
    return [x0, y0]


def get_intersections(
    lines=None,
):
    """Finds the intersections between groups of lines."""
    intersections = []

    group_lines = list(
        itertools.product(lines[0], lines[1])
    )

    for line_i, line_j in group_lines:
        int_point = intersection(line_i, line_j)
        intersections.append(int_point)

    return np.array(intersections)


def get_optimal_cluster(
    points=None,
    max_k=20
):
    inertia_list = []
    for n_clusters in range(1, max_k+1):
        if len(points) >= n_clusters:
            model = KMeans(
                n_clusters=n_clusters,
                init="k-means++",
                max_iter=100,
                n_init=10,
                random_state=0
            ).fit(points)

            inertia_list.append(model.inertia_)

    k = [i*100 for i in np.diff(inertia_list, 2)].index(
        min(
            [i*100 for i in np.diff(inertia_list, 2)]
        )
    )

    return k


def find_cluster_centers(
    intersections,
    n_clusters=None
):

    if n_clusters is None:
        n_clusters = get_optimal_cluster(points=intersections)

    model = KMeans(
        n_clusters=n_clusters,
        init="k-means++",
        max_iter=100,
        n_init=10,
        random_state=0
    ).fit(intersections)

    return model.cluster_centers_


def unit_vector(vector):
    """ Returns the unit vector of the vector.  """
    norm = np.linalg.norm(vector)
    response = vector / norm
    return response


def angle_between(v1, v2):
    """ Returns the angle in radians between vectors 'v1' and 'v2'::

            >>> angle_between((1, 0, 0), (0, 1, 0))
            1.5707963267948966
            >>> angle_between((1, 0, 0), (1, 0, 0))
            0.0
            >>> angle_between((1, 0, 0), (-1, 0, 0))
            3.141592653589793
    """
    v1_u = unit_vector(v1)
    v2_u = unit_vector(v2)
    if np.isnan(v1_u).any() or np.isnan(v2_u).any():
        print(v1, v2)
        return None

    return np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))


def check_quadrilateral_angles(
    rect,
    threshold=1.39
):
    p1, p2, p3, p4 = rect

    l1 = p2-p1

    l2 = p3-p2

    l3 = p4-p3

    l4 = p1-p4

    pair_lines = [
        (l1, l2),
        (l2, l3),
        (l3, l4)
    ]

    sum_of_angles = 0
    for line_1, line_2 in pair_lines:
        angle = (
            angle_between(
                line_1,
                line_2
            )
        )

        if angle is None or angle < threshold:
            return None
        sum_of_angles = sum_of_angles + angle

        if (2*np.pi - sum_of_angles) < threshold:
            return None

    return True


def get_max_width(
    rect
):
    (tl, tr, br, bl) = rect
    # compute the width of the new image, which will be the
    # maximum distance between bottom-right and bottom-left
    # x-coordiates or the top-right and top-left x-coordinates
    widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
    widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
    maxWidth = max(int(widthA), int(widthB))

    return maxWidth


def get_max_height(
    rect
):
    (tl, tr, br, bl) = rect
    # compute the height of the new image, which will be the
    # maximum distance between the top-right and bottom-right
    # y-coordinates or the top-left and bottom-left y-coordinates
    heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
    heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
    maxHeight = max(int(heightA), int(heightB))

    return maxHeight


def check_aspect_ratio(
    rect,
    aspect_ratio=16/10
):

    response = None

    maxWidth = get_max_width(rect)

    maxHeight = get_max_height(rect)

    aspect_ratio_check = get_aspect_ratio_check(
        height=maxHeight,
        width=maxWidth,
        aspect_ratio=aspect_ratio,
        threshold=.05
    )

    if aspect_ratio_check:
        response = True

    return response


def check_quadrilateral(
    two_line_segments,
    checks=[
        check_quadrilateral_angles,
        check_aspect_ratio
    ]
):
    response = None
    pts = np.array(
        [point for segment in two_line_segments for point in segment]
    )

    rect = get_bounding_box_points(pts)

    unique = np.unique(rect, axis=0)

    if len(unique) < rect.shape[0]:
        return None
    for checker in checks:
        check_response = checker(rect)
        if check_response is None:
            return response

    return True


def get_convex_quadrilaterals(
    points,
    check=check_quadrilateral
):
    """
    Generate the convex quadrilaterals among points on a 2D Surface (np.array).
    """
    points = [point for point in points]
    # points = map(np.array, points)
    segments = itertools.combinations(points, 2)

    for s0, s1 in itertools.combinations(segments, 2):
        response = check((s0, s1))
        if response is not None:
            yield s0, s1


def get_points_from_quad(quad):
    pts = np.array(
        [point for segment in quad for point in segment]
    )
    rect = get_bounding_box_points(pts)
    return rect


def get_convex_quad_array(convex_quads):
    return map(get_points_from_quad, convex_quads)


def get_bounding_box_quad(
    convex_quadrilateals=None
):
    convex_quads_pts = get_convex_quad_array(
        convex_quadrilateals
    )
    max_quad = []
    max_area = 0
    for quad in convex_quads_pts:
        area = get_max_width(quad)*get_max_height(quad)
        if area > max_area:
            max_area = area
            max_quad = quad

    return max_quad
