from Crypto import Random
from Crypto.Cipher import AES
from omnitools import sha3_256d, str_or_bytes, b64e, b64d, try_utf8e, try_utf8d


class AESCipherGCM_Base:
    _cipher = None

    def destroy(self):
        self._cipher = None

    def encrypt(self, raw: str_or_bytes) -> str:
        raise Exception("use encrypt_and_digest instead")

    def decrypt(self, enc: str) -> str_or_bytes:
        raise Exception("use decrypt_and_verify instead")

    def encrypt_and_digest(self, raw: str_or_bytes) -> tuple:
        raise NotImplementedError

    def decrypt_and_verify(self, enc: str, assoc_data: bytes) -> str_or_bytes:
        raise NotImplementedError


class AESCipherGCMwIV_Base(AESCipherGCM_Base):
    def encrypt_and_digest(self, raw: str_or_bytes) -> tuple:
        raw = try_utf8e(raw)
        iv = Random.new().read(AES.block_size)
        _ = self._cipher(iv)
        return b64e(iv + _.encrypt(raw)), _.digest()

    def decrypt_and_verify(self, enc: str, assoc_data: bytes) -> str_or_bytes:
        enc = b64d(enc)
        iv = enc[:AES.block_size]
        _ = self._cipher(iv)
        __ = _.decrypt(enc[AES.block_size:])
        _.verify(assoc_data)
        return try_utf8d(__)


class AESCipherGCMwoIV_Base(AESCipherGCM_Base):
    def encrypt_and_digest(self, raw: str_or_bytes) -> tuple:
        raw = try_utf8e(raw)
        _ = self._cipher()
        return b64e(_.encrypt(raw)), _.digest()

    def decrypt_and_verify(self, enc: str, assoc_data: bytes) -> str_or_bytes:
        enc = b64d(enc)
        _ = self._cipher()
        __ = _.decrypt(enc)
        _.verify(assoc_data)
        return try_utf8d(__)


class AESCipherGCM(AESCipherGCMwIV_Base):
    def __init__(self, key: str_or_bytes, assoc_data: bytes) -> None:
        self._cipher = lambda iv: AES.new(sha3_256d(key), AES.MODE_GCM, iv).update(assoc_data)


class AESCipherGCMnoHASH(AESCipherGCMwIV_Base):
    def __init__(self, key: str_or_bytes, assoc_data: bytes) -> None:
        self._cipher = lambda iv: AES.new(try_utf8e(key), AES.MODE_GCM, iv).update(assoc_data)


class AESCipherGCMwoIV(AESCipherGCMwoIV_Base):
    def __init__(self, key: str_or_bytes, iv: bytes, assoc_data: bytes) -> None:
        self._cipher = lambda: AES.new(sha3_256d(key), AES.MODE_GCM, iv).update(assoc_data)


class AESCipherGCMnoHASHwoIV(AESCipherGCMwoIV_Base):
    def __init__(self, key: str_or_bytes, iv: bytes, assoc_data: bytes) -> None:
        self._cipher = lambda: AES.new(try_utf8e(key), AES.MODE_GCM, iv).update(assoc_data)



