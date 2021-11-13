#import face_recognition
import cv2
import os
import wget
import pandas as pd
from PIL import Image

from sabhi_utils.image_utils.utils import load_image
from pathlib import Path


def initialize_face_detector(detector_backend):
    home = str(Path.home())
    output_dir = os.path.join(
        home,
        '.sabhi_utils/weights/'
    )

    os.makedirs(output_dir, exist_ok=True)
    if detector_backend == 'ssd':

        # check required ssd model exists in the home/.sabhi_utils/weights folder

        # model structure
        if os.path.isfile(
            os.path.join(output_dir, 'deploy.prototxt')
        ) != True:

            print("deploy.prototxt will be downloaded...")

            url = "https://github.com/opencv/opencv/raw/3.4.0/samples/dnn/face_detector/deploy.prototxt"

            output = os.path.join(output_dir, 'deploy.prototxt')

            wget.download(url, output)

        # pre-trained weights
        if os.path.isfile(
            os.path.join(
                output_dir,
                'res10_300x300_ssd_iter_140000.caffemodel')
        ) != True:

            print("res10_300x300_ssd_iter_140000.caffemodel will be downloaded...")

            url = "https://github.com/opencv/opencv_3rdparty/raw/dnn_samples_face_detector_20170830/res10_300x300_ssd_iter_140000.caffemodel"

            output = os.path.join(
                output_dir,
                'res10_300x300_ssd_iter_140000.caffemodel'
            )

            wget.download(url, output)

        face_detector = cv2.dnn.readNetFromCaffe(
            home+"/.sabhi_utils/weights/deploy.prototxt",
            home+"/.sabhi_utils/weights/res10_300x300_ssd_iter_140000.caffemodel"
        )

    return face_detector


def detect_face(
    img,
    detector_backend='ssd',
    grayscale=False,
    tolerance=.88,
    enforce_detection=True,
    debug=False
):

    img = load_image(img)
    face_detector = initialize_face_detector(
        detector_backend=detector_backend
    )

    if detector_backend == 'ssd':
        ssd_labels = ["img_id", "is_face", "confidence",
                      "left", "top", "right", "bottom"]

        target_size = (300, 300)

        base_img = img.copy()  # we will restore base_img to img later
        original_size = img.shape

        img = cv2.resize(base_img, target_size)
        if debug:
            cv2.imshow("img", img)
            cv2.waitKey(0)
        #aspect_ratio_x = (original_size[1] / target_size[1])
        #aspect_ratio_y = (original_size[0] / target_size[0])
        imageBlob = cv2.dnn.blobFromImage(image=img)

        face_detector.setInput(imageBlob)
        detections = face_detector.forward()

        detections_df = pd.DataFrame(detections[0][0], columns=ssd_labels)

        detections_df = detections_df.loc[
            detections_df['confidence'] >= tolerance
        ]

        return detections_df


def num_of_faces(image):

    return len(detect_face(image).index)


class FaceRecognition:

    def __init__(
        self,
        debug=False
    ):

        self._debug = debug

    def __call__(
        self,
        image=None,
    ):
        self._image = image
        self._columns = [
            "confidence",
            "left",
            "top"
        ]

        self._detected_faces_df = detect_face(image)

        self._num_faces = len(self._detected_faces_df)

        if self._num_faces > 0:

            return {
                "num_of_faces": self._num_faces,
                self._columns[0]: self._detected_faces_df.loc[0, self._columns[0]],
                self._columns[1]: self._detected_faces_df.loc[0, self._columns[1]],
                self._columns[2]: self._detected_faces_df.loc[0, self._columns[2]]
            }
