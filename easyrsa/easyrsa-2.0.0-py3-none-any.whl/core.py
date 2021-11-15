from omnitools import str_or_bytes, b64e, b64d, try_utf8d, try_utf8e, jl, jd_and_utf8e, utf8d
from Crypto.Signature import PKCS1_v1_5, PKCS1_PSS
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import SHA3_512, SHA3_384
from Crypto.PublicKey import RSA


class EasyRSA(object):
    def __init__(
            self, *, bits: int = None,
            public_key: str_or_bytes = None,
            private_key: str_or_bytes = None
    ) -> None:
        if not (
                (public_key is None and private_key is None and bits is not None) or
                (bits is None and private_key is None and public_key is not None) or
                (public_key is None and bits is None and private_key is not None)
        ):
            raise Exception("only one operation per instance is allowed")
        self.__key = bits
        self.__public_key = public_key
        self.__private_key = private_key
        if isinstance(self.__public_key, str):
            self.__public_key = b64d(self.__public_key)
        if isinstance(self.__private_key, str):
            self.__private_key = b64d(self.__private_key)

    def gen_key_pair(self):
        key = RSA.generate(bits=self.__key)
        try:
            return dict(
                private_key=key.export_key(),
                public_key=key.public_key().export_key()
            )
        except Exception as e:
            raise e
        finally:
            self.__key = None

    def max_msg_size(self) -> int:
        try:
            if self.__public_key:
                return RSA.import_key(extern_key=self.__public_key).n.bit_length() // 8 - 42
            elif self.__private_key:
                return RSA.import_key(extern_key=self.__private_key).n.bit_length() // 8 - 42
        except Exception as e:
            raise e
        finally:
            self.__private_key = None
            self.__public_key = None

    def encrypt(self, v: str_or_bytes) -> bytes:
        if len(try_utf8e(v)) > EasyRSA(public_key=self.__public_key).max_msg_size():
            return self.encryptlong(v)
        v = try_utf8e(v)
        return PKCS1_OAEP.new(key=RSA.import_key(extern_key=self.__public_key)).encrypt(v)

    def encryptlong(self, v: str_or_bytes) -> bytes:
        max_msg_size = EasyRSA(public_key=self.__public_key).max_msg_size()
        parts = []
        while v:
            parts.append(b64e(self.encrypt(v[:max_msg_size])))
            v = v[max_msg_size:]
        return jd_and_utf8e(parts)

    def decrypt(self, v: bytes) -> str_or_bytes:
        try:
            return self.decryptlong(jl(utf8d(v)))
        except:
            pass
        v = PKCS1_OAEP.new(key=RSA.import_key(extern_key=self.__private_key)).decrypt(v)
        return try_utf8d(v)

    def decryptlong(self, parts: list) -> str_or_bytes:
        v = []
        for part in parts:
            v.append(self.decrypt(b64d(part)))
        if isinstance(v[0], str):
            return "".join(v)
        else:
            return b"".join(v)

    def sign(self, msg: str_or_bytes) -> bytes:
        return PKCS1_PSS.new(rsa_key=RSA.import_key(extern_key=self.__private_key)).sign(SHA3_384.new(try_utf8e(msg)))

    def verify(self, msg: str_or_bytes, sig: bytes) -> bool:
        PKCS1_PSS.new(rsa_key=RSA.importKey(self.__public_key).publickey()).verify(SHA3_384.new(try_utf8e(msg)), sig)
        return True


class EasyRSAv1(EasyRSA):
    def sign(self, msg: str_or_bytes) -> bytes:
        return PKCS1_v1_5.new(rsa_key=RSA.import_key(extern_key=self.__private_key)).sign(SHA3_512.new(try_utf8e(msg)))

    def verify(self, msg: str_or_bytes, sig: bytes) -> bool:
        PKCS1_v1_5.new(rsa_key=RSA.importKey(self.__public_key).publickey()).verify(SHA3_512.new(try_utf8e(msg)), sig)
        return True


