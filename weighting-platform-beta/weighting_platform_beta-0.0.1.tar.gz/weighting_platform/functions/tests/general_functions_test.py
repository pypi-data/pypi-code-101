import unittest
from weighting_platform.functions import general_functions
from weighting_platform.tests.test_objects import test_sql_shell
from qdk.main import QDK
from time import sleep


class GfTest(unittest.TestCase):
    def test_get_percent(self):
        first = 1000
        second = 500
        result_must = 50
        result = general_functions.get_change_percent(first, second)
        self.assertEqual(result, result_must)

    def test_send_status(self):
        qdk = QDK('localhost', 4455)
        qdk.make_connection()
        qdk.subscribe()
        while True:
            general_functions.send_status('SASD')
            print("RESPONSE:", qdk.get_data())
            sleep(1)

    def test_update_last_events(self):
        response = general_functions.update_last_events(test_sql_shell, car_id=895, carrier=1,
                                                        trash_type=1, trash_cat=1, polygon=1)
        print(response)

    def test_get_mac_ar(self):
        response = general_functions.get_mac_ar()
        print(response)

    def test_send_mac_ar(self):
        qdk = QDK('192.168.100.118', 8888)
        qdk.make_connection()
        qdk.subscribe()
        send = general_functions.send_mac_ar('12:12:12')
        print(send)
        get_answer = qdk.get_data()
        print(get_answer)


if __name__ == '__main__':
    unittest.main()
