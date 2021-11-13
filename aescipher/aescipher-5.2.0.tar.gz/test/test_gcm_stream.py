from aescipher import *


def get_cipher(noHASH=False, woIV=False):
    if noHASH:
        if woIV:
            return AESCipherGCMSTREAMnoHASHwoIV(key, iv, code)
        else:
            return AESCipherGCMSTREAMnoHASH(key, code)
    else:
        if woIV:
            return AESCipherGCMSTREAMwoIV(key, iv, code)
        else:
            return AESCipherGCMSTREAM(key, code)


key = "ab一" or "ab一".encode()
# key = Random.new().read(32)
iv = Random.new().read(8)
code = b"asd" or Random.new().read(8)
plaintext = "ab一" or "ab一".encode()
plaintext2 = "bc一" or "bc一".encode()
cipher = get_cipher(woIV=True)
# cipher = get_cipher()
# iv = cipher._iv
ciphertext = cipher.encrypt(plaintext)
ciphertext2 = cipher.encrypt(plaintext2)
digest = cipher.digest()
print(digest)
print(plaintext, ciphertext)
print(plaintext2, ciphertext2)
cipher = get_cipher(woIV=True)
print(plaintext == cipher.decrypt(ciphertext))
print(plaintext2 == cipher.decrypt(ciphertext2))
cipher.verify(digest)
cipher = get_cipher(woIV=True)
cipher.decrypt(b"\x00"*len(plaintext.encode()))
print(plaintext2 == cipher.decrypt(ciphertext2))
try:
    cipher.verify(digest)
except Exception as e:
    print(e, "since the cipher decrypted garbage in the first place which altered the digest")
exit()
cipher = get_cipher(woIV=True)
ciphertext3 = cipher.encrypt(plaintext)
ciphertext4 = cipher.encrypt(plaintext)
cipher = get_cipher(woIV=True)
ciphertext5 = cipher.encrypt(plaintext)
cipher = get_cipher(woIV=True)
ciphertext6 = cipher.encrypt(plaintext)
print(ciphertext3, ciphertext5, ciphertext3 == ciphertext5)
print(ciphertext4, ciphertext6, ciphertext4 == ciphertext6)
print(ciphertext5, ciphertext6, ciphertext5 == ciphertext6)
cipher = get_cipher(woIV=True)
print(plaintext == cipher.decrypt(ciphertext3))
print(plaintext == cipher.decrypt(ciphertext4))
cipher = get_cipher(woIV=True)
print(plaintext == cipher.decrypt(ciphertext5))
print(plaintext == cipher.decrypt(ciphertext6))
cipher = get_cipher(woIV=True)
cipher.decrypt(b"\x00"*len(plaintext.encode()))
print(plaintext == cipher.decrypt(ciphertext4))

