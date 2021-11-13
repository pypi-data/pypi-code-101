from aescipher import *


code = Random.new().read(32)


key = "ab一" or "ab一".encode()
plaintext = "ab一" or "ab一".encode()
ciphertext, digest = AESCipherGCM(key, code).encrypt_and_digest(plaintext)
print(plaintext, ciphertext)
print(plaintext == AESCipherGCM(key, code).decrypt_and_verify(ciphertext, digest))


key = Random.new().read(32)
plaintext = "ab一" or "ab一".encode()
ciphertext, digest = AESCipherGCMnoHASH(key, code).encrypt_and_digest(plaintext)
print(plaintext, ciphertext)
print(plaintext == AESCipherGCMnoHASH(key, code).decrypt_and_verify(ciphertext, digest))


key = "ab一" or "ab一".encode()
plaintext = "ab一" or "ab一".encode()
iv = Random.new().read(AES.block_size)
ciphertext, digest = AESCipherGCMwoIV(key, iv, code).encrypt_and_digest(plaintext)
print(plaintext, ciphertext)
print(plaintext == AESCipherGCMwoIV(key, iv, code).decrypt_and_verify(ciphertext, digest))


key = Random.new().read(32)
plaintext = "ab一" or "ab一".encode()
iv = Random.new().read(AES.block_size)
ciphertext, digest = AESCipherGCMnoHASHwoIV(key, iv, code).encrypt_and_digest(plaintext)
print(plaintext, ciphertext)
print(plaintext == AESCipherGCMnoHASHwoIV(key, iv, code).decrypt_and_verify(ciphertext, digest))
