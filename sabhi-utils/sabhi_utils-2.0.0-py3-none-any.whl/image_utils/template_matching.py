import cv2
import numpy as np
import imutils
from sabhi_utils.image_utils.utils import load_image


class TemplateMatching:

    def __init__(
        self,
        method=cv2.TM_CCOEFF_NORMED,
        matching_threshold=0.75,
        scales=np.linspace(0.2, 1.0, 20)[::-1],
        debug=False
    ):

        self._method = method
        self._matching_threshold = matching_threshold
        self._scales = scales
        self._debug = debug

    def _multi_scale_match_template(self, found=None):
        image = self._image.copy()
        for scale in self._scales:
            resized_image = imutils.resize(
                image,
                width=int(image.shape[1] * scale)
            )

            r = image.shape[1] / float(resized_image.shape[1])

            if resized_image.shape[0] < self._template_height or resized_image.shape[1] < self._template_width:
                break

            result = cv2.matchTemplate(
                resized_image,
                self._template,
                method=self._method
            )

            #match_locations = np.where(
            #    result >= self._matching_threshold
            #)

            (_, maxVal, _, maxLoc) = cv2.minMaxLoc(result)

            if self._debug:
                # draw a bounding box around the detected region
                clone = resized_image
                cv2.rectangle(clone, (maxLoc[0], maxLoc[1]),
                              (maxLoc[0] + self._template_width, maxLoc[1] + self._template_height), (0, 0, 255), 2)
                cv2.imshow("Visualize", clone)
                cv2.waitKey(0)

                #cv2.imshow("result", result)
                # cv2.waitKey(0)
            if found is None or maxVal > found[0]:
                found = (maxVal, maxLoc, r)
        return found

    def __call__(
        self,
        image,
        template,
        label="1"
    ):
        self._image = load_image(image)
        self._template = template

        self._template_height, self._template_width = self._template.shape[:2]

        result = self._multi_scale_match_template()
        return result
