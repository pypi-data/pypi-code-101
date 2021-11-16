
from test_framework.database.dut_database import update_slot


class OakgateSlot(object):

    def __init__(self, config_name):
        self.config_name = config_name

    @update_slot
    def refresh(self):
        pass

