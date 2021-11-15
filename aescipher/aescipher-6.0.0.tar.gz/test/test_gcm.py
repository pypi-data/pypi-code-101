from aescipher import *


code = Random.new().read(32)


key = "ab一" or "ab一".encode()
plaintext = "ab一" or "ab一".encode()
ciphertext, digest = AESCipherGCM(key=key, assoc_data=code).encrypt_and_digest(plaintext)
print(plaintext, ciphertext)
print(plaintext == AESCipherGCM(key=key, assoc_data=code).decrypt_and_verify(ciphertext, digest))


key = Random.new().read(32)
plaintext = "ab一" or "ab一".encode()
ciphertext, digest = AESCipherGCMnoHASH(key=key, assoc_data=code).encrypt_and_digest(plaintext)
print(plaintext, ciphertext)
print(plaintext == AESCipherGCMnoHASH(key=key, assoc_data=code).decrypt_and_verify(ciphertext, digest))


key = "ab一" or "ab一".encode()
plaintext = "ab一" or "ab一".encode()
iv = Random.new().read(AES.block_size)
ciphertext, digest = AESCipherGCMwoIV(key=key, iv=iv, assoc_data=code).encrypt_and_digest(plaintext)
print(plaintext, ciphertext)
print(plaintext == AESCipherGCMwoIV(key=key, iv=iv, assoc_data=code).decrypt_and_verify(ciphertext, digest))


key = Random.new().read(32)
plaintext = "ab一" or "ab一".encode()
iv = Random.new().read(AES.block_size)
ciphertext, digest = AESCipherGCMnoHASHwoIV(key=key, iv=iv, assoc_data=code).encrypt_and_digest(plaintext)
print(plaintext, ciphertext)
print(plaintext == AESCipherGCMnoHASHwoIV(key=key, iv=iv, assoc_data=code).decrypt_and_verify(ciphertext, digest))
