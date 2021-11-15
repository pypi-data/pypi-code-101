import logging
dExaj=bool
dExab=hasattr
dExac=set
dExan=True
dExaO=False
dExai=isinstance
dExay=dict
dExap=getattr
dExao=None
dExaI=str
dExaD=Exception
dExak=open
import os
from typing import Any,Callable,List,OrderedDict,Set,Tuple
import dill
from localstack.utils.common import ObjectIdHashComparator
API_STATES_DIR="api_states"
LOG=logging.getLogger(__name__)
def check_already_visited(obj,visited:Set)->Tuple[dExaj,Set]:
 if dExab(obj,"__dict__"):
  visited=visited or dExac()
  wrapper=ObjectIdHashComparator(obj)
  if wrapper in visited:
   return dExan,visited
  visited.add(wrapper)
 return dExaO,visited
def get_object_dict(obj):
 if dExai(obj,dExay):
  return obj
 obj_dict=dExap(obj,"__dict__",dExao)
 return obj_dict
def is_composite_type(obj):
 return dExai(obj,(dExay,OrderedDict))or dExab(obj,"__dict__")
def api_states_traverse(api_states_path:dExaI,side_effect:Callable[...,dExao],mutables:List[Any]):
 for dir_name,_,file_list in os.walk(api_states_path):
  for file_name in file_list:
   try:
    subdirs=os.path.normpath(dir_name).split(os.sep)
    region=subdirs[-1]
    service_name=subdirs[-2]
    side_effect(dir_name=dir_name,fname=file_name,region=region,service_name=service_name,mutables=mutables)
   except dExaD as e:
    LOG.warning(f"Failed to apply {side_effect.__name__} for {file_name} in dir {dir_name}: {e}")
    continue
def load_persisted_object(state_file):
 if not os.path.isfile(state_file):
  return
 import dill
 with dExak(state_file,"rb")as f:
  try:
   content=f.read()
   result=dill.loads(content)
   return result
  except dExaD as e:
   LOG.debug("Unable to read pickled persistence file %s: %s"%(state_file,e))
def persist_object(obj,state_file):
 with dExak(state_file,"wb")as f:
  result=f.write(dill.dumps(obj))
  return result
# Created by pyminifier (https://github.com/liftoff/pyminifier)
