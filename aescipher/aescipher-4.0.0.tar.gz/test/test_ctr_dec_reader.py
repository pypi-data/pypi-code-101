from aescipher import *
from omnitools import randb


# decrypt during read
# supply decrypted data to high level program
# use cb_before and cb_after to handle events before and after decryption
reader = AESCipherCTRFileDecReader(
    "ciphertext.txt",
    buffer=8192,
    cb_before=lambda x: print("before", x),
    cb_after=lambda x: print("after", x),
    key="hi",
    iv=b"\x00"*8 or randb(8),
    initial_value=1,
)
print(reader.read())
