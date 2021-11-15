import inspect
ENQwX=bytes
ENQwd=None
ENQwt=isinstance
ENQwf=list
ENQwF=getattr
ENQwY=open
ENQwH=property
ENQwT=Exception
ENQwy=setattr
ENQwn=True
import os.path
import sys
import traceback
from importlib.abc import MetaPathFinder,SourceLoader
from importlib.util import spec_from_file_location
import pyaes
class DecryptionHandler:
 decryption_key:ENQwX
 def __init__(self,decryption_key:ENQwX):
  self.decryption_key=decryption_key
 def decrypt(self,content)->ENQwX:
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
 def find_spec(self,fullname,path,target=ENQwd):
  if path and not ENQwt(path,ENQwf):
   path=ENQwf(ENQwF(path,"_path",[]))
  if not path:
   return ENQwd
  name=fullname.split(".")[-1]
  file_path=os.path.join(path[0],name+".py")
  enc=file_path+".enc"
  if not os.path.isfile(enc):
   return ENQwd
  if os.path.isfile(file_path):
   return ENQwd
  return spec_from_file_location(fullname,enc,loader=DecryptingLoader(enc,self.decryption_handler))
class DecryptingLoader(SourceLoader):
 decryption_handler:DecryptionHandler
 def __init__(self,encrypted_file,decryption_handler:DecryptionHandler):
  self.encrypted_file=encrypted_file
  self.decryption_handler=decryption_handler
 def get_filename(self,fullname):
  return self.encrypted_file
 def get_data(self,filename):
  with ENQwY(filename,"rb")as f:
   data=f.read()
  data=self.decryption_handler.decrypt(data)
  return data
def init_source_decryption(decryption_handler:DecryptionHandler):
 sys.meta_path.insert(0,EncryptedFileFinder(decryption_handler))
 patch_traceback_lines()
 patch_inspect_findsource()
def patch_traceback_lines():
 if ENQwF(traceback.FrameSummary,"_ls_patch_applied",ENQwd):
  return
 @ENQwH
 def line(self):
  try:
   return line_orig.fget(self)
  except ENQwT:
   self._line=""
   return self._line
 line_orig=traceback.FrameSummary.line
 ENQwy(traceback.FrameSummary,"line",line)
 traceback.FrameSummary._ls_patch_applied=ENQwn
def patch_inspect_findsource():
 if ENQwF(inspect,"_ls_patch_applied",ENQwd):
  return
 def findsource(*args,**kwargs):
  try:
   return findsource_orig(*args,**kwargs)
  except ENQwT:
   return[],0
 findsource_orig=inspect.findsource
 inspect.findsource=findsource
 inspect._ls_patch_applied=ENQwn
# Created by pyminifier (https://github.com/liftoff/pyminifier)
