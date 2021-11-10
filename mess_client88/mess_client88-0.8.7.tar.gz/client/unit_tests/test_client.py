import os
import sys
import unittest
sys.path.append(os.path.join(os.getcwd(), '../../..'))
from packets.client.common.variables import TIME, ACTION, PRESENCE, USER, RESPONSE, ERROR

from packets.client import Client
from packets.server import Server

class TestClass(unittest.TestCase):
    '''
    Класс с тестами
    '''


    def test_def_presence(self):
        """Тест коректного запроса"""
        test = Client.client_presence()
        test[TIME] = 1.1  # время необходимо приравнять принудительно
                          # иначе тест никогда не будет пройден
        self.assertEqual(test, {ACTION: PRESENCE, TIME: 1.1, USER: 'Guest'})

    def test_200_ans(self):
        """Тест корректтного разбора ответа 200"""
        self.assertEqual(Client.check_presence_answer({RESPONSE: 200}), '200 : OK')

    def test_400_ans(self):
        """Тест корректного разбора 400"""
        self.assertEqual(Client.check_presence_answer({RESPONSE: 400, ERROR: 'Bad Request'}), '400 : Bad Request')

    def test_no_response(self):
        """Тест исключения без поля RESPONSE"""
        self.assertRaises(ValueError, Client.check_presence_answer, {ERROR: 'Bad Request'})


if __name__ == '__main__':
    Server()
    unittest.main()
