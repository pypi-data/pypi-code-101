
import os
import sys
from .oakgate_slot import OakgateSlot
from .linux_slot import LinuxSlot


class Slot(object):

    def __init__(self, name, config_name):
        self.config_name = config_name
        self.name = name
        self.dev = self.get_slot()

    def refresh(self):
        self.dev.refresh()

    def get_slot(self):
        platform = os.environ.get('platform', '')
        if platform == "oakgate":
            slot = OakgateSlot(self.config_name)
        elif platform == "linux":
            slot = LinuxSlot(self.config_name)
        else:
            if "win" in sys.platform:
                slot = OakgateSlot(self.config_name)
            else:
                slot = LinuxSlot(self.config_name)
        return slot
