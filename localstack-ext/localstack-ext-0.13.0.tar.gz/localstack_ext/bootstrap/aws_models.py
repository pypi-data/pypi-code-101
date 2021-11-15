from localstack.utils.aws import aws_models
BkRrC=super
BkRra=None
BkRrx=id
class LambdaLayer(aws_models.LambdaFunction):
 def __init__(self,arn):
  BkRrC(LambdaLayer,self).__init__(arn)
  self.cwd=BkRra
  self.runtime=""
  self.handler=""
  self.envvars={}
  self.versions={}
class BaseComponent(aws_models.Component):
 def name(self):
  return self.BkRrx.split(":")[-1]
class RDSDatabase(BaseComponent):
 def __init__(self,BkRrx,env=BkRra):
  BkRrC(RDSDatabase,self).__init__(BkRrx,env=env)
class RDSCluster(BaseComponent):
 def __init__(self,BkRrx,env=BkRra):
  BkRrC(RDSCluster,self).__init__(BkRrx,env=env)
class AppSyncAPI(BaseComponent):
 def __init__(self,BkRrx,env=BkRra):
  BkRrC(AppSyncAPI,self).__init__(BkRrx,env=env)
class AmplifyApp(BaseComponent):
 def __init__(self,BkRrx,env=BkRra):
  BkRrC(AmplifyApp,self).__init__(BkRrx,env=env)
class ElastiCacheCluster(BaseComponent):
 def __init__(self,BkRrx,env=BkRra):
  BkRrC(ElastiCacheCluster,self).__init__(BkRrx,env=env)
class TransferServer(BaseComponent):
 def __init__(self,BkRrx,env=BkRra):
  BkRrC(TransferServer,self).__init__(BkRrx,env=env)
class CloudFrontDistribution(BaseComponent):
 def __init__(self,BkRrx,env=BkRra):
  BkRrC(CloudFrontDistribution,self).__init__(BkRrx,env=env)
class CodeCommitRepository(BaseComponent):
 def __init__(self,BkRrx,env=BkRra):
  BkRrC(CodeCommitRepository,self).__init__(BkRrx,env=env)
# Created by pyminifier (https://github.com/liftoff/pyminifier)
