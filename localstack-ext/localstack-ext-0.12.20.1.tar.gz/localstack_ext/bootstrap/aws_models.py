from localstack.utils.aws import aws_models
WDNOK=super
WDNOg=None
WDNOc=id
class LambdaLayer(aws_models.LambdaFunction):
 def __init__(self,arn):
  WDNOK(LambdaLayer,self).__init__(arn)
  self.cwd=WDNOg
  self.runtime=""
  self.handler=""
  self.envvars={}
  self.versions={}
class BaseComponent(aws_models.Component):
 def name(self):
  return self.WDNOc.split(":")[-1]
class RDSDatabase(BaseComponent):
 def __init__(self,WDNOc,env=WDNOg):
  WDNOK(RDSDatabase,self).__init__(WDNOc,env=env)
class RDSCluster(BaseComponent):
 def __init__(self,WDNOc,env=WDNOg):
  WDNOK(RDSCluster,self).__init__(WDNOc,env=env)
class AppSyncAPI(BaseComponent):
 def __init__(self,WDNOc,env=WDNOg):
  WDNOK(AppSyncAPI,self).__init__(WDNOc,env=env)
class AmplifyApp(BaseComponent):
 def __init__(self,WDNOc,env=WDNOg):
  WDNOK(AmplifyApp,self).__init__(WDNOc,env=env)
class ElastiCacheCluster(BaseComponent):
 def __init__(self,WDNOc,env=WDNOg):
  WDNOK(ElastiCacheCluster,self).__init__(WDNOc,env=env)
class TransferServer(BaseComponent):
 def __init__(self,WDNOc,env=WDNOg):
  WDNOK(TransferServer,self).__init__(WDNOc,env=env)
class CloudFrontDistribution(BaseComponent):
 def __init__(self,WDNOc,env=WDNOg):
  WDNOK(CloudFrontDistribution,self).__init__(WDNOc,env=env)
class CodeCommitRepository(BaseComponent):
 def __init__(self,WDNOc,env=WDNOg):
  WDNOK(CodeCommitRepository,self).__init__(WDNOc,env=env)
# Created by pyminifier (https://github.com/liftoff/pyminifier)
