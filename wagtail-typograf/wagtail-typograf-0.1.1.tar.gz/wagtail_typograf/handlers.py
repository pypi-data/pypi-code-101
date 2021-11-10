import logging
import re
from typing import Callable

from typus import en_typus, ru_typus


logger = logging.getLogger(__name__)


class Typograf:
    def __init__(self, value: str) -> None:
        self.value = value
        self.func = self.get_func()
        logger.debug("Typograf initialized: %s \"%s...\"", self.func.__name__, self.value[:100])

    def get_func(self) -> Callable:
        return ru_typus if re.search(r'[а-яА-Я]', self.value) else en_typus

    def process(self) -> str:
        return self.func(self.value)
