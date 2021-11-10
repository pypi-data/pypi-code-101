import cv2
from sabhi_utils.image_utils.utils import get_image, get_hsv_means_for_windows
from sabhi_utils.image_utils.utils import pad, load_image
from matplotlib import pyplot as plt
from scipy.stats import wasserstein_distance
import numpy as np
import imutils
import skimage.metrics as metrics
from skimage.io import imshow
from scipy import ndimage
import pandas as pd
import skimage.measure as measure


class GrayscaleHistogramComparison:

    def __init__(
        self,
        hist_size=256,
        hist_range=(0, 256),
        norm_type=cv2.NORM_MINMAX,
        comparison_method=wasserstein_distance,
        debug=False
    ):

        self._hist_size = hist_size
        self._hist_range = hist_range
        self._norm_type = norm_type
        self._comparison_method = comparison_method
        self._debug = debug

    def _visualize(self):
        # plt.figure()
        # plt.title("Grayscale Histogram")
        # plt.xlabel("Bins") # plt.ylabel("# of Pixels")
        # plt.plot(hist)
        # plt.xlim([0, 256])

        (fig, ax) = plt.subplots(1, 2, )
        ax[0].plot(self._hist_image)
        ax[0].set_title("self._hist_image")
        ax[0].set_xticks([])
        ax[0].set_yticks([])
        # display the magnitude image
        ax[1].plot(self._hist_template)
        ax[1].set_title("self._hist_template")
        ax[1].set_xticks([])
        ax[1].set_yticks([])
        # show our plots
        plt.show()

    def _compare(self):
        return self._comparison_method(
            self._hist_image.flatten(), self._hist_template.flatten())

    def __call__(
        self,
        image,
        template,
        vis=False,
    ):
        self._image = image

        self._template = template
        if len(self._image.shape) > 2:
            self._image = cv2.cvtColor(self._image, cv2.COLOR_BGR2GRAY)

        if len(self._template.shape) > 2:
            self._template = cv2.cvtColor(self._template, cv2.COLOR_BGR2GRAY)

        self._hist_image = cv2.calcHist(
            [self._image], [0], None, [self._hist_size], self._hist_range)
        self._hist_template = cv2.calcHist(
            [self._template], [0], None, [self._hist_size], self._hist_range)

        cv2.normalize(
            self._hist_image,
            self._hist_image,
            alpha=0,
            beta=255,
            norm_type=self._norm_type
        )

        cv2.normalize(
            self._hist_template,
            self._hist_template,
            0,
            255,
            self._norm_type
        )

        if vis:
            self._visualize()

        if self._debug:
            cv2.imshow("self._image", self._image)
            cv2.waitKey(0)
            cv2.imshow("self._template", self._template)
            cv2.waitKey(0)

        return self._compare()


class HueSaturationDifference:
    def __init__(
        self,
        N_h=5,
        N_w=10,
        h_magic_number=179,
        s_magic_number=255
    ):

        self._N_h = N_h
        self._N_w = N_w
        self._total_bins = self._N_h * self._N_w

        self._h_magic_number = h_magic_number
        self._s_magic_number = s_magic_number

    def _get_hsd_score(self):
        hsd_score = np.sum(
            self._image_h_s_means - self._template_h_s_means, axis=0
        )

        h_denom = self._h_magic_number * self._total_bins
        s_denom = self._s_magic_number * self._total_bins
        hsd_score = (hsd_score[0] * hsd_score[1])/(h_denom*s_denom)
        return abs(hsd_score)

    def __call__(self, image, template):
        self._template = cv2.cvtColor(template, cv2.COLOR_BGR2HSV)
        _, self._template_width, _ = self._template.shape

        self._image = imutils.resize(image, width=self._template_width)
        self._image = cv2.cvtColor(self._image, cv2.COLOR_BGR2HSV)

        self._image_h_s_means = get_hsv_means_for_windows(self._image,
                                                          N_h=self._N_h,
                                                          N_w=self._N_w,
                                                          debug=False)

        self._template_h_s_means = get_hsv_means_for_windows(self._template,
                                                             N_h=self._N_h,
                                                             N_w=self._N_w,
                                                             debug=False)
        return self._get_hsd_score()


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
                raise RuntimeError("Image has too many bright spots")

        return True


