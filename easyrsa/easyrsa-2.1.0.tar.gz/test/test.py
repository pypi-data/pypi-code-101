from easyrsa import EasyRSA as EasyRSAv2, EasyRSAv1
from omnitools import randb


kp = EasyRSAv2(bits=1024).gen_key_pair()
print(kp)
print(EasyRSAv2(public_key=kp["public_key"]).max_msg_size())
print(EasyRSAv2(private_key=kp["private_key"]).max_msg_size())

from base64 import b64encode
symmetric_key = "abc"*1000 or b"abc" or b64encode(b"abc")
encrypted_key = EasyRSAv2(public_key=kp["public_key"]).encrypt(symmetric_key)
print(encrypted_key)
print(symmetric_key == EasyRSAv2(private_key=kp["private_key"]).decrypt(encrypted_key))

msg = randb(1024)
s = EasyRSAv2(private_key=kp["private_key"]).sign(msg)
print(msg, s)
print(EasyRSAv2(public_key=kp["public_key"]).verify(msg, s))
