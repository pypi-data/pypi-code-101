from localstack.utils.aws import aws_models
LuXax=super
LuXaM=None
LuXar=id
class LambdaLayer(aws_models.LambdaFunction):
 def __init__(self,arn):
  LuXax(LambdaLayer,self).__init__(arn)
  self.cwd=LuXaM
  self.runtime=""
  self.handler=""
  self.envvars={}
  self.versions={}
class BaseComponent(aws_models.Component):
 def name(self):
  return self.LuXar.split(":")[-1]
class RDSDatabase(BaseComponent):
 def __init__(self,LuXar,env=LuXaM):
  LuXax(RDSDatabase,self).__init__(LuXar,env=env)
class RDSCluster(BaseComponent):
 def __init__(self,LuXar,env=LuXaM):
  LuXax(RDSCluster,self).__init__(LuXar,env=env)
class AppSyncAPI(BaseComponent):
 def __init__(self,LuXar,env=LuXaM):
  LuXax(AppSyncAPI,self).__init__(LuXar,env=env)
class AmplifyApp(BaseComponent):
 def __init__(self,LuXar,env=LuXaM):
  LuXax(AmplifyApp,self).__init__(LuXar,env=env)
class ElastiCacheCluster(BaseComponent):
 def __init__(self,LuXar,env=LuXaM):
  LuXax(ElastiCacheCluster,self).__init__(LuXar,env=env)
class TransferServer(BaseComponent):
 def __init__(self,LuXar,env=LuXaM):
  LuXax(TransferServer,self).__init__(LuXar,env=env)
class CloudFrontDistribution(BaseComponent):
 def __init__(self,LuXar,env=LuXaM):
  LuXax(CloudFrontDistribution,self).__init__(LuXar,env=env)
class CodeCommitRepository(BaseComponent):
 def __init__(self,LuXar,env=LuXaM):
  LuXax(CodeCommitRepository,self).__init__(LuXar,env=env)
# Created by pyminifier (https://github.com/liftoff/pyminifier)
