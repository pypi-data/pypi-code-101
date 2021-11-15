from omnitools import key_pair_format, machd, jd, b64d, b64e, sha3_512hd, jl
from aescipher import AESCipherCBC, AESCipherCBCnoHASH, Random
from easyrsa import EasyRSA, EasyRSAv1
from .broker import Broker
from typing import Any


class Agent:
    def __init__(self, *, app_name: str, key_pair: key_pair_format, **kwargs) -> None:
        self.__aese = lambda v, _={}: self.__check() and (
            _.update({0: Random.new().read(32)}) or
            (EasyRSA(public_key=key_pair["public_key"]).encrypt(_[0]), AESCipherCBCnoHASH(key=_[0]).encrypt(v))
        )
        self.__aesd = lambda k, v: self.__check() and AESCipherCBCnoHASH(
            key=EasyRSA(private_key=key_pair["private_key"]).decrypt(k)
        ).decrypt(v)
        self.__sign = lambda m: self.__check() and EasyRSA(private_key=key_pair["private_key"]).sign(m)
        self.__verify = lambda m, s: self.__check() and EasyRSA(public_key=key_pair["public_key"]).verify(msg=m, sig=s)
        self.__setk = lambda k, v: self.__check() and machd(key=sha3_512hd(k), content=v)
        self.__setn = lambda v: self.__check() and self.__setk(k=key_pair["public_key"], v=v)
        self.__broker = lambda id: self.__check() and Broker(app_name=self.__setn(app_name), username=self.__setn(id), **kwargs)

    @staticmethod
    def __check() -> bool:
        import inspect
        if not inspect.stack()[2][1].replace("\\", ".").replace("/", ".").endswith("-packages.credsafe.agent.py"):
            raise Exception("call outside Agent() is prohibited")
        return True

    def __encrypt(self, v: Any) -> str:
        self.__check()
        sk, v = self.__aese(jd(v))
        sk = b64e(sk)
        hash = b64e(self.__sign(sk+v))
        return "{} {} {}".format(hash, sk, v)

    def set(self, id: str, pw: str, k: str, v: Any) -> Any:
        self.__broker(id).set(k=self.__setk(k=pw, v=k), v=self.__encrypt(v))
        return self

    def __decrypt(self, v: str) -> Any:
        self.__check()
        hash, sk, v = v.split(" ")
        if self.__verify(m=sk+v, s=b64d(hash)):
            return jl(self.__aesd(b64d(sk), v))
        raise Exception("credentials are tampered due to different hmac")

    def get(self, id: str, pw: str, k: str) -> Any:
        return self.__decrypt(self.__broker(id).get(self.__setk(k=pw, v=k)))

    def rm(self, id: str, pw: str, k: str) -> bool:
        return self.__broker(id).rm(self.__setk(k=pw, v=k))

    def destroy(self, id: str) -> bool:
        return self.__broker(id).destroy()


class AgentV2(Agent):
    def __encrypt(self, v: Any) -> str:
        self.__check()
        sk, v = self.__aese(jd(v))
        sk = b64e(sk)
        hash = b64e(self.__sign(v))
        return "{} {} {}".format(hash, sk, v)

    def __decrypt(self, v: str) -> Any:
        self.__check()
        hash, sk, v = v.split(" ")
        if self.__verify(m=v, s=b64d(hash)):
            return jl(self.__aesd(b64d(sk), v))
        raise Exception("credentials are tampered due to different hmac")


class AgentV1(AgentV2):
    def __init__(self, app_name: str, key_pair: key_pair_format) -> None:
        super().__init__(app_name=app_name, key_pair=key_pair)
        self.__aese = lambda v, _={}: self.__check() and (
            _.update({0: Random.new().read(256)}) or
            (EasyRSAv1(public_key=key_pair["public_key"]).encrypt(_[0]), AESCipherCBC(key=_[0]).encrypt(v))
        )
        self.__aesd = lambda k, v: self.__check() and AESCipherCBC(
            key=EasyRSAv1(private_key=key_pair["private_key"]).decrypt(k)
        ).decrypt(v)




