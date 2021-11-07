import ctypes
from time import sleep
from typing import List

from PIL import Image, ImageGrab

from .color import Color, ColorThiefCustom
from .const import Settings


class ColorGenerator:
    """
    At intervals generates colors based on Image objects
    (the source can be the entire screen, part of it).
    """

    def __init__(self, strategy: int = Settings.ALL_SCREEN_STRATEGY):
        """

        :param strategy: Defines what parts of screen would be parsed.
        """
        self.strategy = strategy

    def generator(self, delay=0.1):
        """
        Generator, yields colors with delay
        :param delay: delay in seconds
        :return:
        """
        while True:
            sleep(delay)
            yield self.generate_color()

    def generate_color(self) -> Color:
        """
        Generates one color using settings (from __init__).
        Makes a screenshot of a player window or default boxes. Then extracts key color.
        :return: dominated screen color
        """
        images = self.parse_screen()
        color = self.get_key_color(images)
        return color

    def parse_screen(self) -> List[Image.Image]:
        """
        :return: List of parts (Image objects) of screen due to parsing strategy.
        """
        boxes = self._get_boxes()
        screen_parts = []
        for box in boxes:
            screen_parts.append(self.make_screenshot(box))
        return screen_parts

    def _get_boxes(self):
        """
        :return: list of coordinates (x0, y0, x1, y1) of screen areas to capture.
        """
        if self.strategy == Settings.CENTER_STRATEGY:
            bbox = self._get_screen_borders()
            new_bbox = self.cut_borders(bbox, 50)
            boxes = [new_bbox]
        elif self.strategy == Settings.BORDERS_STRATEGY:
            bbox = self._get_screen_borders()
            boxes = self.extract_borders_boxes(bbox, 30, 20)
        elif self.strategy == Settings.ALL_SCREEN_STRATEGY:
            bbox = self._get_screen_borders()
            boxes = [self.cut_borders(bbox, 20)]
        else:
            boxes = [self._get_screen_borders()]
        return boxes

    @staticmethod
    def _get_screen_borders():
        """
        :return: bbox by screen size
        """
        user32 = ctypes.windll.user32
        user32.SetProcessDPIAware()
        x, y = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
        return 0, 0, x, y

    @staticmethod
    def cut_borders(bbox, percentage=10):
        """
        Extracts centered rectangle with cut edges.
        :param bbox: tuple of (x0, y0, x1, y1), first point (x0 y0) higher and left.
        :param percentage: percentage of length to cut
        :return: centered rectangle with cut edges
        """
        if 0 < percentage < 100:
            x0, y0, x1, y1 = bbox
            width = abs(x1 - x0)
            height = abs(y1 - y0)

            width_shift = int(width * percentage / 100 / 2)
            height_shift = int(height * percentage / 100 / 2)

            x0, y0, x1, y1 = (x0 + width_shift, y0 + height_shift, x1 - width_shift, y1 - height_shift)
            if x0 < x1 and y0 < y1:
                bbox = (x0, y0, x1, y1)
        return bbox

    def extract_borders_boxes(self, bbox, percentage=30, vertical_shift_percentage=0) -> List[tuple]:
        """
        Extract two rectangles: p1 area and p2 area.
        ----------------
        | p1 | p1 | p1 |
        ----------------
        |    |    |    |
        ----------------
        | p2 | p2 | p2 |
        ----------------
        :param vertical_shift_percentage: vertical shift of p1, p2 to center to avoid player buttons in screenshots
        :param bbox: tuple of (x0, y0, x1, y1), first point (x0 y0) higher and left.
        :param percentage: percentage of length to cut
        :return:
        """
        if 0 < percentage < 100:
            x0, y0, x1, y1 = bbox
            x2, y2, x3, y3 = self.cut_borders(bbox, percentage)
            vertical_shift = int(self._get_screen_borders()[3] * vertical_shift_percentage / 100)
            return [(x0, y0 + vertical_shift, x1, y2 + vertical_shift),
                    (x0, y3 - vertical_shift, x1, y1 - vertical_shift)]
        return [bbox]

    @staticmethod
    def make_screenshot(bbox):
        """
        :param bbox: area to capture
        :return: Image of captured area
        """
        img = ImageGrab.grab(bbox)
        # img.show()
        return img

    def get_key_color(self, screens: List[Image.Image], palette_size=2) -> Color:
        """
        :param screens: list of images to extract from
        :param palette_size: amount of dominant colors per image.
        :return: Average color of all dominant colors in images.
        """
        colors = []
        for screen in screens:
            color_thief = ColorThiefCustom(screen)
            col = color_thief.get_palette(color_count=palette_size)
            colors.extend([Color(*c) for c in col])

        avg_color = self.extract_avg_color(colors)
        return avg_color

    @staticmethod
    def extract_avg_color(colors: List[Color]) -> Color:
        """
        :param colors: list of colors
        :return: Color object representing average color.
        """
        r, g, b = 0, 0, 0

        for cl in colors:
            r_t, g_t, b_t = cl.tuple()
            r += r_t
            g += g_t
            b += b_t

        avg_color = Color(int(r / len(colors)), int(g / len(colors)), int(b / len(colors)))
        return avg_color
