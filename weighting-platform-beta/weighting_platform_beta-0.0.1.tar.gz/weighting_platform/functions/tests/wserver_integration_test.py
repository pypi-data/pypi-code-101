from weighting_platform.functions import wserver_act_sender
from gravityRecorder.main import Recorder
from whikoperator.main import Wpicoperator
import unittest
import os


class WServerTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.main = wserver_act_sender.WServerActIntegration()
        self.main.make_connection()
        self.main.get_polygon_id(login=os.environ.get('WSERVER_LOGIN'),
                                 password=os.environ.get('WSERVER_PASS'))

        self.recorder = Recorder(dbname=os.environ.get('DBNAME'),
                                 user=os.environ.get('DBUSER'),
                                 password=os.environ.get('DBPASS'),
                                 host=os.environ.get('DBHOST'))

    def test_send_act(self):
        self.main.send_act_operation(self.recorder, 1060)
        result = self.main.get_data()
        self.assertTrue(result['info']['status']
                        and isinstance(result['info']['info'], int))

    def test_send_photo(self):
        cam_operator = Wpicoperator('192.168.100.139', 'admin', 'hect0r1337',
                                    test_mode=True)
        photo_path = '.'
        self.main.send_photo(photo_path, 1337, 'gross', 1, 784672)
        response = self.main.get_data()
        print('TARGET:', response)

    def test_send_act_photo(self):
        self.main.send_act_photo(self.recorder, 1060, '.')

    def test_time_sender(self):
        unsend_acts = self.act_sender_timing.get_unsend_acts_id(self.recorder)
        self.assertTrue(not unsend_acts or isinstance(unsend_acts, list))


if __name__ == '__main__':
    unittest.main()