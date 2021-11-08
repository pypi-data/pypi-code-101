from pymetaf.parser import parse_text
from .case import *


def test_metars():
    for base_case in BASE_CASES:
        result = parse_text(**base_case['kwargs'])
        assert result == base_case['result']