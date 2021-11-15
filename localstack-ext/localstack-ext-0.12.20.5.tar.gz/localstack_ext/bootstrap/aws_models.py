from localstack.utils.aws import aws_models
zwlEV=super
zwlED=None
zwlEx=id
class LambdaLayer(aws_models.LambdaFunction):
 def __init__(self,arn):
  zwlEV(LambdaLayer,self).__init__(arn)
  self.cwd=zwlED
  self.runtime=""
  self.handler=""
  self.envvars={}
  self.versions={}
class BaseComponent(aws_models.Component):
 def name(self):
  return self.zwlEx.split(":")[-1]
class RDSDatabase(BaseComponent):
 def __init__(self,zwlEx,env=zwlED):
  zwlEV(RDSDatabase,self).__init__(zwlEx,env=env)
class RDSCluster(BaseComponent):
 def __init__(self,zwlEx,env=zwlED):
  zwlEV(RDSCluster,self).__init__(zwlEx,env=env)
class AppSyncAPI(BaseComponent):
 def __init__(self,zwlEx,env=zwlED):
  zwlEV(AppSyncAPI,self).__init__(zwlEx,env=env)
class AmplifyApp(BaseComponent):
 def __init__(self,zwlEx,env=zwlED):
  zwlEV(AmplifyApp,self).__init__(zwlEx,env=env)
class ElastiCacheCluster(BaseComponent):
 def __init__(self,zwlEx,env=zwlED):
  zwlEV(ElastiCacheCluster,self).__init__(zwlEx,env=env)
class TransferServer(BaseComponent):
 def __init__(self,zwlEx,env=zwlED):
  zwlEV(TransferServer,self).__init__(zwlEx,env=env)
class CloudFrontDistribution(BaseComponent):
 def __init__(self,zwlEx,env=zwlED):
  zwlEV(CloudFrontDistribution,self).__init__(zwlEx,env=env)
class CodeCommitRepository(BaseComponent):
 def __init__(self,zwlEx,env=zwlED):
  zwlEV(CodeCommitRepository,self).__init__(zwlEx,env=env)
# Created by pyminifier (https://github.com/liftoff/pyminifier)
