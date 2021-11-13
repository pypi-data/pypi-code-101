from aescipher import *


def get_cipher(noHASH=False, noIV=False, initial_value=1):
    if noHASH:
        if noIV:
            return AESCipherCTRnoHASHnoIV(key)
        else:
            return AESCipherCTRnoHASH(key, iv, initial_value)
    else:
        if noIV:
            return AESCipherCTRnoIV(key)
        else:
            return AESCipherCTR(key, iv, initial_value)


key = "ab一" or "ab一".encode()
# key = Random.new().read(32)
iv = Random.new().read(8)
plaintext = "ab一" or "ab一".encode()
plaintext2 = "bc一" or "bc一".encode()
cipher = get_cipher()
ciphertext = cipher.encrypt(plaintext)
ciphertext2 = cipher.encrypt(plaintext2)
print(plaintext, ciphertext)
print(plaintext2, ciphertext2)
cipher = get_cipher()
print(plaintext == cipher.decrypt(ciphertext))
print(plaintext2 == cipher.decrypt(ciphertext2))
cipher = get_cipher()
cipher.decrypt(b"\x00"*len(plaintext.encode()))
print(plaintext2 == cipher.decrypt(ciphertext2))
cipher = get_cipher()
ciphertext3 = cipher.encrypt(plaintext)
ciphertext4 = cipher.encrypt(plaintext)
cipher = get_cipher()
ciphertext5 = cipher.encrypt(plaintext)
cipher = get_cipher()
ciphertext6 = cipher.encrypt(plaintext)
print(ciphertext3, ciphertext5, ciphertext3 == ciphertext5)
print(ciphertext4, ciphertext6, ciphertext4 == ciphertext6)
print(ciphertext5, ciphertext6, ciphertext5 == ciphertext6)
cipher = get_cipher()
print(plaintext == cipher.decrypt(ciphertext3))
print(plaintext == cipher.decrypt(ciphertext4))
cipher = get_cipher()
print(plaintext == cipher.decrypt(ciphertext5))
print(plaintext == cipher.decrypt(ciphertext6))
cipher = get_cipher()
cipher.decrypt(b"\x00"*len(plaintext.encode()))
print(plaintext == cipher.decrypt(ciphertext4))
