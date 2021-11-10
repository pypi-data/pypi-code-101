from aescipher import *
from omnitools import randb


# decrypt during write
# write decrypted data to file
# use cb_before and cb_after to handle events before and after decryption
writer = AESCipherCTRFileDecWriter(
    "decrypted.txt",
    buffer=8192,
    cb_before=lambda x: print("before", x),
    cb_after=lambda x: print("after", x),
    key="hi",
    iv=b"\x00"*8 or randb(8),
    initial_value=1,
)
writer.write(open("ciphertext.txt", "rb").read())
print("see decrypted.txt")
