from localstack.services.cloudformation.service_models import REF_ID_ATTRS,GenericBaseModel
lzSmi=staticmethod
lzSmb=super
class KinesisAnalyticsApplicationOutput(GenericBaseModel):
 @lzSmi
 def cloudformation_type():
  return "AWS::KinesisAnalytics::ApplicationOutput"
 def get_cfn_attribute(self,attribute_name):
  if attribute_name in REF_ID_ATTRS:
   app_name=self.props.get("ApplicationName")
   output_name=self.props.get("Output",{}).get("Name")
   if app_name and output_name:
    return "%s!%s"%(app_name,output_name)
  return lzSmb(KinesisAnalyticsApplicationOutput,self).get_cfn_attribute(attribute_name)
class KinesisAnalyticsApplication(GenericBaseModel):
 @lzSmi
 def cloudformation_type():
  return "AWS::KinesisAnalytics::Application"
 def get_cfn_attribute(self,attribute_name):
  if attribute_name in REF_ID_ATTRS:
   app_name=self.props.get("ApplicationName")
   if app_name:
    return app_name
  return lzSmb(KinesisAnalyticsApplication,self).get_cfn_attribute(attribute_name)
# Created by pyminifier (https://github.com/liftoff/pyminifier)
