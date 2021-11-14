import logging
import os
import sys
from unittest import TestCase

TEST_DIR = os.path.sep.join([os.getcwd(), 'test'])
log = logging.getLogger()
log.setLevel(logging.DEBUG)
handler = logging.StreamHandler(stream=sys.stdout)
handler.setFormatter(logging.Formatter(fmt='[%(asctime)s: %(levelname)s\t] %(message)s'))
log.addHandler(handler)


class TestParser(TestCase):
    def test_read(self):
        # entity = Entity().
        pass