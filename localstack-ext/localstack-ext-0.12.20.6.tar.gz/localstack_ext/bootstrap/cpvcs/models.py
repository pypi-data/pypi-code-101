from datetime import datetime
ckCHn=str
ckCHI=int
ckCHz=super
ckCHS=False
ckCHh=isinstance
ckCHw=hash
ckCHe=True
ckCHB=list
ckCHD=map
ckCHa=None
from typing import Set
from localstack_ext.bootstrap.cpvcs.constants import(COMMIT_TXT_LAYOUT,REV_TXT_LAYOUT,STATE_TXT_LAYOUT,STATE_TXT_METADATA,VER_TXT_LAYOUT)
class CPVCSObj:
 def __init__(self,hash_ref:ckCHn):
  self.hash_ref:ckCHn=hash_ref
class StateFileRef(CPVCSObj):
 txt_layout=STATE_TXT_LAYOUT
 metadata_layout=STATE_TXT_METADATA
 def __init__(self,hash_ref:ckCHn,rel_path:ckCHn,file_name:ckCHn,size:ckCHI,service:ckCHn,region:ckCHn):
  ckCHz(StateFileRef,self).__init__(hash_ref)
  self.rel_path:ckCHn=rel_path
  self.file_name:ckCHn=file_name
  self.size:ckCHI=size
  self.service:ckCHn=service
  self.region:ckCHn=region
 def __str__(self):
  return self.txt_layout.format(size=self.size,service=self.service,region=self.region,hash_ref=self.hash_ref,file_name=self.file_name,rel_path=self.rel_path)
 def __eq__(self,other):
  if not other:
   return ckCHS
  if not ckCHh(other,StateFileRef):
   return ckCHS
  return(self.hash_ref==other.hash_ref and self.region==other.region and self.service==self.service and self.file_name==other.file_name and self.size==other.size)
 def __hash__(self):
  return ckCHw((self.hash_ref,self.region,self.service,self.file_name,self.size))
 def congruent(self,other):
  if not other:
   return ckCHS
  if not ckCHh(other,StateFileRef):
   return ckCHS
  return(self.region==other.region and self.service==other.service and self.file_name==other.file_name and self.rel_path==other.rel_path)
 def any_congruence(self,others):
  for other in others:
   if self.congruent(other):
    return ckCHe
  return ckCHS
 def metadata(self)->ckCHn:
  return self.metadata_layout.format(size=self.size,service=self.service,region=self.region)
class CPVCSNode(CPVCSObj):
 def __init__(self,hash_ref:ckCHn,state_files:Set[StateFileRef],parent_ptr:ckCHn):
  ckCHz(CPVCSNode,self).__init__(hash_ref)
  self.state_files:Set[StateFileRef]=state_files
  self.parent_ptr:ckCHn=parent_ptr
 def state_files_info(self)->ckCHn:
  return "\n".join(ckCHB(ckCHD(lambda state_file:ckCHn(state_file),self.state_files)))
class Commit:
 txt_layout=COMMIT_TXT_LAYOUT
 def __init__(self,tail_ptr:ckCHn,head_ptr:ckCHn,message:ckCHn,timestamp:ckCHn=ckCHn(datetime.now().timestamp()),delta_log_ptr:ckCHn=ckCHa):
  self.tail_ptr:ckCHn=tail_ptr
  self.head_ptr:ckCHn=head_ptr
  self.message:ckCHn=message
  self.timestamp:ckCHn=timestamp
  self.delta_log_ptr:ckCHn=delta_log_ptr
 def __str__(self):
  return self.txt_layout.format(tail_ptr=self.tail_ptr,head_ptr=self.head_ptr,message=self.message,timestamp=self.timestamp,log_hash=self.delta_log_ptr)
 def info_str(self,from_node:ckCHn,to_node:ckCHn)->ckCHn:
  return f"from: {from_node}, to: {to_node}, message: {self.message}, time: {datetime.fromtimestamp(float(self.timestamp))}"
class Revision(CPVCSNode):
 txt_layout=REV_TXT_LAYOUT
 def __init__(self,hash_ref:ckCHn,state_files:Set[StateFileRef],parent_ptr:ckCHn,creator:ckCHn,rid:ckCHn,revision_number:ckCHI,assoc_commit:Commit=ckCHa):
  ckCHz(Revision,self).__init__(hash_ref,state_files,parent_ptr)
  self.creator:ckCHn=creator
  self.rid:ckCHn=rid
  self.revision_number:ckCHI=revision_number
  self.assoc_commit=assoc_commit
 def __str__(self):
  return self.txt_layout.format(hash_ref=self.hash_ref,parent=self.parent_ptr,creator=self.creator,rid=self.rid,rev_no=self.revision_number,state_files=";".join(ckCHD(lambda state_file:ckCHn(state_file),self.state_files))if self.state_files else "",assoc_commit=self.assoc_commit)
class Version(CPVCSNode):
 txt_layout=VER_TXT_LAYOUT
 def __init__(self,hash_ref:ckCHn,state_files:Set[StateFileRef],parent_ptr:ckCHn,creator:ckCHn,comment:ckCHn,active_revision_ptr:ckCHn,outgoing_revision_ptrs:Set[ckCHn],incoming_revision_ptr:ckCHn,version_number:ckCHI):
  ckCHz(Version,self).__init__(hash_ref,state_files,parent_ptr)
  self.creator=creator
  self.comment=comment
  self.active_revision_ptr=active_revision_ptr
  self.outgoing_revision_ptrs=outgoing_revision_ptrs
  self.incoming_revision_ptr=incoming_revision_ptr
  self.version_number=version_number
 def __str__(self):
  return VER_TXT_LAYOUT.format(hash_ref=self.hash_ref,parent=self.parent_ptr,creator=self.creator,comment=self.comment,version_number=self.version_number,active_revision=self.active_revision_ptr,outgoing_revisions=";".join(self.outgoing_revision_ptrs),incoming_revision=self.incoming_revision_ptr,state_files=";".join(ckCHD(lambda stat_file:ckCHn(stat_file),self.state_files))if self.state_files else "")
 def info_str(self):
  return f"{self.version_number}, {self.creator}, {self.comment}"
# Created by pyminifier (https://github.com/liftoff/pyminifier)
