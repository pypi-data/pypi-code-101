from localstack.services.cloudformation.service_models import GenericBaseModel
sLoKN=None
sLoKW=classmethod
sLoKD=staticmethod
from localstack.utils.aws import aws_stack
class ServiceDiscoveryNamespace(GenericBaseModel):
 def fetch_state(self,stack_name,resources):
  client=aws_stack.connect_to_service("servicediscovery")
  ns_name=self.resolve_refs_recursively(stack_name,self.props["Name"],resources)
  namespaces=client.list_namespaces()["Namespaces"]
  namespace=[ns for ns in namespaces if ns["Type"]==self._type()and ns["Name"]==ns_name]
  return(namespace or[sLoKN])[0]
 def get_physical_resource_id(self,attribute,**kwargs):
  return self.props.get("Id")
 @sLoKW
 def get_deploy_templates(cls):
  def delete_params(resource_props,resources,resource_id,**kwargs):
   resource=cls(resources[resource_id])
   return{"Id":resource.props.get("Id")}
  create_func=cls._create_function()
  return{"create":{"function":create_func},"delete":{"function":"delete_namespace","parameters":delete_params}}
 def _type(self):
  raise
class ServiceDiscoveryService(ServiceDiscoveryNamespace):
 @sLoKD
 def cloudformation_type():
  return "AWS::ServiceDiscovery::Service"
 def fetch_state(self,stack_name,resources):
  client=aws_stack.connect_to_service("servicediscovery")
  service_name=self.resolve_refs_recursively(stack_name,self.props["Name"],resources)
  services=client.list_services()["Services"]
  service=[s for s in services if s["Name"]==service_name]
  return(service or[sLoKN])[0]
 def get_physical_resource_id(self,attribute,**kwargs):
  if attribute=="Arn":
   return self.props.get("Arn")
  return self.props.get("Id")
 @sLoKW
 def get_deploy_templates(cls):
  def delete_params(resource_props,resources,resource_id,**kwargs):
   resource=cls(resources[resource_id])
   return{"Id":resource.props.get("Id")}
  return{"create":{"function":"create_service"},"delete":{"function":"delete_service","parameters":delete_params}}
class ServiceDiscoveryHttpNamespace(ServiceDiscoveryNamespace):
 @sLoKD
 def cloudformation_type():
  return "AWS::ServiceDiscovery::HttpNamespace"
 @sLoKW
 def _type(cls):
  return "HTTP"
 @sLoKW
 def _create_function(cls):
  return "create_http_namespace"
class ServiceDiscoveryPublicDnsNamespace(ServiceDiscoveryNamespace):
 @sLoKD
 def cloudformation_type():
  return "AWS::ServiceDiscovery::PublicDnsNamespace"
 @sLoKW
 def _type(cls):
  return "DNS_PUBLIC"
 @sLoKW
 def _create_function(cls):
  return "create_public_dns_namespace"
class ServiceDiscoveryPrivateDnsNamespace(ServiceDiscoveryNamespace):
 @sLoKD
 def cloudformation_type():
  return "AWS::ServiceDiscovery::PrivateDnsNamespace"
 @sLoKW
 def _type(cls):
  return "DNS_PRIVATE"
 @sLoKW
 def _create_function(cls):
  return "create_private_dns_namespace"
# Created by pyminifier (https://github.com/liftoff/pyminifier)
