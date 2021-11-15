"""
This module tests that all of bavera can be imported, mostly to help reduce issues
with untested code that will not even parse/run on Py3
"""
from bavera.api.client import *
from bavera.api.http import *
from bavera.api.ratelimit import *
from bavera.bot.bot import *
from bavera.bot.command import *
from bavera.bot.parser import *
from bavera.bot.plugin import *
from bavera.bot.storage import *
from bavera.gateway.client import *
from bavera.gateway.events import *
from bavera.gateway.ipc import *
from bavera.gateway.packets import *
# Not imported, GIPC is required but not provided by default
# from bavera.gateway.sharder import *
from bavera.types.base import *
from bavera.types.channel import *
from bavera.types.guild import *
from bavera.types.invite import *
from bavera.types.message import *
from bavera.types.permissions import *
from bavera.types.user import *
from bavera.types.voice import *
from bavera.types.webhook import *
from bavera.util.backdoor import *
from bavera.util.config import *
from bavera.util.functional import *
from bavera.util.hashmap import *
from bavera.util.limiter import *
from bavera.util.logging import *
from bavera.util.serializer import *
from bavera.util.snowflake import *
from bavera.util.websocket import *
from bavera.voice.client import *
from bavera.voice.opus import *
from bavera.voice.packets import *
from bavera.voice.playable import *
from bavera.voice.player import *
