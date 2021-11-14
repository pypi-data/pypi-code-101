import abc


class Sensor(abc.ABC):
    @abc.abstractmethod
    def get_reading(self) -> int:
        raise NotImplementedError()


class BrightnessModel(abc.ABC):
    @abc.abstractmethod
    def map(self, reading: int) -> int:
        raise NotImplementedError()


class Display(abc.ABC):
    @abc.abstractmethod
    def set_brightness(self, brightness: int) -> None:
        raise NotImplementedError()
