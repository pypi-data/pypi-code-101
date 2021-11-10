import os
import sys
import unittest
sys.path.append(os.path.join(os.getcwd(), '../../..'))
from packets.client.common.variables import RESPONSE, ACTION, TIME, USER, ERROR, PRESENCE

from packets.server import Server

class TestServer(unittest.TestCase):
    '''
    В сервере только 1 функция для тестирования
    '''

    #
    def setUp(self):
        self.norm_dict = {ACTION: PRESENCE, TIME: '1.1', USER: 'Guest'}
        self.without_presence = {TIME: '1.1', USER:'Guest'}
        self.wrong_action = {ACTION: 'Wrong', TIME: '1.1', USER: 'Guest'}
        self.without_time = {ACTION: PRESENCE, USER:'Guest'}
        self.without_user = {ACTION: PRESENCE, TIME: '1.1'}
        self.not_guest = {ACTION: PRESENCE, TIME: '1.1', USER: 'Guest12'}

        self.err_dict = {RESPONSE: 400, ERROR: 'Bad Request'}
        self.ok_dict = {RESPONSE: 200}
    # err_dict = {
    #     RESPONSE: 400,
    #     ERROR: 'Bad Request'
    # }
    # ok_dict = {RESPONSE: 200}

    def test_no_action(self):
        """Ошибка если нет действия"""
        self.assertEqual(Server.client_presence_answer(
            self.without_presence), self.err_dict)

    def test_wrong_action(self):
        """Ошибка если неизвестное действие"""
        self.assertEqual(Server.client_presence_answer(
            self.wrong_action), self.err_dict)

    def test_no_time(self):
        """Ошибка, если  запрос не содержит штампа времени"""
        self.assertEqual(Server.client_presence_answer(
            self.without_time), self.err_dict)

    def test_no_user(self):
        """Ошибка - нет пользователя"""
        self.assertEqual(Server.client_presence_answer(
            self.without_user), self.err_dict)

    def test_unknown_user(self):
        """Ошибка - не Guest"""
        self.assertEqual(Server.client_presence_answer(
            self.not_guest), self.err_dict)

    def test_ok_check(self):
        """Корректный запрос"""
        self.assertEqual(Server.client_presence_answer(
            self.norm_dict), self.ok_dict)


if __name__ == '__main__':
    unittest.main()