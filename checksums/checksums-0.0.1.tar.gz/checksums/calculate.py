import hashlib
import os

def checksums(algr, path):
    if algr == "md5":
        hash = hashlib.md5()
    elif algr == "sha1":
        hash = hashlib.sha1()
    elif algr == "sha256":
        hash = hashlib.sha256()
    elif algr == "sha512":
        hash = hashlib.sha512()

    file = open((os.path.abspath(path)), "rb")
    content = file.read()
    hash.update(content)
    digest = hash.hexdigest()
    
    return digest
