# Copyright (C) <2021>  YUANXIN INFORMATION TECHNOLOGY GROUP CO.LTD and Jinzhe Wang
# This file is part of uitestrunner_syberos
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import math
from lxml import etree
import cv2
import xml.dom.minidom
import numpy as np
import random
from time import sleep


class Item:
    node = None
    xpath = ""
    __text = ""
    __tempId = ""
    __x = 0.0
    __y = 0.0
    __z = 0
    __center_x_to_item = 0.0
    __center_y_to_item = 0.0
    __center_x_to_global = 0.0
    __center_y_to_global = 0.0
    __height = 0.0
    __width = 0.0
    __className = ""
    __objectName = ""
    __opacity = 0.0
    __focus = None
    __enabled = None
    __visible = None
    __scale = 0.0
    __rotation = 0
    __clip = None
    device = None
    app = None
    __display_width = 0
    __display_height = 0
    rect = []

    def __init__(self, d=None, a=None, node=None, xpath=""):
        self.app = a
        self.device = d
        self.__display_width = self.device.display_width()
        self.__display_height = self.device.display_height()
        self.node = node
        self.xpath = xpath
        self.__refresh_attribute()

    def __refresh_node(self):
        self.device.refresh_layout()
        selector = etree.XML(self.device.xmlStr.encode('utf-8'))
        nodes = selector.xpath(self.xpath)
        if len(nodes) > 0 and selector.get("sopId") == self.app.sopId:
            self.node = nodes[0]

    def __refresh_attribute(self):
        self.__x = float(self.node.get("x"))
        self.__y = float(self.node.get("y"))
        self.__center_x_to_item = float(self.node.get("centerXToItem"))
        self.__center_y_to_item = float(self.node.get("centerYToItem"))
        self.__center_x_to_global = float(self.node.get("centerXToGlobal"))
        self.__center_y_to_global = float(self.node.get("centerYToGlobal"))
        self.__z = int(self.node.get("z"))
        self.__height = float(self.node.get("height"))
        self.__width = float(self.node.get("width"))
        self.__tempId = self.node.get("tempID")
        self.__text__ = self.node.get("text")
        self.__objectName = self.node.get("objectName")
        self.__className = self.node.tag
        self.__opacity = float(self.node.get("opacity"))
        self.__enabled = bool(int(self.node.get("enabled")))
        self.__visible = bool(int(self.node.get("visible")))
        self.__focus = bool(int(self.node.get("focus")))
        self.__scale = float(self.node.get("scale"))
        self.__rotation = int(self.node.get("rotation"))
        self.__clip = bool(int(self.node.get("clip")))

    def x(self, refresh=False):
        if refresh:
            self.__refresh_node()
            self.__refresh_attribute()
        return self.__x

    def y(self, refresh=False):
        if refresh:
            self.__refresh_node()
            self.__refresh_attribute()
        return self.__y

    def center_x_to_item(self, refresh=False):
        if refresh:
            self.__refresh_node()
            self.__refresh_attribute()
        return self.__center_x_to_item

    def center_y_to_item(self, refresh=False):
        if refresh:
            self.__refresh_node()
            self.__refresh_attribute()
        return self.__center_y_to_item

    def center_x_to_global(self, refresh=False):
        if refresh:
            self.__refresh_node()
            self.__refresh_attribute()
        return self.__center_x_to_global

    def center_y_to_global(self, refresh=False):
        if refresh:
            self.__refresh_node()
            self.__refresh_attribute()
        return self.__center_y_to_global

    def z(self, refresh=False):
        if refresh:
            self.__refresh_node()
            self.__refresh_attribute()
        return self.__z

    def scale(self, refresh=False):
        if refresh:
            self.__refresh_node()
            self.__refresh_attribute()
        return self.__scale

    def rotation(self, refresh=False):
        if refresh:
            self.__refresh_node()
            self.__refresh_attribute()
        return self.__rotation

    def clip(self, refresh=False):
        if refresh:
            self.__refresh_node()
            self.__refresh_attribute()
        return self.__clip

    def height(self, refresh=False):
        if refresh:
            self.__refresh_node()
            self.__refresh_attribute()
        return self.__height

    def width(self, refresh=False):
        if refresh:
            self.__refresh_node()
            self.__refresh_attribute()
        return self.__width

    def temp_id(self, refresh=False):
        if refresh:
            self.__refresh_node()
            self.__refresh_attribute()
        return self.__tempId

    def text(self, refresh=False):
        if refresh:
            self.__refresh_node()
            self.__refresh_attribute()
        return self.__text__

    def object_name(self, refresh=False):
        if refresh:
            self.__refresh_node()
            self.__refresh_attribute()
        return self.__objectName

    def class_name(self, refresh=False):
        if refresh:
            self.__refresh_node()
            self.__refresh_attribute()
        return self.__className

    def opacity(self, refresh=False):
        if refresh:
            self.__refresh_node()
            self.__refresh_attribute()
        return self.__opacity

    def enabled(self, refresh=False):
        if refresh:
            self.__refresh_node()
            self.__refresh_attribute()
        return self.__enabled

    def visible(self, refresh=False):
        if refresh:
            self.__refresh_node()
            self.__refresh_attribute()
        return self.__visible

    def focus(self, refresh=False):
        if refresh:
            self.__refresh_node()
            self.__refresh_attribute()
        return self.__focus

    def exist(self, timeout=None):
        if timeout is None:
            timeout = self.device.default_timeout
        for m_iter in range(0, timeout):
            if m_iter > 0:
                sleep(1)
            self.rect = self.__exist()
            if len(self.rect) > 0:
                return True
        return False

    def __exist(self):
        self.device.refresh_layout()
        tree = xml.dom.minidom.parseString(self.device.xmlStr)
        if tree.documentElement.getAttribute("sopId") == self.app.sopId:
            image = []
            for node in tree.documentElement.childNodes:
                if node.childNodes[0].nodeName == "QQuickMouseArea" and node.childNodes[0].childNodes.length == 0:
                    surface = node.childNodes[1]
                else:
                    surface = node.childNodes[0]
                if len(image) == 0:
                    image = self.__xml_tree_traversed(surface.childNodes, 1)
                else:
                    image = self.__img_cover(image, self.__xml_tree_traversed(surface.childNodes, 1))
            # cv2.imshow("ss", image)
            # cv2.waitKey(0)
            b, g, r = cv2.split(image)
            if len(np.argwhere(r == 255)) > 0:
                return np.argwhere(r == 255)
        return []

    def __xml_tree_traversed(self, nodes, fs):
        images = {}
        for node in nodes:
            clip = int(node.getAttribute("clip"))
            scale = abs(float(node.getAttribute("scale"))*fs)
            height = round(float(node.getAttribute("height"))*scale)
            width = round(float(node.getAttribute("width"))*scale)
            rotation = 0 - int(node.getAttribute("rotation"))
            cx = round(float(node.getAttribute("centerXToGlobal")))
            cy = round(float(node.getAttribute("centerYToGlobal")))
            if float(node.getAttribute("opacity")) != 0 \
                    and int(node.getAttribute("visible")) == 1 \
                    and node.nodeName != "CScrollDecorator" \
                    and node.nodeName != "QQuickShaderEffectSource" \
                    and node.nodeName != "PerformanceOverlay" \
                    and node.nodeName != "QQuickDropArea" \
                    and height > 0 and width > 0 \
                    and not (node.nodeName == "QQuickMouseArea" and node.childNodes.length == 0) \
                    and not (
                        node.getAttribute("objectName") == "multitouchGrid" and int(node.getAttribute("enabled")) == 0):
                index_z = int(node.getAttribute("z"))
                image = np.zeros((height, width), dtype=np.uint8)
                image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
                if node.nodeName != "QQuickLoader" or (node.nodeName == "QQuickLoader" and node.getAttribute("z") == "10000" and node.getAttribute("tempID") == "temp6"):
                    if node.getAttribute("tempID") == self.__tempId:
                        cv2.rectangle(image, (0, 0), (width, height), (0, 0, 255), -1)
                    else:
                        cv2.rectangle(image, (0, 0), (width, height), (255, 0, 0), -1)
                        # cv2.rectangle(image, (0, 0), (width, height), (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), -1)
                hypotenuse = int(math.sqrt(height**2+width**2))
                M1 = np.float32([[1, 0, (hypotenuse - width) / 2], [0, 1, (hypotenuse - height) / 2]])
                image = cv2.warpAffine(image, M1, (hypotenuse, hypotenuse))
                M2 = cv2.getRotationMatrix2D((hypotenuse / 2, hypotenuse / 2), rotation, 1)
                image = cv2.warpAffine(image, M2, (hypotenuse, hypotenuse))
                M3 = np.float32([[1, 0, cx - (hypotenuse / 2)], [0, 1, cy - (hypotenuse / 2)]])
                image = cv2.warpAffine(image, M3, (self.__display_width, self.__display_height))
                if node.childNodes.length > 0:
                    c_images = self.__xml_tree_traversed(node.childNodes, scale)
                    image = self.__img_cover(image, c_images, clip)
                if index_z in images.keys():
                    images[index_z] = self.__img_cover(images[index_z], image)
                else:
                    images[index_z] = image
        im_list = list(images.keys())
        im_list.sort()
        r_image = np.zeros((self.__display_height, self.__display_width), dtype=np.uint8)
        r_image = cv2.cvtColor(r_image, cv2.COLOR_GRAY2BGR)
        for index in im_list:
            r_image = self.__img_cover(r_image, images[index])
        return r_image

    @staticmethod
    def __img_cover(src1, src2, clip=0):
        rows, cols, channels = src2.shape
        roi = src1[0:rows, 0:cols]
        roi2 = src2[0:rows, 0:cols]
        if clip == 1:
            src1_2gray = cv2.cvtColor(src1, cv2.COLOR_BGR2GRAY)
            ret1, mask1 = cv2.threshold(src1_2gray, 1, 255, cv2.THRESH_BINARY_INV)
            image_bg1 = cv2.bitwise_and(roi2, roi2, mask=mask1)
            src2 = cv2.subtract(src2, image_bg1)
        src2_2gray = cv2.cvtColor(src2, cv2.COLOR_BGR2GRAY)
        ret, mask = cv2.threshold(src2_2gray, 1, 255, cv2.THRESH_BINARY)
        image_bg = cv2.bitwise_and(roi, roi, mask=mask)
        image = cv2.subtract(src1, image_bg)
        image = cv2.add(image, src2)
        return image

    def click(self):
        self.device.click(self.__center_x_to_global, self.__center_y_to_global)

    def click_exist(self, timeout=None):
        if timeout is None:
            timeout = self.device.default_timeout
        for m_iter in range(0, timeout):
            if m_iter > 0:
                sleep(1)
            if self.exist():
                if (self.rect[len(self.rect) - 1][1] - self.rect[0][1] + 1) \
                        * (self.rect[len(self.rect) - 1][0] - self.rect[0][0] + 1) == len(self.rect):
                    x = self.rect[0][1] + int((self.rect[len(self.rect) - 1][1] - self.rect[0][1] + 1) / 2)
                    y = self.rect[0][0] + int((self.rect[len(self.rect) - 1][0] - self.rect[0][0] + 1) / 2)
                    self.device.click(x, y)
                    return True
                self.device.click(self.rect[100][1], self.rect[100][0])
                return True
        return False

    def submit_string(self, text):
        self.click()
        self.device.submit_string(text)
