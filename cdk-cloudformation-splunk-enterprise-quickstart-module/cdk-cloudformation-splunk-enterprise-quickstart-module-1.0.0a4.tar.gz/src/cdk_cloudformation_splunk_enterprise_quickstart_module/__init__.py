'''
# splunk-enterprise-quickstart-module

> AWS CDK [L1 construct](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html) and data structures for the [AWS CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) type `Splunk::Enterprise::QuickStart::MODULE` v1.0.0.

## Description

Schema for Module Fragment of type Splunk::Enterprise::QuickStart::MODULE

## Usage

In order to use this library, you will need to activate this AWS CloudFormation Registry type in your account. You can do this via the AWS Management Console or using the [AWS CLI](https://aws.amazon.com/cli/) using the following command:

```sh
aws cloudformation activate-type \
  --type-name Splunk::Enterprise::QuickStart::MODULE \
  --publisher-id c90b10f63c592300fda916a73ffef76788069f34 \
  --type MODULE \
  --execution-role-arn ROLE-ARN
```

Alternatively:

```sh
aws cloudformation activate-type \
  --public-type-arn arn:aws:cloudformation:us-east-1::type/module/c90b10f63c592300fda916a73ffef76788069f34/Splunk-Enterprise-QuickStart-MODULE \
  --execution-role-arn ROLE-ARN
```

You can find more information about activating this type in the [AWS CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html).

## Feedback

This library is auto-generated and published to all supported programming languages by the [cdklabs/cdk-cloudformation](https://github.com/cdklabs/cdk-cloudformation) project based on the API schema published for `Splunk::Enterprise::QuickStart::MODULE`.

* Issues related to this generated library should be [reported here](https://github.com/cdklabs/cdk-cloudformation/issues/new?title=Issue+with+%40cdk-cloudformation%2Fsplunk-enterprise-quickstart-module+v1.0.0).
* Issues related to `Splunk::Enterprise::QuickStart::MODULE` should be reported to the [publisher](undefined).

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


class CfnQuickStartModule(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnQuickStartModule",
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
        parameters: typing.Optional["CfnQuickStartModulePropsParameters"] = None,
        resources: typing.Optional["CfnQuickStartModulePropsResources"] = None,
    ) -> None:
        '''Create a new ``Splunk::Enterprise::QuickStart::MODULE``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param parameters: 
        :param resources: 
        '''
        props = CfnQuickStartModuleProps(parameters=parameters, resources=resources)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnQuickStartModuleProps":
        '''Resource props.'''
        return typing.cast("CfnQuickStartModuleProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnQuickStartModuleProps",
    jsii_struct_bases=[],
    name_mapping={"parameters": "parameters", "resources": "resources"},
)
class CfnQuickStartModuleProps:
    def __init__(
        self,
        *,
        parameters: typing.Optional["CfnQuickStartModulePropsParameters"] = None,
        resources: typing.Optional["CfnQuickStartModulePropsResources"] = None,
    ) -> None:
        '''Schema for Module Fragment of type Splunk::Enterprise::QuickStart::MODULE.

        :param parameters: 
        :param resources: 

        :schema: CfnQuickStartModuleProps
        '''
        if isinstance(parameters, dict):
            parameters = CfnQuickStartModulePropsParameters(**parameters)
        if isinstance(resources, dict):
            resources = CfnQuickStartModulePropsResources(**resources)
        self._values: typing.Dict[str, typing.Any] = {}
        if parameters is not None:
            self._values["parameters"] = parameters
        if resources is not None:
            self._values["resources"] = resources

    @builtins.property
    def parameters(self) -> typing.Optional["CfnQuickStartModulePropsParameters"]:
        '''
        :schema: CfnQuickStartModuleProps#Parameters
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional["CfnQuickStartModulePropsParameters"], result)

    @builtins.property
    def resources(self) -> typing.Optional["CfnQuickStartModulePropsResources"]:
        '''
        :schema: CfnQuickStartModuleProps#Resources
        '''
        result = self._values.get("resources")
        return typing.cast(typing.Optional["CfnQuickStartModulePropsResources"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnQuickStartModuleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnQuickStartModulePropsParameters",
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
class CfnQuickStartModulePropsParameters:
    def __init__(
        self,
        *,
        availability_zones: typing.Optional["CfnQuickStartModulePropsParametersAvailabilityZones"] = None,
        hec_client_location: typing.Optional["CfnQuickStartModulePropsParametersHecClientLocation"] = None,
        indexer_instance_type: typing.Optional["CfnQuickStartModulePropsParametersIndexerInstanceType"] = None,
        key_name: typing.Optional["CfnQuickStartModulePropsParametersKeyName"] = None,
        number_of_a_zs: typing.Optional["CfnQuickStartModulePropsParametersNumberOfAZs"] = None,
        public_subnet1_cidr: typing.Optional["CfnQuickStartModulePropsParametersPublicSubnet1Cidr"] = None,
        public_subnet2_cidr: typing.Optional["CfnQuickStartModulePropsParametersPublicSubnet2Cidr"] = None,
        public_subnet3_cidr: typing.Optional["CfnQuickStartModulePropsParametersPublicSubnet3Cidr"] = None,
        search_head_instance_type: typing.Optional["CfnQuickStartModulePropsParametersSearchHeadInstanceType"] = None,
        shc_enabled: typing.Optional["CfnQuickStartModulePropsParametersShcEnabled"] = None,
        smart_store_bucket_name: typing.Optional["CfnQuickStartModulePropsParametersSmartStoreBucketName"] = None,
        splunk_admin_password: typing.Optional["CfnQuickStartModulePropsParametersSplunkAdminPassword"] = None,
        splunk_cluster_secret: typing.Optional["CfnQuickStartModulePropsParametersSplunkClusterSecret"] = None,
        splunk_indexer_count: typing.Optional["CfnQuickStartModulePropsParametersSplunkIndexerCount"] = None,
        splunk_indexer_discovery_secret: typing.Optional["CfnQuickStartModulePropsParametersSplunkIndexerDiscoverySecret"] = None,
        splunk_indexer_disk_size: typing.Optional["CfnQuickStartModulePropsParametersSplunkIndexerDiskSize"] = None,
        splunk_license_bucket: typing.Optional["CfnQuickStartModulePropsParametersSplunkLicenseBucket"] = None,
        splunk_license_path: typing.Optional["CfnQuickStartModulePropsParametersSplunkLicensePath"] = None,
        splunk_replication_factor: typing.Optional["CfnQuickStartModulePropsParametersSplunkReplicationFactor"] = None,
        splunk_search_factor: typing.Optional["CfnQuickStartModulePropsParametersSplunkSearchFactor"] = None,
        splunk_search_head_disk_size: typing.Optional["CfnQuickStartModulePropsParametersSplunkSearchHeadDiskSize"] = None,
        ssh_client_location: typing.Optional["CfnQuickStartModulePropsParametersSshClientLocation"] = None,
        vpccidr: typing.Optional["CfnQuickStartModulePropsParametersVpccidr"] = None,
        web_client_location: typing.Optional["CfnQuickStartModulePropsParametersWebClientLocation"] = None,
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

        :schema: CfnQuickStartModulePropsParameters
        '''
        if isinstance(availability_zones, dict):
            availability_zones = CfnQuickStartModulePropsParametersAvailabilityZones(**availability_zones)
        if isinstance(hec_client_location, dict):
            hec_client_location = CfnQuickStartModulePropsParametersHecClientLocation(**hec_client_location)
        if isinstance(indexer_instance_type, dict):
            indexer_instance_type = CfnQuickStartModulePropsParametersIndexerInstanceType(**indexer_instance_type)
        if isinstance(key_name, dict):
            key_name = CfnQuickStartModulePropsParametersKeyName(**key_name)
        if isinstance(number_of_a_zs, dict):
            number_of_a_zs = CfnQuickStartModulePropsParametersNumberOfAZs(**number_of_a_zs)
        if isinstance(public_subnet1_cidr, dict):
            public_subnet1_cidr = CfnQuickStartModulePropsParametersPublicSubnet1Cidr(**public_subnet1_cidr)
        if isinstance(public_subnet2_cidr, dict):
            public_subnet2_cidr = CfnQuickStartModulePropsParametersPublicSubnet2Cidr(**public_subnet2_cidr)
        if isinstance(public_subnet3_cidr, dict):
            public_subnet3_cidr = CfnQuickStartModulePropsParametersPublicSubnet3Cidr(**public_subnet3_cidr)
        if isinstance(search_head_instance_type, dict):
            search_head_instance_type = CfnQuickStartModulePropsParametersSearchHeadInstanceType(**search_head_instance_type)
        if isinstance(shc_enabled, dict):
            shc_enabled = CfnQuickStartModulePropsParametersShcEnabled(**shc_enabled)
        if isinstance(smart_store_bucket_name, dict):
            smart_store_bucket_name = CfnQuickStartModulePropsParametersSmartStoreBucketName(**smart_store_bucket_name)
        if isinstance(splunk_admin_password, dict):
            splunk_admin_password = CfnQuickStartModulePropsParametersSplunkAdminPassword(**splunk_admin_password)
        if isinstance(splunk_cluster_secret, dict):
            splunk_cluster_secret = CfnQuickStartModulePropsParametersSplunkClusterSecret(**splunk_cluster_secret)
        if isinstance(splunk_indexer_count, dict):
            splunk_indexer_count = CfnQuickStartModulePropsParametersSplunkIndexerCount(**splunk_indexer_count)
        if isinstance(splunk_indexer_discovery_secret, dict):
            splunk_indexer_discovery_secret = CfnQuickStartModulePropsParametersSplunkIndexerDiscoverySecret(**splunk_indexer_discovery_secret)
        if isinstance(splunk_indexer_disk_size, dict):
            splunk_indexer_disk_size = CfnQuickStartModulePropsParametersSplunkIndexerDiskSize(**splunk_indexer_disk_size)
        if isinstance(splunk_license_bucket, dict):
            splunk_license_bucket = CfnQuickStartModulePropsParametersSplunkLicenseBucket(**splunk_license_bucket)
        if isinstance(splunk_license_path, dict):
            splunk_license_path = CfnQuickStartModulePropsParametersSplunkLicensePath(**splunk_license_path)
        if isinstance(splunk_replication_factor, dict):
            splunk_replication_factor = CfnQuickStartModulePropsParametersSplunkReplicationFactor(**splunk_replication_factor)
        if isinstance(splunk_search_factor, dict):
            splunk_search_factor = CfnQuickStartModulePropsParametersSplunkSearchFactor(**splunk_search_factor)
        if isinstance(splunk_search_head_disk_size, dict):
            splunk_search_head_disk_size = CfnQuickStartModulePropsParametersSplunkSearchHeadDiskSize(**splunk_search_head_disk_size)
        if isinstance(ssh_client_location, dict):
            ssh_client_location = CfnQuickStartModulePropsParametersSshClientLocation(**ssh_client_location)
        if isinstance(vpccidr, dict):
            vpccidr = CfnQuickStartModulePropsParametersVpccidr(**vpccidr)
        if isinstance(web_client_location, dict):
            web_client_location = CfnQuickStartModulePropsParametersWebClientLocation(**web_client_location)
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
    ) -> typing.Optional["CfnQuickStartModulePropsParametersAvailabilityZones"]:
        '''
        :schema: CfnQuickStartModulePropsParameters#AvailabilityZones
        '''
        result = self._values.get("availability_zones")
        return typing.cast(typing.Optional["CfnQuickStartModulePropsParametersAvailabilityZones"], result)

    @builtins.property
    def hec_client_location(
        self,
    ) -> typing.Optional["CfnQuickStartModulePropsParametersHecClientLocation"]:
        '''
        :schema: CfnQuickStartModulePropsParameters#HECClientLocation
        '''
        result = self._values.get("hec_client_location")
        return typing.cast(typing.Optional["CfnQuickStartModulePropsParametersHecClientLocation"], result)

    @builtins.property
    def indexer_instance_type(
        self,
    ) -> typing.Optional["CfnQuickStartModulePropsParametersIndexerInstanceType"]:
        '''
        :schema: CfnQuickStartModulePropsParameters#IndexerInstanceType
        '''
        result = self._values.get("indexer_instance_type")
        return typing.cast(typing.Optional["CfnQuickStartModulePropsParametersIndexerInstanceType"], result)

    @builtins.property
    def key_name(self) -> typing.Optional["CfnQuickStartModulePropsParametersKeyName"]:
        '''
        :schema: CfnQuickStartModulePropsParameters#KeyName
        '''
        result = self._values.get("key_name")
        return typing.cast(typing.Optional["CfnQuickStartModulePropsParametersKeyName"], result)

    @builtins.property
    def number_of_a_zs(
        self,
    ) -> typing.Optional["CfnQuickStartModulePropsParametersNumberOfAZs"]:
        '''
        :schema: CfnQuickStartModulePropsParameters#NumberOfAZs
        '''
        result = self._values.get("number_of_a_zs")
        return typing.cast(typing.Optional["CfnQuickStartModulePropsParametersNumberOfAZs"], result)

    @builtins.property
    def public_subnet1_cidr(
        self,
    ) -> typing.Optional["CfnQuickStartModulePropsParametersPublicSubnet1Cidr"]:
        '''
        :schema: CfnQuickStartModulePropsParameters#PublicSubnet1CIDR
        '''
        result = self._values.get("public_subnet1_cidr")
        return typing.cast(typing.Optional["CfnQuickStartModulePropsParametersPublicSubnet1Cidr"], result)

    @builtins.property
    def public_subnet2_cidr(
        self,
    ) -> typing.Optional["CfnQuickStartModulePropsParametersPublicSubnet2Cidr"]:
        '''
        :schema: CfnQuickStartModulePropsParameters#PublicSubnet2CIDR
        '''
        result = self._values.get("public_subnet2_cidr")
        return typing.cast(typing.Optional["CfnQuickStartModulePropsParametersPublicSubnet2Cidr"], result)

    @builtins.property
    def public_subnet3_cidr(
        self,
    ) -> typing.Optional["CfnQuickStartModulePropsParametersPublicSubnet3Cidr"]:
        '''
        :schema: CfnQuickStartModulePropsParameters#PublicSubnet3CIDR
        '''
        result = self._values.get("public_subnet3_cidr")
        return typing.cast(typing.Optional["CfnQuickStartModulePropsParametersPublicSubnet3Cidr"], result)

    @builtins.property
    def search_head_instance_type(
        self,
    ) -> typing.Optional["CfnQuickStartModulePropsParametersSearchHeadInstanceType"]:
        '''
        :schema: CfnQuickStartModulePropsParameters#SearchHeadInstanceType
        '''
        result = self._values.get("search_head_instance_type")
        return typing.cast(typing.Optional["CfnQuickStartModulePropsParametersSearchHeadInstanceType"], result)

    @builtins.property
    def shc_enabled(
        self,
    ) -> typing.Optional["CfnQuickStartModulePropsParametersShcEnabled"]:
        '''
        :schema: CfnQuickStartModulePropsParameters#SHCEnabled
        '''
        result = self._values.get("shc_enabled")
        return typing.cast(typing.Optional["CfnQuickStartModulePropsParametersShcEnabled"], result)

    @builtins.property
    def smart_store_bucket_name(
        self,
    ) -> typing.Optional["CfnQuickStartModulePropsParametersSmartStoreBucketName"]:
        '''
        :schema: CfnQuickStartModulePropsParameters#SmartStoreBucketName
        '''
        result = self._values.get("smart_store_bucket_name")
        return typing.cast(typing.Optional["CfnQuickStartModulePropsParametersSmartStoreBucketName"], result)

    @builtins.property
    def splunk_admin_password(
        self,
    ) -> typing.Optional["CfnQuickStartModulePropsParametersSplunkAdminPassword"]:
        '''
        :schema: CfnQuickStartModulePropsParameters#SplunkAdminPassword
        '''
        result = self._values.get("splunk_admin_password")
        return typing.cast(typing.Optional["CfnQuickStartModulePropsParametersSplunkAdminPassword"], result)

    @builtins.property
    def splunk_cluster_secret(
        self,
    ) -> typing.Optional["CfnQuickStartModulePropsParametersSplunkClusterSecret"]:
        '''
        :schema: CfnQuickStartModulePropsParameters#SplunkClusterSecret
        '''
        result = self._values.get("splunk_cluster_secret")
        return typing.cast(typing.Optional["CfnQuickStartModulePropsParametersSplunkClusterSecret"], result)

    @builtins.property
    def splunk_indexer_count(
        self,
    ) -> typing.Optional["CfnQuickStartModulePropsParametersSplunkIndexerCount"]:
        '''
        :schema: CfnQuickStartModulePropsParameters#SplunkIndexerCount
        '''
        result = self._values.get("splunk_indexer_count")
        return typing.cast(typing.Optional["CfnQuickStartModulePropsParametersSplunkIndexerCount"], result)

    @builtins.property
    def splunk_indexer_discovery_secret(
        self,
    ) -> typing.Optional["CfnQuickStartModulePropsParametersSplunkIndexerDiscoverySecret"]:
        '''
        :schema: CfnQuickStartModulePropsParameters#SplunkIndexerDiscoverySecret
        '''
        result = self._values.get("splunk_indexer_discovery_secret")
        return typing.cast(typing.Optional["CfnQuickStartModulePropsParametersSplunkIndexerDiscoverySecret"], result)

    @builtins.property
    def splunk_indexer_disk_size(
        self,
    ) -> typing.Optional["CfnQuickStartModulePropsParametersSplunkIndexerDiskSize"]:
        '''
        :schema: CfnQuickStartModulePropsParameters#SplunkIndexerDiskSize
        '''
        result = self._values.get("splunk_indexer_disk_size")
        return typing.cast(typing.Optional["CfnQuickStartModulePropsParametersSplunkIndexerDiskSize"], result)

    @builtins.property
    def splunk_license_bucket(
        self,
    ) -> typing.Optional["CfnQuickStartModulePropsParametersSplunkLicenseBucket"]:
        '''
        :schema: CfnQuickStartModulePropsParameters#SplunkLicenseBucket
        '''
        result = self._values.get("splunk_license_bucket")
        return typing.cast(typing.Optional["CfnQuickStartModulePropsParametersSplunkLicenseBucket"], result)

    @builtins.property
    def splunk_license_path(
        self,
    ) -> typing.Optional["CfnQuickStartModulePropsParametersSplunkLicensePath"]:
        '''
        :schema: CfnQuickStartModulePropsParameters#SplunkLicensePath
        '''
        result = self._values.get("splunk_license_path")
        return typing.cast(typing.Optional["CfnQuickStartModulePropsParametersSplunkLicensePath"], result)

    @builtins.property
    def splunk_replication_factor(
        self,
    ) -> typing.Optional["CfnQuickStartModulePropsParametersSplunkReplicationFactor"]:
        '''
        :schema: CfnQuickStartModulePropsParameters#SplunkReplicationFactor
        '''
        result = self._values.get("splunk_replication_factor")
        return typing.cast(typing.Optional["CfnQuickStartModulePropsParametersSplunkReplicationFactor"], result)

    @builtins.property
    def splunk_search_factor(
        self,
    ) -> typing.Optional["CfnQuickStartModulePropsParametersSplunkSearchFactor"]:
        '''
        :schema: CfnQuickStartModulePropsParameters#SplunkSearchFactor
        '''
        result = self._values.get("splunk_search_factor")
        return typing.cast(typing.Optional["CfnQuickStartModulePropsParametersSplunkSearchFactor"], result)

    @builtins.property
    def splunk_search_head_disk_size(
        self,
    ) -> typing.Optional["CfnQuickStartModulePropsParametersSplunkSearchHeadDiskSize"]:
        '''
        :schema: CfnQuickStartModulePropsParameters#SplunkSearchHeadDiskSize
        '''
        result = self._values.get("splunk_search_head_disk_size")
        return typing.cast(typing.Optional["CfnQuickStartModulePropsParametersSplunkSearchHeadDiskSize"], result)

    @builtins.property
    def ssh_client_location(
        self,
    ) -> typing.Optional["CfnQuickStartModulePropsParametersSshClientLocation"]:
        '''
        :schema: CfnQuickStartModulePropsParameters#SSHClientLocation
        '''
        result = self._values.get("ssh_client_location")
        return typing.cast(typing.Optional["CfnQuickStartModulePropsParametersSshClientLocation"], result)

    @builtins.property
    def vpccidr(self) -> typing.Optional["CfnQuickStartModulePropsParametersVpccidr"]:
        '''
        :schema: CfnQuickStartModulePropsParameters#VPCCIDR
        '''
        result = self._values.get("vpccidr")
        return typing.cast(typing.Optional["CfnQuickStartModulePropsParametersVpccidr"], result)

    @builtins.property
    def web_client_location(
        self,
    ) -> typing.Optional["CfnQuickStartModulePropsParametersWebClientLocation"]:
        '''
        :schema: CfnQuickStartModulePropsParameters#WebClientLocation
        '''
        result = self._values.get("web_client_location")
        return typing.cast(typing.Optional["CfnQuickStartModulePropsParametersWebClientLocation"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnQuickStartModulePropsParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnQuickStartModulePropsParametersAvailabilityZones",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnQuickStartModulePropsParametersAvailabilityZones:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnQuickStartModulePropsParametersAvailabilityZones
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnQuickStartModulePropsParametersAvailabilityZones#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnQuickStartModulePropsParametersAvailabilityZones(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnQuickStartModulePropsParametersHecClientLocation",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnQuickStartModulePropsParametersHecClientLocation:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnQuickStartModulePropsParametersHecClientLocation
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnQuickStartModulePropsParametersHecClientLocation#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnQuickStartModulePropsParametersHecClientLocation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnQuickStartModulePropsParametersIndexerInstanceType",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnQuickStartModulePropsParametersIndexerInstanceType:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnQuickStartModulePropsParametersIndexerInstanceType
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnQuickStartModulePropsParametersIndexerInstanceType#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnQuickStartModulePropsParametersIndexerInstanceType(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnQuickStartModulePropsParametersKeyName",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnQuickStartModulePropsParametersKeyName:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnQuickStartModulePropsParametersKeyName
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnQuickStartModulePropsParametersKeyName#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnQuickStartModulePropsParametersKeyName(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnQuickStartModulePropsParametersNumberOfAZs",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnQuickStartModulePropsParametersNumberOfAZs:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnQuickStartModulePropsParametersNumberOfAZs
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnQuickStartModulePropsParametersNumberOfAZs#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnQuickStartModulePropsParametersNumberOfAZs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnQuickStartModulePropsParametersPublicSubnet1Cidr",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnQuickStartModulePropsParametersPublicSubnet1Cidr:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnQuickStartModulePropsParametersPublicSubnet1Cidr
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnQuickStartModulePropsParametersPublicSubnet1Cidr#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnQuickStartModulePropsParametersPublicSubnet1Cidr(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnQuickStartModulePropsParametersPublicSubnet2Cidr",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnQuickStartModulePropsParametersPublicSubnet2Cidr:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnQuickStartModulePropsParametersPublicSubnet2Cidr
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnQuickStartModulePropsParametersPublicSubnet2Cidr#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnQuickStartModulePropsParametersPublicSubnet2Cidr(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnQuickStartModulePropsParametersPublicSubnet3Cidr",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnQuickStartModulePropsParametersPublicSubnet3Cidr:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnQuickStartModulePropsParametersPublicSubnet3Cidr
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnQuickStartModulePropsParametersPublicSubnet3Cidr#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnQuickStartModulePropsParametersPublicSubnet3Cidr(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnQuickStartModulePropsParametersSearchHeadInstanceType",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnQuickStartModulePropsParametersSearchHeadInstanceType:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnQuickStartModulePropsParametersSearchHeadInstanceType
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnQuickStartModulePropsParametersSearchHeadInstanceType#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnQuickStartModulePropsParametersSearchHeadInstanceType(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnQuickStartModulePropsParametersShcEnabled",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnQuickStartModulePropsParametersShcEnabled:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnQuickStartModulePropsParametersShcEnabled
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnQuickStartModulePropsParametersShcEnabled#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnQuickStartModulePropsParametersShcEnabled(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnQuickStartModulePropsParametersSmartStoreBucketName",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnQuickStartModulePropsParametersSmartStoreBucketName:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnQuickStartModulePropsParametersSmartStoreBucketName
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnQuickStartModulePropsParametersSmartStoreBucketName#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnQuickStartModulePropsParametersSmartStoreBucketName(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnQuickStartModulePropsParametersSplunkAdminPassword",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnQuickStartModulePropsParametersSplunkAdminPassword:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnQuickStartModulePropsParametersSplunkAdminPassword
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnQuickStartModulePropsParametersSplunkAdminPassword#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnQuickStartModulePropsParametersSplunkAdminPassword(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnQuickStartModulePropsParametersSplunkClusterSecret",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnQuickStartModulePropsParametersSplunkClusterSecret:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnQuickStartModulePropsParametersSplunkClusterSecret
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnQuickStartModulePropsParametersSplunkClusterSecret#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnQuickStartModulePropsParametersSplunkClusterSecret(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnQuickStartModulePropsParametersSplunkIndexerCount",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnQuickStartModulePropsParametersSplunkIndexerCount:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnQuickStartModulePropsParametersSplunkIndexerCount
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnQuickStartModulePropsParametersSplunkIndexerCount#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnQuickStartModulePropsParametersSplunkIndexerCount(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnQuickStartModulePropsParametersSplunkIndexerDiscoverySecret",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnQuickStartModulePropsParametersSplunkIndexerDiscoverySecret:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnQuickStartModulePropsParametersSplunkIndexerDiscoverySecret
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnQuickStartModulePropsParametersSplunkIndexerDiscoverySecret#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnQuickStartModulePropsParametersSplunkIndexerDiscoverySecret(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnQuickStartModulePropsParametersSplunkIndexerDiskSize",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnQuickStartModulePropsParametersSplunkIndexerDiskSize:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnQuickStartModulePropsParametersSplunkIndexerDiskSize
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnQuickStartModulePropsParametersSplunkIndexerDiskSize#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnQuickStartModulePropsParametersSplunkIndexerDiskSize(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnQuickStartModulePropsParametersSplunkLicenseBucket",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnQuickStartModulePropsParametersSplunkLicenseBucket:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnQuickStartModulePropsParametersSplunkLicenseBucket
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnQuickStartModulePropsParametersSplunkLicenseBucket#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnQuickStartModulePropsParametersSplunkLicenseBucket(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnQuickStartModulePropsParametersSplunkLicensePath",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnQuickStartModulePropsParametersSplunkLicensePath:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnQuickStartModulePropsParametersSplunkLicensePath
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnQuickStartModulePropsParametersSplunkLicensePath#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnQuickStartModulePropsParametersSplunkLicensePath(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnQuickStartModulePropsParametersSplunkReplicationFactor",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnQuickStartModulePropsParametersSplunkReplicationFactor:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnQuickStartModulePropsParametersSplunkReplicationFactor
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnQuickStartModulePropsParametersSplunkReplicationFactor#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnQuickStartModulePropsParametersSplunkReplicationFactor(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnQuickStartModulePropsParametersSplunkSearchFactor",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnQuickStartModulePropsParametersSplunkSearchFactor:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnQuickStartModulePropsParametersSplunkSearchFactor
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnQuickStartModulePropsParametersSplunkSearchFactor#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnQuickStartModulePropsParametersSplunkSearchFactor(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnQuickStartModulePropsParametersSplunkSearchHeadDiskSize",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnQuickStartModulePropsParametersSplunkSearchHeadDiskSize:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnQuickStartModulePropsParametersSplunkSearchHeadDiskSize
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnQuickStartModulePropsParametersSplunkSearchHeadDiskSize#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnQuickStartModulePropsParametersSplunkSearchHeadDiskSize(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnQuickStartModulePropsParametersSshClientLocation",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnQuickStartModulePropsParametersSshClientLocation:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnQuickStartModulePropsParametersSshClientLocation
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnQuickStartModulePropsParametersSshClientLocation#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnQuickStartModulePropsParametersSshClientLocation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnQuickStartModulePropsParametersVpccidr",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnQuickStartModulePropsParametersVpccidr:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnQuickStartModulePropsParametersVpccidr
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnQuickStartModulePropsParametersVpccidr#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnQuickStartModulePropsParametersVpccidr(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnQuickStartModulePropsParametersWebClientLocation",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnQuickStartModulePropsParametersWebClientLocation:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnQuickStartModulePropsParametersWebClientLocation
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnQuickStartModulePropsParametersWebClientLocation#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnQuickStartModulePropsParametersWebClientLocation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnQuickStartModulePropsResources",
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
class CfnQuickStartModulePropsResources:
    def __init__(
        self,
        *,
        bucket_policy: typing.Optional["CfnQuickStartModulePropsResourcesBucketPolicy"] = None,
        cfn_keys: typing.Optional["CfnQuickStartModulePropsResourcesCfnKeys"] = None,
        cfn_user: typing.Optional["CfnQuickStartModulePropsResourcesCfnUser"] = None,
        internet_gateway: typing.Optional["CfnQuickStartModulePropsResourcesInternetGateway"] = None,
        public_subnet1: typing.Optional["CfnQuickStartModulePropsResourcesPublicSubnet1"] = None,
        public_subnet1_route_table_association: typing.Optional["CfnQuickStartModulePropsResourcesPublicSubnet1RouteTableAssociation"] = None,
        public_subnet2: typing.Optional["CfnQuickStartModulePropsResourcesPublicSubnet2"] = None,
        public_subnet2_route_table_association: typing.Optional["CfnQuickStartModulePropsResourcesPublicSubnet2RouteTableAssociation"] = None,
        public_subnet3: typing.Optional["CfnQuickStartModulePropsResourcesPublicSubnet3"] = None,
        public_subnet3_route_table_association: typing.Optional["CfnQuickStartModulePropsResourcesPublicSubnet3RouteTableAssociation"] = None,
        public_subnet_route: typing.Optional["CfnQuickStartModulePropsResourcesPublicSubnetRoute"] = None,
        public_subnet_route_table: typing.Optional["CfnQuickStartModulePropsResourcesPublicSubnetRouteTable"] = None,
        smart_store_s3_access_instance_profile: typing.Optional["CfnQuickStartModulePropsResourcesSmartStoreS3AccessInstanceProfile"] = None,
        smart_store_s3_bucket_policy: typing.Optional["CfnQuickStartModulePropsResourcesSmartStoreS3BucketPolicy"] = None,
        smart_store_s3_bucket_role: typing.Optional["CfnQuickStartModulePropsResourcesSmartStoreS3BucketRole"] = None,
        splunk_cm: typing.Optional["CfnQuickStartModulePropsResourcesSplunkCm"] = None,
        splunk_cm_wait_condition: typing.Optional["CfnQuickStartModulePropsResourcesSplunkCmWaitCondition"] = None,
        splunk_cm_wait_handle: typing.Optional["CfnQuickStartModulePropsResourcesSplunkCmWaitHandle"] = None,
        splunk_http_event_collector_load_balancer: typing.Optional["CfnQuickStartModulePropsResourcesSplunkHttpEventCollectorLoadBalancer"] = None,
        splunk_http_event_collector_load_balancer_security_group: typing.Optional["CfnQuickStartModulePropsResourcesSplunkHttpEventCollectorLoadBalancerSecurityGroup"] = None,
        splunk_indexer_launch_configuration: typing.Optional["CfnQuickStartModulePropsResourcesSplunkIndexerLaunchConfiguration"] = None,
        splunk_indexer_nodes_asg: typing.Optional["CfnQuickStartModulePropsResourcesSplunkIndexerNodesAsg"] = None,
        splunk_indexer_security_group: typing.Optional["CfnQuickStartModulePropsResourcesSplunkIndexerSecurityGroup"] = None,
        splunk_search_head_instance: typing.Optional["CfnQuickStartModulePropsResourcesSplunkSearchHeadInstance"] = None,
        splunk_search_head_security_group: typing.Optional["CfnQuickStartModulePropsResourcesSplunkSearchHeadSecurityGroup"] = None,
        splunk_security_group: typing.Optional["CfnQuickStartModulePropsResourcesSplunkSecurityGroup"] = None,
        splunk_shc_deployer: typing.Optional["CfnQuickStartModulePropsResourcesSplunkShcDeployer"] = None,
        splunk_shc_load_balancer: typing.Optional["CfnQuickStartModulePropsResourcesSplunkShcLoadBalancer"] = None,
        splunk_shc_member1: typing.Optional["CfnQuickStartModulePropsResourcesSplunkShcMember1"] = None,
        splunk_shc_member2: typing.Optional["CfnQuickStartModulePropsResourcesSplunkShcMember2"] = None,
        splunk_shc_member3: typing.Optional["CfnQuickStartModulePropsResourcesSplunkShcMember3"] = None,
        splunk_smartstore_bucket: typing.Optional["CfnQuickStartModulePropsResourcesSplunkSmartstoreBucket"] = None,
        vpc: typing.Optional["CfnQuickStartModulePropsResourcesVpc"] = None,
        vpc_gateway_attachment: typing.Optional["CfnQuickStartModulePropsResourcesVpcGatewayAttachment"] = None,
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

        :schema: CfnQuickStartModulePropsResources
        '''
        if isinstance(bucket_policy, dict):
            bucket_policy = CfnQuickStartModulePropsResourcesBucketPolicy(**bucket_policy)
        if isinstance(cfn_keys, dict):
            cfn_keys = CfnQuickStartModulePropsResourcesCfnKeys(**cfn_keys)
        if isinstance(cfn_user, dict):
            cfn_user = CfnQuickStartModulePropsResourcesCfnUser(**cfn_user)
        if isinstance(internet_gateway, dict):
            internet_gateway = CfnQuickStartModulePropsResourcesInternetGateway(**internet_gateway)
        if isinstance(public_subnet1, dict):
            public_subnet1 = CfnQuickStartModulePropsResourcesPublicSubnet1(**public_subnet1)
        if isinstance(public_subnet1_route_table_association, dict):
            public_subnet1_route_table_association = CfnQuickStartModulePropsResourcesPublicSubnet1RouteTableAssociation(**public_subnet1_route_table_association)
        if isinstance(public_subnet2, dict):
            public_subnet2 = CfnQuickStartModulePropsResourcesPublicSubnet2(**public_subnet2)
        if isinstance(public_subnet2_route_table_association, dict):
            public_subnet2_route_table_association = CfnQuickStartModulePropsResourcesPublicSubnet2RouteTableAssociation(**public_subnet2_route_table_association)
        if isinstance(public_subnet3, dict):
            public_subnet3 = CfnQuickStartModulePropsResourcesPublicSubnet3(**public_subnet3)
        if isinstance(public_subnet3_route_table_association, dict):
            public_subnet3_route_table_association = CfnQuickStartModulePropsResourcesPublicSubnet3RouteTableAssociation(**public_subnet3_route_table_association)
        if isinstance(public_subnet_route, dict):
            public_subnet_route = CfnQuickStartModulePropsResourcesPublicSubnetRoute(**public_subnet_route)
        if isinstance(public_subnet_route_table, dict):
            public_subnet_route_table = CfnQuickStartModulePropsResourcesPublicSubnetRouteTable(**public_subnet_route_table)
        if isinstance(smart_store_s3_access_instance_profile, dict):
            smart_store_s3_access_instance_profile = CfnQuickStartModulePropsResourcesSmartStoreS3AccessInstanceProfile(**smart_store_s3_access_instance_profile)
        if isinstance(smart_store_s3_bucket_policy, dict):
            smart_store_s3_bucket_policy = CfnQuickStartModulePropsResourcesSmartStoreS3BucketPolicy(**smart_store_s3_bucket_policy)
        if isinstance(smart_store_s3_bucket_role, dict):
            smart_store_s3_bucket_role = CfnQuickStartModulePropsResourcesSmartStoreS3BucketRole(**smart_store_s3_bucket_role)
        if isinstance(splunk_cm, dict):
            splunk_cm = CfnQuickStartModulePropsResourcesSplunkCm(**splunk_cm)
        if isinstance(splunk_cm_wait_condition, dict):
            splunk_cm_wait_condition = CfnQuickStartModulePropsResourcesSplunkCmWaitCondition(**splunk_cm_wait_condition)
        if isinstance(splunk_cm_wait_handle, dict):
            splunk_cm_wait_handle = CfnQuickStartModulePropsResourcesSplunkCmWaitHandle(**splunk_cm_wait_handle)
        if isinstance(splunk_http_event_collector_load_balancer, dict):
            splunk_http_event_collector_load_balancer = CfnQuickStartModulePropsResourcesSplunkHttpEventCollectorLoadBalancer(**splunk_http_event_collector_load_balancer)
        if isinstance(splunk_http_event_collector_load_balancer_security_group, dict):
            splunk_http_event_collector_load_balancer_security_group = CfnQuickStartModulePropsResourcesSplunkHttpEventCollectorLoadBalancerSecurityGroup(**splunk_http_event_collector_load_balancer_security_group)
        if isinstance(splunk_indexer_launch_configuration, dict):
            splunk_indexer_launch_configuration = CfnQuickStartModulePropsResourcesSplunkIndexerLaunchConfiguration(**splunk_indexer_launch_configuration)
        if isinstance(splunk_indexer_nodes_asg, dict):
            splunk_indexer_nodes_asg = CfnQuickStartModulePropsResourcesSplunkIndexerNodesAsg(**splunk_indexer_nodes_asg)
        if isinstance(splunk_indexer_security_group, dict):
            splunk_indexer_security_group = CfnQuickStartModulePropsResourcesSplunkIndexerSecurityGroup(**splunk_indexer_security_group)
        if isinstance(splunk_search_head_instance, dict):
            splunk_search_head_instance = CfnQuickStartModulePropsResourcesSplunkSearchHeadInstance(**splunk_search_head_instance)
        if isinstance(splunk_search_head_security_group, dict):
            splunk_search_head_security_group = CfnQuickStartModulePropsResourcesSplunkSearchHeadSecurityGroup(**splunk_search_head_security_group)
        if isinstance(splunk_security_group, dict):
            splunk_security_group = CfnQuickStartModulePropsResourcesSplunkSecurityGroup(**splunk_security_group)
        if isinstance(splunk_shc_deployer, dict):
            splunk_shc_deployer = CfnQuickStartModulePropsResourcesSplunkShcDeployer(**splunk_shc_deployer)
        if isinstance(splunk_shc_load_balancer, dict):
            splunk_shc_load_balancer = CfnQuickStartModulePropsResourcesSplunkShcLoadBalancer(**splunk_shc_load_balancer)
        if isinstance(splunk_shc_member1, dict):
            splunk_shc_member1 = CfnQuickStartModulePropsResourcesSplunkShcMember1(**splunk_shc_member1)
        if isinstance(splunk_shc_member2, dict):
            splunk_shc_member2 = CfnQuickStartModulePropsResourcesSplunkShcMember2(**splunk_shc_member2)
        if isinstance(splunk_shc_member3, dict):
            splunk_shc_member3 = CfnQuickStartModulePropsResourcesSplunkShcMember3(**splunk_shc_member3)
        if isinstance(splunk_smartstore_bucket, dict):
            splunk_smartstore_bucket = CfnQuickStartModulePropsResourcesSplunkSmartstoreBucket(**splunk_smartstore_bucket)
        if isinstance(vpc, dict):
            vpc = CfnQuickStartModulePropsResourcesVpc(**vpc)
        if isinstance(vpc_gateway_attachment, dict):
            vpc_gateway_attachment = CfnQuickStartModulePropsResourcesVpcGatewayAttachment(**vpc_gateway_attachment)
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
    def bucket_policy(
        self,
    ) -> typing.Optional["CfnQuickStartModulePropsResourcesBucketPolicy"]:
        '''
        :schema: CfnQuickStartModulePropsResources#BucketPolicy
        '''
        result = self._values.get("bucket_policy")
        return typing.cast(typing.Optional["CfnQuickStartModulePropsResourcesBucketPolicy"], result)

    @builtins.property
    def cfn_keys(self) -> typing.Optional["CfnQuickStartModulePropsResourcesCfnKeys"]:
        '''
        :schema: CfnQuickStartModulePropsResources#CfnKeys
        '''
        result = self._values.get("cfn_keys")
        return typing.cast(typing.Optional["CfnQuickStartModulePropsResourcesCfnKeys"], result)

    @builtins.property
    def cfn_user(self) -> typing.Optional["CfnQuickStartModulePropsResourcesCfnUser"]:
        '''
        :schema: CfnQuickStartModulePropsResources#CfnUser
        '''
        result = self._values.get("cfn_user")
        return typing.cast(typing.Optional["CfnQuickStartModulePropsResourcesCfnUser"], result)

    @builtins.property
    def internet_gateway(
        self,
    ) -> typing.Optional["CfnQuickStartModulePropsResourcesInternetGateway"]:
        '''
        :schema: CfnQuickStartModulePropsResources#InternetGateway
        '''
        result = self._values.get("internet_gateway")
        return typing.cast(typing.Optional["CfnQuickStartModulePropsResourcesInternetGateway"], result)

    @builtins.property
    def public_subnet1(
        self,
    ) -> typing.Optional["CfnQuickStartModulePropsResourcesPublicSubnet1"]:
        '''
        :schema: CfnQuickStartModulePropsResources#PublicSubnet1
        '''
        result = self._values.get("public_subnet1")
        return typing.cast(typing.Optional["CfnQuickStartModulePropsResourcesPublicSubnet1"], result)

    @builtins.property
    def public_subnet1_route_table_association(
        self,
    ) -> typing.Optional["CfnQuickStartModulePropsResourcesPublicSubnet1RouteTableAssociation"]:
        '''
        :schema: CfnQuickStartModulePropsResources#PublicSubnet1RouteTableAssociation
        '''
        result = self._values.get("public_subnet1_route_table_association")
        return typing.cast(typing.Optional["CfnQuickStartModulePropsResourcesPublicSubnet1RouteTableAssociation"], result)

    @builtins.property
    def public_subnet2(
        self,
    ) -> typing.Optional["CfnQuickStartModulePropsResourcesPublicSubnet2"]:
        '''
        :schema: CfnQuickStartModulePropsResources#PublicSubnet2
        '''
        result = self._values.get("public_subnet2")
        return typing.cast(typing.Optional["CfnQuickStartModulePropsResourcesPublicSubnet2"], result)

    @builtins.property
    def public_subnet2_route_table_association(
        self,
    ) -> typing.Optional["CfnQuickStartModulePropsResourcesPublicSubnet2RouteTableAssociation"]:
        '''
        :schema: CfnQuickStartModulePropsResources#PublicSubnet2RouteTableAssociation
        '''
        result = self._values.get("public_subnet2_route_table_association")
        return typing.cast(typing.Optional["CfnQuickStartModulePropsResourcesPublicSubnet2RouteTableAssociation"], result)

    @builtins.property
    def public_subnet3(
        self,
    ) -> typing.Optional["CfnQuickStartModulePropsResourcesPublicSubnet3"]:
        '''
        :schema: CfnQuickStartModulePropsResources#PublicSubnet3
        '''
        result = self._values.get("public_subnet3")
        return typing.cast(typing.Optional["CfnQuickStartModulePropsResourcesPublicSubnet3"], result)

    @builtins.property
    def public_subnet3_route_table_association(
        self,
    ) -> typing.Optional["CfnQuickStartModulePropsResourcesPublicSubnet3RouteTableAssociation"]:
        '''
        :schema: CfnQuickStartModulePropsResources#PublicSubnet3RouteTableAssociation
        '''
        result = self._values.get("public_subnet3_route_table_association")
        return typing.cast(typing.Optional["CfnQuickStartModulePropsResourcesPublicSubnet3RouteTableAssociation"], result)

    @builtins.property
    def public_subnet_route(
        self,
    ) -> typing.Optional["CfnQuickStartModulePropsResourcesPublicSubnetRoute"]:
        '''
        :schema: CfnQuickStartModulePropsResources#PublicSubnetRoute
        '''
        result = self._values.get("public_subnet_route")
        return typing.cast(typing.Optional["CfnQuickStartModulePropsResourcesPublicSubnetRoute"], result)

    @builtins.property
    def public_subnet_route_table(
        self,
    ) -> typing.Optional["CfnQuickStartModulePropsResourcesPublicSubnetRouteTable"]:
        '''
        :schema: CfnQuickStartModulePropsResources#PublicSubnetRouteTable
        '''
        result = self._values.get("public_subnet_route_table")
        return typing.cast(typing.Optional["CfnQuickStartModulePropsResourcesPublicSubnetRouteTable"], result)

    @builtins.property
    def smart_store_s3_access_instance_profile(
        self,
    ) -> typing.Optional["CfnQuickStartModulePropsResourcesSmartStoreS3AccessInstanceProfile"]:
        '''
        :schema: CfnQuickStartModulePropsResources#SmartStoreS3AccessInstanceProfile
        '''
        result = self._values.get("smart_store_s3_access_instance_profile")
        return typing.cast(typing.Optional["CfnQuickStartModulePropsResourcesSmartStoreS3AccessInstanceProfile"], result)

    @builtins.property
    def smart_store_s3_bucket_policy(
        self,
    ) -> typing.Optional["CfnQuickStartModulePropsResourcesSmartStoreS3BucketPolicy"]:
        '''
        :schema: CfnQuickStartModulePropsResources#SmartStoreS3BucketPolicy
        '''
        result = self._values.get("smart_store_s3_bucket_policy")
        return typing.cast(typing.Optional["CfnQuickStartModulePropsResourcesSmartStoreS3BucketPolicy"], result)

    @builtins.property
    def smart_store_s3_bucket_role(
        self,
    ) -> typing.Optional["CfnQuickStartModulePropsResourcesSmartStoreS3BucketRole"]:
        '''
        :schema: CfnQuickStartModulePropsResources#SmartStoreS3BucketRole
        '''
        result = self._values.get("smart_store_s3_bucket_role")
        return typing.cast(typing.Optional["CfnQuickStartModulePropsResourcesSmartStoreS3BucketRole"], result)

    @builtins.property
    def splunk_cm(self) -> typing.Optional["CfnQuickStartModulePropsResourcesSplunkCm"]:
        '''
        :schema: CfnQuickStartModulePropsResources#SplunkCM
        '''
        result = self._values.get("splunk_cm")
        return typing.cast(typing.Optional["CfnQuickStartModulePropsResourcesSplunkCm"], result)

    @builtins.property
    def splunk_cm_wait_condition(
        self,
    ) -> typing.Optional["CfnQuickStartModulePropsResourcesSplunkCmWaitCondition"]:
        '''
        :schema: CfnQuickStartModulePropsResources#SplunkCMWaitCondition
        '''
        result = self._values.get("splunk_cm_wait_condition")
        return typing.cast(typing.Optional["CfnQuickStartModulePropsResourcesSplunkCmWaitCondition"], result)

    @builtins.property
    def splunk_cm_wait_handle(
        self,
    ) -> typing.Optional["CfnQuickStartModulePropsResourcesSplunkCmWaitHandle"]:
        '''
        :schema: CfnQuickStartModulePropsResources#SplunkCMWaitHandle
        '''
        result = self._values.get("splunk_cm_wait_handle")
        return typing.cast(typing.Optional["CfnQuickStartModulePropsResourcesSplunkCmWaitHandle"], result)

    @builtins.property
    def splunk_http_event_collector_load_balancer(
        self,
    ) -> typing.Optional["CfnQuickStartModulePropsResourcesSplunkHttpEventCollectorLoadBalancer"]:
        '''
        :schema: CfnQuickStartModulePropsResources#SplunkHttpEventCollectorLoadBalancer
        '''
        result = self._values.get("splunk_http_event_collector_load_balancer")
        return typing.cast(typing.Optional["CfnQuickStartModulePropsResourcesSplunkHttpEventCollectorLoadBalancer"], result)

    @builtins.property
    def splunk_http_event_collector_load_balancer_security_group(
        self,
    ) -> typing.Optional["CfnQuickStartModulePropsResourcesSplunkHttpEventCollectorLoadBalancerSecurityGroup"]:
        '''
        :schema: CfnQuickStartModulePropsResources#SplunkHttpEventCollectorLoadBalancerSecurityGroup
        '''
        result = self._values.get("splunk_http_event_collector_load_balancer_security_group")
        return typing.cast(typing.Optional["CfnQuickStartModulePropsResourcesSplunkHttpEventCollectorLoadBalancerSecurityGroup"], result)

    @builtins.property
    def splunk_indexer_launch_configuration(
        self,
    ) -> typing.Optional["CfnQuickStartModulePropsResourcesSplunkIndexerLaunchConfiguration"]:
        '''
        :schema: CfnQuickStartModulePropsResources#SplunkIndexerLaunchConfiguration
        '''
        result = self._values.get("splunk_indexer_launch_configuration")
        return typing.cast(typing.Optional["CfnQuickStartModulePropsResourcesSplunkIndexerLaunchConfiguration"], result)

    @builtins.property
    def splunk_indexer_nodes_asg(
        self,
    ) -> typing.Optional["CfnQuickStartModulePropsResourcesSplunkIndexerNodesAsg"]:
        '''
        :schema: CfnQuickStartModulePropsResources#SplunkIndexerNodesASG
        '''
        result = self._values.get("splunk_indexer_nodes_asg")
        return typing.cast(typing.Optional["CfnQuickStartModulePropsResourcesSplunkIndexerNodesAsg"], result)

    @builtins.property
    def splunk_indexer_security_group(
        self,
    ) -> typing.Optional["CfnQuickStartModulePropsResourcesSplunkIndexerSecurityGroup"]:
        '''
        :schema: CfnQuickStartModulePropsResources#SplunkIndexerSecurityGroup
        '''
        result = self._values.get("splunk_indexer_security_group")
        return typing.cast(typing.Optional["CfnQuickStartModulePropsResourcesSplunkIndexerSecurityGroup"], result)

    @builtins.property
    def splunk_search_head_instance(
        self,
    ) -> typing.Optional["CfnQuickStartModulePropsResourcesSplunkSearchHeadInstance"]:
        '''
        :schema: CfnQuickStartModulePropsResources#SplunkSearchHeadInstance
        '''
        result = self._values.get("splunk_search_head_instance")
        return typing.cast(typing.Optional["CfnQuickStartModulePropsResourcesSplunkSearchHeadInstance"], result)

    @builtins.property
    def splunk_search_head_security_group(
        self,
    ) -> typing.Optional["CfnQuickStartModulePropsResourcesSplunkSearchHeadSecurityGroup"]:
        '''
        :schema: CfnQuickStartModulePropsResources#SplunkSearchHeadSecurityGroup
        '''
        result = self._values.get("splunk_search_head_security_group")
        return typing.cast(typing.Optional["CfnQuickStartModulePropsResourcesSplunkSearchHeadSecurityGroup"], result)

    @builtins.property
    def splunk_security_group(
        self,
    ) -> typing.Optional["CfnQuickStartModulePropsResourcesSplunkSecurityGroup"]:
        '''
        :schema: CfnQuickStartModulePropsResources#SplunkSecurityGroup
        '''
        result = self._values.get("splunk_security_group")
        return typing.cast(typing.Optional["CfnQuickStartModulePropsResourcesSplunkSecurityGroup"], result)

    @builtins.property
    def splunk_shc_deployer(
        self,
    ) -> typing.Optional["CfnQuickStartModulePropsResourcesSplunkShcDeployer"]:
        '''
        :schema: CfnQuickStartModulePropsResources#SplunkSHCDeployer
        '''
        result = self._values.get("splunk_shc_deployer")
        return typing.cast(typing.Optional["CfnQuickStartModulePropsResourcesSplunkShcDeployer"], result)

    @builtins.property
    def splunk_shc_load_balancer(
        self,
    ) -> typing.Optional["CfnQuickStartModulePropsResourcesSplunkShcLoadBalancer"]:
        '''
        :schema: CfnQuickStartModulePropsResources#SplunkSHCLoadBalancer
        '''
        result = self._values.get("splunk_shc_load_balancer")
        return typing.cast(typing.Optional["CfnQuickStartModulePropsResourcesSplunkShcLoadBalancer"], result)

    @builtins.property
    def splunk_shc_member1(
        self,
    ) -> typing.Optional["CfnQuickStartModulePropsResourcesSplunkShcMember1"]:
        '''
        :schema: CfnQuickStartModulePropsResources#SplunkSHCMember1
        '''
        result = self._values.get("splunk_shc_member1")
        return typing.cast(typing.Optional["CfnQuickStartModulePropsResourcesSplunkShcMember1"], result)

    @builtins.property
    def splunk_shc_member2(
        self,
    ) -> typing.Optional["CfnQuickStartModulePropsResourcesSplunkShcMember2"]:
        '''
        :schema: CfnQuickStartModulePropsResources#SplunkSHCMember2
        '''
        result = self._values.get("splunk_shc_member2")
        return typing.cast(typing.Optional["CfnQuickStartModulePropsResourcesSplunkShcMember2"], result)

    @builtins.property
    def splunk_shc_member3(
        self,
    ) -> typing.Optional["CfnQuickStartModulePropsResourcesSplunkShcMember3"]:
        '''
        :schema: CfnQuickStartModulePropsResources#SplunkSHCMember3
        '''
        result = self._values.get("splunk_shc_member3")
        return typing.cast(typing.Optional["CfnQuickStartModulePropsResourcesSplunkShcMember3"], result)

    @builtins.property
    def splunk_smartstore_bucket(
        self,
    ) -> typing.Optional["CfnQuickStartModulePropsResourcesSplunkSmartstoreBucket"]:
        '''
        :schema: CfnQuickStartModulePropsResources#SplunkSmartstoreBucket
        '''
        result = self._values.get("splunk_smartstore_bucket")
        return typing.cast(typing.Optional["CfnQuickStartModulePropsResourcesSplunkSmartstoreBucket"], result)

    @builtins.property
    def vpc(self) -> typing.Optional["CfnQuickStartModulePropsResourcesVpc"]:
        '''
        :schema: CfnQuickStartModulePropsResources#VPC
        '''
        result = self._values.get("vpc")
        return typing.cast(typing.Optional["CfnQuickStartModulePropsResourcesVpc"], result)

    @builtins.property
    def vpc_gateway_attachment(
        self,
    ) -> typing.Optional["CfnQuickStartModulePropsResourcesVpcGatewayAttachment"]:
        '''
        :schema: CfnQuickStartModulePropsResources#VPCGatewayAttachment
        '''
        result = self._values.get("vpc_gateway_attachment")
        return typing.cast(typing.Optional["CfnQuickStartModulePropsResourcesVpcGatewayAttachment"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnQuickStartModulePropsResources(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnQuickStartModulePropsResourcesBucketPolicy",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnQuickStartModulePropsResourcesBucketPolicy:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnQuickStartModulePropsResourcesBucketPolicy
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnQuickStartModulePropsResourcesBucketPolicy#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnQuickStartModulePropsResourcesBucketPolicy#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnQuickStartModulePropsResourcesBucketPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnQuickStartModulePropsResourcesCfnKeys",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnQuickStartModulePropsResourcesCfnKeys:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnQuickStartModulePropsResourcesCfnKeys
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnQuickStartModulePropsResourcesCfnKeys#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnQuickStartModulePropsResourcesCfnKeys#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnQuickStartModulePropsResourcesCfnKeys(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnQuickStartModulePropsResourcesCfnUser",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnQuickStartModulePropsResourcesCfnUser:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnQuickStartModulePropsResourcesCfnUser
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnQuickStartModulePropsResourcesCfnUser#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnQuickStartModulePropsResourcesCfnUser#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnQuickStartModulePropsResourcesCfnUser(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnQuickStartModulePropsResourcesInternetGateway",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnQuickStartModulePropsResourcesInternetGateway:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnQuickStartModulePropsResourcesInternetGateway
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnQuickStartModulePropsResourcesInternetGateway#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnQuickStartModulePropsResourcesInternetGateway#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnQuickStartModulePropsResourcesInternetGateway(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnQuickStartModulePropsResourcesPublicSubnet1",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnQuickStartModulePropsResourcesPublicSubnet1:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnQuickStartModulePropsResourcesPublicSubnet1
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnQuickStartModulePropsResourcesPublicSubnet1#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnQuickStartModulePropsResourcesPublicSubnet1#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnQuickStartModulePropsResourcesPublicSubnet1(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnQuickStartModulePropsResourcesPublicSubnet1RouteTableAssociation",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnQuickStartModulePropsResourcesPublicSubnet1RouteTableAssociation:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnQuickStartModulePropsResourcesPublicSubnet1RouteTableAssociation
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnQuickStartModulePropsResourcesPublicSubnet1RouteTableAssociation#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnQuickStartModulePropsResourcesPublicSubnet1RouteTableAssociation#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnQuickStartModulePropsResourcesPublicSubnet1RouteTableAssociation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnQuickStartModulePropsResourcesPublicSubnet2",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnQuickStartModulePropsResourcesPublicSubnet2:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnQuickStartModulePropsResourcesPublicSubnet2
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnQuickStartModulePropsResourcesPublicSubnet2#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnQuickStartModulePropsResourcesPublicSubnet2#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnQuickStartModulePropsResourcesPublicSubnet2(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnQuickStartModulePropsResourcesPublicSubnet2RouteTableAssociation",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnQuickStartModulePropsResourcesPublicSubnet2RouteTableAssociation:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnQuickStartModulePropsResourcesPublicSubnet2RouteTableAssociation
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnQuickStartModulePropsResourcesPublicSubnet2RouteTableAssociation#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnQuickStartModulePropsResourcesPublicSubnet2RouteTableAssociation#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnQuickStartModulePropsResourcesPublicSubnet2RouteTableAssociation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnQuickStartModulePropsResourcesPublicSubnet3",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnQuickStartModulePropsResourcesPublicSubnet3:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnQuickStartModulePropsResourcesPublicSubnet3
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnQuickStartModulePropsResourcesPublicSubnet3#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnQuickStartModulePropsResourcesPublicSubnet3#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnQuickStartModulePropsResourcesPublicSubnet3(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnQuickStartModulePropsResourcesPublicSubnet3RouteTableAssociation",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnQuickStartModulePropsResourcesPublicSubnet3RouteTableAssociation:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnQuickStartModulePropsResourcesPublicSubnet3RouteTableAssociation
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnQuickStartModulePropsResourcesPublicSubnet3RouteTableAssociation#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnQuickStartModulePropsResourcesPublicSubnet3RouteTableAssociation#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnQuickStartModulePropsResourcesPublicSubnet3RouteTableAssociation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnQuickStartModulePropsResourcesPublicSubnetRoute",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnQuickStartModulePropsResourcesPublicSubnetRoute:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnQuickStartModulePropsResourcesPublicSubnetRoute
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnQuickStartModulePropsResourcesPublicSubnetRoute#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnQuickStartModulePropsResourcesPublicSubnetRoute#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnQuickStartModulePropsResourcesPublicSubnetRoute(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnQuickStartModulePropsResourcesPublicSubnetRouteTable",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnQuickStartModulePropsResourcesPublicSubnetRouteTable:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnQuickStartModulePropsResourcesPublicSubnetRouteTable
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnQuickStartModulePropsResourcesPublicSubnetRouteTable#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnQuickStartModulePropsResourcesPublicSubnetRouteTable#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnQuickStartModulePropsResourcesPublicSubnetRouteTable(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnQuickStartModulePropsResourcesSmartStoreS3AccessInstanceProfile",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnQuickStartModulePropsResourcesSmartStoreS3AccessInstanceProfile:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnQuickStartModulePropsResourcesSmartStoreS3AccessInstanceProfile
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnQuickStartModulePropsResourcesSmartStoreS3AccessInstanceProfile#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnQuickStartModulePropsResourcesSmartStoreS3AccessInstanceProfile#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnQuickStartModulePropsResourcesSmartStoreS3AccessInstanceProfile(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnQuickStartModulePropsResourcesSmartStoreS3BucketPolicy",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnQuickStartModulePropsResourcesSmartStoreS3BucketPolicy:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnQuickStartModulePropsResourcesSmartStoreS3BucketPolicy
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnQuickStartModulePropsResourcesSmartStoreS3BucketPolicy#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnQuickStartModulePropsResourcesSmartStoreS3BucketPolicy#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnQuickStartModulePropsResourcesSmartStoreS3BucketPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnQuickStartModulePropsResourcesSmartStoreS3BucketRole",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnQuickStartModulePropsResourcesSmartStoreS3BucketRole:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnQuickStartModulePropsResourcesSmartStoreS3BucketRole
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnQuickStartModulePropsResourcesSmartStoreS3BucketRole#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnQuickStartModulePropsResourcesSmartStoreS3BucketRole#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnQuickStartModulePropsResourcesSmartStoreS3BucketRole(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnQuickStartModulePropsResourcesSplunkCm",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnQuickStartModulePropsResourcesSplunkCm:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnQuickStartModulePropsResourcesSplunkCm
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnQuickStartModulePropsResourcesSplunkCm#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnQuickStartModulePropsResourcesSplunkCm#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnQuickStartModulePropsResourcesSplunkCm(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnQuickStartModulePropsResourcesSplunkCmWaitCondition",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnQuickStartModulePropsResourcesSplunkCmWaitCondition:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnQuickStartModulePropsResourcesSplunkCmWaitCondition
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnQuickStartModulePropsResourcesSplunkCmWaitCondition#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnQuickStartModulePropsResourcesSplunkCmWaitCondition#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnQuickStartModulePropsResourcesSplunkCmWaitCondition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnQuickStartModulePropsResourcesSplunkCmWaitHandle",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnQuickStartModulePropsResourcesSplunkCmWaitHandle:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnQuickStartModulePropsResourcesSplunkCmWaitHandle
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnQuickStartModulePropsResourcesSplunkCmWaitHandle#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnQuickStartModulePropsResourcesSplunkCmWaitHandle#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnQuickStartModulePropsResourcesSplunkCmWaitHandle(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnQuickStartModulePropsResourcesSplunkHttpEventCollectorLoadBalancer",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnQuickStartModulePropsResourcesSplunkHttpEventCollectorLoadBalancer:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnQuickStartModulePropsResourcesSplunkHttpEventCollectorLoadBalancer
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnQuickStartModulePropsResourcesSplunkHttpEventCollectorLoadBalancer#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnQuickStartModulePropsResourcesSplunkHttpEventCollectorLoadBalancer#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnQuickStartModulePropsResourcesSplunkHttpEventCollectorLoadBalancer(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnQuickStartModulePropsResourcesSplunkHttpEventCollectorLoadBalancerSecurityGroup",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnQuickStartModulePropsResourcesSplunkHttpEventCollectorLoadBalancerSecurityGroup:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnQuickStartModulePropsResourcesSplunkHttpEventCollectorLoadBalancerSecurityGroup
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnQuickStartModulePropsResourcesSplunkHttpEventCollectorLoadBalancerSecurityGroup#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnQuickStartModulePropsResourcesSplunkHttpEventCollectorLoadBalancerSecurityGroup#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnQuickStartModulePropsResourcesSplunkHttpEventCollectorLoadBalancerSecurityGroup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnQuickStartModulePropsResourcesSplunkIndexerLaunchConfiguration",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnQuickStartModulePropsResourcesSplunkIndexerLaunchConfiguration:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnQuickStartModulePropsResourcesSplunkIndexerLaunchConfiguration
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnQuickStartModulePropsResourcesSplunkIndexerLaunchConfiguration#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnQuickStartModulePropsResourcesSplunkIndexerLaunchConfiguration#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnQuickStartModulePropsResourcesSplunkIndexerLaunchConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnQuickStartModulePropsResourcesSplunkIndexerNodesAsg",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnQuickStartModulePropsResourcesSplunkIndexerNodesAsg:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnQuickStartModulePropsResourcesSplunkIndexerNodesAsg
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnQuickStartModulePropsResourcesSplunkIndexerNodesAsg#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnQuickStartModulePropsResourcesSplunkIndexerNodesAsg#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnQuickStartModulePropsResourcesSplunkIndexerNodesAsg(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnQuickStartModulePropsResourcesSplunkIndexerSecurityGroup",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnQuickStartModulePropsResourcesSplunkIndexerSecurityGroup:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnQuickStartModulePropsResourcesSplunkIndexerSecurityGroup
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnQuickStartModulePropsResourcesSplunkIndexerSecurityGroup#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnQuickStartModulePropsResourcesSplunkIndexerSecurityGroup#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnQuickStartModulePropsResourcesSplunkIndexerSecurityGroup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnQuickStartModulePropsResourcesSplunkSearchHeadInstance",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnQuickStartModulePropsResourcesSplunkSearchHeadInstance:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnQuickStartModulePropsResourcesSplunkSearchHeadInstance
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnQuickStartModulePropsResourcesSplunkSearchHeadInstance#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnQuickStartModulePropsResourcesSplunkSearchHeadInstance#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnQuickStartModulePropsResourcesSplunkSearchHeadInstance(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnQuickStartModulePropsResourcesSplunkSearchHeadSecurityGroup",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnQuickStartModulePropsResourcesSplunkSearchHeadSecurityGroup:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnQuickStartModulePropsResourcesSplunkSearchHeadSecurityGroup
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnQuickStartModulePropsResourcesSplunkSearchHeadSecurityGroup#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnQuickStartModulePropsResourcesSplunkSearchHeadSecurityGroup#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnQuickStartModulePropsResourcesSplunkSearchHeadSecurityGroup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnQuickStartModulePropsResourcesSplunkSecurityGroup",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnQuickStartModulePropsResourcesSplunkSecurityGroup:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnQuickStartModulePropsResourcesSplunkSecurityGroup
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnQuickStartModulePropsResourcesSplunkSecurityGroup#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnQuickStartModulePropsResourcesSplunkSecurityGroup#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnQuickStartModulePropsResourcesSplunkSecurityGroup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnQuickStartModulePropsResourcesSplunkShcDeployer",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnQuickStartModulePropsResourcesSplunkShcDeployer:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnQuickStartModulePropsResourcesSplunkShcDeployer
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnQuickStartModulePropsResourcesSplunkShcDeployer#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnQuickStartModulePropsResourcesSplunkShcDeployer#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnQuickStartModulePropsResourcesSplunkShcDeployer(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnQuickStartModulePropsResourcesSplunkShcLoadBalancer",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnQuickStartModulePropsResourcesSplunkShcLoadBalancer:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnQuickStartModulePropsResourcesSplunkShcLoadBalancer
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnQuickStartModulePropsResourcesSplunkShcLoadBalancer#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnQuickStartModulePropsResourcesSplunkShcLoadBalancer#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnQuickStartModulePropsResourcesSplunkShcLoadBalancer(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnQuickStartModulePropsResourcesSplunkShcMember1",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnQuickStartModulePropsResourcesSplunkShcMember1:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnQuickStartModulePropsResourcesSplunkShcMember1
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnQuickStartModulePropsResourcesSplunkShcMember1#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnQuickStartModulePropsResourcesSplunkShcMember1#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnQuickStartModulePropsResourcesSplunkShcMember1(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnQuickStartModulePropsResourcesSplunkShcMember2",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnQuickStartModulePropsResourcesSplunkShcMember2:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnQuickStartModulePropsResourcesSplunkShcMember2
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnQuickStartModulePropsResourcesSplunkShcMember2#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnQuickStartModulePropsResourcesSplunkShcMember2#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnQuickStartModulePropsResourcesSplunkShcMember2(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnQuickStartModulePropsResourcesSplunkShcMember3",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnQuickStartModulePropsResourcesSplunkShcMember3:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnQuickStartModulePropsResourcesSplunkShcMember3
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnQuickStartModulePropsResourcesSplunkShcMember3#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnQuickStartModulePropsResourcesSplunkShcMember3#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnQuickStartModulePropsResourcesSplunkShcMember3(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnQuickStartModulePropsResourcesSplunkSmartstoreBucket",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnQuickStartModulePropsResourcesSplunkSmartstoreBucket:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnQuickStartModulePropsResourcesSplunkSmartstoreBucket
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnQuickStartModulePropsResourcesSplunkSmartstoreBucket#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnQuickStartModulePropsResourcesSplunkSmartstoreBucket#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnQuickStartModulePropsResourcesSplunkSmartstoreBucket(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnQuickStartModulePropsResourcesVpc",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnQuickStartModulePropsResourcesVpc:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnQuickStartModulePropsResourcesVpc
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnQuickStartModulePropsResourcesVpc#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnQuickStartModulePropsResourcesVpc#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnQuickStartModulePropsResourcesVpc(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/splunk-enterprise-quickstart-module.CfnQuickStartModulePropsResourcesVpcGatewayAttachment",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnQuickStartModulePropsResourcesVpcGatewayAttachment:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnQuickStartModulePropsResourcesVpcGatewayAttachment
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnQuickStartModulePropsResourcesVpcGatewayAttachment#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnQuickStartModulePropsResourcesVpcGatewayAttachment#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnQuickStartModulePropsResourcesVpcGatewayAttachment(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnQuickStartModule",
    "CfnQuickStartModuleProps",
    "CfnQuickStartModulePropsParameters",
    "CfnQuickStartModulePropsParametersAvailabilityZones",
    "CfnQuickStartModulePropsParametersHecClientLocation",
    "CfnQuickStartModulePropsParametersIndexerInstanceType",
    "CfnQuickStartModulePropsParametersKeyName",
    "CfnQuickStartModulePropsParametersNumberOfAZs",
    "CfnQuickStartModulePropsParametersPublicSubnet1Cidr",
    "CfnQuickStartModulePropsParametersPublicSubnet2Cidr",
    "CfnQuickStartModulePropsParametersPublicSubnet3Cidr",
    "CfnQuickStartModulePropsParametersSearchHeadInstanceType",
    "CfnQuickStartModulePropsParametersShcEnabled",
    "CfnQuickStartModulePropsParametersSmartStoreBucketName",
    "CfnQuickStartModulePropsParametersSplunkAdminPassword",
    "CfnQuickStartModulePropsParametersSplunkClusterSecret",
    "CfnQuickStartModulePropsParametersSplunkIndexerCount",
    "CfnQuickStartModulePropsParametersSplunkIndexerDiscoverySecret",
    "CfnQuickStartModulePropsParametersSplunkIndexerDiskSize",
    "CfnQuickStartModulePropsParametersSplunkLicenseBucket",
    "CfnQuickStartModulePropsParametersSplunkLicensePath",
    "CfnQuickStartModulePropsParametersSplunkReplicationFactor",
    "CfnQuickStartModulePropsParametersSplunkSearchFactor",
    "CfnQuickStartModulePropsParametersSplunkSearchHeadDiskSize",
    "CfnQuickStartModulePropsParametersSshClientLocation",
    "CfnQuickStartModulePropsParametersVpccidr",
    "CfnQuickStartModulePropsParametersWebClientLocation",
    "CfnQuickStartModulePropsResources",
    "CfnQuickStartModulePropsResourcesBucketPolicy",
    "CfnQuickStartModulePropsResourcesCfnKeys",
    "CfnQuickStartModulePropsResourcesCfnUser",
    "CfnQuickStartModulePropsResourcesInternetGateway",
    "CfnQuickStartModulePropsResourcesPublicSubnet1",
    "CfnQuickStartModulePropsResourcesPublicSubnet1RouteTableAssociation",
    "CfnQuickStartModulePropsResourcesPublicSubnet2",
    "CfnQuickStartModulePropsResourcesPublicSubnet2RouteTableAssociation",
    "CfnQuickStartModulePropsResourcesPublicSubnet3",
    "CfnQuickStartModulePropsResourcesPublicSubnet3RouteTableAssociation",
    "CfnQuickStartModulePropsResourcesPublicSubnetRoute",
    "CfnQuickStartModulePropsResourcesPublicSubnetRouteTable",
    "CfnQuickStartModulePropsResourcesSmartStoreS3AccessInstanceProfile",
    "CfnQuickStartModulePropsResourcesSmartStoreS3BucketPolicy",
    "CfnQuickStartModulePropsResourcesSmartStoreS3BucketRole",
    "CfnQuickStartModulePropsResourcesSplunkCm",
    "CfnQuickStartModulePropsResourcesSplunkCmWaitCondition",
    "CfnQuickStartModulePropsResourcesSplunkCmWaitHandle",
    "CfnQuickStartModulePropsResourcesSplunkHttpEventCollectorLoadBalancer",
    "CfnQuickStartModulePropsResourcesSplunkHttpEventCollectorLoadBalancerSecurityGroup",
    "CfnQuickStartModulePropsResourcesSplunkIndexerLaunchConfiguration",
    "CfnQuickStartModulePropsResourcesSplunkIndexerNodesAsg",
    "CfnQuickStartModulePropsResourcesSplunkIndexerSecurityGroup",
    "CfnQuickStartModulePropsResourcesSplunkSearchHeadInstance",
    "CfnQuickStartModulePropsResourcesSplunkSearchHeadSecurityGroup",
    "CfnQuickStartModulePropsResourcesSplunkSecurityGroup",
    "CfnQuickStartModulePropsResourcesSplunkShcDeployer",
    "CfnQuickStartModulePropsResourcesSplunkShcLoadBalancer",
    "CfnQuickStartModulePropsResourcesSplunkShcMember1",
    "CfnQuickStartModulePropsResourcesSplunkShcMember2",
    "CfnQuickStartModulePropsResourcesSplunkShcMember3",
    "CfnQuickStartModulePropsResourcesSplunkSmartstoreBucket",
    "CfnQuickStartModulePropsResourcesVpc",
    "CfnQuickStartModulePropsResourcesVpcGatewayAttachment",
]

publication.publish()
