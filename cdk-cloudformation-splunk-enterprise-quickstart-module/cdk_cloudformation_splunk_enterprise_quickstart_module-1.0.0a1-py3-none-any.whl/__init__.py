'''
# AWS CDK CloudFormation Constructs for Splunk::Enterprise::QuickStart::MODULE

Schema for Module Fragment of type Splunk::Enterprise::QuickStart::MODULE

## License

Distributed under the Apache-2.0 License.
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from ._jsii import *

import aws_cdk.core


class CfnModule(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnModule",
):
    '''A CloudFormation ``Splunk::Enterprise::QuickStart::MODULE``.

    :cloudformationResource: Splunk::Enterprise::QuickStart::MODULE
    :link: http://unknown-url
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        parameters: typing.Optional["CfnModulePropsParameters"] = None,
        resources: typing.Optional["CfnModulePropsResources"] = None,
    ) -> None:
        '''Create a new ``Splunk::Enterprise::QuickStart::MODULE``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param parameters: 
        :param resources: 
        '''
        props = CfnModuleProps(parameters=parameters, resources=resources)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnModuleProps":
        '''Resource props.'''
        return typing.cast("CfnModuleProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnModuleProps",
    jsii_struct_bases=[],
    name_mapping={"parameters": "parameters", "resources": "resources"},
)
class CfnModuleProps:
    def __init__(
        self,
        *,
        parameters: typing.Optional["CfnModulePropsParameters"] = None,
        resources: typing.Optional["CfnModulePropsResources"] = None,
    ) -> None:
        '''Schema for Module Fragment of type Splunk::Enterprise::QuickStart::MODULE.

        :param parameters: 
        :param resources: 

        :schema: CfnModuleProps
        '''
        if isinstance(parameters, dict):
            parameters = CfnModulePropsParameters(**parameters)
        if isinstance(resources, dict):
            resources = CfnModulePropsResources(**resources)
        self._values: typing.Dict[str, typing.Any] = {}
        if parameters is not None:
            self._values["parameters"] = parameters
        if resources is not None:
            self._values["resources"] = resources

    @builtins.property
    def parameters(self) -> typing.Optional["CfnModulePropsParameters"]:
        '''
        :schema: CfnModuleProps#Parameters
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional["CfnModulePropsParameters"], result)

    @builtins.property
    def resources(self) -> typing.Optional["CfnModulePropsResources"]:
        '''
        :schema: CfnModuleProps#Resources
        '''
        result = self._values.get("resources")
        return typing.cast(typing.Optional["CfnModulePropsResources"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModuleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnModulePropsParameters",
    jsii_struct_bases=[],
    name_mapping={
        "availability_zones": "availabilityZones",
        "hec_client_location": "hecClientLocation",
        "indexer_instance_type": "indexerInstanceType",
        "key_name": "keyName",
        "number_of_a_zs": "numberOfAZs",
        "public_subnet1_cidr": "publicSubnet1Cidr",
        "public_subnet2_cidr": "publicSubnet2Cidr",
        "public_subnet3_cidr": "publicSubnet3Cidr",
        "search_head_instance_type": "searchHeadInstanceType",
        "shc_enabled": "shcEnabled",
        "smart_store_bucket_name": "smartStoreBucketName",
        "splunk_admin_password": "splunkAdminPassword",
        "splunk_cluster_secret": "splunkClusterSecret",
        "splunk_indexer_count": "splunkIndexerCount",
        "splunk_indexer_discovery_secret": "splunkIndexerDiscoverySecret",
        "splunk_indexer_disk_size": "splunkIndexerDiskSize",
        "splunk_license_bucket": "splunkLicenseBucket",
        "splunk_license_path": "splunkLicensePath",
        "splunk_replication_factor": "splunkReplicationFactor",
        "splunk_search_factor": "splunkSearchFactor",
        "splunk_search_head_disk_size": "splunkSearchHeadDiskSize",
        "ssh_client_location": "sshClientLocation",
        "vpccidr": "vpccidr",
        "web_client_location": "webClientLocation",
    },
)
class CfnModulePropsParameters:
    def __init__(
        self,
        *,
        availability_zones: typing.Optional["CfnModulePropsParametersAvailabilityZones"] = None,
        hec_client_location: typing.Optional["CfnModulePropsParametersHecClientLocation"] = None,
        indexer_instance_type: typing.Optional["CfnModulePropsParametersIndexerInstanceType"] = None,
        key_name: typing.Optional["CfnModulePropsParametersKeyName"] = None,
        number_of_a_zs: typing.Optional["CfnModulePropsParametersNumberOfAZs"] = None,
        public_subnet1_cidr: typing.Optional["CfnModulePropsParametersPublicSubnet1Cidr"] = None,
        public_subnet2_cidr: typing.Optional["CfnModulePropsParametersPublicSubnet2Cidr"] = None,
        public_subnet3_cidr: typing.Optional["CfnModulePropsParametersPublicSubnet3Cidr"] = None,
        search_head_instance_type: typing.Optional["CfnModulePropsParametersSearchHeadInstanceType"] = None,
        shc_enabled: typing.Optional["CfnModulePropsParametersShcEnabled"] = None,
        smart_store_bucket_name: typing.Optional["CfnModulePropsParametersSmartStoreBucketName"] = None,
        splunk_admin_password: typing.Optional["CfnModulePropsParametersSplunkAdminPassword"] = None,
        splunk_cluster_secret: typing.Optional["CfnModulePropsParametersSplunkClusterSecret"] = None,
        splunk_indexer_count: typing.Optional["CfnModulePropsParametersSplunkIndexerCount"] = None,
        splunk_indexer_discovery_secret: typing.Optional["CfnModulePropsParametersSplunkIndexerDiscoverySecret"] = None,
        splunk_indexer_disk_size: typing.Optional["CfnModulePropsParametersSplunkIndexerDiskSize"] = None,
        splunk_license_bucket: typing.Optional["CfnModulePropsParametersSplunkLicenseBucket"] = None,
        splunk_license_path: typing.Optional["CfnModulePropsParametersSplunkLicensePath"] = None,
        splunk_replication_factor: typing.Optional["CfnModulePropsParametersSplunkReplicationFactor"] = None,
        splunk_search_factor: typing.Optional["CfnModulePropsParametersSplunkSearchFactor"] = None,
        splunk_search_head_disk_size: typing.Optional["CfnModulePropsParametersSplunkSearchHeadDiskSize"] = None,
        ssh_client_location: typing.Optional["CfnModulePropsParametersSshClientLocation"] = None,
        vpccidr: typing.Optional["CfnModulePropsParametersVpccidr"] = None,
        web_client_location: typing.Optional["CfnModulePropsParametersWebClientLocation"] = None,
    ) -> None:
        '''
        :param availability_zones: 
        :param hec_client_location: 
        :param indexer_instance_type: 
        :param key_name: 
        :param number_of_a_zs: 
        :param public_subnet1_cidr: 
        :param public_subnet2_cidr: 
        :param public_subnet3_cidr: 
        :param search_head_instance_type: 
        :param shc_enabled: 
        :param smart_store_bucket_name: 
        :param splunk_admin_password: 
        :param splunk_cluster_secret: 
        :param splunk_indexer_count: 
        :param splunk_indexer_discovery_secret: 
        :param splunk_indexer_disk_size: 
        :param splunk_license_bucket: 
        :param splunk_license_path: 
        :param splunk_replication_factor: 
        :param splunk_search_factor: 
        :param splunk_search_head_disk_size: 
        :param ssh_client_location: 
        :param vpccidr: 
        :param web_client_location: 

        :schema: CfnModulePropsParameters
        '''
        if isinstance(availability_zones, dict):
            availability_zones = CfnModulePropsParametersAvailabilityZones(**availability_zones)
        if isinstance(hec_client_location, dict):
            hec_client_location = CfnModulePropsParametersHecClientLocation(**hec_client_location)
        if isinstance(indexer_instance_type, dict):
            indexer_instance_type = CfnModulePropsParametersIndexerInstanceType(**indexer_instance_type)
        if isinstance(key_name, dict):
            key_name = CfnModulePropsParametersKeyName(**key_name)
        if isinstance(number_of_a_zs, dict):
            number_of_a_zs = CfnModulePropsParametersNumberOfAZs(**number_of_a_zs)
        if isinstance(public_subnet1_cidr, dict):
            public_subnet1_cidr = CfnModulePropsParametersPublicSubnet1Cidr(**public_subnet1_cidr)
        if isinstance(public_subnet2_cidr, dict):
            public_subnet2_cidr = CfnModulePropsParametersPublicSubnet2Cidr(**public_subnet2_cidr)
        if isinstance(public_subnet3_cidr, dict):
            public_subnet3_cidr = CfnModulePropsParametersPublicSubnet3Cidr(**public_subnet3_cidr)
        if isinstance(search_head_instance_type, dict):
            search_head_instance_type = CfnModulePropsParametersSearchHeadInstanceType(**search_head_instance_type)
        if isinstance(shc_enabled, dict):
            shc_enabled = CfnModulePropsParametersShcEnabled(**shc_enabled)
        if isinstance(smart_store_bucket_name, dict):
            smart_store_bucket_name = CfnModulePropsParametersSmartStoreBucketName(**smart_store_bucket_name)
        if isinstance(splunk_admin_password, dict):
            splunk_admin_password = CfnModulePropsParametersSplunkAdminPassword(**splunk_admin_password)
        if isinstance(splunk_cluster_secret, dict):
            splunk_cluster_secret = CfnModulePropsParametersSplunkClusterSecret(**splunk_cluster_secret)
        if isinstance(splunk_indexer_count, dict):
            splunk_indexer_count = CfnModulePropsParametersSplunkIndexerCount(**splunk_indexer_count)
        if isinstance(splunk_indexer_discovery_secret, dict):
            splunk_indexer_discovery_secret = CfnModulePropsParametersSplunkIndexerDiscoverySecret(**splunk_indexer_discovery_secret)
        if isinstance(splunk_indexer_disk_size, dict):
            splunk_indexer_disk_size = CfnModulePropsParametersSplunkIndexerDiskSize(**splunk_indexer_disk_size)
        if isinstance(splunk_license_bucket, dict):
            splunk_license_bucket = CfnModulePropsParametersSplunkLicenseBucket(**splunk_license_bucket)
        if isinstance(splunk_license_path, dict):
            splunk_license_path = CfnModulePropsParametersSplunkLicensePath(**splunk_license_path)
        if isinstance(splunk_replication_factor, dict):
            splunk_replication_factor = CfnModulePropsParametersSplunkReplicationFactor(**splunk_replication_factor)
        if isinstance(splunk_search_factor, dict):
            splunk_search_factor = CfnModulePropsParametersSplunkSearchFactor(**splunk_search_factor)
        if isinstance(splunk_search_head_disk_size, dict):
            splunk_search_head_disk_size = CfnModulePropsParametersSplunkSearchHeadDiskSize(**splunk_search_head_disk_size)
        if isinstance(ssh_client_location, dict):
            ssh_client_location = CfnModulePropsParametersSshClientLocation(**ssh_client_location)
        if isinstance(vpccidr, dict):
            vpccidr = CfnModulePropsParametersVpccidr(**vpccidr)
        if isinstance(web_client_location, dict):
            web_client_location = CfnModulePropsParametersWebClientLocation(**web_client_location)
        self._values: typing.Dict[str, typing.Any] = {}
        if availability_zones is not None:
            self._values["availability_zones"] = availability_zones
        if hec_client_location is not None:
            self._values["hec_client_location"] = hec_client_location
        if indexer_instance_type is not None:
            self._values["indexer_instance_type"] = indexer_instance_type
        if key_name is not None:
            self._values["key_name"] = key_name
        if number_of_a_zs is not None:
            self._values["number_of_a_zs"] = number_of_a_zs
        if public_subnet1_cidr is not None:
            self._values["public_subnet1_cidr"] = public_subnet1_cidr
        if public_subnet2_cidr is not None:
            self._values["public_subnet2_cidr"] = public_subnet2_cidr
        if public_subnet3_cidr is not None:
            self._values["public_subnet3_cidr"] = public_subnet3_cidr
        if search_head_instance_type is not None:
            self._values["search_head_instance_type"] = search_head_instance_type
        if shc_enabled is not None:
            self._values["shc_enabled"] = shc_enabled
        if smart_store_bucket_name is not None:
            self._values["smart_store_bucket_name"] = smart_store_bucket_name
        if splunk_admin_password is not None:
            self._values["splunk_admin_password"] = splunk_admin_password
        if splunk_cluster_secret is not None:
            self._values["splunk_cluster_secret"] = splunk_cluster_secret
        if splunk_indexer_count is not None:
            self._values["splunk_indexer_count"] = splunk_indexer_count
        if splunk_indexer_discovery_secret is not None:
            self._values["splunk_indexer_discovery_secret"] = splunk_indexer_discovery_secret
        if splunk_indexer_disk_size is not None:
            self._values["splunk_indexer_disk_size"] = splunk_indexer_disk_size
        if splunk_license_bucket is not None:
            self._values["splunk_license_bucket"] = splunk_license_bucket
        if splunk_license_path is not None:
            self._values["splunk_license_path"] = splunk_license_path
        if splunk_replication_factor is not None:
            self._values["splunk_replication_factor"] = splunk_replication_factor
        if splunk_search_factor is not None:
            self._values["splunk_search_factor"] = splunk_search_factor
        if splunk_search_head_disk_size is not None:
            self._values["splunk_search_head_disk_size"] = splunk_search_head_disk_size
        if ssh_client_location is not None:
            self._values["ssh_client_location"] = ssh_client_location
        if vpccidr is not None:
            self._values["vpccidr"] = vpccidr
        if web_client_location is not None:
            self._values["web_client_location"] = web_client_location

    @builtins.property
    def availability_zones(
        self,
    ) -> typing.Optional["CfnModulePropsParametersAvailabilityZones"]:
        '''
        :schema: CfnModulePropsParameters#AvailabilityZones
        '''
        result = self._values.get("availability_zones")
        return typing.cast(typing.Optional["CfnModulePropsParametersAvailabilityZones"], result)

    @builtins.property
    def hec_client_location(
        self,
    ) -> typing.Optional["CfnModulePropsParametersHecClientLocation"]:
        '''
        :schema: CfnModulePropsParameters#HECClientLocation
        '''
        result = self._values.get("hec_client_location")
        return typing.cast(typing.Optional["CfnModulePropsParametersHecClientLocation"], result)

    @builtins.property
    def indexer_instance_type(
        self,
    ) -> typing.Optional["CfnModulePropsParametersIndexerInstanceType"]:
        '''
        :schema: CfnModulePropsParameters#IndexerInstanceType
        '''
        result = self._values.get("indexer_instance_type")
        return typing.cast(typing.Optional["CfnModulePropsParametersIndexerInstanceType"], result)

    @builtins.property
    def key_name(self) -> typing.Optional["CfnModulePropsParametersKeyName"]:
        '''
        :schema: CfnModulePropsParameters#KeyName
        '''
        result = self._values.get("key_name")
        return typing.cast(typing.Optional["CfnModulePropsParametersKeyName"], result)

    @builtins.property
    def number_of_a_zs(self) -> typing.Optional["CfnModulePropsParametersNumberOfAZs"]:
        '''
        :schema: CfnModulePropsParameters#NumberOfAZs
        '''
        result = self._values.get("number_of_a_zs")
        return typing.cast(typing.Optional["CfnModulePropsParametersNumberOfAZs"], result)

    @builtins.property
    def public_subnet1_cidr(
        self,
    ) -> typing.Optional["CfnModulePropsParametersPublicSubnet1Cidr"]:
        '''
        :schema: CfnModulePropsParameters#PublicSubnet1CIDR
        '''
        result = self._values.get("public_subnet1_cidr")
        return typing.cast(typing.Optional["CfnModulePropsParametersPublicSubnet1Cidr"], result)

    @builtins.property
    def public_subnet2_cidr(
        self,
    ) -> typing.Optional["CfnModulePropsParametersPublicSubnet2Cidr"]:
        '''
        :schema: CfnModulePropsParameters#PublicSubnet2CIDR
        '''
        result = self._values.get("public_subnet2_cidr")
        return typing.cast(typing.Optional["CfnModulePropsParametersPublicSubnet2Cidr"], result)

    @builtins.property
    def public_subnet3_cidr(
        self,
    ) -> typing.Optional["CfnModulePropsParametersPublicSubnet3Cidr"]:
        '''
        :schema: CfnModulePropsParameters#PublicSubnet3CIDR
        '''
        result = self._values.get("public_subnet3_cidr")
        return typing.cast(typing.Optional["CfnModulePropsParametersPublicSubnet3Cidr"], result)

    @builtins.property
    def search_head_instance_type(
        self,
    ) -> typing.Optional["CfnModulePropsParametersSearchHeadInstanceType"]:
        '''
        :schema: CfnModulePropsParameters#SearchHeadInstanceType
        '''
        result = self._values.get("search_head_instance_type")
        return typing.cast(typing.Optional["CfnModulePropsParametersSearchHeadInstanceType"], result)

    @builtins.property
    def shc_enabled(self) -> typing.Optional["CfnModulePropsParametersShcEnabled"]:
        '''
        :schema: CfnModulePropsParameters#SHCEnabled
        '''
        result = self._values.get("shc_enabled")
        return typing.cast(typing.Optional["CfnModulePropsParametersShcEnabled"], result)

    @builtins.property
    def smart_store_bucket_name(
        self,
    ) -> typing.Optional["CfnModulePropsParametersSmartStoreBucketName"]:
        '''
        :schema: CfnModulePropsParameters#SmartStoreBucketName
        '''
        result = self._values.get("smart_store_bucket_name")
        return typing.cast(typing.Optional["CfnModulePropsParametersSmartStoreBucketName"], result)

    @builtins.property
    def splunk_admin_password(
        self,
    ) -> typing.Optional["CfnModulePropsParametersSplunkAdminPassword"]:
        '''
        :schema: CfnModulePropsParameters#SplunkAdminPassword
        '''
        result = self._values.get("splunk_admin_password")
        return typing.cast(typing.Optional["CfnModulePropsParametersSplunkAdminPassword"], result)

    @builtins.property
    def splunk_cluster_secret(
        self,
    ) -> typing.Optional["CfnModulePropsParametersSplunkClusterSecret"]:
        '''
        :schema: CfnModulePropsParameters#SplunkClusterSecret
        '''
        result = self._values.get("splunk_cluster_secret")
        return typing.cast(typing.Optional["CfnModulePropsParametersSplunkClusterSecret"], result)

    @builtins.property
    def splunk_indexer_count(
        self,
    ) -> typing.Optional["CfnModulePropsParametersSplunkIndexerCount"]:
        '''
        :schema: CfnModulePropsParameters#SplunkIndexerCount
        '''
        result = self._values.get("splunk_indexer_count")
        return typing.cast(typing.Optional["CfnModulePropsParametersSplunkIndexerCount"], result)

    @builtins.property
    def splunk_indexer_discovery_secret(
        self,
    ) -> typing.Optional["CfnModulePropsParametersSplunkIndexerDiscoverySecret"]:
        '''
        :schema: CfnModulePropsParameters#SplunkIndexerDiscoverySecret
        '''
        result = self._values.get("splunk_indexer_discovery_secret")
        return typing.cast(typing.Optional["CfnModulePropsParametersSplunkIndexerDiscoverySecret"], result)

    @builtins.property
    def splunk_indexer_disk_size(
        self,
    ) -> typing.Optional["CfnModulePropsParametersSplunkIndexerDiskSize"]:
        '''
        :schema: CfnModulePropsParameters#SplunkIndexerDiskSize
        '''
        result = self._values.get("splunk_indexer_disk_size")
        return typing.cast(typing.Optional["CfnModulePropsParametersSplunkIndexerDiskSize"], result)

    @builtins.property
    def splunk_license_bucket(
        self,
    ) -> typing.Optional["CfnModulePropsParametersSplunkLicenseBucket"]:
        '''
        :schema: CfnModulePropsParameters#SplunkLicenseBucket
        '''
        result = self._values.get("splunk_license_bucket")
        return typing.cast(typing.Optional["CfnModulePropsParametersSplunkLicenseBucket"], result)

    @builtins.property
    def splunk_license_path(
        self,
    ) -> typing.Optional["CfnModulePropsParametersSplunkLicensePath"]:
        '''
        :schema: CfnModulePropsParameters#SplunkLicensePath
        '''
        result = self._values.get("splunk_license_path")
        return typing.cast(typing.Optional["CfnModulePropsParametersSplunkLicensePath"], result)

    @builtins.property
    def splunk_replication_factor(
        self,
    ) -> typing.Optional["CfnModulePropsParametersSplunkReplicationFactor"]:
        '''
        :schema: CfnModulePropsParameters#SplunkReplicationFactor
        '''
        result = self._values.get("splunk_replication_factor")
        return typing.cast(typing.Optional["CfnModulePropsParametersSplunkReplicationFactor"], result)

    @builtins.property
    def splunk_search_factor(
        self,
    ) -> typing.Optional["CfnModulePropsParametersSplunkSearchFactor"]:
        '''
        :schema: CfnModulePropsParameters#SplunkSearchFactor
        '''
        result = self._values.get("splunk_search_factor")
        return typing.cast(typing.Optional["CfnModulePropsParametersSplunkSearchFactor"], result)

    @builtins.property
    def splunk_search_head_disk_size(
        self,
    ) -> typing.Optional["CfnModulePropsParametersSplunkSearchHeadDiskSize"]:
        '''
        :schema: CfnModulePropsParameters#SplunkSearchHeadDiskSize
        '''
        result = self._values.get("splunk_search_head_disk_size")
        return typing.cast(typing.Optional["CfnModulePropsParametersSplunkSearchHeadDiskSize"], result)

    @builtins.property
    def ssh_client_location(
        self,
    ) -> typing.Optional["CfnModulePropsParametersSshClientLocation"]:
        '''
        :schema: CfnModulePropsParameters#SSHClientLocation
        '''
        result = self._values.get("ssh_client_location")
        return typing.cast(typing.Optional["CfnModulePropsParametersSshClientLocation"], result)

    @builtins.property
    def vpccidr(self) -> typing.Optional["CfnModulePropsParametersVpccidr"]:
        '''
        :schema: CfnModulePropsParameters#VPCCIDR
        '''
        result = self._values.get("vpccidr")
        return typing.cast(typing.Optional["CfnModulePropsParametersVpccidr"], result)

    @builtins.property
    def web_client_location(
        self,
    ) -> typing.Optional["CfnModulePropsParametersWebClientLocation"]:
        '''
        :schema: CfnModulePropsParameters#WebClientLocation
        '''
        result = self._values.get("web_client_location")
        return typing.cast(typing.Optional["CfnModulePropsParametersWebClientLocation"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnModulePropsParametersAvailabilityZones",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnModulePropsParametersAvailabilityZones:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnModulePropsParametersAvailabilityZones
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersAvailabilityZones#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersAvailabilityZones(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnModulePropsParametersHecClientLocation",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnModulePropsParametersHecClientLocation:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnModulePropsParametersHecClientLocation
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersHecClientLocation#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersHecClientLocation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnModulePropsParametersIndexerInstanceType",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnModulePropsParametersIndexerInstanceType:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnModulePropsParametersIndexerInstanceType
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersIndexerInstanceType#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersIndexerInstanceType(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnModulePropsParametersKeyName",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnModulePropsParametersKeyName:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnModulePropsParametersKeyName
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersKeyName#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersKeyName(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnModulePropsParametersNumberOfAZs",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnModulePropsParametersNumberOfAZs:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnModulePropsParametersNumberOfAZs
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersNumberOfAZs#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersNumberOfAZs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnModulePropsParametersPublicSubnet1Cidr",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnModulePropsParametersPublicSubnet1Cidr:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnModulePropsParametersPublicSubnet1Cidr
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersPublicSubnet1Cidr#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersPublicSubnet1Cidr(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnModulePropsParametersPublicSubnet2Cidr",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnModulePropsParametersPublicSubnet2Cidr:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnModulePropsParametersPublicSubnet2Cidr
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersPublicSubnet2Cidr#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersPublicSubnet2Cidr(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnModulePropsParametersPublicSubnet3Cidr",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnModulePropsParametersPublicSubnet3Cidr:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnModulePropsParametersPublicSubnet3Cidr
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersPublicSubnet3Cidr#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersPublicSubnet3Cidr(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnModulePropsParametersSearchHeadInstanceType",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnModulePropsParametersSearchHeadInstanceType:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnModulePropsParametersSearchHeadInstanceType
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersSearchHeadInstanceType#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersSearchHeadInstanceType(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnModulePropsParametersShcEnabled",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnModulePropsParametersShcEnabled:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnModulePropsParametersShcEnabled
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersShcEnabled#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersShcEnabled(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnModulePropsParametersSmartStoreBucketName",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnModulePropsParametersSmartStoreBucketName:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnModulePropsParametersSmartStoreBucketName
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersSmartStoreBucketName#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersSmartStoreBucketName(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnModulePropsParametersSplunkAdminPassword",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnModulePropsParametersSplunkAdminPassword:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnModulePropsParametersSplunkAdminPassword
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersSplunkAdminPassword#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersSplunkAdminPassword(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnModulePropsParametersSplunkClusterSecret",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnModulePropsParametersSplunkClusterSecret:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnModulePropsParametersSplunkClusterSecret
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersSplunkClusterSecret#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersSplunkClusterSecret(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnModulePropsParametersSplunkIndexerCount",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnModulePropsParametersSplunkIndexerCount:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnModulePropsParametersSplunkIndexerCount
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersSplunkIndexerCount#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersSplunkIndexerCount(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnModulePropsParametersSplunkIndexerDiscoverySecret",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnModulePropsParametersSplunkIndexerDiscoverySecret:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnModulePropsParametersSplunkIndexerDiscoverySecret
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersSplunkIndexerDiscoverySecret#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersSplunkIndexerDiscoverySecret(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnModulePropsParametersSplunkIndexerDiskSize",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnModulePropsParametersSplunkIndexerDiskSize:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnModulePropsParametersSplunkIndexerDiskSize
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersSplunkIndexerDiskSize#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersSplunkIndexerDiskSize(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnModulePropsParametersSplunkLicenseBucket",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnModulePropsParametersSplunkLicenseBucket:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnModulePropsParametersSplunkLicenseBucket
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersSplunkLicenseBucket#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersSplunkLicenseBucket(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnModulePropsParametersSplunkLicensePath",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnModulePropsParametersSplunkLicensePath:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnModulePropsParametersSplunkLicensePath
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersSplunkLicensePath#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersSplunkLicensePath(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnModulePropsParametersSplunkReplicationFactor",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnModulePropsParametersSplunkReplicationFactor:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnModulePropsParametersSplunkReplicationFactor
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersSplunkReplicationFactor#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersSplunkReplicationFactor(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnModulePropsParametersSplunkSearchFactor",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnModulePropsParametersSplunkSearchFactor:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnModulePropsParametersSplunkSearchFactor
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersSplunkSearchFactor#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersSplunkSearchFactor(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnModulePropsParametersSplunkSearchHeadDiskSize",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnModulePropsParametersSplunkSearchHeadDiskSize:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnModulePropsParametersSplunkSearchHeadDiskSize
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersSplunkSearchHeadDiskSize#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersSplunkSearchHeadDiskSize(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnModulePropsParametersSshClientLocation",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnModulePropsParametersSshClientLocation:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnModulePropsParametersSshClientLocation
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersSshClientLocation#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersSshClientLocation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnModulePropsParametersVpccidr",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnModulePropsParametersVpccidr:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnModulePropsParametersVpccidr
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersVpccidr#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersVpccidr(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnModulePropsParametersWebClientLocation",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnModulePropsParametersWebClientLocation:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnModulePropsParametersWebClientLocation
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersWebClientLocation#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersWebClientLocation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnModulePropsResources",
    jsii_struct_bases=[],
    name_mapping={
        "bucket_policy": "bucketPolicy",
        "cfn_keys": "cfnKeys",
        "cfn_user": "cfnUser",
        "internet_gateway": "internetGateway",
        "public_subnet1": "publicSubnet1",
        "public_subnet1_route_table_association": "publicSubnet1RouteTableAssociation",
        "public_subnet2": "publicSubnet2",
        "public_subnet2_route_table_association": "publicSubnet2RouteTableAssociation",
        "public_subnet3": "publicSubnet3",
        "public_subnet3_route_table_association": "publicSubnet3RouteTableAssociation",
        "public_subnet_route": "publicSubnetRoute",
        "public_subnet_route_table": "publicSubnetRouteTable",
        "smart_store_s3_access_instance_profile": "smartStoreS3AccessInstanceProfile",
        "smart_store_s3_bucket_policy": "smartStoreS3BucketPolicy",
        "smart_store_s3_bucket_role": "smartStoreS3BucketRole",
        "splunk_cm": "splunkCm",
        "splunk_cm_wait_condition": "splunkCmWaitCondition",
        "splunk_cm_wait_handle": "splunkCmWaitHandle",
        "splunk_http_event_collector_load_balancer": "splunkHttpEventCollectorLoadBalancer",
        "splunk_http_event_collector_load_balancer_security_group": "splunkHttpEventCollectorLoadBalancerSecurityGroup",
        "splunk_indexer_launch_configuration": "splunkIndexerLaunchConfiguration",
        "splunk_indexer_nodes_asg": "splunkIndexerNodesAsg",
        "splunk_indexer_security_group": "splunkIndexerSecurityGroup",
        "splunk_search_head_instance": "splunkSearchHeadInstance",
        "splunk_search_head_security_group": "splunkSearchHeadSecurityGroup",
        "splunk_security_group": "splunkSecurityGroup",
        "splunk_shc_deployer": "splunkShcDeployer",
        "splunk_shc_load_balancer": "splunkShcLoadBalancer",
        "splunk_shc_member1": "splunkShcMember1",
        "splunk_shc_member2": "splunkShcMember2",
        "splunk_shc_member3": "splunkShcMember3",
        "splunk_smartstore_bucket": "splunkSmartstoreBucket",
        "vpc": "vpc",
        "vpc_gateway_attachment": "vpcGatewayAttachment",
    },
)
class CfnModulePropsResources:
    def __init__(
        self,
        *,
        bucket_policy: typing.Optional["CfnModulePropsResourcesBucketPolicy"] = None,
        cfn_keys: typing.Optional["CfnModulePropsResourcesCfnKeys"] = None,
        cfn_user: typing.Optional["CfnModulePropsResourcesCfnUser"] = None,
        internet_gateway: typing.Optional["CfnModulePropsResourcesInternetGateway"] = None,
        public_subnet1: typing.Optional["CfnModulePropsResourcesPublicSubnet1"] = None,
        public_subnet1_route_table_association: typing.Optional["CfnModulePropsResourcesPublicSubnet1RouteTableAssociation"] = None,
        public_subnet2: typing.Optional["CfnModulePropsResourcesPublicSubnet2"] = None,
        public_subnet2_route_table_association: typing.Optional["CfnModulePropsResourcesPublicSubnet2RouteTableAssociation"] = None,
        public_subnet3: typing.Optional["CfnModulePropsResourcesPublicSubnet3"] = None,
        public_subnet3_route_table_association: typing.Optional["CfnModulePropsResourcesPublicSubnet3RouteTableAssociation"] = None,
        public_subnet_route: typing.Optional["CfnModulePropsResourcesPublicSubnetRoute"] = None,
        public_subnet_route_table: typing.Optional["CfnModulePropsResourcesPublicSubnetRouteTable"] = None,
        smart_store_s3_access_instance_profile: typing.Optional["CfnModulePropsResourcesSmartStoreS3AccessInstanceProfile"] = None,
        smart_store_s3_bucket_policy: typing.Optional["CfnModulePropsResourcesSmartStoreS3BucketPolicy"] = None,
        smart_store_s3_bucket_role: typing.Optional["CfnModulePropsResourcesSmartStoreS3BucketRole"] = None,
        splunk_cm: typing.Optional["CfnModulePropsResourcesSplunkCm"] = None,
        splunk_cm_wait_condition: typing.Optional["CfnModulePropsResourcesSplunkCmWaitCondition"] = None,
        splunk_cm_wait_handle: typing.Optional["CfnModulePropsResourcesSplunkCmWaitHandle"] = None,
        splunk_http_event_collector_load_balancer: typing.Optional["CfnModulePropsResourcesSplunkHttpEventCollectorLoadBalancer"] = None,
        splunk_http_event_collector_load_balancer_security_group: typing.Optional["CfnModulePropsResourcesSplunkHttpEventCollectorLoadBalancerSecurityGroup"] = None,
        splunk_indexer_launch_configuration: typing.Optional["CfnModulePropsResourcesSplunkIndexerLaunchConfiguration"] = None,
        splunk_indexer_nodes_asg: typing.Optional["CfnModulePropsResourcesSplunkIndexerNodesAsg"] = None,
        splunk_indexer_security_group: typing.Optional["CfnModulePropsResourcesSplunkIndexerSecurityGroup"] = None,
        splunk_search_head_instance: typing.Optional["CfnModulePropsResourcesSplunkSearchHeadInstance"] = None,
        splunk_search_head_security_group: typing.Optional["CfnModulePropsResourcesSplunkSearchHeadSecurityGroup"] = None,
        splunk_security_group: typing.Optional["CfnModulePropsResourcesSplunkSecurityGroup"] = None,
        splunk_shc_deployer: typing.Optional["CfnModulePropsResourcesSplunkShcDeployer"] = None,
        splunk_shc_load_balancer: typing.Optional["CfnModulePropsResourcesSplunkShcLoadBalancer"] = None,
        splunk_shc_member1: typing.Optional["CfnModulePropsResourcesSplunkShcMember1"] = None,
        splunk_shc_member2: typing.Optional["CfnModulePropsResourcesSplunkShcMember2"] = None,
        splunk_shc_member3: typing.Optional["CfnModulePropsResourcesSplunkShcMember3"] = None,
        splunk_smartstore_bucket: typing.Optional["CfnModulePropsResourcesSplunkSmartstoreBucket"] = None,
        vpc: typing.Optional["CfnModulePropsResourcesVpc"] = None,
        vpc_gateway_attachment: typing.Optional["CfnModulePropsResourcesVpcGatewayAttachment"] = None,
    ) -> None:
        '''
        :param bucket_policy: 
        :param cfn_keys: 
        :param cfn_user: 
        :param internet_gateway: 
        :param public_subnet1: 
        :param public_subnet1_route_table_association: 
        :param public_subnet2: 
        :param public_subnet2_route_table_association: 
        :param public_subnet3: 
        :param public_subnet3_route_table_association: 
        :param public_subnet_route: 
        :param public_subnet_route_table: 
        :param smart_store_s3_access_instance_profile: 
        :param smart_store_s3_bucket_policy: 
        :param smart_store_s3_bucket_role: 
        :param splunk_cm: 
        :param splunk_cm_wait_condition: 
        :param splunk_cm_wait_handle: 
        :param splunk_http_event_collector_load_balancer: 
        :param splunk_http_event_collector_load_balancer_security_group: 
        :param splunk_indexer_launch_configuration: 
        :param splunk_indexer_nodes_asg: 
        :param splunk_indexer_security_group: 
        :param splunk_search_head_instance: 
        :param splunk_search_head_security_group: 
        :param splunk_security_group: 
        :param splunk_shc_deployer: 
        :param splunk_shc_load_balancer: 
        :param splunk_shc_member1: 
        :param splunk_shc_member2: 
        :param splunk_shc_member3: 
        :param splunk_smartstore_bucket: 
        :param vpc: 
        :param vpc_gateway_attachment: 

        :schema: CfnModulePropsResources
        '''
        if isinstance(bucket_policy, dict):
            bucket_policy = CfnModulePropsResourcesBucketPolicy(**bucket_policy)
        if isinstance(cfn_keys, dict):
            cfn_keys = CfnModulePropsResourcesCfnKeys(**cfn_keys)
        if isinstance(cfn_user, dict):
            cfn_user = CfnModulePropsResourcesCfnUser(**cfn_user)
        if isinstance(internet_gateway, dict):
            internet_gateway = CfnModulePropsResourcesInternetGateway(**internet_gateway)
        if isinstance(public_subnet1, dict):
            public_subnet1 = CfnModulePropsResourcesPublicSubnet1(**public_subnet1)
        if isinstance(public_subnet1_route_table_association, dict):
            public_subnet1_route_table_association = CfnModulePropsResourcesPublicSubnet1RouteTableAssociation(**public_subnet1_route_table_association)
        if isinstance(public_subnet2, dict):
            public_subnet2 = CfnModulePropsResourcesPublicSubnet2(**public_subnet2)
        if isinstance(public_subnet2_route_table_association, dict):
            public_subnet2_route_table_association = CfnModulePropsResourcesPublicSubnet2RouteTableAssociation(**public_subnet2_route_table_association)
        if isinstance(public_subnet3, dict):
            public_subnet3 = CfnModulePropsResourcesPublicSubnet3(**public_subnet3)
        if isinstance(public_subnet3_route_table_association, dict):
            public_subnet3_route_table_association = CfnModulePropsResourcesPublicSubnet3RouteTableAssociation(**public_subnet3_route_table_association)
        if isinstance(public_subnet_route, dict):
            public_subnet_route = CfnModulePropsResourcesPublicSubnetRoute(**public_subnet_route)
        if isinstance(public_subnet_route_table, dict):
            public_subnet_route_table = CfnModulePropsResourcesPublicSubnetRouteTable(**public_subnet_route_table)
        if isinstance(smart_store_s3_access_instance_profile, dict):
            smart_store_s3_access_instance_profile = CfnModulePropsResourcesSmartStoreS3AccessInstanceProfile(**smart_store_s3_access_instance_profile)
        if isinstance(smart_store_s3_bucket_policy, dict):
            smart_store_s3_bucket_policy = CfnModulePropsResourcesSmartStoreS3BucketPolicy(**smart_store_s3_bucket_policy)
        if isinstance(smart_store_s3_bucket_role, dict):
            smart_store_s3_bucket_role = CfnModulePropsResourcesSmartStoreS3BucketRole(**smart_store_s3_bucket_role)
        if isinstance(splunk_cm, dict):
            splunk_cm = CfnModulePropsResourcesSplunkCm(**splunk_cm)
        if isinstance(splunk_cm_wait_condition, dict):
            splunk_cm_wait_condition = CfnModulePropsResourcesSplunkCmWaitCondition(**splunk_cm_wait_condition)
        if isinstance(splunk_cm_wait_handle, dict):
            splunk_cm_wait_handle = CfnModulePropsResourcesSplunkCmWaitHandle(**splunk_cm_wait_handle)
        if isinstance(splunk_http_event_collector_load_balancer, dict):
            splunk_http_event_collector_load_balancer = CfnModulePropsResourcesSplunkHttpEventCollectorLoadBalancer(**splunk_http_event_collector_load_balancer)
        if isinstance(splunk_http_event_collector_load_balancer_security_group, dict):
            splunk_http_event_collector_load_balancer_security_group = CfnModulePropsResourcesSplunkHttpEventCollectorLoadBalancerSecurityGroup(**splunk_http_event_collector_load_balancer_security_group)
        if isinstance(splunk_indexer_launch_configuration, dict):
            splunk_indexer_launch_configuration = CfnModulePropsResourcesSplunkIndexerLaunchConfiguration(**splunk_indexer_launch_configuration)
        if isinstance(splunk_indexer_nodes_asg, dict):
            splunk_indexer_nodes_asg = CfnModulePropsResourcesSplunkIndexerNodesAsg(**splunk_indexer_nodes_asg)
        if isinstance(splunk_indexer_security_group, dict):
            splunk_indexer_security_group = CfnModulePropsResourcesSplunkIndexerSecurityGroup(**splunk_indexer_security_group)
        if isinstance(splunk_search_head_instance, dict):
            splunk_search_head_instance = CfnModulePropsResourcesSplunkSearchHeadInstance(**splunk_search_head_instance)
        if isinstance(splunk_search_head_security_group, dict):
            splunk_search_head_security_group = CfnModulePropsResourcesSplunkSearchHeadSecurityGroup(**splunk_search_head_security_group)
        if isinstance(splunk_security_group, dict):
            splunk_security_group = CfnModulePropsResourcesSplunkSecurityGroup(**splunk_security_group)
        if isinstance(splunk_shc_deployer, dict):
            splunk_shc_deployer = CfnModulePropsResourcesSplunkShcDeployer(**splunk_shc_deployer)
        if isinstance(splunk_shc_load_balancer, dict):
            splunk_shc_load_balancer = CfnModulePropsResourcesSplunkShcLoadBalancer(**splunk_shc_load_balancer)
        if isinstance(splunk_shc_member1, dict):
            splunk_shc_member1 = CfnModulePropsResourcesSplunkShcMember1(**splunk_shc_member1)
        if isinstance(splunk_shc_member2, dict):
            splunk_shc_member2 = CfnModulePropsResourcesSplunkShcMember2(**splunk_shc_member2)
        if isinstance(splunk_shc_member3, dict):
            splunk_shc_member3 = CfnModulePropsResourcesSplunkShcMember3(**splunk_shc_member3)
        if isinstance(splunk_smartstore_bucket, dict):
            splunk_smartstore_bucket = CfnModulePropsResourcesSplunkSmartstoreBucket(**splunk_smartstore_bucket)
        if isinstance(vpc, dict):
            vpc = CfnModulePropsResourcesVpc(**vpc)
        if isinstance(vpc_gateway_attachment, dict):
            vpc_gateway_attachment = CfnModulePropsResourcesVpcGatewayAttachment(**vpc_gateway_attachment)
        self._values: typing.Dict[str, typing.Any] = {}
        if bucket_policy is not None:
            self._values["bucket_policy"] = bucket_policy
        if cfn_keys is not None:
            self._values["cfn_keys"] = cfn_keys
        if cfn_user is not None:
            self._values["cfn_user"] = cfn_user
        if internet_gateway is not None:
            self._values["internet_gateway"] = internet_gateway
        if public_subnet1 is not None:
            self._values["public_subnet1"] = public_subnet1
        if public_subnet1_route_table_association is not None:
            self._values["public_subnet1_route_table_association"] = public_subnet1_route_table_association
        if public_subnet2 is not None:
            self._values["public_subnet2"] = public_subnet2
        if public_subnet2_route_table_association is not None:
            self._values["public_subnet2_route_table_association"] = public_subnet2_route_table_association
        if public_subnet3 is not None:
            self._values["public_subnet3"] = public_subnet3
        if public_subnet3_route_table_association is not None:
            self._values["public_subnet3_route_table_association"] = public_subnet3_route_table_association
        if public_subnet_route is not None:
            self._values["public_subnet_route"] = public_subnet_route
        if public_subnet_route_table is not None:
            self._values["public_subnet_route_table"] = public_subnet_route_table
        if smart_store_s3_access_instance_profile is not None:
            self._values["smart_store_s3_access_instance_profile"] = smart_store_s3_access_instance_profile
        if smart_store_s3_bucket_policy is not None:
            self._values["smart_store_s3_bucket_policy"] = smart_store_s3_bucket_policy
        if smart_store_s3_bucket_role is not None:
            self._values["smart_store_s3_bucket_role"] = smart_store_s3_bucket_role
        if splunk_cm is not None:
            self._values["splunk_cm"] = splunk_cm
        if splunk_cm_wait_condition is not None:
            self._values["splunk_cm_wait_condition"] = splunk_cm_wait_condition
        if splunk_cm_wait_handle is not None:
            self._values["splunk_cm_wait_handle"] = splunk_cm_wait_handle
        if splunk_http_event_collector_load_balancer is not None:
            self._values["splunk_http_event_collector_load_balancer"] = splunk_http_event_collector_load_balancer
        if splunk_http_event_collector_load_balancer_security_group is not None:
            self._values["splunk_http_event_collector_load_balancer_security_group"] = splunk_http_event_collector_load_balancer_security_group
        if splunk_indexer_launch_configuration is not None:
            self._values["splunk_indexer_launch_configuration"] = splunk_indexer_launch_configuration
        if splunk_indexer_nodes_asg is not None:
            self._values["splunk_indexer_nodes_asg"] = splunk_indexer_nodes_asg
        if splunk_indexer_security_group is not None:
            self._values["splunk_indexer_security_group"] = splunk_indexer_security_group
        if splunk_search_head_instance is not None:
            self._values["splunk_search_head_instance"] = splunk_search_head_instance
        if splunk_search_head_security_group is not None:
            self._values["splunk_search_head_security_group"] = splunk_search_head_security_group
        if splunk_security_group is not None:
            self._values["splunk_security_group"] = splunk_security_group
        if splunk_shc_deployer is not None:
            self._values["splunk_shc_deployer"] = splunk_shc_deployer
        if splunk_shc_load_balancer is not None:
            self._values["splunk_shc_load_balancer"] = splunk_shc_load_balancer
        if splunk_shc_member1 is not None:
            self._values["splunk_shc_member1"] = splunk_shc_member1
        if splunk_shc_member2 is not None:
            self._values["splunk_shc_member2"] = splunk_shc_member2
        if splunk_shc_member3 is not None:
            self._values["splunk_shc_member3"] = splunk_shc_member3
        if splunk_smartstore_bucket is not None:
            self._values["splunk_smartstore_bucket"] = splunk_smartstore_bucket
        if vpc is not None:
            self._values["vpc"] = vpc
        if vpc_gateway_attachment is not None:
            self._values["vpc_gateway_attachment"] = vpc_gateway_attachment

    @builtins.property
    def bucket_policy(self) -> typing.Optional["CfnModulePropsResourcesBucketPolicy"]:
        '''
        :schema: CfnModulePropsResources#BucketPolicy
        '''
        result = self._values.get("bucket_policy")
        return typing.cast(typing.Optional["CfnModulePropsResourcesBucketPolicy"], result)

    @builtins.property
    def cfn_keys(self) -> typing.Optional["CfnModulePropsResourcesCfnKeys"]:
        '''
        :schema: CfnModulePropsResources#CfnKeys
        '''
        result = self._values.get("cfn_keys")
        return typing.cast(typing.Optional["CfnModulePropsResourcesCfnKeys"], result)

    @builtins.property
    def cfn_user(self) -> typing.Optional["CfnModulePropsResourcesCfnUser"]:
        '''
        :schema: CfnModulePropsResources#CfnUser
        '''
        result = self._values.get("cfn_user")
        return typing.cast(typing.Optional["CfnModulePropsResourcesCfnUser"], result)

    @builtins.property
    def internet_gateway(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesInternetGateway"]:
        '''
        :schema: CfnModulePropsResources#InternetGateway
        '''
        result = self._values.get("internet_gateway")
        return typing.cast(typing.Optional["CfnModulePropsResourcesInternetGateway"], result)

    @builtins.property
    def public_subnet1(self) -> typing.Optional["CfnModulePropsResourcesPublicSubnet1"]:
        '''
        :schema: CfnModulePropsResources#PublicSubnet1
        '''
        result = self._values.get("public_subnet1")
        return typing.cast(typing.Optional["CfnModulePropsResourcesPublicSubnet1"], result)

    @builtins.property
    def public_subnet1_route_table_association(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesPublicSubnet1RouteTableAssociation"]:
        '''
        :schema: CfnModulePropsResources#PublicSubnet1RouteTableAssociation
        '''
        result = self._values.get("public_subnet1_route_table_association")
        return typing.cast(typing.Optional["CfnModulePropsResourcesPublicSubnet1RouteTableAssociation"], result)

    @builtins.property
    def public_subnet2(self) -> typing.Optional["CfnModulePropsResourcesPublicSubnet2"]:
        '''
        :schema: CfnModulePropsResources#PublicSubnet2
        '''
        result = self._values.get("public_subnet2")
        return typing.cast(typing.Optional["CfnModulePropsResourcesPublicSubnet2"], result)

    @builtins.property
    def public_subnet2_route_table_association(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesPublicSubnet2RouteTableAssociation"]:
        '''
        :schema: CfnModulePropsResources#PublicSubnet2RouteTableAssociation
        '''
        result = self._values.get("public_subnet2_route_table_association")
        return typing.cast(typing.Optional["CfnModulePropsResourcesPublicSubnet2RouteTableAssociation"], result)

    @builtins.property
    def public_subnet3(self) -> typing.Optional["CfnModulePropsResourcesPublicSubnet3"]:
        '''
        :schema: CfnModulePropsResources#PublicSubnet3
        '''
        result = self._values.get("public_subnet3")
        return typing.cast(typing.Optional["CfnModulePropsResourcesPublicSubnet3"], result)

    @builtins.property
    def public_subnet3_route_table_association(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesPublicSubnet3RouteTableAssociation"]:
        '''
        :schema: CfnModulePropsResources#PublicSubnet3RouteTableAssociation
        '''
        result = self._values.get("public_subnet3_route_table_association")
        return typing.cast(typing.Optional["CfnModulePropsResourcesPublicSubnet3RouteTableAssociation"], result)

    @builtins.property
    def public_subnet_route(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesPublicSubnetRoute"]:
        '''
        :schema: CfnModulePropsResources#PublicSubnetRoute
        '''
        result = self._values.get("public_subnet_route")
        return typing.cast(typing.Optional["CfnModulePropsResourcesPublicSubnetRoute"], result)

    @builtins.property
    def public_subnet_route_table(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesPublicSubnetRouteTable"]:
        '''
        :schema: CfnModulePropsResources#PublicSubnetRouteTable
        '''
        result = self._values.get("public_subnet_route_table")
        return typing.cast(typing.Optional["CfnModulePropsResourcesPublicSubnetRouteTable"], result)

    @builtins.property
    def smart_store_s3_access_instance_profile(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesSmartStoreS3AccessInstanceProfile"]:
        '''
        :schema: CfnModulePropsResources#SmartStoreS3AccessInstanceProfile
        '''
        result = self._values.get("smart_store_s3_access_instance_profile")
        return typing.cast(typing.Optional["CfnModulePropsResourcesSmartStoreS3AccessInstanceProfile"], result)

    @builtins.property
    def smart_store_s3_bucket_policy(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesSmartStoreS3BucketPolicy"]:
        '''
        :schema: CfnModulePropsResources#SmartStoreS3BucketPolicy
        '''
        result = self._values.get("smart_store_s3_bucket_policy")
        return typing.cast(typing.Optional["CfnModulePropsResourcesSmartStoreS3BucketPolicy"], result)

    @builtins.property
    def smart_store_s3_bucket_role(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesSmartStoreS3BucketRole"]:
        '''
        :schema: CfnModulePropsResources#SmartStoreS3BucketRole
        '''
        result = self._values.get("smart_store_s3_bucket_role")
        return typing.cast(typing.Optional["CfnModulePropsResourcesSmartStoreS3BucketRole"], result)

    @builtins.property
    def splunk_cm(self) -> typing.Optional["CfnModulePropsResourcesSplunkCm"]:
        '''
        :schema: CfnModulePropsResources#SplunkCM
        '''
        result = self._values.get("splunk_cm")
        return typing.cast(typing.Optional["CfnModulePropsResourcesSplunkCm"], result)

    @builtins.property
    def splunk_cm_wait_condition(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesSplunkCmWaitCondition"]:
        '''
        :schema: CfnModulePropsResources#SplunkCMWaitCondition
        '''
        result = self._values.get("splunk_cm_wait_condition")
        return typing.cast(typing.Optional["CfnModulePropsResourcesSplunkCmWaitCondition"], result)

    @builtins.property
    def splunk_cm_wait_handle(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesSplunkCmWaitHandle"]:
        '''
        :schema: CfnModulePropsResources#SplunkCMWaitHandle
        '''
        result = self._values.get("splunk_cm_wait_handle")
        return typing.cast(typing.Optional["CfnModulePropsResourcesSplunkCmWaitHandle"], result)

    @builtins.property
    def splunk_http_event_collector_load_balancer(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesSplunkHttpEventCollectorLoadBalancer"]:
        '''
        :schema: CfnModulePropsResources#SplunkHttpEventCollectorLoadBalancer
        '''
        result = self._values.get("splunk_http_event_collector_load_balancer")
        return typing.cast(typing.Optional["CfnModulePropsResourcesSplunkHttpEventCollectorLoadBalancer"], result)

    @builtins.property
    def splunk_http_event_collector_load_balancer_security_group(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesSplunkHttpEventCollectorLoadBalancerSecurityGroup"]:
        '''
        :schema: CfnModulePropsResources#SplunkHttpEventCollectorLoadBalancerSecurityGroup
        '''
        result = self._values.get("splunk_http_event_collector_load_balancer_security_group")
        return typing.cast(typing.Optional["CfnModulePropsResourcesSplunkHttpEventCollectorLoadBalancerSecurityGroup"], result)

    @builtins.property
    def splunk_indexer_launch_configuration(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesSplunkIndexerLaunchConfiguration"]:
        '''
        :schema: CfnModulePropsResources#SplunkIndexerLaunchConfiguration
        '''
        result = self._values.get("splunk_indexer_launch_configuration")
        return typing.cast(typing.Optional["CfnModulePropsResourcesSplunkIndexerLaunchConfiguration"], result)

    @builtins.property
    def splunk_indexer_nodes_asg(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesSplunkIndexerNodesAsg"]:
        '''
        :schema: CfnModulePropsResources#SplunkIndexerNodesASG
        '''
        result = self._values.get("splunk_indexer_nodes_asg")
        return typing.cast(typing.Optional["CfnModulePropsResourcesSplunkIndexerNodesAsg"], result)

    @builtins.property
    def splunk_indexer_security_group(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesSplunkIndexerSecurityGroup"]:
        '''
        :schema: CfnModulePropsResources#SplunkIndexerSecurityGroup
        '''
        result = self._values.get("splunk_indexer_security_group")
        return typing.cast(typing.Optional["CfnModulePropsResourcesSplunkIndexerSecurityGroup"], result)

    @builtins.property
    def splunk_search_head_instance(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesSplunkSearchHeadInstance"]:
        '''
        :schema: CfnModulePropsResources#SplunkSearchHeadInstance
        '''
        result = self._values.get("splunk_search_head_instance")
        return typing.cast(typing.Optional["CfnModulePropsResourcesSplunkSearchHeadInstance"], result)

    @builtins.property
    def splunk_search_head_security_group(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesSplunkSearchHeadSecurityGroup"]:
        '''
        :schema: CfnModulePropsResources#SplunkSearchHeadSecurityGroup
        '''
        result = self._values.get("splunk_search_head_security_group")
        return typing.cast(typing.Optional["CfnModulePropsResourcesSplunkSearchHeadSecurityGroup"], result)

    @builtins.property
    def splunk_security_group(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesSplunkSecurityGroup"]:
        '''
        :schema: CfnModulePropsResources#SplunkSecurityGroup
        '''
        result = self._values.get("splunk_security_group")
        return typing.cast(typing.Optional["CfnModulePropsResourcesSplunkSecurityGroup"], result)

    @builtins.property
    def splunk_shc_deployer(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesSplunkShcDeployer"]:
        '''
        :schema: CfnModulePropsResources#SplunkSHCDeployer
        '''
        result = self._values.get("splunk_shc_deployer")
        return typing.cast(typing.Optional["CfnModulePropsResourcesSplunkShcDeployer"], result)

    @builtins.property
    def splunk_shc_load_balancer(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesSplunkShcLoadBalancer"]:
        '''
        :schema: CfnModulePropsResources#SplunkSHCLoadBalancer
        '''
        result = self._values.get("splunk_shc_load_balancer")
        return typing.cast(typing.Optional["CfnModulePropsResourcesSplunkShcLoadBalancer"], result)

    @builtins.property
    def splunk_shc_member1(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesSplunkShcMember1"]:
        '''
        :schema: CfnModulePropsResources#SplunkSHCMember1
        '''
        result = self._values.get("splunk_shc_member1")
        return typing.cast(typing.Optional["CfnModulePropsResourcesSplunkShcMember1"], result)

    @builtins.property
    def splunk_shc_member2(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesSplunkShcMember2"]:
        '''
        :schema: CfnModulePropsResources#SplunkSHCMember2
        '''
        result = self._values.get("splunk_shc_member2")
        return typing.cast(typing.Optional["CfnModulePropsResourcesSplunkShcMember2"], result)

    @builtins.property
    def splunk_shc_member3(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesSplunkShcMember3"]:
        '''
        :schema: CfnModulePropsResources#SplunkSHCMember3
        '''
        result = self._values.get("splunk_shc_member3")
        return typing.cast(typing.Optional["CfnModulePropsResourcesSplunkShcMember3"], result)

    @builtins.property
    def splunk_smartstore_bucket(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesSplunkSmartstoreBucket"]:
        '''
        :schema: CfnModulePropsResources#SplunkSmartstoreBucket
        '''
        result = self._values.get("splunk_smartstore_bucket")
        return typing.cast(typing.Optional["CfnModulePropsResourcesSplunkSmartstoreBucket"], result)

    @builtins.property
    def vpc(self) -> typing.Optional["CfnModulePropsResourcesVpc"]:
        '''
        :schema: CfnModulePropsResources#VPC
        '''
        result = self._values.get("vpc")
        return typing.cast(typing.Optional["CfnModulePropsResourcesVpc"], result)

    @builtins.property
    def vpc_gateway_attachment(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesVpcGatewayAttachment"]:
        '''
        :schema: CfnModulePropsResources#VPCGatewayAttachment
        '''
        result = self._values.get("vpc_gateway_attachment")
        return typing.cast(typing.Optional["CfnModulePropsResourcesVpcGatewayAttachment"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResources(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnModulePropsResourcesBucketPolicy",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesBucketPolicy:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesBucketPolicy
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesBucketPolicy#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesBucketPolicy#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesBucketPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnModulePropsResourcesCfnKeys",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesCfnKeys:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesCfnKeys
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesCfnKeys#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesCfnKeys#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesCfnKeys(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnModulePropsResourcesCfnUser",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesCfnUser:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesCfnUser
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesCfnUser#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesCfnUser#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesCfnUser(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnModulePropsResourcesInternetGateway",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesInternetGateway:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesInternetGateway
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesInternetGateway#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesInternetGateway#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesInternetGateway(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnModulePropsResourcesPublicSubnet1",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesPublicSubnet1:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesPublicSubnet1
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesPublicSubnet1#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesPublicSubnet1#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesPublicSubnet1(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnModulePropsResourcesPublicSubnet1RouteTableAssociation",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesPublicSubnet1RouteTableAssociation:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesPublicSubnet1RouteTableAssociation
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesPublicSubnet1RouteTableAssociation#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesPublicSubnet1RouteTableAssociation#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesPublicSubnet1RouteTableAssociation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnModulePropsResourcesPublicSubnet2",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesPublicSubnet2:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesPublicSubnet2
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesPublicSubnet2#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesPublicSubnet2#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesPublicSubnet2(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnModulePropsResourcesPublicSubnet2RouteTableAssociation",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesPublicSubnet2RouteTableAssociation:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesPublicSubnet2RouteTableAssociation
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesPublicSubnet2RouteTableAssociation#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesPublicSubnet2RouteTableAssociation#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesPublicSubnet2RouteTableAssociation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnModulePropsResourcesPublicSubnet3",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesPublicSubnet3:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesPublicSubnet3
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesPublicSubnet3#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesPublicSubnet3#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesPublicSubnet3(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnModulePropsResourcesPublicSubnet3RouteTableAssociation",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesPublicSubnet3RouteTableAssociation:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesPublicSubnet3RouteTableAssociation
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesPublicSubnet3RouteTableAssociation#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesPublicSubnet3RouteTableAssociation#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesPublicSubnet3RouteTableAssociation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnModulePropsResourcesPublicSubnetRoute",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesPublicSubnetRoute:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesPublicSubnetRoute
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesPublicSubnetRoute#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesPublicSubnetRoute#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesPublicSubnetRoute(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnModulePropsResourcesPublicSubnetRouteTable",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesPublicSubnetRouteTable:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesPublicSubnetRouteTable
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesPublicSubnetRouteTable#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesPublicSubnetRouteTable#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesPublicSubnetRouteTable(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnModulePropsResourcesSmartStoreS3AccessInstanceProfile",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesSmartStoreS3AccessInstanceProfile:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesSmartStoreS3AccessInstanceProfile
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesSmartStoreS3AccessInstanceProfile#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesSmartStoreS3AccessInstanceProfile#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesSmartStoreS3AccessInstanceProfile(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnModulePropsResourcesSmartStoreS3BucketPolicy",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesSmartStoreS3BucketPolicy:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesSmartStoreS3BucketPolicy
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesSmartStoreS3BucketPolicy#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesSmartStoreS3BucketPolicy#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesSmartStoreS3BucketPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnModulePropsResourcesSmartStoreS3BucketRole",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesSmartStoreS3BucketRole:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesSmartStoreS3BucketRole
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesSmartStoreS3BucketRole#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesSmartStoreS3BucketRole#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesSmartStoreS3BucketRole(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnModulePropsResourcesSplunkCm",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesSplunkCm:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesSplunkCm
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesSplunkCm#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesSplunkCm#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesSplunkCm(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnModulePropsResourcesSplunkCmWaitCondition",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesSplunkCmWaitCondition:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesSplunkCmWaitCondition
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesSplunkCmWaitCondition#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesSplunkCmWaitCondition#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesSplunkCmWaitCondition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnModulePropsResourcesSplunkCmWaitHandle",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesSplunkCmWaitHandle:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesSplunkCmWaitHandle
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesSplunkCmWaitHandle#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesSplunkCmWaitHandle#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesSplunkCmWaitHandle(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnModulePropsResourcesSplunkHttpEventCollectorLoadBalancer",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesSplunkHttpEventCollectorLoadBalancer:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesSplunkHttpEventCollectorLoadBalancer
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesSplunkHttpEventCollectorLoadBalancer#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesSplunkHttpEventCollectorLoadBalancer#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesSplunkHttpEventCollectorLoadBalancer(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnModulePropsResourcesSplunkHttpEventCollectorLoadBalancerSecurityGroup",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesSplunkHttpEventCollectorLoadBalancerSecurityGroup:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesSplunkHttpEventCollectorLoadBalancerSecurityGroup
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesSplunkHttpEventCollectorLoadBalancerSecurityGroup#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesSplunkHttpEventCollectorLoadBalancerSecurityGroup#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesSplunkHttpEventCollectorLoadBalancerSecurityGroup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnModulePropsResourcesSplunkIndexerLaunchConfiguration",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesSplunkIndexerLaunchConfiguration:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesSplunkIndexerLaunchConfiguration
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesSplunkIndexerLaunchConfiguration#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesSplunkIndexerLaunchConfiguration#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesSplunkIndexerLaunchConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnModulePropsResourcesSplunkIndexerNodesAsg",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesSplunkIndexerNodesAsg:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesSplunkIndexerNodesAsg
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesSplunkIndexerNodesAsg#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesSplunkIndexerNodesAsg#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesSplunkIndexerNodesAsg(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnModulePropsResourcesSplunkIndexerSecurityGroup",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesSplunkIndexerSecurityGroup:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesSplunkIndexerSecurityGroup
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesSplunkIndexerSecurityGroup#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesSplunkIndexerSecurityGroup#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesSplunkIndexerSecurityGroup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnModulePropsResourcesSplunkSearchHeadInstance",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesSplunkSearchHeadInstance:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesSplunkSearchHeadInstance
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesSplunkSearchHeadInstance#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesSplunkSearchHeadInstance#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesSplunkSearchHeadInstance(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnModulePropsResourcesSplunkSearchHeadSecurityGroup",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesSplunkSearchHeadSecurityGroup:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesSplunkSearchHeadSecurityGroup
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesSplunkSearchHeadSecurityGroup#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesSplunkSearchHeadSecurityGroup#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesSplunkSearchHeadSecurityGroup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnModulePropsResourcesSplunkSecurityGroup",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesSplunkSecurityGroup:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesSplunkSecurityGroup
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesSplunkSecurityGroup#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesSplunkSecurityGroup#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesSplunkSecurityGroup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnModulePropsResourcesSplunkShcDeployer",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesSplunkShcDeployer:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesSplunkShcDeployer
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesSplunkShcDeployer#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesSplunkShcDeployer#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesSplunkShcDeployer(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnModulePropsResourcesSplunkShcLoadBalancer",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesSplunkShcLoadBalancer:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesSplunkShcLoadBalancer
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesSplunkShcLoadBalancer#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesSplunkShcLoadBalancer#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesSplunkShcLoadBalancer(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnModulePropsResourcesSplunkShcMember1",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesSplunkShcMember1:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesSplunkShcMember1
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesSplunkShcMember1#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesSplunkShcMember1#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesSplunkShcMember1(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnModulePropsResourcesSplunkShcMember2",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesSplunkShcMember2:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesSplunkShcMember2
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesSplunkShcMember2#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesSplunkShcMember2#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesSplunkShcMember2(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnModulePropsResourcesSplunkShcMember3",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesSplunkShcMember3:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesSplunkShcMember3
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesSplunkShcMember3#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesSplunkShcMember3#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesSplunkShcMember3(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnModulePropsResourcesSplunkSmartstoreBucket",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesSplunkSmartstoreBucket:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesSplunkSmartstoreBucket
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesSplunkSmartstoreBucket#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesSplunkSmartstoreBucket#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesSplunkSmartstoreBucket(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnModulePropsResourcesVpc",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesVpc:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesVpc
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesVpc#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesVpc#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesVpc(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnModulePropsResourcesVpcGatewayAttachment",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesVpcGatewayAttachment:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesVpcGatewayAttachment
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesVpcGatewayAttachment#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesVpcGatewayAttachment#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesVpcGatewayAttachment(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnModule",
    "CfnModuleProps",
    "CfnModulePropsParameters",
    "CfnModulePropsParametersAvailabilityZones",
    "CfnModulePropsParametersHecClientLocation",
    "CfnModulePropsParametersIndexerInstanceType",
    "CfnModulePropsParametersKeyName",
    "CfnModulePropsParametersNumberOfAZs",
    "CfnModulePropsParametersPublicSubnet1Cidr",
    "CfnModulePropsParametersPublicSubnet2Cidr",
    "CfnModulePropsParametersPublicSubnet3Cidr",
    "CfnModulePropsParametersSearchHeadInstanceType",
    "CfnModulePropsParametersShcEnabled",
    "CfnModulePropsParametersSmartStoreBucketName",
    "CfnModulePropsParametersSplunkAdminPassword",
    "CfnModulePropsParametersSplunkClusterSecret",
    "CfnModulePropsParametersSplunkIndexerCount",
    "CfnModulePropsParametersSplunkIndexerDiscoverySecret",
    "CfnModulePropsParametersSplunkIndexerDiskSize",
    "CfnModulePropsParametersSplunkLicenseBucket",
    "CfnModulePropsParametersSplunkLicensePath",
    "CfnModulePropsParametersSplunkReplicationFactor",
    "CfnModulePropsParametersSplunkSearchFactor",
    "CfnModulePropsParametersSplunkSearchHeadDiskSize",
    "CfnModulePropsParametersSshClientLocation",
    "CfnModulePropsParametersVpccidr",
    "CfnModulePropsParametersWebClientLocation",
    "CfnModulePropsResources",
    "CfnModulePropsResourcesBucketPolicy",
    "CfnModulePropsResourcesCfnKeys",
    "CfnModulePropsResourcesCfnUser",
    "CfnModulePropsResourcesInternetGateway",
    "CfnModulePropsResourcesPublicSubnet1",
    "CfnModulePropsResourcesPublicSubnet1RouteTableAssociation",
    "CfnModulePropsResourcesPublicSubnet2",
    "CfnModulePropsResourcesPublicSubnet2RouteTableAssociation",
    "CfnModulePropsResourcesPublicSubnet3",
    "CfnModulePropsResourcesPublicSubnet3RouteTableAssociation",
    "CfnModulePropsResourcesPublicSubnetRoute",
    "CfnModulePropsResourcesPublicSubnetRouteTable",
    "CfnModulePropsResourcesSmartStoreS3AccessInstanceProfile",
    "CfnModulePropsResourcesSmartStoreS3BucketPolicy",
    "CfnModulePropsResourcesSmartStoreS3BucketRole",
    "CfnModulePropsResourcesSplunkCm",
    "CfnModulePropsResourcesSplunkCmWaitCondition",
    "CfnModulePropsResourcesSplunkCmWaitHandle",
    "CfnModulePropsResourcesSplunkHttpEventCollectorLoadBalancer",
    "CfnModulePropsResourcesSplunkHttpEventCollectorLoadBalancerSecurityGroup",
    "CfnModulePropsResourcesSplunkIndexerLaunchConfiguration",
    "CfnModulePropsResourcesSplunkIndexerNodesAsg",
    "CfnModulePropsResourcesSplunkIndexerSecurityGroup",
    "CfnModulePropsResourcesSplunkSearchHeadInstance",
    "CfnModulePropsResourcesSplunkSearchHeadSecurityGroup",
    "CfnModulePropsResourcesSplunkSecurityGroup",
    "CfnModulePropsResourcesSplunkShcDeployer",
    "CfnModulePropsResourcesSplunkShcLoadBalancer",
    "CfnModulePropsResourcesSplunkShcMember1",
    "CfnModulePropsResourcesSplunkShcMember2",
    "CfnModulePropsResourcesSplunkShcMember3",
    "CfnModulePropsResourcesSplunkSmartstoreBucket",
    "CfnModulePropsResourcesVpc",
    "CfnModulePropsResourcesVpcGatewayAttachment",
]

publication.publish()
