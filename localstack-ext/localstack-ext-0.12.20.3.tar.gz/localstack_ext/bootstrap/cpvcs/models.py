from datetime import datetime
jTxoy=str
jTxoe=int
jTxoM=super
jTxoK=False
jTxoL=isinstance
jTxoI=hash
jTxoS=True
jTxof=list
jTxoc=map
jTxoF=None
from typing import Set
from localstack_ext.bootstrap.cpvcs.constants import(COMMIT_TXT_LAYOUT,REV_TXT_LAYOUT,STATE_TXT_LAYOUT,STATE_TXT_METADATA,VER_TXT_LAYOUT)
class CPVCSObj:
 def __init__(self,hash_ref:jTxoy):
  self.hash_ref:jTxoy=hash_ref
class StateFileRef(CPVCSObj):
 txt_layout=STATE_TXT_LAYOUT
 metadata_layout=STATE_TXT_METADATA
 def __init__(self,hash_ref:jTxoy,rel_path:jTxoy,file_name:jTxoy,size:jTxoe,service:jTxoy,region:jTxoy):
  jTxoM(StateFileRef,self).__init__(hash_ref)
  self.rel_path:jTxoy=rel_path
  self.file_name:jTxoy=file_name
  self.size:jTxoe=size
  self.service:jTxoy=service
  self.region:jTxoy=region
 def __str__(self):
  return self.txt_layout.format(size=self.size,service=self.service,region=self.region,hash_ref=self.hash_ref,file_name=self.file_name,rel_path=self.rel_path)
 def __eq__(self,other):
  if not other:
   return jTxoK
  if not jTxoL(other,StateFileRef):
   return jTxoK
  return(self.hash_ref==other.hash_ref and self.region==other.region and self.service==self.service and self.file_name==other.file_name and self.size==other.size)
 def __hash__(self):
  return jTxoI((self.hash_ref,self.region,self.service,self.file_name,self.size))
 def congruent(self,other):
  if not other:
   return jTxoK
  if not jTxoL(other,StateFileRef):
   return jTxoK
  return(self.region==other.region and self.service==other.service and self.file_name==other.file_name and self.rel_path==other.rel_path)
 def any_congruence(self,others):
  for other in others:
   if self.congruent(other):
    return jTxoS
  return jTxoK
 def metadata(self)->jTxoy:
  return self.metadata_layout.format(size=self.size,service=self.service,region=self.region)
class CPVCSNode(CPVCSObj):
 def __init__(self,hash_ref:jTxoy,state_files:Set[StateFileRef],parent_ptr:jTxoy):
  jTxoM(CPVCSNode,self).__init__(hash_ref)
  self.state_files:Set[StateFileRef]=state_files
  self.parent_ptr:jTxoy=parent_ptr
 def state_files_info(self)->jTxoy:
  return "\n".join(jTxof(jTxoc(lambda state_file:jTxoy(state_file),self.state_files)))
class Commit:
 txt_layout=COMMIT_TXT_LAYOUT
 def __init__(self,tail_ptr:jTxoy,head_ptr:jTxoy,message:jTxoy,timestamp:jTxoy=jTxoy(datetime.now().timestamp()),delta_log_ptr:jTxoy=jTxoF):
  self.tail_ptr:jTxoy=tail_ptr
  self.head_ptr:jTxoy=head_ptr
  self.message:jTxoy=message
  self.timestamp:jTxoy=timestamp
  self.delta_log_ptr:jTxoy=delta_log_ptr
 def __str__(self):
  return self.txt_layout.format(tail_ptr=self.tail_ptr,head_ptr=self.head_ptr,message=self.message,timestamp=self.timestamp,log_hash=self.delta_log_ptr)
 def info_str(self,from_node:jTxoy,to_node:jTxoy)->jTxoy:
  return f"from: {from_node}, to: {to_node}, message: {self.message}, time: {datetime.fromtimestamp(float(self.timestamp))}"
class Revision(CPVCSNode):
 txt_layout=REV_TXT_LAYOUT
 def __init__(self,hash_ref:jTxoy,state_files:Set[StateFileRef],parent_ptr:jTxoy,creator:jTxoy,rid:jTxoy,revision_number:jTxoe,assoc_commit:Commit=jTxoF):
  jTxoM(Revision,self).__init__(hash_ref,state_files,parent_ptr)
  self.creator:jTxoy=creator
  self.rid:jTxoy=rid
  self.revision_number:jTxoe=revision_number
  self.assoc_commit=assoc_commit
 def __str__(self):
  return self.txt_layout.format(hash_ref=self.hash_ref,parent=self.parent_ptr,creator=self.creator,rid=self.rid,rev_no=self.revision_number,state_files=";".join(jTxoc(lambda state_file:jTxoy(state_file),self.state_files))if self.state_files else "",assoc_commit=self.assoc_commit)
class Version(CPVCSNode):
 txt_layout=VER_TXT_LAYOUT
 def __init__(self,hash_ref:jTxoy,state_files:Set[StateFileRef],parent_ptr:jTxoy,creator:jTxoy,comment:jTxoy,active_revision_ptr:jTxoy,outgoing_revision_ptrs:Set[jTxoy],incoming_revision_ptr:jTxoy,version_number:jTxoe):
  jTxoM(Version,self).__init__(hash_ref,state_files,parent_ptr)
  self.creator=creator
  self.comment=comment
  self.active_revision_ptr=active_revision_ptr
  self.outgoing_revision_ptrs=outgoing_revision_ptrs
  self.incoming_revision_ptr=incoming_revision_ptr
  self.version_number=version_number
 def __str__(self):
  return VER_TXT_LAYOUT.format(hash_ref=self.hash_ref,parent=self.parent_ptr,creator=self.creator,comment=self.comment,version_number=self.version_number,active_revision=self.active_revision_ptr,outgoing_revisions=";".join(self.outgoing_revision_ptrs),incoming_revision=self.incoming_revision_ptr,state_files=";".join(jTxoc(lambda stat_file:jTxoy(stat_file),self.state_files))if self.state_files else "")
 def info_str(self):
  return f"{self.version_number}, {self.creator}, {self.comment}"
# Created by pyminifier (https://github.com/liftoff/pyminifier)
