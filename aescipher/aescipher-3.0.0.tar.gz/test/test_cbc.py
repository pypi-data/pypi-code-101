from aescipher import *


key = "ab一" or "ab一".encode()
plaintext = "ab一" or "ab一".encode()
ciphertext = AESCipherCBC(key).encrypt(plaintext)
print(plaintext, ciphertext)
print(plaintext == AESCipherCBC(key).decrypt(ciphertext))
