from aescipher import *


key = "ab一" or "ab一".encode()
plaintext = "ab一" or "ab一".encode()
ciphertext = AESCipherCBC(key=key).encrypt(plaintext)
print(plaintext, ciphertext)
print(plaintext == AESCipherCBC(key=key).decrypt(ciphertext))


key = Random.new().read(32)
plaintext = "ab一" or "ab一".encode()
ciphertext = AESCipherCBCnoHASH(key=key).encrypt(plaintext)
print(plaintext, ciphertext)
print(plaintext == AESCipherCBCnoHASH(key=key).decrypt(ciphertext))


key = "ab一" or "ab一".encode()
plaintext = "ab一" or "ab一".encode()
iv = Random.new().read(AES.block_size)
ciphertext = AESCipherCBCwoIV(key=key, iv=iv).encrypt(plaintext)
print(plaintext, ciphertext)
print(plaintext == AESCipherCBCwoIV(key=key, iv=iv).decrypt(ciphertext))


key = Random.new().read(32)
plaintext = "ab一" or "ab一".encode()
iv = Random.new().read(AES.block_size)
ciphertext = AESCipherCBCnoHASHwoIV(key=key, iv=iv).encrypt(plaintext)
print(plaintext, ciphertext)
print(plaintext == AESCipherCBCnoHASHwoIV(key=key, iv=iv).decrypt(ciphertext))
