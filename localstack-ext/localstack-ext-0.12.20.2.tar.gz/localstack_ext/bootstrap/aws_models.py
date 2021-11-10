from localstack.utils.aws import aws_models
MFwlm=super
MFwlc=None
MFwlY=id
class LambdaLayer(aws_models.LambdaFunction):
 def __init__(self,arn):
  MFwlm(LambdaLayer,self).__init__(arn)
  self.cwd=MFwlc
  self.runtime=""
  self.handler=""
  self.envvars={}
  self.versions={}
class BaseComponent(aws_models.Component):
 def name(self):
  return self.MFwlY.split(":")[-1]
class RDSDatabase(BaseComponent):
 def __init__(self,MFwlY,env=MFwlc):
  MFwlm(RDSDatabase,self).__init__(MFwlY,env=env)
class RDSCluster(BaseComponent):
 def __init__(self,MFwlY,env=MFwlc):
  MFwlm(RDSCluster,self).__init__(MFwlY,env=env)
class AppSyncAPI(BaseComponent):
 def __init__(self,MFwlY,env=MFwlc):
  MFwlm(AppSyncAPI,self).__init__(MFwlY,env=env)
class AmplifyApp(BaseComponent):
 def __init__(self,MFwlY,env=MFwlc):
  MFwlm(AmplifyApp,self).__init__(MFwlY,env=env)
class ElastiCacheCluster(BaseComponent):
 def __init__(self,MFwlY,env=MFwlc):
  MFwlm(ElastiCacheCluster,self).__init__(MFwlY,env=env)
class TransferServer(BaseComponent):
 def __init__(self,MFwlY,env=MFwlc):
  MFwlm(TransferServer,self).__init__(MFwlY,env=env)
class CloudFrontDistribution(BaseComponent):
 def __init__(self,MFwlY,env=MFwlc):
  MFwlm(CloudFrontDistribution,self).__init__(MFwlY,env=env)
class CodeCommitRepository(BaseComponent):
 def __init__(self,MFwlY,env=MFwlc):
  MFwlm(CodeCommitRepository,self).__init__(MFwlY,env=env)
# Created by pyminifier (https://github.com/liftoff/pyminifier)
