from sabhi_utils.image_utils.utils import load_image
from sabhi_utils.image_utils.utils import get_image_area
from sabhi_utils.image_utils.utils import quantize_image

from matplotlib import pyplot as plt
from skimage.io import imshow
import skimage.measure as measure
from scipy import ndimage
import cv2
import math
import pandas as pd
import time


def plot_figures(figures, nrows=None, ncols=None):
    """Plot a dictionary of figures.

    Parameters
    ----------
    figures : <title, figure> dictionary
    ncols : number of columns of subplots wanted in the display
    nrows : number of rows of subplots wanted in the figure
    """

    if (not nrows) and (not ncols):

        half_len = math.sqrt(len(figures))
        nrows = math.floor(half_len)
        ncols = math.ceil(half_len)

    fig, axeslist = plt.subplots(ncols=ncols, nrows=nrows)
    for ind, title in zip(range(len(figures)), figures):
        axeslist.ravel()[ind].imshow(figures[title])
        axeslist.ravel()[ind].set_title(title)
        axeslist.ravel()[ind].set_axis_off()
    plt.tight_layout()  # optional


def label_components(
    image,
):

    # im, number_of_objects = ndimage.label(image)
    # blobs = ndimage.find_objects(im)

    labeled_image = measure.label(
        image
    )

    return labeled_image


def get_region_thresholds(
    area,
    low_ratio=None,
    high_ratio=None
):
    region_low_thresh = area*low_ratio
    region_high_thresh = area*high_ratio

    return region_low_thresh, region_high_thresh


class CCVQuantizedImage:

    def __init__(
        self,
        debug=False
    ):
        self._debug = debug

    def _get_quantized_channels(
        self,
        channels
    ):
        quantized_channels = {}

        for channel_name, channel_array in channels.items():
            quantized_channels[channel_name] = self._quantize_channel(
                channel_array
            )
        return quantized_channels

    def _get_connected_components(
        self,
        channels
    ):
        connected_components = {}

        for channel_name, channel_array in channels.items():

            connected_components[
                channel_name] = label_components(
                channels[channel_name]
            )
        return connected_components

    def _get_connected_blobs_skimage(
        self,
        connected_components,
        list_of_index,
        key
    ):
        blobs = connected_components[key]

        connected_regions = {}
        for x in list_of_index[key]:
            sl = ndimage.find_objects(blobs == x)
            region_selected = self._image[sl[0]]
            connected_regions[x] = region_selected
        return connected_regions

    def _is_reasonable_area(
        self,
        region
    ):
        return self._region_low_thresh < region.area < self._region_high_thresh

    def _is_reasonable_intensity(
        self,
        region
    ):
        return region.mean_intensity > self._intensity_threshold

    def _area_and_intensity(
        self,
        region
    ):
        return all(
            [
                self._is_reasonable_area(region)  # ,
                # self._is_reasonable_intensity(region),
            ]
        )

    def _filtered_region_list_index(
        self,
        labeled_image,
        criteria
    ):

        regions = measure.regionprops(
            labeled_image
        )
        list_of_index = []
        for region in regions:
            if criteria(region):
                list_of_index.append(region.label)

        return list_of_index

    def _filtered_index_list(
        self,
        connected_components,
        criteria
    ):
        filtered_cc = {}
        for key, labeled_image in connected_components.items():
            filtered_cc[key] = self._filtered_region_list_index(
                labeled_image,
                criteria
            )
        return filtered_cc

    def __call__(
        self,
        image=None,
        bins=6,
        blur=True,
        area_low_ratio=.02,
        area_high_ratio=.4,
        intensity_threshold=150
    ):

        self._bins = bins
        self._image = load_image(image)
        self._image_area = get_image_area(self._image)
        if blur:
            self._image = cv2.blur(self._image, (5, 5))

        (self._region_low_thresh,
         self._region_high_thresh) = get_region_thresholds(
            self._image_area,
            area_low_ratio,
            area_high_ratio
        )

        self._intensity_threshold = intensity_threshold

        self._image_rgb = cv2.cvtColor(
            self._image,
            cv2.COLOR_BGR2RGB
        )

        self._image_hsv = cv2.cvtColor(
            self._image_rgb,
            cv2.COLOR_BGR2HSV
        )

        quantized_image = quantize_image(
            self._image_hsv,
            clusters=self._bins
        )

        (h_quantized_image,
         s_quantized_image,
         v_quantized_image) = cv2.split(quantized_image)

        quantized_image_channels = {
            "h_quantized_image": h_quantized_image,
            "s_quantized_image": s_quantized_image,
            "v_quantized_image": v_quantized_image
        }

        connected_components_quantized_image = self._get_connected_components(
            quantized_image_channels
        )

        start_time = time.perf_counter()

        image_indices = self._filtered_index_list(
            connected_components_quantized_image,
            criteria=self._area_and_intensity
        )

        elapsed_time = time.perf_counter() - start_time
        print(f"LOOP {elapsed_time=}")

        if self._debug:
            images = {
              "hsv": self._image_hsv,
              "hsv_quantized": quantized_image["hsv"],
              "h_quantized_image": h_quantized_image,
              "s_quantized_image": s_quantized_image,
              "v_quantized_image": v_quantized_image,
            }

            plot_figures(images,2,2)
            plt.show()

            print(image_indices)
            connected_regions = self._get_connected_blobs_skimage(
                connected_components_quantized_image,
                image_indices,
                key="s_quantized_image"
            )

            plot_figures(connected_regions)
            plt.show()

            connected_regions = self._get_connected_blobs_skimage(
                connected_components_quantized_image,
                image_indices,
                key="h_quantized_image"
            )
            plot_figures(connected_regions)
            plt.show()
        return None


