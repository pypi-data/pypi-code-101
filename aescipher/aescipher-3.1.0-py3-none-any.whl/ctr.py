from Crypto.Cipher import AES
from Crypto.Util import Counter
from omnitools import sha256d, str_or_bytes, try_utf8e, try_utf8d


class AESCipherCTR:
    mode: str = None

    def __init__(self, key: str_or_bytes, iv: bytes = b"\x00"*8, initial_value: int = 1):
        self.__cipher = AES.new(sha256d(key), AES.MODE_CTR, counter=Counter.new(64, iv, initial_value=initial_value))

    def encrypt(self, raw: str_or_bytes) -> bytes:
        mode = "encryption"
        if not self.mode:
            self.mode = mode
        elif self.mode != mode:
            raise Exception("this cipher is currently in '{}' mode. create a new object instead.".format(self.mode))
        return self.__cipher.encrypt(try_utf8e(raw))

    def decrypt(self, raw: bytes) -> str_or_bytes:
        mode = "decryption"
        if not self.mode:
            self.mode = mode
        elif self.mode != mode:
            raise Exception("this cipher is currently in '{}' mode. create a new object instead.".format(self.mode))
        return try_utf8d(self.__cipher.decrypt(raw))


