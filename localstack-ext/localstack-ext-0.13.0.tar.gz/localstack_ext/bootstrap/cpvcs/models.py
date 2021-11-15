from datetime import datetime
XOrdL=str
XOrdv=int
XOrdJ=super
XOrdY=False
XOrdn=isinstance
XOrdU=hash
XOrdc=True
XOrdF=list
XOrdk=map
XOrdW=None
from typing import Set
from localstack_ext.bootstrap.cpvcs.constants import(COMMIT_TXT_LAYOUT,REV_TXT_LAYOUT,STATE_TXT_LAYOUT,STATE_TXT_METADATA,VER_TXT_LAYOUT)
class CPVCSObj:
 def __init__(self,hash_ref:XOrdL):
  self.hash_ref:XOrdL=hash_ref
class StateFileRef(CPVCSObj):
 txt_layout=STATE_TXT_LAYOUT
 metadata_layout=STATE_TXT_METADATA
 def __init__(self,hash_ref:XOrdL,rel_path:XOrdL,file_name:XOrdL,size:XOrdv,service:XOrdL,region:XOrdL):
  XOrdJ(StateFileRef,self).__init__(hash_ref)
  self.rel_path:XOrdL=rel_path
  self.file_name:XOrdL=file_name
  self.size:XOrdv=size
  self.service:XOrdL=service
  self.region:XOrdL=region
 def __str__(self):
  return self.txt_layout.format(size=self.size,service=self.service,region=self.region,hash_ref=self.hash_ref,file_name=self.file_name,rel_path=self.rel_path)
 def __eq__(self,other):
  if not other:
   return XOrdY
  if not XOrdn(other,StateFileRef):
   return XOrdY
  return(self.hash_ref==other.hash_ref and self.region==other.region and self.service==self.service and self.file_name==other.file_name and self.size==other.size)
 def __hash__(self):
  return XOrdU((self.hash_ref,self.region,self.service,self.file_name,self.size))
 def congruent(self,other):
  if not other:
   return XOrdY
  if not XOrdn(other,StateFileRef):
   return XOrdY
  return(self.region==other.region and self.service==other.service and self.file_name==other.file_name and self.rel_path==other.rel_path)
 def any_congruence(self,others):
  for other in others:
   if self.congruent(other):
    return XOrdc
  return XOrdY
 def metadata(self)->XOrdL:
  return self.metadata_layout.format(size=self.size,service=self.service,region=self.region)
class CPVCSNode(CPVCSObj):
 def __init__(self,hash_ref:XOrdL,state_files:Set[StateFileRef],parent_ptr:XOrdL):
  XOrdJ(CPVCSNode,self).__init__(hash_ref)
  self.state_files:Set[StateFileRef]=state_files
  self.parent_ptr:XOrdL=parent_ptr
 def state_files_info(self)->XOrdL:
  return "\n".join(XOrdF(XOrdk(lambda state_file:XOrdL(state_file),self.state_files)))
class Commit:
 txt_layout=COMMIT_TXT_LAYOUT
 def __init__(self,tail_ptr:XOrdL,head_ptr:XOrdL,message:XOrdL,timestamp:XOrdL=XOrdL(datetime.now().timestamp()),delta_log_ptr:XOrdL=XOrdW):
  self.tail_ptr:XOrdL=tail_ptr
  self.head_ptr:XOrdL=head_ptr
  self.message:XOrdL=message
  self.timestamp:XOrdL=timestamp
  self.delta_log_ptr:XOrdL=delta_log_ptr
 def __str__(self):
  return self.txt_layout.format(tail_ptr=self.tail_ptr,head_ptr=self.head_ptr,message=self.message,timestamp=self.timestamp,log_hash=self.delta_log_ptr)
 def info_str(self,from_node:XOrdL,to_node:XOrdL)->XOrdL:
  return f"from: {from_node}, to: {to_node}, message: {self.message}, time: {datetime.fromtimestamp(float(self.timestamp))}"
class Revision(CPVCSNode):
 txt_layout=REV_TXT_LAYOUT
 def __init__(self,hash_ref:XOrdL,state_files:Set[StateFileRef],parent_ptr:XOrdL,creator:XOrdL,rid:XOrdL,revision_number:XOrdv,assoc_commit:Commit=XOrdW):
  XOrdJ(Revision,self).__init__(hash_ref,state_files,parent_ptr)
  self.creator:XOrdL=creator
  self.rid:XOrdL=rid
  self.revision_number:XOrdv=revision_number
  self.assoc_commit=assoc_commit
 def __str__(self):
  return self.txt_layout.format(hash_ref=self.hash_ref,parent=self.parent_ptr,creator=self.creator,rid=self.rid,rev_no=self.revision_number,state_files=";".join(XOrdk(lambda state_file:XOrdL(state_file),self.state_files))if self.state_files else "",assoc_commit=self.assoc_commit)
class Version(CPVCSNode):
 txt_layout=VER_TXT_LAYOUT
 def __init__(self,hash_ref:XOrdL,state_files:Set[StateFileRef],parent_ptr:XOrdL,creator:XOrdL,comment:XOrdL,active_revision_ptr:XOrdL,outgoing_revision_ptrs:Set[XOrdL],incoming_revision_ptr:XOrdL,version_number:XOrdv):
  XOrdJ(Version,self).__init__(hash_ref,state_files,parent_ptr)
  self.creator=creator
  self.comment=comment
  self.active_revision_ptr=active_revision_ptr
  self.outgoing_revision_ptrs=outgoing_revision_ptrs
  self.incoming_revision_ptr=incoming_revision_ptr
  self.version_number=version_number
 def __str__(self):
  return VER_TXT_LAYOUT.format(hash_ref=self.hash_ref,parent=self.parent_ptr,creator=self.creator,comment=self.comment,version_number=self.version_number,active_revision=self.active_revision_ptr,outgoing_revisions=";".join(self.outgoing_revision_ptrs),incoming_revision=self.incoming_revision_ptr,state_files=";".join(XOrdk(lambda stat_file:XOrdL(stat_file),self.state_files))if self.state_files else "")
 def info_str(self):
  return f"{self.version_number}, {self.creator}, {self.comment}"
# Created by pyminifier (https://github.com/liftoff/pyminifier)
