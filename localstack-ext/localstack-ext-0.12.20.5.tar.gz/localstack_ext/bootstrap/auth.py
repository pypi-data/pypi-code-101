import getpass
aYCrE=object
aYCrA=staticmethod
aYCri=False
aYCrn=Exception
aYCrx=None
aYCrX=input
aYCrz=list
import json
import logging
import sys
from localstack.config import load_config_file,save_config_file
from localstack.constants import API_ENDPOINT
from localstack.utils.common import safe_requests,to_str
LOG=logging.getLogger(__name__)
class AuthProvider(aYCrE):
 @aYCrA
 def name():
  raise
 def get_or_create_token(self,username,password,headers):
  pass
 def get_user_for_token(self,token):
  pass
 @aYCrA
 def providers():
  return{c.name():c for c in AuthProvider.__subclasses__()}
 @aYCrA
 def get(provider,raise_error=aYCri):
  provider_class=AuthProvider.providers().get(provider)
  if not provider_class:
   msg='Unable to find auth provider class "%s"'%provider
   LOG.warning(msg)
   if raise_error:
    raise aYCrn(msg)
   return aYCrx
  return provider_class()
class AuthProviderInternal(AuthProvider):
 @aYCrA
 def name():
  return "internal"
 def get_or_create_token(self,username,password,headers):
  data={"username":username,"password":password}
  response=safe_requests.post("%s/user/signin"%API_ENDPOINT,json.dumps(data),headers=headers)
  if response.status_code>=400:
   return
  try:
   result=json.loads(to_str(response.content or "{}"))
   return result["token"]
  except aYCrn:
   pass
 def read_credentials(self,username):
  print("Please provide your login credentials below")
  if not username:
   sys.stdout.write("Username: ")
   sys.stdout.flush()
   username=aYCrX()
  password=getpass.getpass()
  return username,password,{}
 def get_user_for_token(self,token):
  raise aYCrn("Not implemented")
def login(provider,username=aYCrx):
 auth_provider=AuthProvider.get(provider)
 if not auth_provider:
  providers=aYCrz(AuthProvider.providers().keys())
  raise aYCrn('Unknown provider "%s", should be one of %s'%(provider,providers))
 username,password,headers=auth_provider.read_credentials(username)
 print("Verifying credentials ... (this may take a few moments)")
 token=auth_provider.get_or_create_token(username,password,headers)
 if not token:
  raise aYCrn("Unable to verify login credentials - please try again")
 configs=load_config_file()
 configs["login"]={"provider":provider,"username":username,"token":token}
 save_config_file(configs)
def logout():
 configs=load_config_file()
 configs["login"]={}
 save_config_file(configs)
def json_loads(s):
 return json.loads(to_str(s))
# Created by pyminifier (https://github.com/liftoff/pyminifier)
