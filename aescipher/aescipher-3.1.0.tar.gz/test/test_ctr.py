from aescipher import *
from omnitools import randb


iv = randb(8)
key = "ab一" or "ab一".encode()
plaintext = "ab一" or "ab一".encode()
plaintext2 = "bc一" or "bc一".encode()
cipher = AESCipherCTR(key, iv)
ciphertext = cipher.encrypt(plaintext)
ciphertext2 = cipher.encrypt(plaintext2)
print(plaintext, ciphertext)
print(plaintext2, ciphertext2)
cipher = AESCipherCTR(key, iv)
print(plaintext == cipher.decrypt(ciphertext))
print(plaintext2 == cipher.decrypt(ciphertext2))
cipher = AESCipherCTR(key, iv)
cipher.decrypt(b"\x00"*len(plaintext.encode()))
print(plaintext2 == cipher.decrypt(ciphertext2))
