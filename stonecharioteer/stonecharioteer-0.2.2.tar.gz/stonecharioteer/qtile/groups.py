"""This module defines the groups in Qtile"""

from enum import Enum
from libqtile.config import Group


class GroupName(Enum):
    """Enumerated group names"""

    MAIL = "mail"
    CHAT = "chat"
    TERM = "terminal"
    PERSONAL = "personal"
    TINKERING = "tinkering"
    DEV = "dev"
    CALL = "call"


groups = [Group(group.value) for group in list(GroupName)]
