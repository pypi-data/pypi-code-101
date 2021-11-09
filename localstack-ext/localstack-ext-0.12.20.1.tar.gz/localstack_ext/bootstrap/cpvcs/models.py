from datetime import datetime
VbIUm=str
VbIUe=int
VbIUN=super
VbIUi=False
VbIUK=isinstance
VbIUF=hash
VbIUC=True
VbIUh=list
VbIUa=map
VbIUW=None
from typing import Set
from localstack_ext.bootstrap.cpvcs.constants import(COMMIT_TXT_LAYOUT,REV_TXT_LAYOUT,STATE_TXT_LAYOUT,STATE_TXT_METADATA,VER_TXT_LAYOUT)
class CPVCSObj:
 def __init__(self,hash_ref:VbIUm):
  self.hash_ref:VbIUm=hash_ref
class StateFileRef(CPVCSObj):
 txt_layout=STATE_TXT_LAYOUT
 metadata_layout=STATE_TXT_METADATA
 def __init__(self,hash_ref:VbIUm,rel_path:VbIUm,file_name:VbIUm,size:VbIUe,service:VbIUm,region:VbIUm):
  VbIUN(StateFileRef,self).__init__(hash_ref)
  self.rel_path:VbIUm=rel_path
  self.file_name:VbIUm=file_name
  self.size:VbIUe=size
  self.service:VbIUm=service
  self.region:VbIUm=region
 def __str__(self):
  return self.txt_layout.format(size=self.size,service=self.service,region=self.region,hash_ref=self.hash_ref,file_name=self.file_name,rel_path=self.rel_path)
 def __eq__(self,other):
  if not other:
   return VbIUi
  if not VbIUK(other,StateFileRef):
   return VbIUi
  return(self.hash_ref==other.hash_ref and self.region==other.region and self.service==self.service and self.file_name==other.file_name and self.size==other.size)
 def __hash__(self):
  return VbIUF((self.hash_ref,self.region,self.service,self.file_name,self.size))
 def congruent(self,other):
  if not other:
   return VbIUi
  if not VbIUK(other,StateFileRef):
   return VbIUi
  return(self.region==other.region and self.service==other.service and self.file_name==other.file_name and self.rel_path==other.rel_path)
 def any_congruence(self,others):
  for other in others:
   if self.congruent(other):
    return VbIUC
  return VbIUi
 def metadata(self)->VbIUm:
  return self.metadata_layout.format(size=self.size,service=self.service,region=self.region)
class CPVCSNode(CPVCSObj):
 def __init__(self,hash_ref:VbIUm,state_files:Set[StateFileRef],parent_ptr:VbIUm):
  VbIUN(CPVCSNode,self).__init__(hash_ref)
  self.state_files:Set[StateFileRef]=state_files
  self.parent_ptr:VbIUm=parent_ptr
 def state_files_info(self)->VbIUm:
  return "\n".join(VbIUh(VbIUa(lambda state_file:VbIUm(state_file),self.state_files)))
class Commit:
 txt_layout=COMMIT_TXT_LAYOUT
 def __init__(self,tail_ptr:VbIUm,head_ptr:VbIUm,message:VbIUm,timestamp:VbIUm=VbIUm(datetime.now().timestamp()),delta_log_ptr:VbIUm=VbIUW):
  self.tail_ptr:VbIUm=tail_ptr
  self.head_ptr:VbIUm=head_ptr
  self.message:VbIUm=message
  self.timestamp:VbIUm=timestamp
  self.delta_log_ptr:VbIUm=delta_log_ptr
 def __str__(self):
  return self.txt_layout.format(tail_ptr=self.tail_ptr,head_ptr=self.head_ptr,message=self.message,timestamp=self.timestamp,log_hash=self.delta_log_ptr)
 def info_str(self,from_node:VbIUm,to_node:VbIUm)->VbIUm:
  return f"from: {from_node}, to: {to_node}, message: {self.message}, time: {datetime.fromtimestamp(float(self.timestamp))}"
class Revision(CPVCSNode):
 txt_layout=REV_TXT_LAYOUT
 def __init__(self,hash_ref:VbIUm,state_files:Set[StateFileRef],parent_ptr:VbIUm,creator:VbIUm,rid:VbIUm,revision_number:VbIUe,assoc_commit:Commit=VbIUW):
  VbIUN(Revision,self).__init__(hash_ref,state_files,parent_ptr)
  self.creator:VbIUm=creator
  self.rid:VbIUm=rid
  self.revision_number:VbIUe=revision_number
  self.assoc_commit=assoc_commit
 def __str__(self):
  return self.txt_layout.format(hash_ref=self.hash_ref,parent=self.parent_ptr,creator=self.creator,rid=self.rid,rev_no=self.revision_number,state_files=";".join(VbIUa(lambda state_file:VbIUm(state_file),self.state_files))if self.state_files else "",assoc_commit=self.assoc_commit)
class Version(CPVCSNode):
 txt_layout=VER_TXT_LAYOUT
 def __init__(self,hash_ref:VbIUm,state_files:Set[StateFileRef],parent_ptr:VbIUm,creator:VbIUm,comment:VbIUm,active_revision_ptr:VbIUm,outgoing_revision_ptrs:Set[VbIUm],incoming_revision_ptr:VbIUm,version_number:VbIUe):
  VbIUN(Version,self).__init__(hash_ref,state_files,parent_ptr)
  self.creator=creator
  self.comment=comment
  self.active_revision_ptr=active_revision_ptr
  self.outgoing_revision_ptrs=outgoing_revision_ptrs
  self.incoming_revision_ptr=incoming_revision_ptr
  self.version_number=version_number
 def __str__(self):
  return VER_TXT_LAYOUT.format(hash_ref=self.hash_ref,parent=self.parent_ptr,creator=self.creator,comment=self.comment,version_number=self.version_number,active_revision=self.active_revision_ptr,outgoing_revisions=";".join(self.outgoing_revision_ptrs),incoming_revision=self.incoming_revision_ptr,state_files=";".join(VbIUa(lambda stat_file:VbIUm(stat_file),self.state_files))if self.state_files else "")
 def info_str(self):
  return f"{self.version_number}, {self.creator}, {self.comment}"
# Created by pyminifier (https://github.com/liftoff/pyminifier)
