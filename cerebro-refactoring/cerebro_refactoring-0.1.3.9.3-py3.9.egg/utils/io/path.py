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

import os
import shutil
from copy import copy
from datetime import datetime
from pathlib import Path as BasePath


class Path:
    """
    This class is used to handle a path.
    ---------
    @author:    Hieu Pham.
    @created:   19.10.2021.
    @updated:   19.10.2021.
    """

    @property
    def path(self):
        """
        Get current path.
        :return: path.
        """
        return str(self._path)

    def __init__(self, path: str = None, **kwargs):
        """
        Created new object.
        :param path:    given path.
        :param kwargs:  keyword arguments.
        """
        super().__init__()
        self._path = BasePath(os.path.expanduser(path))

    def makedir(self, **kwargs):
        """
        Make directory if it does not exist.
        :param kwargs:  keyword arguments.
        :return:        path object.
        """
        suffixes = list(self._path.suffixes)
        if len(suffixes) > 0:
            parts = list(self._path.parts)[:-1]
            BasePath(*parts).makedir()
        else:
            self._path.makedir()
        return self

    def copy(self, dst: str = None, **kwargs):
        """
        Copy path to given destination.
        :param dst:     given destination.
        :param kwargs:  keyword arguments.
        :return:        path object.
        """
        suffixes = list(self._path.suffixes)
        if len(suffixes) > 0:
            shutil.copy2(self.path, dst)
        else:
            shutil.copytree(self.path, dst)
        return self

    def move(self, dst: str = None, **kwargs):
        """
        Move path to given destination.
        :param dst:     given destination.
        :param kwargs:  keyword arguments.
        :return:        path object.
        """
        shutil.move(self.path, dst)
        return self

    def delete(self, **kwargs):
        """
        Delete path.
        :param kwargs:  keyword arguments.
        :return:        path object.
        """
        suffixes = list(self._path.suffixes)
        if len(suffixes) > 0:
            os.remove(self.path)
        else:
            shutil.rmtree(self.path)
        return self

    def insert(self, index, candidate, **kwargs):
        """
        Insert a candidate into current path.
        :param index:       index to insert.
        :param candidate:   candidate to insert.
        :param kwargs:      keyword arguments.
        :return:            path object.
        """
        parts = list(self._path.parts)
        parts.insert(index, candidate)
        self._path = BasePath(*parts)
        return self

    def remove(self, index, **kwargs):
        """
        Remove a candidate from current path.
        :param index:   index to be removed.
        :param kwargs:  keyword arguments.
        :return:        path object.
        """
        parts = list(self._path.parts)
        parts.pop(index)
        self._path = BasePath(*parts)
        return self

    def replace(self, index, candidate, **kwargs):
        """
        Replace with a candidate.
        :param index:       index to be replaced.
        :param candidate:   candidate to replace.
        :param kwargs:      keyword arguments.
        :return:            path object.
        """
        parts = list(self._path.parts)
        parts[index] = candidate
        self._path = BasePath(*parts)
        return self

    def unique_suffix(self, **kwargs):
        """
        Make unique suffix by insert number.
        :param kwargs:  keyword arguments.
        :return:        path object.
        """
        parts = list(self._path.parts)
        parts.pop(-1)
        count = 0
        while True:
            stem = [self._path.stem, '-%s' % count if count > 0 else '']
            stem.extend(list(self._path.suffixes))
            stem = ''.join(stem)
            new_parts = copy(parts)
            new_parts.append(stem)
            new_path = BasePath(*new_parts)
            if new_path.is_dir() or new_path.is_file():
                count += 1
                continue
            self._path = new_path
            return self

    def datetime_suffix(self, strftime: str = '-%Y-%m-%d-%H-%M-%S', **kwargs):
        """
        Make datetime suffix.
        :param strftime:    string format of time.
        :param kwargs:      keyword arguments.
        :return:            path object.
        """
        parts = list(self._path.parts)
        parts.pop(-1)
        stem = [self._path.stem, datetime.now().strftime(strftime)]
        stem.extend(list(self._path.suffixes))
        stem = ''.join(stem)
        parts.append(stem)
        self._path = BasePath(*parts)
        return self
