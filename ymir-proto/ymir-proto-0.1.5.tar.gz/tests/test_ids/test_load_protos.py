import unittest

from ymir.protos import mir_common_pb2 as mir_common
from ymir.protos import mir_controller_service_pb2 as mirsvrpb


class TestTaskUtil(unittest.TestCase):
    def test_load_protos(self):
        # will fail if no protos were found.
        pass
