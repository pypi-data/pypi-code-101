import subprocess

from autobright.core import Display


class DDCControl(Display):
    def __init__(self, device: int):
        self.device = device

    def set_brightness(self, brightness: int) -> None:
        assert 0 <= brightness <= 100, "Brightness must be between 0 and 100."

        command = [
            "ddccontrol",
            "-r",
            "0x10",
            "-w",
            str(brightness),
            f"dev:/dev/i2c-{self.device}",
        ]
        status = subprocess.call(command)

        if status != 0:
            print("ddccontrol failed but it might still have worked")
