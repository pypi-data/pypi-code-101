# Copyright 2021 Vincent Texier <vit@free.fr>
#
# This software is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import json
import os
import shutil
from pathlib import Path
from typing import Any

from tikka.data.constants import CONFIG_FILENAME, DEFAULT_CONFIG_PATH


class Config:
    data: dict = {}
    filepath = None

    def __init__(self, path: Path):
        """
        Create config file in user config path

        :param path: Path instance of config file path
        :return:
        """
        self.filepath = Path().joinpath(path, CONFIG_FILENAME).expanduser()

        if not path.expanduser().exists():
            os.makedirs(path.expanduser())

        if not self.filepath.exists():
            # copy default config in user config path
            shutil.copyfile(DEFAULT_CONFIG_PATH.expanduser(), self.filepath)

        # load config file in data
        self.load()

    def load(self):
        """
        Load config file content in data

        :return:
        """
        with self.filepath.open("r", encoding="utf-8") as file_handler:
            self.data = json.load(file_handler)

    def save(self):
        """
        Save data in config file

        :return:
        """
        with self.filepath.open("w", encoding="utf-8") as file_handler:
            json.dump(self.data, file_handler)

    def set(self, name: str, value: Any):
        """
        Set named parameter to value

        :param name: Name of parameter
        :param value: New value
        :return:
        """
        self.data[name] = value
        self.save()

    def get(self, name: str):
        """
        Get value of named parameter

        :param name:
        :return:
        """
        return self.data[name]
