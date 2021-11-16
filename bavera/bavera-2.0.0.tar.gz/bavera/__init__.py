"""
Discord API Wrapper
~~~~~~~~~~~~~~~~~~~

A basic wrapper for the Discord API.

:copyright: (c) 2015-present Rapptz
:license: MIT, see LICENSE for more details.

"""

__title__ = "bavera"
__author__ = "bavera"
__license__ = "MIT"
__copyright__ = "Copyright 2021-present Bavera"
__version__ = "2.0.0"

__path__ = __import__("pkgutil").extend_path(__path__, __name__)

import logging
from typing import NamedTuple, Literal

from .plugin_manager import *
from .properties.appinfo import *
from .user import *
from .properties.emoji import *
from .partial_emoji import *
from .properties.activity import *
from .properties.channel import *
from .properties.guild import *
from .flags import *
from .properties.member import *
from .message import *
from .properties.asset import *
from .errors import *
from .permissions import *
from .properties.role import *
from .properties.file import *
from .managers.colour import *
from .advanced.integrations import *
from .invite import *
from .template import *
from .widget import *
from .properties.object import *
from .reaction import *
from . import utils, abc, ui
from .properties import abc
from .enums import *
from .properties.embeds import *
from .mentions import *
from .managers.shard import *
from .player import *
from .webhook import *
from .properties.audit_logs import *
from .raw_models import *
from .team import *
from .properties.sticker import *
from .stage_instance import *
from .advanced.interactions import *
from .properties.components import *
from .properties.threads import *


class VersionInfo(NamedTuple):
    major: int
    minor: int
    micro: int
    releaselevel: Literal["alpha", "beta", "candidate", "final"]
    serial: int


version_info: VersionInfo = VersionInfo(
    major=2, minor=0, micro=0, releaselevel="alpha", serial=0
)

logging.getLogger(__name__).addHandler(logging.NullHandler())
