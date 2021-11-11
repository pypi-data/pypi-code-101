from PIL import Image
import cv2
from sabhi_utils.utility import initial_logger
from sabhi_utils.utility import check_and_read_gif, get_image_file_list
import imutils
import numpy as np
import base64
from math import sqrt, ceil, floor

from sklearn.cluster import KMeans

import numpy as np
import cv2

from typing import Union
from typing import Tuple

import urllib.request
import base64

import operator

logger = initial_logger()


def get_image(image_path, resize_width=None):

    img, flag = check_and_read_gif(image_path)
    if not flag:
        img = cv2.imread(image_path)

        if resize_width:
            img = imutils.resize(img, width=resize_width)
        return img
    if img is None:
        logger.info("error in loading image:{}".format(image_path))


def get_hsv_means_for_windows(image, N_h=5, N_w=10, debug=False):

    h_means = []
    s_means = []
    image_slices = slice_image(image, row=N_w, col=N_h)
    for slice in image_slices:
        slice_cv = cv2.cvtColor(np.array(slice), cv2.COLOR_RGB2HSV)
        if debug:
            cv2.imshow("slice_cv", slice_cv)
            cv2.waitKey(0)
        h, s, _ = cv2.split(slice_cv)
        h_means.append(h.mean())
        s_means.append(s.mean())

    return np.column_stack((h_means, s_means))


def calc_columns_rows(n):
    """
    Calculate the number of columns and rows required to divide an image
    into ``n`` parts.
    Return a tuple of integers in the format (num_columns, num_rows)
    """
    num_columns = int(ceil(sqrt(n)))
    num_rows = int(ceil(n / float(num_columns)))
    return (num_columns, num_rows)


def validate_image(image, number_tiles):
    """Basic sanity checks prior to performing a split."""
    TILE_LIMIT = 99 * 99

    try:
        number_tiles = int(number_tiles)
    except BaseException:
        raise ValueError("number_tiles could not be cast to integer.")

    if number_tiles > TILE_LIMIT or number_tiles < 2:
        raise ValueError(
            "Number of tiles must be between 2 and {} (you \
                          asked for {}).".format(
                TILE_LIMIT, number_tiles
            )
        )


def validate_image_col_row(image, col, row):
    """Basic checks for columns and rows values"""
    SPLIT_LIMIT = 99

    try:
        col = int(col)
        row = int(row)
    except BaseException:
        raise ValueError(
            "columns and rows values could not be cast to integer.")

    if col < 1 or row < 1 or col > SPLIT_LIMIT or row > SPLIT_LIMIT:
        raise ValueError(
            "Number of columns and rows must be between 1 and"
            #f"{SPLIT_LIMIT} (you asked for rows: {row} and col: {col})."
        )
    if col == 1 and row == 1:
        raise ValueError(
            "There is nothing to divide. You asked for the entire image.")


def slice_image(
    image,
    number_tiles=None,
    col=None,
    row=None,
    DecompressionBombWarning=True,
):
    """
    Split an image into a specified number of tiles.
    Args:
       image (cv2 array):  The image to split.
       number_tiles (int):  The number of tiles required.
    Kwargs:
       save (bool): Whether or not to save tiles to disk.
       DecompressionBombWarning (bool): Whether to suppress
       Pillow DecompressionBombWarning
    Returns:
        Tuple of :class:`Tile` instances.
    """
    if DecompressionBombWarning is False:
        Image.MAX_IMAGE_PIXELS = None

    im = Image.fromarray(image)
    im_w, im_h = im.size

    columns = 0
    rows = 0
    if number_tiles:
        validate_image(im, number_tiles)
        columns, rows = calc_columns_rows(number_tiles)
    else:
        validate_image_col_row(im, col, row)
        columns = col
        rows = row

    tile_w, tile_h = int(floor(im_w / columns)), int(floor(im_h / rows))

    tiles = []
    number = 1
    for pos_y in range(0, im_h - rows, tile_h):  # -rows for rounding error.
        for pos_x in range(0, im_w - columns, tile_w):  # as above.
            area = (pos_x, pos_y, pos_x + tile_w, pos_y + tile_h)
            image = im.crop(area)
            #position = (int(floor(pos_x / tile_w)) + 1, int(floor(pos_y / tile_h)) + 1)
            #coords = (pos_x, pos_y)
            tiles.append(image)
            number += 1
    return tuple(tiles)


def is_grayscale(image):
    return len(image.shape) == 2