class CCVQuantizedChannels:

    def __init__(
        self,
        debug=False
    ):
        self._debug = debug

    def _quantize_image(
        self,
        channel,
    ):
        return quantize_image(
            channel,
            clusters=self._bins)

    def _label_components(
        self,
        image,
    ):

        # im, number_of_objects = ndimage.label(image)
        # blobs = ndimage.find_objects(im)

        labeled_image = measure.label(
            image
        )

        return labeled_image

    def _get_quantized_channels(
        self,
        channels
    ):
        quantized_channels = {}

        for channel_name, channel_array in channels.items():
            quantized_channels[channel_name] = self._quantize_channel(
                channel_array
            )
        return quantized_channels

    def _get_connected_components_(
        self,
        channels
    ):
        connected_components = {}

        for channel_name, channel_array in channels.items():

            connected_components[
                channel_name] = self._label_components(
                channels[channel_name]
            )
        return connected_components

    def _get_connected_blobs_skimage(
        self,
        connected_components,
        list_of_index,
        key
    ):
        blobs = connected_components[key]
        # for i, j in enumerate(blobs):
        #    blob[i] = self._image[j]

        connected_regions = {}
        for x in list_of_index[key]:
            sl = ndimage.find_objects(blobs == x)
            region_selected = self._image[sl[0]]
            connected_regions[x] = region_selected
        return connected_regions

    def _is_reasonable_area(
        self,
        region
    ):
        return self._region_low_thresh < region.area < self._region_high_thresh

    def _is_reasonable_intensity(
        self,
        region
    ):
        return region.mean_intensity > self._intensity_threshold

    def _area_and_intensity(
        self,
        region
    ):
        return all(
            [
                self._is_reasonable_area(region)  # ,
                # self._is_reasonable_intensity(region),
            ]
        )

    # def _filter_regions(
    #    self,
    #    labeled_image,
    #    quantized_image
    #    criteria
    # ):
    #    region_df = pd.DataFrame(
    #        skimage.measure.regionprops_table(
    #       labeled_image,
    #       quantized_image,
    #       properties=['area', 'mean_intensity']
    #    )
    #    )

    def _filter_list_index(
        self,
        labeled_image,
        image,
    ):
        region_df = pd.DataFrame(
            measure.regionprops_table(
                labeled_image,
                image,
                properties=['label', 'area', 'mean_intensity']
            )
        )
        filtered_areas_df = region_df[
            (region_df["area"] >= self._region_low_thresh) &
            (region_df["area"] <= self._region_high_thresh)
        ]

        return filtered_areas_df["label"].tolist()

    def _filter_connected_components(
        self,
        connected_components,
        criteria
    ):
        filtered_cc = {}
        for key, labeled_image in connected_components.items():
            filtered_cc[key] = self._filter_list_index(
                labeled_image,
                self._image
            )
        return filtered_cc

    def __call__(
        self,
        image=None,
        bins=6,
        blur=True,
        area_low_ratio=.02,
        area_high_ratio=.4,
        intensity_threshold=150
    ):

        self._bins = bins
        self._image = load_image(image)
        self._image_area = self._image.shape[0] * self._image.shape[1]
        if blur:
            self._image = cv2.blur(self._image, (7, 7))

        self._region_low_thresh = self._image_area*area_low_ratio
        self._region_high_thresh = self._image_area*area_high_ratio
        self._intensity_threshold = intensity_threshold

        self._image_rgb = cv2.cvtColor(
            self._image,
            cv2.COLOR_BGR2RGB
        )

        self._image_hsv = cv2.cvtColor(
            self._image_rgb,
            cv2.COLOR_BGR2HSV
        )

        quantized_image = self._quantize_image(self._image_hsv)

        (h_quantized_image,
         s_quantized_image,
         v_quantized_image) = cv2.split(quantized_image)

        quantized_image_channels = {
            "h_quantized_image": h_quantized_image,
            "s_quantized_image": s_quantized_image,
            "v_quantized_image": v_quantized_image
        }

        connected_components_quantized_image = self._get_connected_components_(
            quantized_image_channels
        )

        quantized_image_indices = self._filter_connected_components(
            connected_components_quantized_image,
            criteria=self._area_and_intensity
        )

        h, s, v = cv2.split(self._image_hsv)

        quantized_h = quantize_image(h)
        quantized_s = quantize_image(s)
        quantized_v = quantize_image(v)

        quantized_channels = {
            "h_quantized": quantized_h,
            "s_quantized": quantized_s,
            "v_quantized": quantized_v
        }

        connected_components_quantized_channels = self._get_connected_components_(
            quantized_channels
        )

        quantized_channels_indices = self._filter_connected_components(
            connected_components_quantized_channels,
            criteria=self._area_and_intensity
        )

        if self._debug:
            images = {
                "hsv": self._image_hsv,
                "hsv_quantized": quantized_image["hsv"],
                "h_quantized_image": h_quantized_image,
                "s_quantized_image": s_quantized_image,
                "v_quantized_image": v_quantized_image,
                "h_quantized": quantized_h,
                "s_quantized": quantized_s,
                "v_quantized": quantized_v
            }

            plot_figures(images)
            plt.show()
            # key = "s_quantized"

            connected_regions = self._get_connected_blobs_skimage(
                connected_components_quantized_image,
                quantized_image_indices,
                key="h_quantized_image"
            )
            print(connected_regions)

            plot_figures(connected_regions, 5, 5)
            plt.show()

            connected_regions = self._get_connected_blobs_skimage(
                connected_components_quantized_channels,
                quantized_channels_indices,
                key="h_quantized"
            )
            print(connected_regions)

            plot_figures(connected_regions, 2, 2)
            plt.show()

        return None
