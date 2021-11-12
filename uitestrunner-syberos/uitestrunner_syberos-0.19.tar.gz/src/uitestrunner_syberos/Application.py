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

from time import sleep
from .Item import Item
from lxml import etree


class Application:
    sopId = ""
    uiAppId = ""
    device = None

    def __init__(self, d=None, sop="", ui=""):
        self.sopId = sop
        self.uiAppId = ui
        self.device = d

    def launch(self, timeout=None):
        self.device.refresh_layout()
        self.device.con.get(path="launchApp", args="sopid=" + self.sopId + "&" + "uiappid=" + self.uiAppId)
        if timeout is None:
            timeout = self.device.default_timeout
        for m_iter in range(0, timeout):
            self.device.refresh_layout()
            selector = etree.XML(self.device.xmlStr.encode('utf-8'))
            if selector.get("sopId") == self.sopId:
                return True
            self.device.con.get(path="launchApp", args="sopid=" + self.sopId + "&" + "uiappid=" + self.uiAppId)
            sleep(1)
        return False

    def is_topmost(self):
        self.device.refresh_layout()
        selector = etree.XML(self.device.xmlStr.encode('utf-8'))
        if selector.get("sopId") == self.sopId:
            return True
        return False

    def close(self):
        self.device.con.get(path="quitApp", args="sopid=" + self.sopId)

    def __get_device_default_time(self):
        return self.device.default_timeout

    def find_item_by_xpath_key(self, xpath_key, timeout=None):
        i = self.__find_item_by_xpath(self.device.get_xpath(self.sopId, xpath_key), timeout)
        self.device.log("debug", "find_item_by_xpath_key(), xpath_key=%s, find Item successful, %s" % (xpath_key, str(i)))
        return i

    def find_item_by_xpath(self, xpath, timeout=None):
        i = self.__find_item_by_xpath(xpath, timeout)
        self.device.log("debug", "find_item_by_xpath(), find Item successful, %s" % (str(i)))
        return i

    def __find_item_by_xpath(self, xpath, timeout=None):
        if timeout is None:
            timeout = self.device.default_timeout
        for m_iter in range(0, timeout):
            if m_iter > 0:
                sleep(1)
            self.device.refresh_layout()
            selector = etree.XML(self.device.xmlStr.encode('utf-8'))
            nodes = selector.xpath(xpath)
            if selector.get("sopId") == self.sopId:
                if len(nodes) > 0:
                    node = nodes[0]
                    i = Item(d=self.device, a=self, node=node, xpath=xpath)
                    return i
            else:
                raise Exception('error: application is not the top window!')
        raise Exception('timeout: not found that item!')
