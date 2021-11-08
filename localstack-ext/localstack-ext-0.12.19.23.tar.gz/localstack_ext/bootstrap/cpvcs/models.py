from datetime import datetime
Vhxnu=str
VhxnC=int
VhxnD=super
Vhxnd=False
Vhxnc=isinstance
VhxnN=hash
Vhxnp=True
Vhxnf=list
Vhxnz=map
VhxnX=None
from typing import Set
from localstack_ext.bootstrap.cpvcs.constants import(COMMIT_TXT_LAYOUT,REV_TXT_LAYOUT,STATE_TXT_LAYOUT,STATE_TXT_METADATA,VER_TXT_LAYOUT)
class CPVCSObj:
 def __init__(self,hash_ref:Vhxnu):
  self.hash_ref:Vhxnu=hash_ref
class StateFileRef(CPVCSObj):
 txt_layout=STATE_TXT_LAYOUT
 metadata_layout=STATE_TXT_METADATA
 def __init__(self,hash_ref:Vhxnu,rel_path:Vhxnu,file_name:Vhxnu,size:VhxnC,service:Vhxnu,region:Vhxnu):
  VhxnD(StateFileRef,self).__init__(hash_ref)
  self.rel_path:Vhxnu=rel_path
  self.file_name:Vhxnu=file_name
  self.size:VhxnC=size
  self.service:Vhxnu=service
  self.region:Vhxnu=region
 def __str__(self):
  return self.txt_layout.format(size=self.size,service=self.service,region=self.region,hash_ref=self.hash_ref,file_name=self.file_name,rel_path=self.rel_path)
 def __eq__(self,other):
  if not other:
   return Vhxnd
  if not Vhxnc(other,StateFileRef):
   return Vhxnd
  return(self.hash_ref==other.hash_ref and self.region==other.region and self.service==self.service and self.file_name==other.file_name and self.size==other.size)
 def __hash__(self):
  return VhxnN((self.hash_ref,self.region,self.service,self.file_name,self.size))
 def congruent(self,other):
  if not other:
   return Vhxnd
  if not Vhxnc(other,StateFileRef):
   return Vhxnd
  return(self.region==other.region and self.service==other.service and self.file_name==other.file_name and self.rel_path==other.rel_path)
 def any_congruence(self,others):
  for other in others:
   if self.congruent(other):
    return Vhxnp
  return Vhxnd
 def metadata(self)->Vhxnu:
  return self.metadata_layout.format(size=self.size,service=self.service,region=self.region)
class CPVCSNode(CPVCSObj):
 def __init__(self,hash_ref:Vhxnu,state_files:Set[StateFileRef],parent_ptr:Vhxnu):
  VhxnD(CPVCSNode,self).__init__(hash_ref)
  self.state_files:Set[StateFileRef]=state_files
  self.parent_ptr:Vhxnu=parent_ptr
 def state_files_info(self)->Vhxnu:
  return "\n".join(Vhxnf(Vhxnz(lambda state_file:Vhxnu(state_file),self.state_files)))
class Commit:
 txt_layout=COMMIT_TXT_LAYOUT
 def __init__(self,tail_ptr:Vhxnu,head_ptr:Vhxnu,message:Vhxnu,timestamp:Vhxnu=Vhxnu(datetime.now().timestamp()),delta_log_ptr:Vhxnu=VhxnX):
  self.tail_ptr:Vhxnu=tail_ptr
  self.head_ptr:Vhxnu=head_ptr
  self.message:Vhxnu=message
  self.timestamp:Vhxnu=timestamp
  self.delta_log_ptr:Vhxnu=delta_log_ptr
 def __str__(self):
  return self.txt_layout.format(tail_ptr=self.tail_ptr,head_ptr=self.head_ptr,message=self.message,timestamp=self.timestamp,log_hash=self.delta_log_ptr)
 def info_str(self,from_node:Vhxnu,to_node:Vhxnu)->Vhxnu:
  return f"from: {from_node}, to: {to_node}, message: {self.message}, time: {datetime.fromtimestamp(float(self.timestamp))}"
class Revision(CPVCSNode):
 txt_layout=REV_TXT_LAYOUT
 def __init__(self,hash_ref:Vhxnu,state_files:Set[StateFileRef],parent_ptr:Vhxnu,creator:Vhxnu,rid:Vhxnu,revision_number:VhxnC,assoc_commit:Commit=VhxnX):
  VhxnD(Revision,self).__init__(hash_ref,state_files,parent_ptr)
  self.creator:Vhxnu=creator
  self.rid:Vhxnu=rid
  self.revision_number:VhxnC=revision_number
  self.assoc_commit=assoc_commit
 def __str__(self):
  return self.txt_layout.format(hash_ref=self.hash_ref,parent=self.parent_ptr,creator=self.creator,rid=self.rid,rev_no=self.revision_number,state_files=";".join(Vhxnz(lambda state_file:Vhxnu(state_file),self.state_files))if self.state_files else "",assoc_commit=self.assoc_commit)
class Version(CPVCSNode):
 txt_layout=VER_TXT_LAYOUT
 def __init__(self,hash_ref:Vhxnu,state_files:Set[StateFileRef],parent_ptr:Vhxnu,creator:Vhxnu,comment:Vhxnu,active_revision_ptr:Vhxnu,outgoing_revision_ptrs:Set[Vhxnu],incoming_revision_ptr:Vhxnu,version_number:VhxnC):
  VhxnD(Version,self).__init__(hash_ref,state_files,parent_ptr)
  self.creator=creator
  self.comment=comment
  self.active_revision_ptr=active_revision_ptr
  self.outgoing_revision_ptrs=outgoing_revision_ptrs
  self.incoming_revision_ptr=incoming_revision_ptr
  self.version_number=version_number
 def __str__(self):
  return VER_TXT_LAYOUT.format(hash_ref=self.hash_ref,parent=self.parent_ptr,creator=self.creator,comment=self.comment,version_number=self.version_number,active_revision=self.active_revision_ptr,outgoing_revisions=";".join(self.outgoing_revision_ptrs),incoming_revision=self.incoming_revision_ptr,state_files=";".join(Vhxnz(lambda stat_file:Vhxnu(stat_file),self.state_files))if self.state_files else "")
 def info_str(self):
  return f"{self.version_number}, {self.creator}, {self.comment}"
# Created by pyminifier (https://github.com/liftoff/pyminifier)
