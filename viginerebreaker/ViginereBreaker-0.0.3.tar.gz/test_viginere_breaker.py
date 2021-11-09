from CustomCrypto import viginere, decipher_viginere
from ViginereBreaker import ViginereBreaker
from string import ascii_uppercase


def cipher(text: str, key: str) -> str:
    key_length = len(key)
    counter = 0
    cipher = ""
    for char in text:
        if char in ascii_uppercase:
            cipher += viginere(char, key[counter % key_length], ascii_uppercase)
            counter += 1
        else:
            cipher += char
    return cipher


def decipher(cipher: str, key: str) -> str:
    key_length = len(key)
    counter = 0
    decipher = ""
    for char in cipher:
        if char in ascii_uppercase:
            decipher += decipher_viginere(
                char, key[counter % key_length], ascii_uppercase
            )
            counter += 1
        else:
            decipher += char
    return decipher


text = open("text.txt").read()
text = text.upper()
key = "TEST"

cipher = cipher(text, key)

open("cipher.txt", "w").write(cipher)

breaker = ViginereBreaker(cipher, statistics={"E": 10, "A": 7})
print(breaker.breaker())

# {2: [['H'], ['I']], 4: [['T'], ['E'], ['S'], ['T']]}

decipher = decipher(cipher, key)
# print(decipher)
