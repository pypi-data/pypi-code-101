from aescipher import *


key = "ab一" or "ab一".encode()
plaintext = "ab一" or "ab一".encode()
ciphertext = AESCipherCBC(key).encrypt(plaintext)
print(plaintext, ciphertext)
print(plaintext == AESCipherCBC(key).decrypt(ciphertext))


key = Random.new().read(32)
plaintext = "ab一" or "ab一".encode()
ciphertext = AESCipherCBCnoHASH(key).encrypt(plaintext)
print(plaintext, ciphertext)
print(plaintext == AESCipherCBCnoHASH(key).decrypt(ciphertext))


key = "ab一" or "ab一".encode()
plaintext = "ab一" or "ab一".encode()
iv = Random.new().read(AES.block_size)
ciphertext = AESCipherCBCwoIV(key, iv).encrypt(plaintext)
print(plaintext, ciphertext)
print(plaintext == AESCipherCBCwoIV(key, iv).decrypt(ciphertext))


key = Random.new().read(32)
plaintext = "ab一" or "ab一".encode()
iv = Random.new().read(AES.block_size)
ciphertext = AESCipherCBCnoHASHwoIV(key, iv).encrypt(plaintext)
print(plaintext, ciphertext)
print(plaintext == AESCipherCBCnoHASHwoIV(key, iv).decrypt(ciphertext))
