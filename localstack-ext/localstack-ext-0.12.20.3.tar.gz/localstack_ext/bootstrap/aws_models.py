from localstack.utils.aws import aws_models
lsTPk=super
lsTPa=None
lsTPr=id
class LambdaLayer(aws_models.LambdaFunction):
 def __init__(self,arn):
  lsTPk(LambdaLayer,self).__init__(arn)
  self.cwd=lsTPa
  self.runtime=""
  self.handler=""
  self.envvars={}
  self.versions={}
class BaseComponent(aws_models.Component):
 def name(self):
  return self.lsTPr.split(":")[-1]
class RDSDatabase(BaseComponent):
 def __init__(self,lsTPr,env=lsTPa):
  lsTPk(RDSDatabase,self).__init__(lsTPr,env=env)
class RDSCluster(BaseComponent):
 def __init__(self,lsTPr,env=lsTPa):
  lsTPk(RDSCluster,self).__init__(lsTPr,env=env)
class AppSyncAPI(BaseComponent):
 def __init__(self,lsTPr,env=lsTPa):
  lsTPk(AppSyncAPI,self).__init__(lsTPr,env=env)
class AmplifyApp(BaseComponent):
 def __init__(self,lsTPr,env=lsTPa):
  lsTPk(AmplifyApp,self).__init__(lsTPr,env=env)
class ElastiCacheCluster(BaseComponent):
 def __init__(self,lsTPr,env=lsTPa):
  lsTPk(ElastiCacheCluster,self).__init__(lsTPr,env=env)
class TransferServer(BaseComponent):
 def __init__(self,lsTPr,env=lsTPa):
  lsTPk(TransferServer,self).__init__(lsTPr,env=env)
class CloudFrontDistribution(BaseComponent):
 def __init__(self,lsTPr,env=lsTPa):
  lsTPk(CloudFrontDistribution,self).__init__(lsTPr,env=env)
class CodeCommitRepository(BaseComponent):
 def __init__(self,lsTPr,env=lsTPa):
  lsTPk(CodeCommitRepository,self).__init__(lsTPr,env=env)
# Created by pyminifier (https://github.com/liftoff/pyminifier)
