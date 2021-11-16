# pylint: skip-file
import asyncio
import unittest

from .. import connections


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        try:
            self.loop = asyncio.get_event_loop()
        except RuntimeError:
            self.loop = asyncio.new_event_loop()
            asyncio.set_event_loop(self.loop)
        self.run_async(connections.clear)

    def tearDown(self):
        self.run_async(connections.disconnect)

    def assertCanConnect(self, name: str):
        connection = connections.get(name)
        self.run_async(connection.connect)

        handle = self.run_async(connection.begin)
        self.run_async(handle.close)

    def add_connection(self, name, opts):
        connections.add(name, opts)

    def run_async(self, func, *args, **kwargs):
        return self.loop.run_until_complete(func(*args, **kwargs))
