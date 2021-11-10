from cryptography.fernet import Fernet
import os

def nonagenkey():
  key = Fernet.generate_key()
  with open("pass.key", "wb") as key_file:
    key_file.write(key)
  return key

def nonaregenkey():
  if os.path.exists("pass.key"):
    os.remove("pass.key")
  nonagenkey()
  
def nonacall_key():
  try:
    key = open("pass.key", "rb").read()
    if str(key) == "b''":
      nonagenkey()
      key = open("pass.key", "rb").read()
    return key
  except:
    nonagenkey()
    key = open("pass.key", "rb").read()
    return key

def nonaencrypt(slogan):
  key = nonacall_key()
  slogan = slogan.encode()
  a = Fernet(key)
  coded_slogan = a.encrypt(slogan)
  return coded_slogan

def nonadecrypt(coded_slogan):
  key = nonacall_key()
  b = Fernet(key)
  decoded_slogan = b.decrypt(coded_slogan)
  decoded_slogan = str(decoded_slogan)
  decoded_slogan = decoded_slogan[2:]
  decoded_slogan = decoded_slogan[:-1]
  return(decoded_slogan)