import unittest

from ymir.ids import task_id as task_util


class TestTaskUtil(unittest.TestCase):
    def __init__(self, methodName: str) -> None:
        super().__init__(methodName=methodName)
        self.id_type = 't'
        self.sub_task_id = '0'
        self.id_reserve = '00'
        self.user_id = 'a' * task_util.IDProto.ID_LEN_USER_ID
        self.repo_id = 'b' * task_util.IDProto.ID_LEN_REPO_ID
        self.hex_task_id = 'z' * task_util.IDProto.ID_LEN_HEX_TASK_ID

        self.task_id_str = ''.join(
            [self.id_type, self.sub_task_id, self.id_reserve, self.user_id, self.repo_id, self.hex_task_id])

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_build_task_id(self):
        task_id_cls = task_util.TaskId(self.id_type, self.sub_task_id, self.id_reserve, self.user_id, self.repo_id,
                                       self.hex_task_id)

        assert str(task_id_cls) == self.task_id_str
        assert self.id_type == task_id_cls.id_type
        assert self.sub_task_id == task_id_cls.sub_task_id
        assert self.id_reserve == task_id_cls.id_reserve
        assert self.user_id == task_id_cls.user_id
        assert self.repo_id == task_id_cls.repo_id
        assert self.hex_task_id == task_id_cls.hex_task_id

    def test_build_from_task_id(self):
        task_id_cls = task_util.TaskId.from_task_id(self.task_id_str)
        assert self.id_type == task_id_cls.id_type
        assert self.sub_task_id == task_id_cls.sub_task_id
        assert self.id_reserve == task_id_cls.id_reserve
        assert self.user_id == task_id_cls.user_id
        assert self.repo_id == task_id_cls.repo_id
        assert self.hex_task_id == task_id_cls.hex_task_id