def pad(
    image,
    height=500,
    width=500,
    color=(0, 0, 0)
):
    # read image
    hh, ww = height, width

    ht, wd, cc = image.shape

    result = np.full((hh, ww, cc), color, dtype=np.uint8)

    # compute center offset
    xx = (ww - wd) // 2
    yy = (hh - ht) // 2

    # copy img image into center of result image
    result[yy:yy+ht, xx:xx+wd] = image

    return result


def pad_unet(
    image: np.array,
    factor: int = 32,
    border: int = cv2.BORDER_REFLECT_101
) -> tuple:
    """Pads the image on the sides, so that it will be divisible by factor.
    Common use case: UNet type architectures.

    Args:
        image:
        factor:
        border: cv2 type border.

    Returns: padded_image

    """
    height, width = image.shape[:2]

    if height % factor == 0:
        y_min_pad = 0
        y_max_pad = 0
    else:
        y_pad = factor - height % factor
        y_min_pad = y_pad // 2
        y_max_pad = y_pad - y_min_pad

    if width % factor == 0:
        x_min_pad = 0
        x_max_pad = 0
    else:
        x_pad = factor - width % factor
        x_min_pad = x_pad // 2
        x_max_pad = x_pad - x_min_pad

    padded_image = cv2.copyMakeBorder(
        image, y_min_pad, y_max_pad, x_min_pad, x_max_pad, border)

    return padded_image, (x_min_pad, y_min_pad, x_max_pad, y_max_pad)


def unpad_unet(image: np.array, pads: Tuple[int, int, int, int]) -> np.ndarray:
    """Crops patch from the center so that sides are equal to pads.

    Args:
        image:
        pads: (x_min_pad, y_min_pad, x_max_pad, y_max_pad)

    Returns: cropped image

    """
    x_min_pad, y_min_pad, x_max_pad, y_max_pad = pads
    height, width = image.shape[:2]

    return image[y_min_pad: height - y_max_pad, x_min_pad: width - x_max_pad]


def isBase64(sb):
    try:
        if isinstance(sb, str):
            # If there's any unicode here, an exception will be thrown and the function will return false
            sb_bytes = bytes(sb, 'ascii')
        elif isinstance(sb, bytes):
            sb_bytes = sb
        else:
            raise ValueError("Argument must be string or bytes")
        return base64.b64encode(base64.b64decode(sb_bytes)) == sb_bytes
    except Exception:
        return False


def load_image(
    image,
    resize_width=None
):

    if isBase64(image):
        image = bytes(image, 'ascii')
        im_bytes = base64.b64decode(image)
        nparr = np.frombuffer(im_bytes, dtype=np.uint8)
        result = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    elif isinstance(image, str):
        result = get_image(
            image,
            resize_width=resize_width
        )

    elif type(image) == np.ndarray:
        result = image

    else:
        return None

    return result


def crop_image(
    image=None,
    y=None,
    x=None,
    h=None,
    w=None
):

    image = load_image(image)
    cropped_image = image[y:y+h, x:x+w]

    return cropped_image


def get_bounding_box_points(pts):
    """
    Function for getting the bounding box points in the correct
    order

    Params
    pts     The points in the bounding box. (x, y) coordinates

    Returns
    rect    The ordered set of points
    """
    # initialzie a list of coordinates that will be ordered such that
    # 1st point -> Top left
    # 2nd point -> Top right
    # 3rd point -> Bottom right
    # 4th point -> Bottom left
    rect = np.zeros((4, 2), dtype="float32")

    # the top-left point will have the smallest sum, whereas
    # the bottom-right point will have the largest sum
    s = pts.sum(axis=1)
    rect[0] = pts[np.argmin(s)]
    rect[2] = pts[np.argmax(s)]
# now, compute the difference between the points, the
    # top-right point will have the smallest difference,
    # whereas the bottom-left will have the largest difference
    diff = np.diff(pts, axis=1)
    rect[1] = pts[np.argmin(diff)]
    rect[3] = pts[np.argmax(diff)]

    # return the ordered coordinates
    return rect


