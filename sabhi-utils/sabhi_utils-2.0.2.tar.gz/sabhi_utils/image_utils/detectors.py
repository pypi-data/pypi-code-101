import matplotlib.pyplot as plt
import numpy as np
import cv2
from skimage import measure
from sabhi_utils.image_utils.utils import load_image


class BlurDetector:

    def __init__(
        self,
        preprocessor=None,
        thresh=20
    ):

        self._preprocessor = preprocessor
        self._thresh = thresh

    def _get_image_center(self):

        return (int(self._w / 2.0), int(self._h / 2.0))

    def _visualize(self):
        # check to see if we are visualizing our output
        # compute the magnitude spectrum of the transform
        # display the original input image
        (fig, ax) = plt.subplots(1, 2, )
        ax[0].imshow(self._image, cmap="gray")
        ax[0].set_title("Input")
        ax[0].set_xticks([])
        ax[0].set_yticks([])
        # display the magnitude image
        ax[1].imshow(self._magnitude, cmap="gray")
        ax[1].set_title("Magnitude Spectrum")
        ax[1].set_xticks([])
        ax[1].set_yticks([])
        # show our plots
        plt.show()

    def _zero_center_inverse(self):
        fft_shift = self._fft_shift.copy()

        fft_shift[
            self._cY - self._size:self._cY + self._size,
            self._cX - self._size:self._cX + self._size
        ] = 0

        fft_shift = np.fft.ifftshift(fft_shift)
        recon = np.fft.ifft2(fft_shift)
        return recon

    def __call__(
        self,
        image,
        vis=False
    ):

        image = load_image(image)
        self._image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        self._h, self._w = self._image.shape
        self._cX, self._cY = self._get_image_center()

        self._size = int(self._h/8)

        self._fft = np.fft.fft2(self._image)
        self._fft_shift = np.fft.fftshift(self._fft)

        self._recon = self._zero_center_inverse()

        self._magnitude = 20 * np.log(
            np.abs(self._recon)
        )

        self._mean = np.mean(self._magnitude)

        if vis:
            self._visualize()

        # the image will be considered "blurry" if the mean value of the
        # magnitudes is less than the threshold value
        # return (self._mean <= self._thresh, self._mean)
        return {
            'isDetected': self._mean <= self._thresh
        }


class BrightspotDetector:
    def __init__(
        self,
        preprocess=[]
    ):

        self._preprocess = preprocess

    def __call__(
        self,
        image,
        percentage_limit=0.02,
        debug=False
    ):

        image = load_image(image)
        self._image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        self._blurred = cv2.GaussianBlur(self._image, (11, 11), 0)
        self._size = self._image.shape[0] * self._image.shape[1]
        self._percentage_limit = percentage_limit
        self._blob_size_limit = int(self._size * self._percentage_limit)

        # threshold the image to reveal light regions in the
        # blurred image

        self._thresh = cv2.threshold(
            self._blurred, 238, 255, cv2.THRESH_BINARY)[1]

        self._thresh = cv2.erode(self._thresh, None, iterations=2)
        self._thresh = cv2.dilate(self._thresh, None, iterations=4)

        # perform a connected component analysis on the thresholded
        # image, then initialize a mask to store only the "large"
        # components
        labels = measure.label(self._thresh, background=0)
        if debug:
            cv2.imshow("self._thresh", self._thresh)
            cv2.waitKey(0)
            print(labels)
        #mask = np.zeros(self._thresh.shape, dtype="uint8")
        # loop over the unique components
        for label in np.unique(labels):
            # if this is the background label, ignore it
            if label == 0:
                continue
            # otherwise, construct the label mask and count the
            # number of pixels
            labelMask = np.zeros(self._thresh.shape, dtype="uint8")
            labelMask[labels == label] = 255
            numPixels = cv2.countNonZero(labelMask)
            # if the number of pixels in the component is sufficiently
            # large, then add it to our mask of "large blobs"
            if numPixels > self._blob_size_limit:
                return {
                    'isDetected': True
                }

        # return (False, "Insignificant bright spots")
        return {
            'isDetected': False
        }
