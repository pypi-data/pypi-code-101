# Copyright (C) 2021 Satoshi Konno. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License")
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http:#www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from .property import Property


class Object(object):
    CODE_MIN = 0x000000
    CODE_MAX = 0xFFFFFF
    CODE_SIZE = 3
    CODE_UNKNOWN = CODE_MIN

    OPERATING_STATUS = 0x80
    MANUFACTURER_CODE = 0x8A
    ANNO_PROPERTY_MAP = 0x9D
    SET_PROPERTY_MAP = 0x9E
    GET_PROPERTY_MAP = 0x9F

    OPERATING_STATUS_ON = 0x30
    OPERATING_STATUS_OFF = 0x31
    OPERATING_STATUS_SIZE = 1
    MANUFACTURER_EVALUATION_CODE_MIN = 0xFFFFF0
    MANUFACTURER_EVALUATION_CODE_MAX = 0xFFFFFF
    MANUFACTURER_CODE_SIZE = 3
    PROPERTY_MAP_MAX_SIZE = 16
    ANNO_PROPERTY_MAP_MAX_SIZE = PROPERTY_MAP_MAX_SIZE + 1
    SET_PROPERTY_MAP_MAX_SIZE = PROPERTY_MAP_MAX_SIZE + 1
    GET_PROPERTY_MAP_MAX_SIZE = PROPERTY_MAP_MAX_SIZE + 1

    MANUFACTURER_UNKNOWN = MANUFACTURER_EVALUATION_CODE_MIN

    def __init__(self):
        self.code = 0
        self.class_group_code = 0
        self.class_code = 0
        self.instance_code = 0
        self.properties = {}
        pass

    def set_code(self, code):
        if type(code) is int:
            self.code = code
            self.class_group_code = ((code >> 16) & 0xFF)
            self.class_code = ((code >> 8) & 0xFF)
            self.instance_code = (code & 0xFF)
            return True
        return False

    def add_property(self, prop):
        if not isinstance(prop, Property):
            return False
        self.properties[prop.code] = prop
        return True
