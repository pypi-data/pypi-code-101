from .ctr import AESCipherCTR
from omnitools import try_utf8e


class AESCipherCTRFileBase:
    def __init__(self, fp: str, mode: str = "a", buffer: int = 8192, cb_before= None, cb_after = None, *args, **kwargs):
        if type(self) == AESCipherCTRFileBase:
            raise NotImplementedError
        self.fp = fp
        self.fo = open(fp, mode+"+b", buffer)
        self.name = self.fo.name
        self.cb_before = cb_before
        self.cb_after = cb_after
        self._cipher = lambda: AESCipherCTR(*args, **kwargs)
        self.seek(0)

    def crypto(self, buf: bytes) -> bytes:
        raise NotImplementedError

    def cb_wrapper(self, buf: bytes) -> bytes:
        if self.cb_before:
            self.cb_before(buf)
        buf = try_utf8e(self.crypto(buf))
        if self.cb_after:
            self.cb_after(buf)
        return buf

    def seek(self, n: int) -> int:
        self.cipher = self._cipher()
        for i in range(0, n):
            self.cipher.decrypt(b"\x00")
        return self.fo.seek(n)

    def _read(self, n: int = -1) -> bytes:
        return self.fo.read(n)

    def _write(self, s: bytes) -> int:
        return self.fo.write(s)

    def read(self, n: int = -1) -> bytes:
        raise NotImplementedError

    def write(self, s: bytes) -> int:
        raise NotImplementedError

    def close(self):
        return self.fo.close()

    def tell(self):
        return self.fo.tell()


class AESCipherCTRFileReader(AESCipherCTRFileBase):
    def __init__(self, *args, **kwargs):
        if type(self) == AESCipherCTRFileReader:
            raise NotImplementedError
        super().__init__(*args, **kwargs)

    def read(self, n: int = -1) -> bytes:
        return self.cb_wrapper(self.fo.read(n))


class AESCipherCTRFileWriter(AESCipherCTRFileBase):
    def __init__(self, *args, **kwargs):
        if type(self) == AESCipherCTRFileWriter:
            raise NotImplementedError
        super().__init__(*args, mode="w", **kwargs)

    def write(self, s: bytes) -> int:
        return self.fo.write(self.cb_wrapper(s))


class AESCipherCTRFileEnc(AESCipherCTRFileBase):
    def __init__(self, *args, **kwargs):
        if type(self) == AESCipherCTRFileEnc:
            raise NotImplementedError
        super().__init__(*args, **kwargs)
        self.crypto = self.cipher.encrypt

    def seek(self, n: int) -> int:
        _ = super().seek(n)
        self.crypto = self.cipher.encrypt
        return _


class AESCipherCTRFileDec(AESCipherCTRFileBase):
    def __init__(self, *args, **kwargs):
        if type(self) == AESCipherCTRFileDec:
            raise NotImplementedError
        super().__init__(*args, **kwargs)
        self.crypto = self.cipher.decrypt

    def seek(self, n: int) -> int:
        _ = super().seek(n)
        self.crypto = self.cipher.decrypt
        return _


class AESCipherCTRFileEncReader(AESCipherCTRFileEnc, AESCipherCTRFileReader):
    pass


class AESCipherCTRFileEncWriter(AESCipherCTRFileEnc, AESCipherCTRFileWriter):
    pass


class AESCipherCTRFileDecReader(AESCipherCTRFileDec, AESCipherCTRFileReader):
    pass


class AESCipherCTRFileDecWriter(AESCipherCTRFileDec, AESCipherCTRFileWriter):
    pass




