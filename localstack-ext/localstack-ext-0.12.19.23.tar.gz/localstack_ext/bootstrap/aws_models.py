from localstack.utils.aws import aws_models
Fpvmx=super
Fpvmo=None
FpvmW=id
class LambdaLayer(aws_models.LambdaFunction):
 def __init__(self,arn):
  Fpvmx(LambdaLayer,self).__init__(arn)
  self.cwd=Fpvmo
  self.runtime=""
  self.handler=""
  self.envvars={}
  self.versions={}
class BaseComponent(aws_models.Component):
 def name(self):
  return self.FpvmW.split(":")[-1]
class RDSDatabase(BaseComponent):
 def __init__(self,FpvmW,env=Fpvmo):
  Fpvmx(RDSDatabase,self).__init__(FpvmW,env=env)
class RDSCluster(BaseComponent):
 def __init__(self,FpvmW,env=Fpvmo):
  Fpvmx(RDSCluster,self).__init__(FpvmW,env=env)
class AppSyncAPI(BaseComponent):
 def __init__(self,FpvmW,env=Fpvmo):
  Fpvmx(AppSyncAPI,self).__init__(FpvmW,env=env)
class AmplifyApp(BaseComponent):
 def __init__(self,FpvmW,env=Fpvmo):
  Fpvmx(AmplifyApp,self).__init__(FpvmW,env=env)
class ElastiCacheCluster(BaseComponent):
 def __init__(self,FpvmW,env=Fpvmo):
  Fpvmx(ElastiCacheCluster,self).__init__(FpvmW,env=env)
class TransferServer(BaseComponent):
 def __init__(self,FpvmW,env=Fpvmo):
  Fpvmx(TransferServer,self).__init__(FpvmW,env=env)
class CloudFrontDistribution(BaseComponent):
 def __init__(self,FpvmW,env=Fpvmo):
  Fpvmx(CloudFrontDistribution,self).__init__(FpvmW,env=env)
class CodeCommitRepository(BaseComponent):
 def __init__(self,FpvmW,env=Fpvmo):
  Fpvmx(CodeCommitRepository,self).__init__(FpvmW,env=env)
# Created by pyminifier (https://github.com/liftoff/pyminifier)
