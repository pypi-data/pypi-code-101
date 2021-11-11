from datetime import datetime
ncgbx=str
ncgbF=int
ncgbG=super
ncgbY=False
ncgbE=isinstance
ncgbk=hash
ncgbW=True
ncgbP=list
ncgbX=map
ncgbQ=None
from typing import Set
from localstack_ext.bootstrap.cpvcs.constants import(COMMIT_TXT_LAYOUT,REV_TXT_LAYOUT,STATE_TXT_LAYOUT,STATE_TXT_METADATA,VER_TXT_LAYOUT)
class CPVCSObj:
 def __init__(self,hash_ref:ncgbx):
  self.hash_ref:ncgbx=hash_ref
class StateFileRef(CPVCSObj):
 txt_layout=STATE_TXT_LAYOUT
 metadata_layout=STATE_TXT_METADATA
 def __init__(self,hash_ref:ncgbx,rel_path:ncgbx,file_name:ncgbx,size:ncgbF,service:ncgbx,region:ncgbx):
  ncgbG(StateFileRef,self).__init__(hash_ref)
  self.rel_path:ncgbx=rel_path
  self.file_name:ncgbx=file_name
  self.size:ncgbF=size
  self.service:ncgbx=service
  self.region:ncgbx=region
 def __str__(self):
  return self.txt_layout.format(size=self.size,service=self.service,region=self.region,hash_ref=self.hash_ref,file_name=self.file_name,rel_path=self.rel_path)
 def __eq__(self,other):
  if not other:
   return ncgbY
  if not ncgbE(other,StateFileRef):
   return ncgbY
  return(self.hash_ref==other.hash_ref and self.region==other.region and self.service==self.service and self.file_name==other.file_name and self.size==other.size)
 def __hash__(self):
  return ncgbk((self.hash_ref,self.region,self.service,self.file_name,self.size))
 def congruent(self,other):
  if not other:
   return ncgbY
  if not ncgbE(other,StateFileRef):
   return ncgbY
  return(self.region==other.region and self.service==other.service and self.file_name==other.file_name and self.rel_path==other.rel_path)
 def any_congruence(self,others):
  for other in others:
   if self.congruent(other):
    return ncgbW
  return ncgbY
 def metadata(self)->ncgbx:
  return self.metadata_layout.format(size=self.size,service=self.service,region=self.region)
class CPVCSNode(CPVCSObj):
 def __init__(self,hash_ref:ncgbx,state_files:Set[StateFileRef],parent_ptr:ncgbx):
  ncgbG(CPVCSNode,self).__init__(hash_ref)
  self.state_files:Set[StateFileRef]=state_files
  self.parent_ptr:ncgbx=parent_ptr
 def state_files_info(self)->ncgbx:
  return "\n".join(ncgbP(ncgbX(lambda state_file:ncgbx(state_file),self.state_files)))
class Commit:
 txt_layout=COMMIT_TXT_LAYOUT
 def __init__(self,tail_ptr:ncgbx,head_ptr:ncgbx,message:ncgbx,timestamp:ncgbx=ncgbx(datetime.now().timestamp()),delta_log_ptr:ncgbx=ncgbQ):
  self.tail_ptr:ncgbx=tail_ptr
  self.head_ptr:ncgbx=head_ptr
  self.message:ncgbx=message
  self.timestamp:ncgbx=timestamp
  self.delta_log_ptr:ncgbx=delta_log_ptr
 def __str__(self):
  return self.txt_layout.format(tail_ptr=self.tail_ptr,head_ptr=self.head_ptr,message=self.message,timestamp=self.timestamp,log_hash=self.delta_log_ptr)
 def info_str(self,from_node:ncgbx,to_node:ncgbx)->ncgbx:
  return f"from: {from_node}, to: {to_node}, message: {self.message}, time: {datetime.fromtimestamp(float(self.timestamp))}"
class Revision(CPVCSNode):
 txt_layout=REV_TXT_LAYOUT
 def __init__(self,hash_ref:ncgbx,state_files:Set[StateFileRef],parent_ptr:ncgbx,creator:ncgbx,rid:ncgbx,revision_number:ncgbF,assoc_commit:Commit=ncgbQ):
  ncgbG(Revision,self).__init__(hash_ref,state_files,parent_ptr)
  self.creator:ncgbx=creator
  self.rid:ncgbx=rid
  self.revision_number:ncgbF=revision_number
  self.assoc_commit=assoc_commit
 def __str__(self):
  return self.txt_layout.format(hash_ref=self.hash_ref,parent=self.parent_ptr,creator=self.creator,rid=self.rid,rev_no=self.revision_number,state_files=";".join(ncgbX(lambda state_file:ncgbx(state_file),self.state_files))if self.state_files else "",assoc_commit=self.assoc_commit)
class Version(CPVCSNode):
 txt_layout=VER_TXT_LAYOUT
 def __init__(self,hash_ref:ncgbx,state_files:Set[StateFileRef],parent_ptr:ncgbx,creator:ncgbx,comment:ncgbx,active_revision_ptr:ncgbx,outgoing_revision_ptrs:Set[ncgbx],incoming_revision_ptr:ncgbx,version_number:ncgbF):
  ncgbG(Version,self).__init__(hash_ref,state_files,parent_ptr)
  self.creator=creator
  self.comment=comment
  self.active_revision_ptr=active_revision_ptr
  self.outgoing_revision_ptrs=outgoing_revision_ptrs
  self.incoming_revision_ptr=incoming_revision_ptr
  self.version_number=version_number
 def __str__(self):
  return VER_TXT_LAYOUT.format(hash_ref=self.hash_ref,parent=self.parent_ptr,creator=self.creator,comment=self.comment,version_number=self.version_number,active_revision=self.active_revision_ptr,outgoing_revisions=";".join(self.outgoing_revision_ptrs),incoming_revision=self.incoming_revision_ptr,state_files=";".join(ncgbX(lambda stat_file:ncgbx(stat_file),self.state_files))if self.state_files else "")
 def info_str(self):
  return f"{self.version_number}, {self.creator}, {self.comment}"
# Created by pyminifier (https://github.com/liftoff/pyminifier)
