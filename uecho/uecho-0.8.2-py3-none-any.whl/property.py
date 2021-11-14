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

from .protocol.property import Property as ProtocolProperty


class Property(ProtocolProperty):
    CODE_MIN = 0x80
    CODE_MAX = 0xFF

    FORMAT1_MAX_SIZE = 15
    FORMAT2_SIZE = 18
    FORMAT_MAX_SIZE = FORMAT2_SIZE

    ATTRIBUTE_NONE = 0x00
    ATTRIBUTE_READ = 0x01
    ATTRIBUTE_WRITE = 0x02
    ATTRIBUTE_ANNO = 0x10
    ATTRIBUTE_READ_WRITE = ATTRIBUTE_READ | ATTRIBUTE_WRITE
    ATTRIBUTE_READ_ANNO = ATTRIBUTE_READ | ATTRIBUTE_ANNO

    def __init__(self):
        super(Property, self).__init__()
        self.attr = Property.ATTRIBUTE_NONE
