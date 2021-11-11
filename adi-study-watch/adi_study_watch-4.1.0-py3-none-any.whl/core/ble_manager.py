import logging
import time
from queue import Queue

import pywinusb.hid as hid

from . import utils

logger = logging.getLogger(__name__)


class BLEManager:
    RID_CMD = 0x01
    RID_RSP = 0x02
    RID_NOT = 0x03

    CMD_SCAN_STOP = 0x01
    CMD_SCAN_START = 0x00
    CMD_CONNECT = 0x02
    CMD_DISCONNECT = 0x03

    MAX_LENGTH = 63

    def __init__(self, vendor_id, timeout):
        self.queue = Queue()
        self.timeout = timeout
        self.device = hid.HidDeviceFilter(vendor_id=vendor_id).get_devices()[0]
        self.device.set_raw_data_handler(self.callback)

    def callback(self, data):
        logger.debug(f"BLE RX :: {':'.join(utils.convert_int_array_to_hex(data))}")
        self.queue.put(data)

    def _send(self, packet):
        packet = packet + [0 for _ in range(self.MAX_LENGTH - len(packet))]
        logger.debug(f"BLE TX :: {':'.join(utils.convert_int_array_to_hex(packet))}")
        self.report.send(packet)

    def _open(self):
        try:
            self.device.open()
        except Exception as e:
            logger.debug(e)
        self.report = self.device.find_output_reports()[0]

    def _scan_start(self, mac_address):
        default_name = "Nordic_USBD_BLE_UART"
        msg = [self.RID_CMD, self.CMD_SCAN_START, 0, 1] + [ord(i) for i in default_name]
        self._send(msg)
        try:
            while True:
                data = self.queue.get(timeout=self.timeout)
                if data[0] == 3 and data[4:10] == mac_address:
                    break
        except Exception as e:
            logger.debug(e)
            raise Exception(f"Failed to find BLE device {'-'.join(['%X' % i for i in mac_address])}.")

    def _scan_stop(self):
        msg = [self.RID_CMD, self.CMD_SCAN_STOP, 0]
        self._send(msg)
        try:
            while True:
                data = self.queue.get(timeout=self.timeout)
                if data[0] == 2:
                    break
        except Exception as e:
            logger.debug(e)
            raise Exception(f"Failed to stop scan.")

    def connect(self, mac_address):
        self._open()
        mac_address = list(map(int, mac_address.split("-"), [16 for _ in mac_address]))
        mac_address = list(reversed(mac_address))
        self._scan_start(mac_address)
        self._scan_stop()
        msg = [self.RID_CMD, self.CMD_CONNECT] + mac_address
        self._send(msg)
        try:
            while True:
                data = self.queue.get(timeout=self.timeout)
                if data[0] == 3:
                    time.sleep(2)
                    break
        except Exception as e:
            logger.debug(e)
            raise Exception(f"Can't connect to BLE {'-'.join(['%X' % i for i in mac_address])}.")
        logger.info(f"BLE connected to {'-'.join(['%X' % i for i in mac_address])}.")

    def disconnect(self):
        self._open()
        msg = [self.RID_CMD, self.CMD_DISCONNECT]
        self._send(msg)
        self.device.close()
        time.sleep(1)
        self.queue.empty()
