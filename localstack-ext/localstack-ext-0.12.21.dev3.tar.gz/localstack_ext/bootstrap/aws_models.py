from localstack.utils.aws import aws_models
JAbvk=super
JAbvl=None
JAbvp=id
class LambdaLayer(aws_models.LambdaFunction):
 def __init__(self,arn):
  JAbvk(LambdaLayer,self).__init__(arn)
  self.cwd=JAbvl
  self.runtime=""
  self.handler=""
  self.envvars={}
  self.versions={}
class BaseComponent(aws_models.Component):
 def name(self):
  return self.JAbvp.split(":")[-1]
class RDSDatabase(BaseComponent):
 def __init__(self,JAbvp,env=JAbvl):
  JAbvk(RDSDatabase,self).__init__(JAbvp,env=env)
class RDSCluster(BaseComponent):
 def __init__(self,JAbvp,env=JAbvl):
  JAbvk(RDSCluster,self).__init__(JAbvp,env=env)
class AppSyncAPI(BaseComponent):
 def __init__(self,JAbvp,env=JAbvl):
  JAbvk(AppSyncAPI,self).__init__(JAbvp,env=env)
class AmplifyApp(BaseComponent):
 def __init__(self,JAbvp,env=JAbvl):
  JAbvk(AmplifyApp,self).__init__(JAbvp,env=env)
class ElastiCacheCluster(BaseComponent):
 def __init__(self,JAbvp,env=JAbvl):
  JAbvk(ElastiCacheCluster,self).__init__(JAbvp,env=env)
class TransferServer(BaseComponent):
 def __init__(self,JAbvp,env=JAbvl):
  JAbvk(TransferServer,self).__init__(JAbvp,env=env)
class CloudFrontDistribution(BaseComponent):
 def __init__(self,JAbvp,env=JAbvl):
  JAbvk(CloudFrontDistribution,self).__init__(JAbvp,env=env)
class CodeCommitRepository(BaseComponent):
 def __init__(self,JAbvp,env=JAbvl):
  JAbvk(CodeCommitRepository,self).__init__(JAbvp,env=env)
# Created by pyminifier (https://github.com/liftoff/pyminifier)
