from enum import IntEnum


class ImageCodec(IntEnum):
    jpeg = 0
    jpegxl = 1

    @classmethod
    def has_key(cls, name):
        return name in cls.__members__


class VideoCodec(IntEnum):
    libx264 = 0
    libx265 = 1

    @classmethod
    def has_key(cls, name):
        return name in cls.__members__
