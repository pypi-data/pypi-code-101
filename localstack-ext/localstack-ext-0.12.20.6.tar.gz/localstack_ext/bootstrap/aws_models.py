from localstack.utils.aws import aws_models
bQqwr=super
bQqwT=None
bQqwc=id
class LambdaLayer(aws_models.LambdaFunction):
 def __init__(self,arn):
  bQqwr(LambdaLayer,self).__init__(arn)
  self.cwd=bQqwT
  self.runtime=""
  self.handler=""
  self.envvars={}
  self.versions={}
class BaseComponent(aws_models.Component):
 def name(self):
  return self.bQqwc.split(":")[-1]
class RDSDatabase(BaseComponent):
 def __init__(self,bQqwc,env=bQqwT):
  bQqwr(RDSDatabase,self).__init__(bQqwc,env=env)
class RDSCluster(BaseComponent):
 def __init__(self,bQqwc,env=bQqwT):
  bQqwr(RDSCluster,self).__init__(bQqwc,env=env)
class AppSyncAPI(BaseComponent):
 def __init__(self,bQqwc,env=bQqwT):
  bQqwr(AppSyncAPI,self).__init__(bQqwc,env=env)
class AmplifyApp(BaseComponent):
 def __init__(self,bQqwc,env=bQqwT):
  bQqwr(AmplifyApp,self).__init__(bQqwc,env=env)
class ElastiCacheCluster(BaseComponent):
 def __init__(self,bQqwc,env=bQqwT):
  bQqwr(ElastiCacheCluster,self).__init__(bQqwc,env=env)
class TransferServer(BaseComponent):
 def __init__(self,bQqwc,env=bQqwT):
  bQqwr(TransferServer,self).__init__(bQqwc,env=env)
class CloudFrontDistribution(BaseComponent):
 def __init__(self,bQqwc,env=bQqwT):
  bQqwr(CloudFrontDistribution,self).__init__(bQqwc,env=env)
class CodeCommitRepository(BaseComponent):
 def __init__(self,bQqwc,env=bQqwT):
  bQqwr(CodeCommitRepository,self).__init__(bQqwc,env=env)
# Created by pyminifier (https://github.com/liftoff/pyminifier)
