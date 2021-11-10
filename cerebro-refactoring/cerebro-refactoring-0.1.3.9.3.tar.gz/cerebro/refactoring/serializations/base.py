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

from cerebro.refactoring import Object
from importlib import import_module
from cerebro.refactoring.designs import Singleton


class Serializer(Object, metaclass=Singleton):
    """
    Encoder can serialize objects into object data. The encoder will be a singleton
    to reduce memory consuming.
    ---------
    @author:    Hieu Pham.
    @created:   10.10.2021.
    @updated:   18.10.2021.
    """
    def data(self, instance: Object = None, **kwargs) -> dict:
        """
        Get object data.
        :param instance: instance to be encoded.
        :param kwargs:   keyword arguments.
        :return:         object data.
        """
        return instance.data(**kwargs) if isinstance(instance, Object) else None


class Deserializer(Object, metaclass=Singleton):
    """
    Decoder can deserialize object data into objects. The decoder will be a singleton
    to reduce memory consuming.
    ---------
    @author:    Hieu Pham.
    @created:   10.10.2021.
    @updated:   18.10.2021.
    """
    @classmethod
    def create(cls, data: dict = None, **kwargs):
        """
        Create object from data.
        :param data:    object data.
        :param kwargs:  keyword arguments.
        :return:        object.
        """
        # Validate data format. The correct format must have classname and module info.
        if 'classname' in data and 'module' in data:
            # Dynamic load module and class based on classname.
            classname, module = data.pop('classname'), data.pop('module')
            classes = getattr(import_module(module), classname)
            # Deserialize object if class is serializable.
            if issubclass(classes, Object):
                return classes(**data)
        # Otherwise, raise an error.
        raise AssertionError('Object data format is invalid!')
