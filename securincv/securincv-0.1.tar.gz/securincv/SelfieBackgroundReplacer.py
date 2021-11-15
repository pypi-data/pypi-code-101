import cv2
import numpy as np
import mediapipe as mp

class SelfieBackgroundReplacer():
    def __init__(self, model = 1):
        self.model = model
        self.mpDraw = mp.solutions.drawing_utils
        self.mpSelfieSegmentation = mp.solutions.selfie_segmentation
        self.SelfieSegmentation = self.mpSelfieSegmentation.SelfieSegmentation(self.model)

    def replace_background(self, img, imgBg = (255, 255, 255), threshold = 0.1):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = self.SelfieSegmentation.process(imgRGB)
        condition = np.stack(
            (results.segmentation_mask,) * 3, axis = -1) > threshold
        if isinstance(imgBg, tuple):
            _imgBg = np.zeros(img.shape, dtype = np.uint8)
            _imgBg[:] = imgBg
            return_image = np.where(condition, img, _imgBg)

        else:
            return_image = np.where(condition, img, imgBg)

        return return_image

def main():
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 480)
    segmentor = SelfieBackgroundReplacer()
    imgBg = cv2.imread('image.jpg')
    imgBg = (255, 0, 255)

    while True:
        success, img = cap.read()
        diff_bg_img = segmentor.replace_background(img, imgBg = imgBg, threshold = 0.1)

        #cv2.imshow('Image', img)
        cv2.imshow('Different Background Image', diff_bg_img)
        if cv2.waitKey(1) & 0XFF == ord('q'):
            break

if __name__ == "__main__":
    main()