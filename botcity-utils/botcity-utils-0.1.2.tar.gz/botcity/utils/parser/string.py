from __future__ import annotations

import os
from typing import List, Optional


class StringParser:
    def __init__(self, content: str):
        """String Parser

        Args:
            content (str): The string content to be parsed.
        """
        self.curr_position = 0
        self.content = content

    @property
    def current_position(self) -> int:
        """The current parser cursor position
        """
        return self.curr_position

    def goto_tag_start(self, tag: str) -> StringParser:
        """Move the parser cursor to the beginning of the tag.

        Args:
            tag (str): The tag to search for.

        Returns:
            StringParser: this object.
        """
        try:
            idx = self.content.index(tag, self.current_position)
            self.curr_position = idx
        except ValueError:
            # Ignore ValueError raised if tag not found
            pass

        return self

    def goto_tag_end(self, tag: str) -> StringParser:
        """Move the parser cursor to the end of the tag.

        Args:
            tag (str): The tag to search for.

        Returns:
            StringParser: this object.
        """
        try:
            idx = self.content.index(tag, self.current_position)
            self.curr_position = idx+len(tag)
        except ValueError:
            # Ignore ValueError raised if tag not found
            pass

        return self

    def next_contains(self, tag: str) -> bool:
        """Whether or not the content contains the tag starting
        from the current cursor position.

        Args:
            tag (str): The tag to search for.

        Returns:
            bool: True in case the tag is found, False otherwise.
        """
        try:
            self.content.index(tag, self.current_position)
            return True
        except ValueError:
            return False

    def backward_contains(self, tag: str) -> bool:
        """Whether or not the content contains the tag starting
        from the beginning until the current cursor position.

        Args:
            tag (str): The tag to search for.

        Returns:
            bool: True in case the tag is found, False otherwise.
        """
        try:
            self.content.rindex(tag, 0, self.current_position)
            return True
        except ValueError:
            return False

    def back_to_tag_start(self, tag: str) -> bool:
        """Move the current cursor position to the beginning of
        the search tag.

        Args:
            tag (str): The tag to search for.

        Returns:
            bool: Whether or not it was possible to move the cursor.
        """
        try:
            idx = self.content.rindex(tag, 0, self.current_position)
            self.curr_position = idx
            return True
        except ValueError:
            return False

    def back_to_tag_end(self, tag: str) -> bool:
        """Move the current cursor position to the end of
        the search tag.

        Args:
            tag (str): The tag to search for.

        Returns:
            bool: Whether or not it was possible to move the cursor.
        """
        try:
            idx = self.content.rindex(tag, 0, self.current_position)
            self.curr_position = idx+len(tag)
            return True
        except ValueError:
            return False

    def read_until(self, end: str) -> str:
        """Read the content from the current cursor position
        until the position given by the `end` tag.

        Args:
            end (str): The tag to search for.

        Returns:
            str: The sliced content between current position and `end` tag location.
        """
        try:
            idx = self.content.index(end, self.current_position)
            return self.content[self.current_position: idx]
        except ValueError:
            return None

    def get_next_chars(self, chars: int) -> str:
        """Reads and return the content starting from the current position
        with the addition of `chars` more characters.

        Args:
            chars (int): Number of characters to read.

        Returns:
            str: The sliced content.
        """
        start = self.current_position
        end = start+chars
        return self.content[start: end]

    def read_next_lines_until(self, tag_end: str, linesep: Optional[str] = None) -> List:
        """Reads lines until a tag is found.

        Args:
            tag_end (str): The tag to search for.
            linesep (str, optional): The line separator. If not specified the system line separator is used.

        Returns:
            List: List of lines found.
        """
        linesep = linesep or os.linesep
        text = self.read_until(tag_end)
        if text:
            return text.split(linesep)
        return []

    def read_next_lines(self, lines: int, linesep: Optional[str] = None) -> List:
        """Reads the next `lines` lines from the content starting at the current position.

        Args:
            lines (int): Number of lines to read
            linesep (str, optional): The line separator. If not specified the system line separator is used.

        Returns:
            List: List of lines found.
        """
        linesep = linesep or os.linesep
        array = self.content[self.current_position:].split(linesep)
        if len(array) >= lines:
            return array[:lines]
        return None

    def goto_next_line(self, linesep: Optional[str] = None) -> StringParser:
        """Move the cursor to the next line found starting from the current position.

        Args:
            linesep (str, optional): The line separator. If not specified the system line separator is used.

        Returns:
            StringParser: this object.
        """
        linesep = linesep or os.linesep
        if self.next_contains(linesep):
            self.goto_tag_start(linesep)
            self.curr_position += len(linesep)

        return self

    def read(self) -> str:
        """Reads the remaining content starting at the current cursor positon.

        Returns:
            str: the remaining content.
        """
        return self.content[self.current_position:]
