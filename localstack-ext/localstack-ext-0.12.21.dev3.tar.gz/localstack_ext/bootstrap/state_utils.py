import logging
wDCzb=bool
wDCzv=hasattr
wDCze=set
wDCzg=True
wDCzm=False
wDCzK=isinstance
wDCzN=dict
wDCzo=getattr
wDCzr=None
wDCzt=str
wDCzI=Exception
wDCzc=open
import os
from typing import Any,Callable,List,OrderedDict,Set,Tuple
import dill
from localstack.utils.common import ObjectIdHashComparator
API_STATES_DIR="api_states"
LOG=logging.getLogger(__name__)
def check_already_visited(obj,visited:Set)->Tuple[wDCzb,Set]:
 if wDCzv(obj,"__dict__"):
  visited=visited or wDCze()
  wrapper=ObjectIdHashComparator(obj)
  if wrapper in visited:
   return wDCzg,visited
  visited.add(wrapper)
 return wDCzm,visited
def get_object_dict(obj):
 if wDCzK(obj,wDCzN):
  return obj
 obj_dict=wDCzo(obj,"__dict__",wDCzr)
 return obj_dict
def is_composite_type(obj):
 return wDCzK(obj,(wDCzN,OrderedDict))or wDCzv(obj,"__dict__")
def api_states_traverse(api_states_path:wDCzt,side_effect:Callable[...,wDCzr],mutables:List[Any]):
 for dir_name,_,file_list in os.walk(api_states_path):
  for file_name in file_list:
   try:
    subdirs=os.path.normpath(dir_name).split(os.sep)
    region=subdirs[-1]
    service_name=subdirs[-2]
    side_effect(dir_name=dir_name,fname=file_name,region=region,service_name=service_name,mutables=mutables)
   except wDCzI as e:
    LOG.warning(f"Failed to apply {side_effect.__name__} for {file_name} in dir {dir_name}: {e}")
    continue
def load_persisted_object(state_file):
 if not os.path.isfile(state_file):
  return
 import dill
 with wDCzc(state_file,"rb")as f:
  try:
   content=f.read()
   result=dill.loads(content)
   return result
  except wDCzI as e:
   LOG.debug("Unable to read pickled persistence file %s: %s"%(state_file,e))
def persist_object(obj,state_file):
 with wDCzc(state_file,"wb")as f:
  result=f.write(dill.dumps(obj))
  return result
# Created by pyminifier (https://github.com/liftoff/pyminifier)
