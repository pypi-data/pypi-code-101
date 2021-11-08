from datetime import datetime
qQpCr=str
qQpCD=int
qQpCc=super
qQpCy=False
qQpCX=isinstance
qQpCj=hash
qQpCA=True
qQpCY=list
qQpCO=map
qQpCh=None
from typing import Set
from localstack_ext.bootstrap.cpvcs.constants import(COMMIT_TXT_LAYOUT,REV_TXT_LAYOUT,STATE_TXT_LAYOUT,STATE_TXT_METADATA,VER_TXT_LAYOUT)
class CPVCSObj:
 def __init__(self,hash_ref:qQpCr):
  self.hash_ref:qQpCr=hash_ref
class StateFileRef(CPVCSObj):
 txt_layout=STATE_TXT_LAYOUT
 metadata_layout=STATE_TXT_METADATA
 def __init__(self,hash_ref:qQpCr,rel_path:qQpCr,file_name:qQpCr,size:qQpCD,service:qQpCr,region:qQpCr):
  qQpCc(StateFileRef,self).__init__(hash_ref)
  self.rel_path:qQpCr=rel_path
  self.file_name:qQpCr=file_name
  self.size:qQpCD=size
  self.service:qQpCr=service
  self.region:qQpCr=region
 def __str__(self):
  return self.txt_layout.format(size=self.size,service=self.service,region=self.region,hash_ref=self.hash_ref,file_name=self.file_name,rel_path=self.rel_path)
 def __eq__(self,other):
  if not other:
   return qQpCy
  if not qQpCX(other,StateFileRef):
   return qQpCy
  return(self.hash_ref==other.hash_ref and self.region==other.region and self.service==self.service and self.file_name==other.file_name and self.size==other.size)
 def __hash__(self):
  return qQpCj((self.hash_ref,self.region,self.service,self.file_name,self.size))
 def congruent(self,other):
  if not other:
   return qQpCy
  if not qQpCX(other,StateFileRef):
   return qQpCy
  return(self.region==other.region and self.service==other.service and self.file_name==other.file_name and self.rel_path==other.rel_path)
 def any_congruence(self,others):
  for other in others:
   if self.congruent(other):
    return qQpCA
  return qQpCy
 def metadata(self)->qQpCr:
  return self.metadata_layout.format(size=self.size,service=self.service,region=self.region)
class CPVCSNode(CPVCSObj):
 def __init__(self,hash_ref:qQpCr,state_files:Set[StateFileRef],parent_ptr:qQpCr):
  qQpCc(CPVCSNode,self).__init__(hash_ref)
  self.state_files:Set[StateFileRef]=state_files
  self.parent_ptr:qQpCr=parent_ptr
 def state_files_info(self)->qQpCr:
  return "\n".join(qQpCY(qQpCO(lambda state_file:qQpCr(state_file),self.state_files)))
class Commit:
 txt_layout=COMMIT_TXT_LAYOUT
 def __init__(self,tail_ptr:qQpCr,head_ptr:qQpCr,message:qQpCr,timestamp:qQpCr=qQpCr(datetime.now().timestamp()),delta_log_ptr:qQpCr=qQpCh):
  self.tail_ptr:qQpCr=tail_ptr
  self.head_ptr:qQpCr=head_ptr
  self.message:qQpCr=message
  self.timestamp:qQpCr=timestamp
  self.delta_log_ptr:qQpCr=delta_log_ptr
 def __str__(self):
  return self.txt_layout.format(tail_ptr=self.tail_ptr,head_ptr=self.head_ptr,message=self.message,timestamp=self.timestamp,log_hash=self.delta_log_ptr)
 def info_str(self,from_node:qQpCr,to_node:qQpCr)->qQpCr:
  return f"from: {from_node}, to: {to_node}, message: {self.message}, time: {datetime.fromtimestamp(float(self.timestamp))}"
class Revision(CPVCSNode):
 txt_layout=REV_TXT_LAYOUT
 def __init__(self,hash_ref:qQpCr,state_files:Set[StateFileRef],parent_ptr:qQpCr,creator:qQpCr,rid:qQpCr,revision_number:qQpCD,assoc_commit:Commit=qQpCh):
  qQpCc(Revision,self).__init__(hash_ref,state_files,parent_ptr)
  self.creator:qQpCr=creator
  self.rid:qQpCr=rid
  self.revision_number:qQpCD=revision_number
  self.assoc_commit=assoc_commit
 def __str__(self):
  return self.txt_layout.format(hash_ref=self.hash_ref,parent=self.parent_ptr,creator=self.creator,rid=self.rid,rev_no=self.revision_number,state_files=";".join(qQpCO(lambda state_file:qQpCr(state_file),self.state_files))if self.state_files else "",assoc_commit=self.assoc_commit)
class Version(CPVCSNode):
 txt_layout=VER_TXT_LAYOUT
 def __init__(self,hash_ref:qQpCr,state_files:Set[StateFileRef],parent_ptr:qQpCr,creator:qQpCr,comment:qQpCr,active_revision_ptr:qQpCr,outgoing_revision_ptrs:Set[qQpCr],incoming_revision_ptr:qQpCr,version_number:qQpCD):
  qQpCc(Version,self).__init__(hash_ref,state_files,parent_ptr)
  self.creator=creator
  self.comment=comment
  self.active_revision_ptr=active_revision_ptr
  self.outgoing_revision_ptrs=outgoing_revision_ptrs
  self.incoming_revision_ptr=incoming_revision_ptr
  self.version_number=version_number
 def __str__(self):
  return VER_TXT_LAYOUT.format(hash_ref=self.hash_ref,parent=self.parent_ptr,creator=self.creator,comment=self.comment,version_number=self.version_number,active_revision=self.active_revision_ptr,outgoing_revisions=";".join(self.outgoing_revision_ptrs),incoming_revision=self.incoming_revision_ptr,state_files=";".join(qQpCO(lambda stat_file:qQpCr(stat_file),self.state_files))if self.state_files else "")
 def info_str(self):
  return f"{self.version_number}, {self.creator}, {self.comment}"
# Created by pyminifier (https://github.com/liftoff/pyminifier)