def warp_birds_eye(
    image=None,
    rect=None,
    output_process=False
):
    (tl, tr, br, bl) = rect
    # compute the width of the new image, which will be the
    # maximum distance between bottom-right and bottom-left
    # x-coordiates or the top-right and top-left x-coordinates
    widthA = np.sqrt(
        ((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2)
    )
    widthB = np.sqrt(
        ((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2)
    )
    maxWidth = max(int(widthA), int(widthB))

    # compute the height of the new image, which will be the
    # maximum distance between the top-right and bottom-right
    # y-coordinates or the top-left and bottom-left y-coordinates
    heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
    heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
    maxHeight = max(int(heightA), int(heightB))

    # now that we have the dimensions of the new image, construct
    # the set of destination points to obtain a "birds eye view",
    # (i.e. top-down view) of the image, again specifying points
    # in the top-left, top-right, bottom-right, and bottom-left
    # order
    dst = np.array(
        [
            [0, 0],  # Top left point
            [maxWidth - 1, 0],  # Top right point
            [maxWidth - 1, maxHeight - 1],  # Bottom right point
            [0, maxHeight - 1],
        ],  # Bottom left point
        dtype="float32",  # Date type
    )

    # compute the perspective transform matrix and then apply it
    M = cv2.getPerspectiveTransform(rect, dst)
    warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))

    if output_process:
        cv2.imwrite("output/deskewed.jpg", warped)

    # return the warped image
    return warped


def quantize_image(
    image,
    clusters=6
):

    if len(image.shape) > 2:
        arr = image.reshape((-1, 3))
    else:
        arr = image
    kmeans = KMeans(n_clusters=clusters).fit(arr)
    labels = kmeans.labels_
    centers = kmeans.cluster_centers_
    less_colors = centers[labels].reshape(image.shape).astype('uint8')

    return less_colors


def get_image_area(
    image
):
    return image.shape[0] * image.shape[1]


def np_to_base64(
    np_array
):
    _, im_arr = cv2.imencode('.jpg', np_array)
    im_bytes = im_arr.tobytes()
    im_b64 = base64.b64encode(im_bytes)
    return im_b64.decode("utf-8")


def load_rgb(
    image: np.array,
    lib: str = "cv2"
) -> np.array:
    """Load RGB image from path.

    Args:
        image_path: path to image
        lib: library used to read an image.
            currently supported `cv2` and `jpeg4py`

    Returns: 3 channel array with RGB image

    """
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return image


def resize(image, width=None, height=None, inter=cv2.INTER_AREA):
    # initialize the dimensions of the image to be resized and # grab the image size
    dim = None
    (h, w) = image.shape[:2]

    # if both the width and height are None, then return the
    # original image
    if width is None and height is None:
        return image

    # check to see if the width is None
    if width is None:
        # calculate the ratio of the height and construct the
        # dimensions
        r = height / float(h)
        dim = (int(w * r), height)

    # otherwise, the height is None
    else:
        # calculate the ratio of the width and construct the
        # dimensions
        r = width / float(w)
        dim = (width, int(h * r))

    # resize the image
    resized = cv2.resize(image, dim, interpolation=inter)

    # return the resized image
    return resized


def image_url_to_cv2_image(url):
    # download the image, convert it to a NumPy array, and then read
    # it into OpenCV format

    resp = image_url_to_byte(url)
    image = np.asarray(
        bytearray(resp),
        dtype="uint8"
    )
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)

    return image


def np_to_base64(
    np_array
):
    _, im_arr = cv2.imencode('.jpg', np_array)
    im_bytes = im_arr.tobytes()
    im_b64 = base64.b64encode(im_bytes)
    return im_b64.decode("utf-8")


def get_aspect_ratio_check(
    image=None,
    height=None,
    width=None,
    aspect_ratio=16/10,
    threshold=.05,
    check=operator.lt
):

    response = False

    h, w = height, width
    if image is not None:
        h, w = image.shape[:2]

    try:
        ratio = w/h

        abs_ratio = abs(1-ratio/aspect_ratio),

        response = check(
            abs(1-ratio/aspect_ratio),
            threshold
        )
    except ZeroDivisionError:
        response = False

    return response


def get_image_ratio(
    image_a,
    image_b,
):
    r = None
    image_a_height, image_a_width = image_a.shape[:2]

    image_b_height, image_b_width = image_b.shape[:2]

    r = image_a_height/image_b_height

    return r


def scaled_point(
    point,
    r
):

    return np.round(point * r).astype(int)


def get_scaled_points(
    intersections=None,
    orig_image=None,
    processed_image=None
):
    ratio = get_image_ratio(
        orig_image,
        processed_image
    )

    scaled_intersection = intersections * ratio

    return np.round(scaled_intersection)
