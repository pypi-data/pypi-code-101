from autobright.core import BrightnessModel


class ProportionalBrightnessModel(BrightnessModel):
    def map(self, reading: int) -> int:
        b = 0.0211292
        return int(min(b * reading, 100))
