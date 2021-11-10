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
from abc import ABC, abstractmethod
from typing import Any, Union, List


class BatchProcess(Object, ABC):
    """
    This pattern is used when we need to process batch of things but every
    item will be processed in the same way.
    ---------
    @author:    Hieu Pham.
    @created:   15.10.2021.
    @updated:   18.10.2021.
    """

    def batch_process(self, payload: Union[Any, List[Any]] = None, **kwargs):
        """
        Process batch of payloads.
        :param payload: batch of payloads.
        :param kwargs:  keyword arguments.
        :return:        any.
        """
        if payload is None:
            return None
        # In case of batch is list, process each item sequentially.
        if isinstance(payload, list):
            result = [self.batch_process(single, **kwargs) for single in payload]
        # In case of batch is not list, process it as singular object.
        else:
            result = self.single_process(payload, **kwargs)
        # Return result.
        return result

    @abstractmethod
    def single_process(self, payload: Any = None, **kwargs):
        """
        Process singular object.
        :param payload: given object.
        :param kwargs:  keyword arguments.
        :return:        any.
        """
        return payload
