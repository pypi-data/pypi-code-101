from localstack.utils.aws import aws_models
TkUjG=super
TkUjL=None
TkUjc=id
class LambdaLayer(aws_models.LambdaFunction):
 def __init__(self,arn):
  TkUjG(LambdaLayer,self).__init__(arn)
  self.cwd=TkUjL
  self.runtime=""
  self.handler=""
  self.envvars={}
  self.versions={}
class BaseComponent(aws_models.Component):
 def name(self):
  return self.TkUjc.split(":")[-1]
class RDSDatabase(BaseComponent):
 def __init__(self,TkUjc,env=TkUjL):
  TkUjG(RDSDatabase,self).__init__(TkUjc,env=env)
class RDSCluster(BaseComponent):
 def __init__(self,TkUjc,env=TkUjL):
  TkUjG(RDSCluster,self).__init__(TkUjc,env=env)
class AppSyncAPI(BaseComponent):
 def __init__(self,TkUjc,env=TkUjL):
  TkUjG(AppSyncAPI,self).__init__(TkUjc,env=env)
class AmplifyApp(BaseComponent):
 def __init__(self,TkUjc,env=TkUjL):
  TkUjG(AmplifyApp,self).__init__(TkUjc,env=env)
class ElastiCacheCluster(BaseComponent):
 def __init__(self,TkUjc,env=TkUjL):
  TkUjG(ElastiCacheCluster,self).__init__(TkUjc,env=env)
class TransferServer(BaseComponent):
 def __init__(self,TkUjc,env=TkUjL):
  TkUjG(TransferServer,self).__init__(TkUjc,env=env)
class CloudFrontDistribution(BaseComponent):
 def __init__(self,TkUjc,env=TkUjL):
  TkUjG(CloudFrontDistribution,self).__init__(TkUjc,env=env)
class CodeCommitRepository(BaseComponent):
 def __init__(self,TkUjc,env=TkUjL):
  TkUjG(CodeCommitRepository,self).__init__(TkUjc,env=env)
# Created by pyminifier (https://github.com/liftoff/pyminifier)
