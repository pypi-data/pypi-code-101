import logging
MTIFi=bool
MTIFg=hasattr
MTIFe=set
MTIFP=True
MTIFS=False
MTIFt=isinstance
MTIFo=dict
MTIFR=getattr
MTIFH=None
MTIFr=str
MTIFA=Exception
MTIFV=open
import os
from typing import Any,Callable,List,OrderedDict,Set,Tuple
import dill
from localstack.utils.common import ObjectIdHashComparator
API_STATES_DIR="api_states"
LOG=logging.getLogger(__name__)
def check_already_visited(obj,visited:Set)->Tuple[MTIFi,Set]:
 if MTIFg(obj,"__dict__"):
  visited=visited or MTIFe()
  wrapper=ObjectIdHashComparator(obj)
  if wrapper in visited:
   return MTIFP,visited
  visited.add(wrapper)
 return MTIFS,visited
def get_object_dict(obj):
 if MTIFt(obj,MTIFo):
  return obj
 obj_dict=MTIFR(obj,"__dict__",MTIFH)
 return obj_dict
def is_composite_type(obj):
 return MTIFt(obj,(MTIFo,OrderedDict))or MTIFg(obj,"__dict__")
def api_states_traverse(api_states_path:MTIFr,side_effect:Callable[...,MTIFH],mutables:List[Any]):
 for dir_name,_,file_list in os.walk(api_states_path):
  for file_name in file_list:
   try:
    subdirs=os.path.normpath(dir_name).split(os.sep)
    region=subdirs[-1]
    service_name=subdirs[-2]
    side_effect(dir_name=dir_name,fname=file_name,region=region,service_name=service_name,mutables=mutables)
   except MTIFA as e:
    LOG.warning(f"Failed to apply {side_effect.__name__} for {file_name} in dir {dir_name}: {e}")
    continue
def load_persisted_object(state_file):
 if not os.path.isfile(state_file):
  return
 import dill
 with MTIFV(state_file,"rb")as f:
  try:
   content=f.read()
   result=dill.loads(content)
   return result
  except MTIFA as e:
   LOG.debug("Unable to read pickled persistence file %s: %s"%(state_file,e))
def persist_object(obj,state_file):
 with MTIFV(state_file,"wb")as f:
  result=f.write(dill.dumps(obj))
  return result
# Created by pyminifier (https://github.com/liftoff/pyminifier)
