import os.path
lXLNc=bytes
lXLNb=None
lXLNm=isinstance
lXLNM=list
lXLNG=getattr
lXLNv=open
lXLNe=property
lXLNy=Exception
lXLNn=setattr
lXLNi=True
import sys
import traceback
from importlib.abc import MetaPathFinder,SourceLoader
from importlib.util import spec_from_file_location
import pyaes
class DecryptionHandler:
 decryption_key:lXLNc
 def __init__(self,decryption_key:lXLNc):
  self.decryption_key=decryption_key
 def decrypt(self,content)->lXLNc:
  cipher=pyaes.AESModeOfOperationCBC(self.decryption_key,iv="\0"*16)
  decrypter=pyaes.Decrypter(cipher)
  decrypted=decrypter.feed(content)
  decrypted+=decrypter.feed()
  decrypted=decrypted.partition(b"\0")[0]
  return decrypted
class EncryptedFileFinder(MetaPathFinder):
 decryption_handler:DecryptionHandler
 def __init__(self,decryption_handler:DecryptionHandler):
  self.decryption_handler=decryption_handler
 def find_spec(self,fullname,path,target=lXLNb):
  if path and not lXLNm(path,lXLNM):
   path=lXLNM(lXLNG(path,"_path",[]))
  if not path:
   return lXLNb
  name=fullname.split(".")[-1]
  file_path=os.path.join(path[0],name+".py")
  enc=file_path+".enc"
  if not os.path.isfile(enc):
   return lXLNb
  if os.path.isfile(file_path):
   return lXLNb
  return spec_from_file_location(fullname,enc,loader=DecryptingLoader(enc,self.decryption_handler))
class DecryptingLoader(SourceLoader):
 decryption_handler:DecryptionHandler
 def __init__(self,encrypted_file,decryption_handler:DecryptionHandler):
  self.encrypted_file=encrypted_file
  self.decryption_handler=decryption_handler
 def get_filename(self,fullname):
  return self.encrypted_file
 def get_data(self,filename):
  with lXLNv(filename,"rb")as f:
   data=f.read()
  data=self.decryption_handler.decrypt(data)
  return data
def init_source_decryption(decryption_handler:DecryptionHandler):
 sys.meta_path.insert(0,EncryptedFileFinder(decryption_handler))
 patch_traceback_lines()
def patch_traceback_lines():
 if lXLNG(traceback.FrameSummary,"_ls_patch_applied",lXLNb):
  return
 @lXLNe
 def line(self):
  try:
   return line_orig.fget(self)
  except lXLNy:
   self._line=""
   return self._line
 line_orig=traceback.FrameSummary.line
 lXLNn(traceback.FrameSummary,"line",line)
 traceback.FrameSummary._ls_patch_applied=lXLNi
# Created by pyminifier (https://github.com/liftoff/pyminifier)
