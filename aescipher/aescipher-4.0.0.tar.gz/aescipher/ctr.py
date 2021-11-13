from Crypto.Cipher import AES
from Crypto.Util import Counter
from omnitools import sha3_256d, str_or_bytes, try_utf8e, try_utf8d


class AESCipherCTR_Base:
    mode: str = None
    _cipher = None
    sequentialize_cv = None

    def encrypt(self, raw: str_or_bytes) -> bytes:
        mode = "encryption"
        if not self.mode:
            self.mode = mode
        elif self.mode != mode:
            raise Exception("this cipher is currently in '{}' mode. create a new object instead.".format(self.mode))
        return b"".join(self.sequentialize_cv() or self._cipher.encrypt(bytes([_])) for _ in try_utf8e(raw))

    def decrypt(self, raw: bytes) -> str_or_bytes:
        mode = "decryption"
        if not self.mode:
            self.mode = mode
        elif self.mode != mode:
            raise Exception("this cipher is currently in '{}' mode. create a new object instead.".format(self.mode))
        return try_utf8d(b"".join(self.sequentialize_cv() or self._cipher.decrypt(bytes([_])) for _ in raw))


class AESCipherCTR(AESCipherCTR_Base):
    def __init__(self, key: str_or_bytes, iv: bytes = b"\x00"*8, initial_value: int = 1, sequentialize_cv: bool = False):
        def aes_gen(_initial_value):
            return AES.new(sha3_256d(key), AES.MODE_CTR, counter=Counter.new(64, iv, initial_value=_initial_value))

        def sequentialize(i=[initial_value-2]):
            if isinstance(i, list):
                _i = i[0]+1
                i.clear()
                i.append(_i)
            else:
                _i = i
            if sequentialize_cv:
                self._cipher = aes_gen(_i)
            elif not self._cipher:
                self._cipher = aes_gen(initial_value)

        self.sequentialize_cv = sequentialize
        self.sequentialize_cv()


class AESCipherCTRnoIV(AESCipherCTR_Base):
    def __init__(self, key: str_or_bytes, sequentialize_cv: bool = False):
        def aes_gen(_initial_value):
            return AES.new(sha3_256d(key), AES.MODE_CTR, counter=Counter.new(64, b"\x00"*8, initial_value=_initial_value))

        def sequentialize(i=[1-2]):
            if isinstance(i, list):
                _i = i[0]+1
                i.clear()
                i.append(_i)
            else:
                _i = i
            if sequentialize_cv:
                self._cipher = aes_gen(_i)
            elif not self._cipher:
                self._cipher = aes_gen(1)

        self.sequentialize_cv = sequentialize
        self.sequentialize_cv()


class AESCipherCTRnoHASH(AESCipherCTR_Base):
    def __init__(self, key: bytes, iv: bytes = b"\x00"*8, initial_value: int = 1, sequentialize_cv: bool = False):
        def aes_gen(_initial_value):
            return AES.new(key, AES.MODE_CTR, counter=Counter.new(64, iv, initial_value=_initial_value))

        def sequentialize(i=[initial_value-2]):
            if isinstance(i, list):
                _i = i[0]+1
                i.clear()
                i.append(_i)
            else:
                _i = i
            if sequentialize_cv:
                self._cipher = aes_gen(_i)
            elif not self._cipher:
                self._cipher = aes_gen(initial_value)

        self.sequentialize_cv = sequentialize
        self.sequentialize_cv()


class AESCipherCTRnoHASHnoIV(AESCipherCTR_Base):
    def __init__(self, key: bytes, sequentialize_cv: bool = False):
        def aes_gen(_initial_value):
            return AES.new(key, AES.MODE_CTR, counter=Counter.new(64, b"\x00"*8, initial_value=_initial_value))

        def sequentialize(i=[1-2]):
            if isinstance(i, list):
                _i = i[0]+1
                i.clear()
                i.append(_i)
            else:
                _i = i
            if sequentialize_cv:
                self._cipher = aes_gen(_i)
            elif not self._cipher:
                self._cipher = aes_gen(1)

        self.sequentialize_cv = sequentialize
        self.sequentialize_cv()



