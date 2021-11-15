#!/usr/bin/env python3
""" AES encryption of strings and bytes """
import sys
import base64

from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random


def encrypt(key, source, bytes_encoding='utf-8', encode_base64=True):
    if not isinstance(key, str):
        bytes_encoding = None
    if isinstance(key, str):
        key = key.encode(bytes_encoding or 'utf-8')
    if not isinstance(source, str):
        bytes_encoding = None
    if isinstance(source, str):
        source = source.encode(bytes_encoding or 'utf-8')

    # use SHA-256 over our key to get a proper-sized AES key (256-bit?):
    key = SHA256.new(key).digest()
    # generate random IV
    IV = Random.new().read(AES.block_size)
    encryptor = AES.new(key, AES.MODE_CBC, IV)
    # calculate how many bytes of padding are needed
    padding_len = AES.block_size - (len(source) % AES.block_size)
    source += bytes([padding_len]) * padding_len
    encrypted = IV + encryptor.encrypt(source)  # store the IV at the beginning and encrypt
    if encode_base64 or bytes_encoding:
        encrypted = base64.b64encode(encrypted)
    if bytes_encoding:
        encrypted = encrypted.decode(bytes_encoding)
    return encrypted


def decrypt(key, source, bytes_encoding='utf-8', decode_base64=True):
    if not isinstance(key, str):
        bytes_encoding = None
    if isinstance(key, str):
        key = key.encode(bytes_encoding or 'utf-8')
    if not isinstance(source, str):
        bytes_encoding = None

    if decode_base64 or bytes_encoding:
        source = base64.b64decode(source)
    if isinstance(source, str):
        source = source.encode(bytes_encoding or 'utf-8')

    # key and source are both now bytes
    key = SHA256.new(key).digest()  # use SHA-256 over our key to get a proper-sized AES key
    # extract the IV from the beginning
    IV = source[:AES.block_size]
    decryptor = AES.new(key, AES.MODE_CBC, IV)
    decrypted = decryptor.decrypt(source[AES.block_size:])
    # get the padding value from the end
    padding = decrypted[-1]
    if decrypted[-padding:] != bytes([padding]) * padding:
        raise ValueError("Invalid padding...")
    decrypted = decrypted[:-padding]  # remove the padding
    # decrypted is now bytes

    if bytes_encoding:
        return decrypted.decode(bytes_encoding)
    return decrypted


if __name__ == '__main__':
    if len(sys.argv) > 3:
        command = sys.argv[1].strip().strip('-')[0]
        source_filepath = sys.argv[2]
        key = sys.argv[3]
        source = open(source_filepath).read()
        if command == 'e':
            encrypted = encrypt(key=key, source=source)
            print(encrypted, end="")
        elif command == 'd':
            decrypted = decrypt(key=key, source=source)
            print(decrypted, end="")
    else:
        usage = ('USAGE: \n'
                 '       python aes.py -e filename.csv password > filename.csv.aes\n'
                 '       python aes.py -d filename.csv.aes password > filename.csv\n')
        raise ValueError(usage)
