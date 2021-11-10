from localstack.utils.aws import aws_models
rqsIY=super
rqsIB=None
rqsIK=id
class LambdaLayer(aws_models.LambdaFunction):
 def __init__(self,arn):
  rqsIY(LambdaLayer,self).__init__(arn)
  self.cwd=rqsIB
  self.runtime=""
  self.handler=""
  self.envvars={}
  self.versions={}
class BaseComponent(aws_models.Component):
 def name(self):
  return self.rqsIK.split(":")[-1]
class RDSDatabase(BaseComponent):
 def __init__(self,rqsIK,env=rqsIB):
  rqsIY(RDSDatabase,self).__init__(rqsIK,env=env)
class RDSCluster(BaseComponent):
 def __init__(self,rqsIK,env=rqsIB):
  rqsIY(RDSCluster,self).__init__(rqsIK,env=env)
class AppSyncAPI(BaseComponent):
 def __init__(self,rqsIK,env=rqsIB):
  rqsIY(AppSyncAPI,self).__init__(rqsIK,env=env)
class AmplifyApp(BaseComponent):
 def __init__(self,rqsIK,env=rqsIB):
  rqsIY(AmplifyApp,self).__init__(rqsIK,env=env)
class ElastiCacheCluster(BaseComponent):
 def __init__(self,rqsIK,env=rqsIB):
  rqsIY(ElastiCacheCluster,self).__init__(rqsIK,env=env)
class TransferServer(BaseComponent):
 def __init__(self,rqsIK,env=rqsIB):
  rqsIY(TransferServer,self).__init__(rqsIK,env=env)
class CloudFrontDistribution(BaseComponent):
 def __init__(self,rqsIK,env=rqsIB):
  rqsIY(CloudFrontDistribution,self).__init__(rqsIK,env=env)
class CodeCommitRepository(BaseComponent):
 def __init__(self,rqsIK,env=rqsIB):
  rqsIY(CodeCommitRepository,self).__init__(rqsIK,env=env)
# Created by pyminifier (https://github.com/liftoff/pyminifier)
