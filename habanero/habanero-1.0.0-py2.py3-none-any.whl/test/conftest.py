"""Test configuration"""

import os
import sys

import pytest

LIB_DIR = os.path.join('lib', os.path.dirname('.'))
sys.path.insert(0, os.path.abspath(LIB_DIR))

@pytest.fixture()
def vcr_cassette_dir():
    return os.path.join('tests', 'vcr_cassettes', os.path.dirname('.'))
