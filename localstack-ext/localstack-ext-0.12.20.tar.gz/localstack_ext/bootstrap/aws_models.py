from localstack.utils.aws import aws_models
AQskG=super
AQskp=None
AQskC=id
class LambdaLayer(aws_models.LambdaFunction):
 def __init__(self,arn):
  AQskG(LambdaLayer,self).__init__(arn)
  self.cwd=AQskp
  self.runtime=""
  self.handler=""
  self.envvars={}
  self.versions={}
class BaseComponent(aws_models.Component):
 def name(self):
  return self.AQskC.split(":")[-1]
class RDSDatabase(BaseComponent):
 def __init__(self,AQskC,env=AQskp):
  AQskG(RDSDatabase,self).__init__(AQskC,env=env)
class RDSCluster(BaseComponent):
 def __init__(self,AQskC,env=AQskp):
  AQskG(RDSCluster,self).__init__(AQskC,env=env)
class AppSyncAPI(BaseComponent):
 def __init__(self,AQskC,env=AQskp):
  AQskG(AppSyncAPI,self).__init__(AQskC,env=env)
class AmplifyApp(BaseComponent):
 def __init__(self,AQskC,env=AQskp):
  AQskG(AmplifyApp,self).__init__(AQskC,env=env)
class ElastiCacheCluster(BaseComponent):
 def __init__(self,AQskC,env=AQskp):
  AQskG(ElastiCacheCluster,self).__init__(AQskC,env=env)
class TransferServer(BaseComponent):
 def __init__(self,AQskC,env=AQskp):
  AQskG(TransferServer,self).__init__(AQskC,env=env)
class CloudFrontDistribution(BaseComponent):
 def __init__(self,AQskC,env=AQskp):
  AQskG(CloudFrontDistribution,self).__init__(AQskC,env=env)
class CodeCommitRepository(BaseComponent):
 def __init__(self,AQskC,env=AQskp):
  AQskG(CodeCommitRepository,self).__init__(AQskC,env=env)
# Created by pyminifier (https://github.com/liftoff/pyminifier)
