import logging
from typing import List

from .data_type import DataType

logger = logging.getLogger(__name__)


class SubStructure(DataType):

    def __init__(self, size: int, reverse: bool = False, default: str = ""):
        super().__init__(size, reverse, default)

    def encode(self):
        return [ord(char) for char in self.get_value()]

    def decode(self, array: List):
        result = ""
        for val in array:
            if val == 0x0:
                break
            result += chr(val)
        self.set_value(str(result))

    def default_value(self):
        return self.set_value("")

    def _value_check(self, value: str):
        if not type(value) == str:
            self.default_value()
            logger.error(f"{value} is not of type str. Using default value {self.get_value()}.")
            return False

        return True
