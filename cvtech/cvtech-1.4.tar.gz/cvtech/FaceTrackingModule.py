import cv2
import mediapipe as mp


class FaceDetector:
    def __init__(self):
        self.mp_face_detection = mp.solutions.face_detection
        self.face_detection = self.mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.5)
        self.mp_draw = mp.solutions.drawing_utils

    def find_faces(self, img, draw=True):
        """
        When the image file is read with the OpenCV function read() ,
        the order of colors is BGR (blue, green, red). So here we are converting
        BGR image to RGB
        """
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        """
        Processes an RGB image and returns a list of the detected face location data.
        It returns a NamedTuple object with a "detections" field that contains a list of the
        detected face location data.
        """
        self.results = self.face_detection.process(img_rgb)
        bboxs = []

        if self.results.detections:
            for detection in self.results.detections:
                bbox_rel = detection.location_data.relative_bounding_box
                ih, iw, ic = img.shape
                """Fitting bbox coordinates with the image shape"""
                bbox = int(bbox_rel.xmin * iw), int(bbox_rel.ymin * ih), int(bbox_rel.width * iw), int(bbox_rel.height * ih)

                bbox_info = {"bbox": bbox, "score": detection.score}

                bboxs.append(bbox_info)

                if draw:
                    img = cv2.rectangle(img, bbox, (0, 255, 0), 2)

                    cv2.putText(img, f'{int(detection.score[0] * 100)}%',
                                (bbox[0], bbox[1] - 20), cv2.FONT_HERSHEY_PLAIN,
                                2, (255, 0, 255), 2)

        return img, bboxs


def main():
    cap = cv2.VideoCapture(0)
    detector = FaceDetector()
    while True:
        success, img = cap.read()
        img, bboxs = detector.find_faces(img)

        cv2.imshow("Image", img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()


