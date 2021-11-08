import unittest
from multiprocessing import Process

from drb import DrbNode
from drb_impl_http import DrbHttpNode, DrbHttpFactory
from tests.utility import start_serve, PORT, PATH

process = Process(target=start_serve)


class TestDrbHttpFactory(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        process.start()

    @classmethod
    def tearDownClass(cls) -> None:
        process.kill()

    def test_create(self):
        factory = DrbHttpFactory()
        node = factory.create('http://localhost:'+PORT+PATH+'test.txt')
        self.assertIsInstance(node, (DrbHttpNode, DrbNode))