class StructuralSimilarity():
    def __init__(
        self,
        debug=False
    ):

        self._debug = debug

    def __call__(
        self,
        image,
        template,
        width=450,
        width_with_padding=600
    ):
        self._image = pad(
            imutils.resize(
                load_image(image),
                width=width
            ),
            width_with_padding
        )
        self._template = pad(
            imutils.resize(
                load_image(template),
                width=width
            ),
            width_with_padding
        )

        self._image_gray = cv2.cvtColor(
            self._image,
            cv2.COLOR_BGR2GRAY
        )

        self._template_gray = cv2.cvtColor(
            self._template,
            cv2.COLOR_BGR2GRAY
        )

        if self._debug:
            cv2.imshow("image", self._image_gray)
            cv2.waitKey(0)
            cv2.imshow("template", self._template_gray)
            cv2.waitKey(0)
        score, diff = metrics.structural_similarity(
            self._image_gray,
            self._template_gray,
            full=True
        )

        return score


class ColoCoherenceVectors():
    def __init__(
        self,
        debug=True
    ):

        self._debug = debug

    def quantize_image(
        image,
        clusters=6
    ):

        arr = image.reshape((-1, 3))
        kmeans = KMeans(n_clusters=clusters).fit(arr)
        labels = kmeans.labels_
        centers = kmeans.cluster_centers_
        less_colors = centers[labels].reshape(image.shape).astype('uint8')

        return less_colors

    def __call__(
        self,
        image=None,
        bins=6,
        area_low_ratio=.10,
        area_high_ratio=.30
    ):

        self._image = load_image(image)
        self._image = cv2.blur(self._image, (3, 3))

        self._bins = bins
        self._image_hsv = cv2.cvtColor(
            self._image,
            cv2.COLOR_BGR2HSV
        )

        #hue, saturation, value = cv2.split(self._image_hsv)
        # self._quantized_hue = quantize_image(
        #    hue,
        #    clusters=self._bins)

        self._quantized_image = quantize_image(
            self._image_hsv,
            clusters=self._bins
        )

        labeled_image, nl = measure.label(
            self._quantized_image,
            return_num=True
        )

        regions = measure.regionprops(labeled_image)
        masks = []
        bbox = []
        list_of_index = []

        area_image = labeled_image.shape[0] * labeled_image.shape[1]
        area_low = area_image*area_low_ratio
        area_high = area_image*area_high_ratio
        for num, x in enumerate(regions):
            area = x.area
            area_low = area*area_low_ratio
            area_high = area*area_high_ratio

            if (num != 0 and area_low < area):
                bbox.append(regions[num].bbox)
                list_of_index.append(num)

        # for box, mask in zip(bbox, masks):
        for box in bbox:
            print(f"{box=}")
            image = self._image_hsv[
                box[0]:box[2],
                box[1]:box[3],
                :
            ]
            # red = self._image_hsv[:, :, 0][
            #    box[0]:box[2], box[1]:box[3]]

            # green = self._image_hsv[:, :, 1][
            #    box[0]:box[2], box[1]:box[3]]

            # blue = self._image_hsv[:, :, 2][
            #    box[0]:box[2], box[1]:box[3]]

            #image = np.dstack([red, green, blue])
            imshow(image)
            plt.show()

        # region_df = pd.DataFrame(skimage.measure.regionprops_table(
        #    labeled_image,
        #    self._quantized_image,
        #    properties=['area', 'mean_intensity']
        # )
        # )
        # print(region_df)

        # filtered_areas_df = region_df[
        #    (region_df["area"] >= area*area_low_ratio) &
        #    (region_df["area"] <= area*area_high_ratio) &
        #    (region_df["mean_intensity"] >= 100)
        # ]

        #list_of_index = filtered_areas_df.index.values.tolist()

        # print(rgb_mask.shape)
        # for x in list_of_index[1:]:

        #    sl = ndimage.find_objects(labeled_image == x)
        #    region_selected = labeled_image[sl[0]]
        #    #cv2.imshow("region_selected",region_selected.astype("uint8"))
        #    #cv2.waitKey(0)
        #    imshow(region_selected)
        #    plt.show()

        # for x in list_of_index[1:]:

        #    print((labeled_image == x).shape)

        #red  =  painting[:,:,0] * rgb_mask
        #green = painting[:,:,1] * rgb_mask
        #blue  = painting[:,:,2] * rgb_mask
        #image = np.dstack([red, green, blue])
        # imshow(image)

        # print(region_selected)
        # print(labeled_image.shape)
        return nl
