from datetime import datetime
eECMy=str
eECMA=int
eECMa=super
eECMH=False
eECMn=isinstance
eECMt=hash
eECMB=True
eECMX=list
eECMG=map
eECMI=None
from typing import Set
from localstack_ext.bootstrap.cpvcs.constants import(COMMIT_TXT_LAYOUT,REV_TXT_LAYOUT,STATE_TXT_LAYOUT,STATE_TXT_METADATA,VER_TXT_LAYOUT)
class CPVCSObj:
 def __init__(self,hash_ref:eECMy):
  self.hash_ref:eECMy=hash_ref
class StateFileRef(CPVCSObj):
 txt_layout=STATE_TXT_LAYOUT
 metadata_layout=STATE_TXT_METADATA
 def __init__(self,hash_ref:eECMy,rel_path:eECMy,file_name:eECMy,size:eECMA,service:eECMy,region:eECMy):
  eECMa(StateFileRef,self).__init__(hash_ref)
  self.rel_path:eECMy=rel_path
  self.file_name:eECMy=file_name
  self.size:eECMA=size
  self.service:eECMy=service
  self.region:eECMy=region
 def __str__(self):
  return self.txt_layout.format(size=self.size,service=self.service,region=self.region,hash_ref=self.hash_ref,file_name=self.file_name,rel_path=self.rel_path)
 def __eq__(self,other):
  if not other:
   return eECMH
  if not eECMn(other,StateFileRef):
   return eECMH
  return(self.hash_ref==other.hash_ref and self.region==other.region and self.service==self.service and self.file_name==other.file_name and self.size==other.size)
 def __hash__(self):
  return eECMt((self.hash_ref,self.region,self.service,self.file_name,self.size))
 def congruent(self,other):
  if not other:
   return eECMH
  if not eECMn(other,StateFileRef):
   return eECMH
  return(self.region==other.region and self.service==other.service and self.file_name==other.file_name and self.rel_path==other.rel_path)
 def any_congruence(self,others):
  for other in others:
   if self.congruent(other):
    return eECMB
  return eECMH
 def metadata(self)->eECMy:
  return self.metadata_layout.format(size=self.size,service=self.service,region=self.region)
class CPVCSNode(CPVCSObj):
 def __init__(self,hash_ref:eECMy,state_files:Set[StateFileRef],parent_ptr:eECMy):
  eECMa(CPVCSNode,self).__init__(hash_ref)
  self.state_files:Set[StateFileRef]=state_files
  self.parent_ptr:eECMy=parent_ptr
 def state_files_info(self)->eECMy:
  return "\n".join(eECMX(eECMG(lambda state_file:eECMy(state_file),self.state_files)))
class Commit:
 txt_layout=COMMIT_TXT_LAYOUT
 def __init__(self,tail_ptr:eECMy,head_ptr:eECMy,message:eECMy,timestamp:eECMy=eECMy(datetime.now().timestamp()),delta_log_ptr:eECMy=eECMI):
  self.tail_ptr:eECMy=tail_ptr
  self.head_ptr:eECMy=head_ptr
  self.message:eECMy=message
  self.timestamp:eECMy=timestamp
  self.delta_log_ptr:eECMy=delta_log_ptr
 def __str__(self):
  return self.txt_layout.format(tail_ptr=self.tail_ptr,head_ptr=self.head_ptr,message=self.message,timestamp=self.timestamp,log_hash=self.delta_log_ptr)
 def info_str(self,from_node:eECMy,to_node:eECMy)->eECMy:
  return f"from: {from_node}, to: {to_node}, message: {self.message}, time: {datetime.fromtimestamp(float(self.timestamp))}"
class Revision(CPVCSNode):
 txt_layout=REV_TXT_LAYOUT
 def __init__(self,hash_ref:eECMy,state_files:Set[StateFileRef],parent_ptr:eECMy,creator:eECMy,rid:eECMy,revision_number:eECMA,assoc_commit:Commit=eECMI):
  eECMa(Revision,self).__init__(hash_ref,state_files,parent_ptr)
  self.creator:eECMy=creator
  self.rid:eECMy=rid
  self.revision_number:eECMA=revision_number
  self.assoc_commit=assoc_commit
 def __str__(self):
  return self.txt_layout.format(hash_ref=self.hash_ref,parent=self.parent_ptr,creator=self.creator,rid=self.rid,rev_no=self.revision_number,state_files=";".join(eECMG(lambda state_file:eECMy(state_file),self.state_files))if self.state_files else "",assoc_commit=self.assoc_commit)
class Version(CPVCSNode):
 txt_layout=VER_TXT_LAYOUT
 def __init__(self,hash_ref:eECMy,state_files:Set[StateFileRef],parent_ptr:eECMy,creator:eECMy,comment:eECMy,active_revision_ptr:eECMy,outgoing_revision_ptrs:Set[eECMy],incoming_revision_ptr:eECMy,version_number:eECMA):
  eECMa(Version,self).__init__(hash_ref,state_files,parent_ptr)
  self.creator=creator
  self.comment=comment
  self.active_revision_ptr=active_revision_ptr
  self.outgoing_revision_ptrs=outgoing_revision_ptrs
  self.incoming_revision_ptr=incoming_revision_ptr
  self.version_number=version_number
 def __str__(self):
  return VER_TXT_LAYOUT.format(hash_ref=self.hash_ref,parent=self.parent_ptr,creator=self.creator,comment=self.comment,version_number=self.version_number,active_revision=self.active_revision_ptr,outgoing_revisions=";".join(self.outgoing_revision_ptrs),incoming_revision=self.incoming_revision_ptr,state_files=";".join(eECMG(lambda stat_file:eECMy(stat_file),self.state_files))if self.state_files else "")
 def info_str(self):
  return f"{self.version_number}, {self.creator}, {self.comment}"
# Created by pyminifier (https://github.com/liftoff/pyminifier)
