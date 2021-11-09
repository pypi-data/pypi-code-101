from cryptography.fernet import Fernet
import os

async def genkey():
  key = Fernet.generate_key()
  with open("pass.key", "wb") as key_file:
    key_file.write(key)
  return key

async def regenkey():
  if os.path.exists("pass.key"):
    os.remove("pass.key")
  await genkey()
  
async def call_key():
  try:
    key = open("pass.key", "rb").read()
    if str(key) == "b''":
      await genkey()
      key = open("pass.key", "rb").read()
    return key
  except:
    await genkey()
    key = open("pass.key", "rb").read()
    return key

async def encrypt(slogan):
  key = await call_key()
  slogan = slogan.encode()
  a = Fernet(key)
  coded_slogan = a.encrypt(slogan)
  return coded_slogan

async def decrypt(coded_slogan):
  key = await call_key()
  b = Fernet(key)
  decoded_slogan = b.decrypt(coded_slogan)
  decoded_slogan = str(decoded_slogan)
  decoded_slogan = decoded_slogan[2:]
  decoded_slogan = decoded_slogan[:-1]
  return(decoded_slogan)