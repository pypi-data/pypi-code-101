import unittest

from ymir.ids import class_ids as ids


class TestIds(unittest.TestCase):
    def __init__(self, methodName: str) -> None:
        super().__init__(methodName=methodName)

    def test_create_id_manager(self):
        class_id_manager = ids.ClassIdManager()
        assert class_id_manager.size() == 1064
