from localstack.utils.aws import aws_models
cEjfA=super
cEjfB=None
cEjfD=id
class LambdaLayer(aws_models.LambdaFunction):
 def __init__(self,arn):
  cEjfA(LambdaLayer,self).__init__(arn)
  self.cwd=cEjfB
  self.runtime=""
  self.handler=""
  self.envvars={}
  self.versions={}
class BaseComponent(aws_models.Component):
 def name(self):
  return self.cEjfD.split(":")[-1]
class RDSDatabase(BaseComponent):
 def __init__(self,cEjfD,env=cEjfB):
  cEjfA(RDSDatabase,self).__init__(cEjfD,env=env)
class RDSCluster(BaseComponent):
 def __init__(self,cEjfD,env=cEjfB):
  cEjfA(RDSCluster,self).__init__(cEjfD,env=env)
class AppSyncAPI(BaseComponent):
 def __init__(self,cEjfD,env=cEjfB):
  cEjfA(AppSyncAPI,self).__init__(cEjfD,env=env)
class AmplifyApp(BaseComponent):
 def __init__(self,cEjfD,env=cEjfB):
  cEjfA(AmplifyApp,self).__init__(cEjfD,env=env)
class ElastiCacheCluster(BaseComponent):
 def __init__(self,cEjfD,env=cEjfB):
  cEjfA(ElastiCacheCluster,self).__init__(cEjfD,env=env)
class TransferServer(BaseComponent):
 def __init__(self,cEjfD,env=cEjfB):
  cEjfA(TransferServer,self).__init__(cEjfD,env=env)
class CloudFrontDistribution(BaseComponent):
 def __init__(self,cEjfD,env=cEjfB):
  cEjfA(CloudFrontDistribution,self).__init__(cEjfD,env=env)
class CodeCommitRepository(BaseComponent):
 def __init__(self,cEjfD,env=cEjfB):
  cEjfA(CodeCommitRepository,self).__init__(cEjfD,env=env)
# Created by pyminifier (https://github.com/liftoff/pyminifier)
