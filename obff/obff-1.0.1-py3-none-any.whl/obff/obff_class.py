import zlib
from enum import Enum

class OBFF_CLASS:

    class OBFF_VERSION(Enum):
        V1 = b'\x4f\x42\x46\x46\x31\x30\x00\x00'

    class Book:
        def __init__(self):
            pass


    def write(self, file_path: str, book: Book, version: OBFF_VERSION = OBFF_VERSION.V1):
        pass

    def read(self, file_path: str) -> Book:
        pass
