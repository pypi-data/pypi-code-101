# ------------------------------------------------------------------------------
#  MIT License
#
#  Copyright (c) 2021 Hieu Pham. All rights reserved.
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.
# ------------------------------------------------------------------------------

import json
from cerebro.refactoring import Object
from cerebro.refactoring.serializations import Serializer, Deserializer
from json import JSONEncoder as BaseJsonEncoder, JSONDecoder as BaseJsonDecoder


class JsonSerializer(BaseJsonEncoder, Serializer):
    """
    This class serialize object into json data.
    ---------
    @author:    Hieu Pham.
    @created:   10.10.2021.
    @updated:   11.10.2021.
    """
    def __init__(self, **kwargs):
        """
        Create new object.
        :param kwargs:  keyword arguments.
        """
        Serializer.__init__(self, name='JsonEncoder')
        BaseJsonEncoder.__init__(self, default=self.data)

    def to_json(self, obj: Object = None, indent: int = 4, sort: bool = False, **kwargs) -> str:
        """
        Encode object instance to json string.
        :param obj:     object to be encoded.
        :param indent:  intent level.
        :param sort:    sort keys or not.
        :param kwargs:  additional keyword arguments.
        :return:        json string.
        """
        return json.dumps(self.data(obj), indent=indent, sort_keys=sort, **kwargs)

    def to_file(self, obj: Object = None, path: str = "default.json", intent: int = 4, sort: bool = False, **kwargs):
        """
        Encode object instance to json file.
        :param obj:     object to be encoded.
        :param path:    path to json file.
        :param intent:  intent level.
        :param sort:    sort keys or not.
        :param kwargs:  additional keyword arguments.
        :return:        none.
        """
        with open(path, 'w+') as file:
            file.seek(0)
            file.write(self.to_json(obj, intent, sort, **kwargs))


class JsonDeserializer(BaseJsonDecoder, Deserializer):
    """
    This class deserialize json data to object.
    ---------
    @author:    Hieu Pham.
    @created:   10.10.2021.
    @updated:   10.10.2021.
    """
    def __init__(self, **kwargs):
        """
        Create new object.
        :param kwargs:  keyword arguments.
        """
        Deserializer.__init__(self, name='JsonDecoder')
        BaseJsonDecoder.__init__(self, object_hook=self.create)

    def from_json(self, data: str = None, **kwargs):
        """
        Decode object from json string.
        :param data:    json data.
        :param kwargs:  keyword arguments.
        :return:        decoded object.
        """
        return self.decode(data) if data is not None else None

    def from_file(self, path: str = "default.json", **kwargs):
        """
        Decode object from json file.
        :param path:    path to json file.
        :param kwargs:  additional keyword arguments.
        :return:        decoded object.
        """
        with open(path, "r+") as file:
            file.seek(0)
            return self.from_json(file.read())
