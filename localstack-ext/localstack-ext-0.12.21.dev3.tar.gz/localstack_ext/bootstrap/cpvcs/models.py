from datetime import datetime
cfRAS=str
cfRAD=int
cfRAl=super
cfRAu=False
cfRAL=isinstance
cfRAq=hash
cfRAt=True
cfRAC=list
cfRAH=map
cfRAK=None
from typing import Set
from localstack_ext.bootstrap.cpvcs.constants import(COMMIT_TXT_LAYOUT,REV_TXT_LAYOUT,STATE_TXT_LAYOUT,STATE_TXT_METADATA,VER_TXT_LAYOUT)
class CPVCSObj:
 def __init__(self,hash_ref:cfRAS):
  self.hash_ref:cfRAS=hash_ref
class StateFileRef(CPVCSObj):
 txt_layout=STATE_TXT_LAYOUT
 metadata_layout=STATE_TXT_METADATA
 def __init__(self,hash_ref:cfRAS,rel_path:cfRAS,file_name:cfRAS,size:cfRAD,service:cfRAS,region:cfRAS):
  cfRAl(StateFileRef,self).__init__(hash_ref)
  self.rel_path:cfRAS=rel_path
  self.file_name:cfRAS=file_name
  self.size:cfRAD=size
  self.service:cfRAS=service
  self.region:cfRAS=region
 def __str__(self):
  return self.txt_layout.format(size=self.size,service=self.service,region=self.region,hash_ref=self.hash_ref,file_name=self.file_name,rel_path=self.rel_path)
 def __eq__(self,other):
  if not other:
   return cfRAu
  if not cfRAL(other,StateFileRef):
   return cfRAu
  return(self.hash_ref==other.hash_ref and self.region==other.region and self.service==self.service and self.file_name==other.file_name and self.size==other.size)
 def __hash__(self):
  return cfRAq((self.hash_ref,self.region,self.service,self.file_name,self.size))
 def congruent(self,other):
  if not other:
   return cfRAu
  if not cfRAL(other,StateFileRef):
   return cfRAu
  return(self.region==other.region and self.service==other.service and self.file_name==other.file_name and self.rel_path==other.rel_path)
 def any_congruence(self,others):
  for other in others:
   if self.congruent(other):
    return cfRAt
  return cfRAu
 def metadata(self)->cfRAS:
  return self.metadata_layout.format(size=self.size,service=self.service,region=self.region)
class CPVCSNode(CPVCSObj):
 def __init__(self,hash_ref:cfRAS,state_files:Set[StateFileRef],parent_ptr:cfRAS):
  cfRAl(CPVCSNode,self).__init__(hash_ref)
  self.state_files:Set[StateFileRef]=state_files
  self.parent_ptr:cfRAS=parent_ptr
 def state_files_info(self)->cfRAS:
  return "\n".join(cfRAC(cfRAH(lambda state_file:cfRAS(state_file),self.state_files)))
class Commit:
 txt_layout=COMMIT_TXT_LAYOUT
 def __init__(self,tail_ptr:cfRAS,head_ptr:cfRAS,message:cfRAS,timestamp:cfRAS=cfRAS(datetime.now().timestamp()),delta_log_ptr:cfRAS=cfRAK):
  self.tail_ptr:cfRAS=tail_ptr
  self.head_ptr:cfRAS=head_ptr
  self.message:cfRAS=message
  self.timestamp:cfRAS=timestamp
  self.delta_log_ptr:cfRAS=delta_log_ptr
 def __str__(self):
  return self.txt_layout.format(tail_ptr=self.tail_ptr,head_ptr=self.head_ptr,message=self.message,timestamp=self.timestamp,log_hash=self.delta_log_ptr)
 def info_str(self,from_node:cfRAS,to_node:cfRAS)->cfRAS:
  return f"from: {from_node}, to: {to_node}, message: {self.message}, time: {datetime.fromtimestamp(float(self.timestamp))}"
class Revision(CPVCSNode):
 txt_layout=REV_TXT_LAYOUT
 def __init__(self,hash_ref:cfRAS,state_files:Set[StateFileRef],parent_ptr:cfRAS,creator:cfRAS,rid:cfRAS,revision_number:cfRAD,assoc_commit:Commit=cfRAK):
  cfRAl(Revision,self).__init__(hash_ref,state_files,parent_ptr)
  self.creator:cfRAS=creator
  self.rid:cfRAS=rid
  self.revision_number:cfRAD=revision_number
  self.assoc_commit=assoc_commit
 def __str__(self):
  return self.txt_layout.format(hash_ref=self.hash_ref,parent=self.parent_ptr,creator=self.creator,rid=self.rid,rev_no=self.revision_number,state_files=";".join(cfRAH(lambda state_file:cfRAS(state_file),self.state_files))if self.state_files else "",assoc_commit=self.assoc_commit)
class Version(CPVCSNode):
 txt_layout=VER_TXT_LAYOUT
 def __init__(self,hash_ref:cfRAS,state_files:Set[StateFileRef],parent_ptr:cfRAS,creator:cfRAS,comment:cfRAS,active_revision_ptr:cfRAS,outgoing_revision_ptrs:Set[cfRAS],incoming_revision_ptr:cfRAS,version_number:cfRAD):
  cfRAl(Version,self).__init__(hash_ref,state_files,parent_ptr)
  self.creator=creator
  self.comment=comment
  self.active_revision_ptr=active_revision_ptr
  self.outgoing_revision_ptrs=outgoing_revision_ptrs
  self.incoming_revision_ptr=incoming_revision_ptr
  self.version_number=version_number
 def __str__(self):
  return VER_TXT_LAYOUT.format(hash_ref=self.hash_ref,parent=self.parent_ptr,creator=self.creator,comment=self.comment,version_number=self.version_number,active_revision=self.active_revision_ptr,outgoing_revisions=";".join(self.outgoing_revision_ptrs),incoming_revision=self.incoming_revision_ptr,state_files=";".join(cfRAH(lambda stat_file:cfRAS(stat_file),self.state_files))if self.state_files else "")
 def info_str(self):
  return f"{self.version_number}, {self.creator}, {self.comment}"
# Created by pyminifier (https://github.com/liftoff/pyminifier)
