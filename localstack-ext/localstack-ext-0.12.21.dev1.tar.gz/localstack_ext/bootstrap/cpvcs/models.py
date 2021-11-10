from datetime import datetime
PsqpK=str
Psqpv=int
Psqpz=super
PsqpM=False
PsqpN=isinstance
Psqpg=hash
PsqpE=True
PsqpO=list
Psqpt=map
PsqpG=None
from typing import Set
from localstack_ext.bootstrap.cpvcs.constants import(COMMIT_TXT_LAYOUT,REV_TXT_LAYOUT,STATE_TXT_LAYOUT,STATE_TXT_METADATA,VER_TXT_LAYOUT)
class CPVCSObj:
 def __init__(self,hash_ref:PsqpK):
  self.hash_ref:PsqpK=hash_ref
class StateFileRef(CPVCSObj):
 txt_layout=STATE_TXT_LAYOUT
 metadata_layout=STATE_TXT_METADATA
 def __init__(self,hash_ref:PsqpK,rel_path:PsqpK,file_name:PsqpK,size:Psqpv,service:PsqpK,region:PsqpK):
  Psqpz(StateFileRef,self).__init__(hash_ref)
  self.rel_path:PsqpK=rel_path
  self.file_name:PsqpK=file_name
  self.size:Psqpv=size
  self.service:PsqpK=service
  self.region:PsqpK=region
 def __str__(self):
  return self.txt_layout.format(size=self.size,service=self.service,region=self.region,hash_ref=self.hash_ref,file_name=self.file_name,rel_path=self.rel_path)
 def __eq__(self,other):
  if not other:
   return PsqpM
  if not PsqpN(other,StateFileRef):
   return PsqpM
  return(self.hash_ref==other.hash_ref and self.region==other.region and self.service==self.service and self.file_name==other.file_name and self.size==other.size)
 def __hash__(self):
  return Psqpg((self.hash_ref,self.region,self.service,self.file_name,self.size))
 def congruent(self,other):
  if not other:
   return PsqpM
  if not PsqpN(other,StateFileRef):
   return PsqpM
  return(self.region==other.region and self.service==other.service and self.file_name==other.file_name and self.rel_path==other.rel_path)
 def any_congruence(self,others):
  for other in others:
   if self.congruent(other):
    return PsqpE
  return PsqpM
 def metadata(self)->PsqpK:
  return self.metadata_layout.format(size=self.size,service=self.service,region=self.region)
class CPVCSNode(CPVCSObj):
 def __init__(self,hash_ref:PsqpK,state_files:Set[StateFileRef],parent_ptr:PsqpK):
  Psqpz(CPVCSNode,self).__init__(hash_ref)
  self.state_files:Set[StateFileRef]=state_files
  self.parent_ptr:PsqpK=parent_ptr
 def state_files_info(self)->PsqpK:
  return "\n".join(PsqpO(Psqpt(lambda state_file:PsqpK(state_file),self.state_files)))
class Commit:
 txt_layout=COMMIT_TXT_LAYOUT
 def __init__(self,tail_ptr:PsqpK,head_ptr:PsqpK,message:PsqpK,timestamp:PsqpK=PsqpK(datetime.now().timestamp()),delta_log_ptr:PsqpK=PsqpG):
  self.tail_ptr:PsqpK=tail_ptr
  self.head_ptr:PsqpK=head_ptr
  self.message:PsqpK=message
  self.timestamp:PsqpK=timestamp
  self.delta_log_ptr:PsqpK=delta_log_ptr
 def __str__(self):
  return self.txt_layout.format(tail_ptr=self.tail_ptr,head_ptr=self.head_ptr,message=self.message,timestamp=self.timestamp,log_hash=self.delta_log_ptr)
 def info_str(self,from_node:PsqpK,to_node:PsqpK)->PsqpK:
  return f"from: {from_node}, to: {to_node}, message: {self.message}, time: {datetime.fromtimestamp(float(self.timestamp))}"
class Revision(CPVCSNode):
 txt_layout=REV_TXT_LAYOUT
 def __init__(self,hash_ref:PsqpK,state_files:Set[StateFileRef],parent_ptr:PsqpK,creator:PsqpK,rid:PsqpK,revision_number:Psqpv,assoc_commit:Commit=PsqpG):
  Psqpz(Revision,self).__init__(hash_ref,state_files,parent_ptr)
  self.creator:PsqpK=creator
  self.rid:PsqpK=rid
  self.revision_number:Psqpv=revision_number
  self.assoc_commit=assoc_commit
 def __str__(self):
  return self.txt_layout.format(hash_ref=self.hash_ref,parent=self.parent_ptr,creator=self.creator,rid=self.rid,rev_no=self.revision_number,state_files=";".join(Psqpt(lambda state_file:PsqpK(state_file),self.state_files))if self.state_files else "",assoc_commit=self.assoc_commit)
class Version(CPVCSNode):
 txt_layout=VER_TXT_LAYOUT
 def __init__(self,hash_ref:PsqpK,state_files:Set[StateFileRef],parent_ptr:PsqpK,creator:PsqpK,comment:PsqpK,active_revision_ptr:PsqpK,outgoing_revision_ptrs:Set[PsqpK],incoming_revision_ptr:PsqpK,version_number:Psqpv):
  Psqpz(Version,self).__init__(hash_ref,state_files,parent_ptr)
  self.creator=creator
  self.comment=comment
  self.active_revision_ptr=active_revision_ptr
  self.outgoing_revision_ptrs=outgoing_revision_ptrs
  self.incoming_revision_ptr=incoming_revision_ptr
  self.version_number=version_number
 def __str__(self):
  return VER_TXT_LAYOUT.format(hash_ref=self.hash_ref,parent=self.parent_ptr,creator=self.creator,comment=self.comment,version_number=self.version_number,active_revision=self.active_revision_ptr,outgoing_revisions=";".join(self.outgoing_revision_ptrs),incoming_revision=self.incoming_revision_ptr,state_files=";".join(Psqpt(lambda stat_file:PsqpK(stat_file),self.state_files))if self.state_files else "")
 def info_str(self):
  return f"{self.version_number}, {self.creator}, {self.comment}"
# Created by pyminifier (https://github.com/liftoff/pyminifier)
