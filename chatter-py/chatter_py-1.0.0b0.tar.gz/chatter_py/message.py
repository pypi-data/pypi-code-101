"""Container types for data that is routed through the :class:`Bot`"""
from dataclasses import dataclass
from typing import List, Optional


@dataclass
class FeatureMessage:
    """A type of message for use by :class:`Feature` classes.

    `FeatureMessages` do not require a `Feature` to know anything
    about the destination of their message."""
    text: List[str]
    room: Optional[str] = None


@dataclass
class Message:
    """
    A type of message that is used for routing purposes throughout the bot.
    The :class:`Message` class is similar to :class:`FeatureMessage` but it
    requires knowing the room that has sent or will be receiving the given
    `Message`.
    """
    text: List[str]
    room: str

    def __post_init__(self):
        self.original_text = self.text.copy()
