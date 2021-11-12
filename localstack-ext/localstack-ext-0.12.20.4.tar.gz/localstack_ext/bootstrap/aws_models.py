from localstack.utils.aws import aws_models
wfoxu=super
wfoxB=None
wfoxt=id
class LambdaLayer(aws_models.LambdaFunction):
 def __init__(self,arn):
  wfoxu(LambdaLayer,self).__init__(arn)
  self.cwd=wfoxB
  self.runtime=""
  self.handler=""
  self.envvars={}
  self.versions={}
class BaseComponent(aws_models.Component):
 def name(self):
  return self.wfoxt.split(":")[-1]
class RDSDatabase(BaseComponent):
 def __init__(self,wfoxt,env=wfoxB):
  wfoxu(RDSDatabase,self).__init__(wfoxt,env=env)
class RDSCluster(BaseComponent):
 def __init__(self,wfoxt,env=wfoxB):
  wfoxu(RDSCluster,self).__init__(wfoxt,env=env)
class AppSyncAPI(BaseComponent):
 def __init__(self,wfoxt,env=wfoxB):
  wfoxu(AppSyncAPI,self).__init__(wfoxt,env=env)
class AmplifyApp(BaseComponent):
 def __init__(self,wfoxt,env=wfoxB):
  wfoxu(AmplifyApp,self).__init__(wfoxt,env=env)
class ElastiCacheCluster(BaseComponent):
 def __init__(self,wfoxt,env=wfoxB):
  wfoxu(ElastiCacheCluster,self).__init__(wfoxt,env=env)
class TransferServer(BaseComponent):
 def __init__(self,wfoxt,env=wfoxB):
  wfoxu(TransferServer,self).__init__(wfoxt,env=env)
class CloudFrontDistribution(BaseComponent):
 def __init__(self,wfoxt,env=wfoxB):
  wfoxu(CloudFrontDistribution,self).__init__(wfoxt,env=env)
class CodeCommitRepository(BaseComponent):
 def __init__(self,wfoxt,env=wfoxB):
  wfoxu(CodeCommitRepository,self).__init__(wfoxt,env=env)
# Created by pyminifier (https://github.com/liftoff/pyminifier)
