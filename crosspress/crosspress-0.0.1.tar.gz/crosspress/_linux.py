import atexit
import os
import re
import struct
import time
from glob import glob


# The code in this file is partially borrowed and modified from the source
# https://github.com/boppreh/keyboard/blob/master/keyboard/_nixcommon.py


def make_uinput():
    if not os.path.exists('/dev/uinput'):
        raise IOError('No uinput module found.')

    import fcntl
    import struct

    uinput = open("/dev/uinput", 'wb')
    fcntl.ioctl(uinput, 0x40045564, 0x01)

    for i in range(256):
        fcntl.ioctl(uinput, 0x40045565, i)

    uinput.write(struct.pack("80sHHHHi64i64i64i64i", b"Virtual Keyboard", 0x03, 1, 1, 1, 0, *[0] * 256))
    uinput.flush()

    fcntl.ioctl(uinput, 0x5501)

    return uinput


class EventDevice(object):
    def __init__(self, path):
        self.path = path
        self._output_file = None

    @property
    def output_file(self):
        if self._output_file is None:
            self._output_file = open(self.path, 'wb')
            atexit.register(self._output_file.close)
        return self._output_file

    def write_event(self, event, code, value):
        integer, fraction = divmod(time.time(), 1)
        seconds = int(integer)
        microseconds = int(fraction * 1e6)
        event_bin_format = 'llHHI'
        data_event = struct.pack(event_bin_format, seconds, microseconds, event, code, value)
        sync_event = struct.pack(event_bin_format, seconds, microseconds, 0x00, 0, 0)

        self.output_file.write(data_event + sync_event)
        self.output_file.flush()


class AggregatedEventDevice(object):
    def __init__(self, devices, output=None):
        self.devices = devices
        self.output = output or self.devices[0]

    def write_event(self, code, value):
        self.output.write_event(0x01, code, value)


def list_devices_from_proc():
    try:
        with open('/proc/bus/input/devices') as f:
            description = f.read()
    except FileNotFoundError:
        return

    for name, handlers in re.findall(r"""N: Name="([^"]+?)".+?H: Handlers=([^\n]+)""", description, re.DOTALL):
        path = '/dev/input/event' + re.search(r'event(\d+)', handlers).group(1)
        if "kbd" in handlers:
            yield EventDevice(path)


def list_devices_from_by_id(by_id=True):
    for path in glob('/dev/input/{}/*-event-{}'.format('by-id' if by_id else 'by-path', "kbd")):
        yield EventDevice(path)


def aggregate_devices():
    try:
        uinput = make_uinput()
        fake_device = EventDevice('uinput Fake Device')
        fake_device._output_file = uinput
    except IOError:
        import warnings
        warnings.warn('Failed to create a device file using `uinput` module. Sending of events may be limited or '
                      'unavailable depending on plugged-in devices.', stacklevel=2)
        fake_device = None

    devices_from_proc = list(list_devices_from_proc())
    if devices_from_proc:
        return AggregatedEventDevice(devices_from_proc, output=fake_device)

    devices_from_by_id = list(list_devices_from_by_id()) or list(list_devices_from_by_id(by_id=False))
    if devices_from_by_id:
        return AggregatedEventDevice(devices_from_by_id, output=fake_device)

    assert fake_device
    return fake_device


device = aggregate_devices()


def sequence(codes, delay):
    for code in codes:
        device.write_event(code[3], 1)
        time.sleep(delay)
    codes.reverse()
    for code in codes:
        device.write_event(code[3], 0)
        time.sleep(delay)
    return
