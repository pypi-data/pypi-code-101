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
import sys
from collections import OrderedDict
from pathlib import Path

# Path constants
DATA_PATH = Path("~/.config/tikka")

# Standalone executable install
if getattr(sys, "frozen", False):
    PACKAGE_PATH = Path(sys.executable).parent
    IMAGES_PATH = PACKAGE_PATH.joinpath("images")
# Python package install
else:
    PACKAGE_PATH = Path(__file__).parents[1]
    IMAGES_PATH = PACKAGE_PATH.joinpath("gui/images/files")

LOCALES_PATH = PACKAGE_PATH.joinpath("locales")
ASSETS_PATH = PACKAGE_PATH.joinpath("assets")
CONFIG_FILENAME = "config.json"
DEFAULT_CONFIG_PATH = ASSETS_PATH.joinpath(CONFIG_FILENAME)
DATABASE_FILE_EXTENSION = ".sqlite3"
DATABASE_MIGRATIONS_PATH = ASSETS_PATH.joinpath("migrations")

# Constants
CURRENCIES = OrderedDict([("g1", "Ğ1"), ("g1-test", "Ğ1-test")])
LANGUAGES = OrderedDict([("en_US", "English"), ("fr_FR", "Français")])
MNEMONIC_LANGUAGES = {"en_US": "english", "fr_FR": "french"}
ACCESS_TYPE_MNEMONIC = "mnemonic"
ACCESS_TYPE_CLASSIC = "classic"
