import numpy as np
from calculation.pixel import Pixel


class Reflection:

    @staticmethod
    def mask_convert_big_image(y0, x0, boundary, horizon):
        segm = []
        for i in range(0, len(boundary[0])-1, 2):
            x, y = boundary[0][i], boundary[0][i+1]
            temp = Pixel.calc_origin(x0, y0, [y, x], 1, 1, horizon)
            segm.append([temp[1], temp[0]])
        segmentation = np.array([segm], np.int32)
        return segmentation