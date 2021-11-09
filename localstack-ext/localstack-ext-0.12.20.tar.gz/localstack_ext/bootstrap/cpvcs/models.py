from datetime import datetime
LrNGt=str
LrNGY=int
LrNGh=super
LrNGC=False
LrNGx=isinstance
LrNGj=hash
LrNGQ=True
LrNGy=list
LrNGX=map
LrNGT=None
from typing import Set
from localstack_ext.bootstrap.cpvcs.constants import(COMMIT_TXT_LAYOUT,REV_TXT_LAYOUT,STATE_TXT_LAYOUT,STATE_TXT_METADATA,VER_TXT_LAYOUT)
class CPVCSObj:
 def __init__(self,hash_ref:LrNGt):
  self.hash_ref:LrNGt=hash_ref
class StateFileRef(CPVCSObj):
 txt_layout=STATE_TXT_LAYOUT
 metadata_layout=STATE_TXT_METADATA
 def __init__(self,hash_ref:LrNGt,rel_path:LrNGt,file_name:LrNGt,size:LrNGY,service:LrNGt,region:LrNGt):
  LrNGh(StateFileRef,self).__init__(hash_ref)
  self.rel_path:LrNGt=rel_path
  self.file_name:LrNGt=file_name
  self.size:LrNGY=size
  self.service:LrNGt=service
  self.region:LrNGt=region
 def __str__(self):
  return self.txt_layout.format(size=self.size,service=self.service,region=self.region,hash_ref=self.hash_ref,file_name=self.file_name,rel_path=self.rel_path)
 def __eq__(self,other):
  if not other:
   return LrNGC
  if not LrNGx(other,StateFileRef):
   return LrNGC
  return(self.hash_ref==other.hash_ref and self.region==other.region and self.service==self.service and self.file_name==other.file_name and self.size==other.size)
 def __hash__(self):
  return LrNGj((self.hash_ref,self.region,self.service,self.file_name,self.size))
 def congruent(self,other):
  if not other:
   return LrNGC
  if not LrNGx(other,StateFileRef):
   return LrNGC
  return(self.region==other.region and self.service==other.service and self.file_name==other.file_name and self.rel_path==other.rel_path)
 def any_congruence(self,others):
  for other in others:
   if self.congruent(other):
    return LrNGQ
  return LrNGC
 def metadata(self)->LrNGt:
  return self.metadata_layout.format(size=self.size,service=self.service,region=self.region)
class CPVCSNode(CPVCSObj):
 def __init__(self,hash_ref:LrNGt,state_files:Set[StateFileRef],parent_ptr:LrNGt):
  LrNGh(CPVCSNode,self).__init__(hash_ref)
  self.state_files:Set[StateFileRef]=state_files
  self.parent_ptr:LrNGt=parent_ptr
 def state_files_info(self)->LrNGt:
  return "\n".join(LrNGy(LrNGX(lambda state_file:LrNGt(state_file),self.state_files)))
class Commit:
 txt_layout=COMMIT_TXT_LAYOUT
 def __init__(self,tail_ptr:LrNGt,head_ptr:LrNGt,message:LrNGt,timestamp:LrNGt=LrNGt(datetime.now().timestamp()),delta_log_ptr:LrNGt=LrNGT):
  self.tail_ptr:LrNGt=tail_ptr
  self.head_ptr:LrNGt=head_ptr
  self.message:LrNGt=message
  self.timestamp:LrNGt=timestamp
  self.delta_log_ptr:LrNGt=delta_log_ptr
 def __str__(self):
  return self.txt_layout.format(tail_ptr=self.tail_ptr,head_ptr=self.head_ptr,message=self.message,timestamp=self.timestamp,log_hash=self.delta_log_ptr)
 def info_str(self,from_node:LrNGt,to_node:LrNGt)->LrNGt:
  return f"from: {from_node}, to: {to_node}, message: {self.message}, time: {datetime.fromtimestamp(float(self.timestamp))}"
class Revision(CPVCSNode):
 txt_layout=REV_TXT_LAYOUT
 def __init__(self,hash_ref:LrNGt,state_files:Set[StateFileRef],parent_ptr:LrNGt,creator:LrNGt,rid:LrNGt,revision_number:LrNGY,assoc_commit:Commit=LrNGT):
  LrNGh(Revision,self).__init__(hash_ref,state_files,parent_ptr)
  self.creator:LrNGt=creator
  self.rid:LrNGt=rid
  self.revision_number:LrNGY=revision_number
  self.assoc_commit=assoc_commit
 def __str__(self):
  return self.txt_layout.format(hash_ref=self.hash_ref,parent=self.parent_ptr,creator=self.creator,rid=self.rid,rev_no=self.revision_number,state_files=";".join(LrNGX(lambda state_file:LrNGt(state_file),self.state_files))if self.state_files else "",assoc_commit=self.assoc_commit)
class Version(CPVCSNode):
 txt_layout=VER_TXT_LAYOUT
 def __init__(self,hash_ref:LrNGt,state_files:Set[StateFileRef],parent_ptr:LrNGt,creator:LrNGt,comment:LrNGt,active_revision_ptr:LrNGt,outgoing_revision_ptrs:Set[LrNGt],incoming_revision_ptr:LrNGt,version_number:LrNGY):
  LrNGh(Version,self).__init__(hash_ref,state_files,parent_ptr)
  self.creator=creator
  self.comment=comment
  self.active_revision_ptr=active_revision_ptr
  self.outgoing_revision_ptrs=outgoing_revision_ptrs
  self.incoming_revision_ptr=incoming_revision_ptr
  self.version_number=version_number
 def __str__(self):
  return VER_TXT_LAYOUT.format(hash_ref=self.hash_ref,parent=self.parent_ptr,creator=self.creator,comment=self.comment,version_number=self.version_number,active_revision=self.active_revision_ptr,outgoing_revisions=";".join(self.outgoing_revision_ptrs),incoming_revision=self.incoming_revision_ptr,state_files=";".join(LrNGX(lambda stat_file:LrNGt(stat_file),self.state_files))if self.state_files else "")
 def info_str(self):
  return f"{self.version_number}, {self.creator}, {self.comment}"
# Created by pyminifier (https://github.com/liftoff/pyminifier)
