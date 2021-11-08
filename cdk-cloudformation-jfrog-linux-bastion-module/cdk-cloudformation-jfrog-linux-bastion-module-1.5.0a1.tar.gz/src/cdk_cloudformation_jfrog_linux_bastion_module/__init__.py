'''
# AWS CDK CloudFormation Constructs for JFrog::Linux::Bastion::MODULE

Schema for Module Fragment of type JFrog::Linux::Bastion::MODULE

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
    jsii_type="@cdk-cloudformation/jfrog-linux-bastion-module.CfnModule",
):
    '''A CloudFormation ``JFrog::Linux::Bastion::MODULE``.

    :cloudformationResource: JFrog::Linux::Bastion::MODULE
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
        '''Create a new ``JFrog::Linux::Bastion::MODULE``.

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
    jsii_type="@cdk-cloudformation/jfrog-linux-bastion-module.CfnModuleProps",
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
        '''Schema for Module Fragment of type JFrog::Linux::Bastion::MODULE.

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
    jsii_type="@cdk-cloudformation/jfrog-linux-bastion-module.CfnModulePropsParameters",
    jsii_struct_bases=[],
    name_mapping={
        "alternative_initialization_script": "alternativeInitializationScript",
        "bastion_amios": "bastionAmios",
        "bastion_banner": "bastionBanner",
        "bastion_host_name": "bastionHostName",
        "bastion_instance_type": "bastionInstanceType",
        "bastion_tenancy": "bastionTenancy",
        "enable_banner": "enableBanner",
        "enable_tcp_forwarding": "enableTcpForwarding",
        "enable_x11_forwarding": "enableX11Forwarding",
        "environment_variables": "environmentVariables",
        "key_pair_name": "keyPairName",
        "logical_id": "logicalId",
        "num_bastion_hosts": "numBastionHosts",
        "os_image_override": "osImageOverride",
        "public_subnet1_id": "publicSubnet1Id",
        "public_subnet2_id": "publicSubnet2Id",
        "qss3_bucket_name": "qss3BucketName",
        "qss3_bucket_region": "qss3BucketRegion",
        "qss3_key_prefix": "qss3KeyPrefix",
        "remote_access_cidr": "remoteAccessCidr",
        "root_volume_size": "rootVolumeSize",
        "vpcid": "vpcid",
    },
)
class CfnModulePropsParameters:
    def __init__(
        self,
        *,
        alternative_initialization_script: typing.Optional["CfnModulePropsParametersAlternativeInitializationScript"] = None,
        bastion_amios: typing.Optional["CfnModulePropsParametersBastionAmios"] = None,
        bastion_banner: typing.Optional["CfnModulePropsParametersBastionBanner"] = None,
        bastion_host_name: typing.Optional["CfnModulePropsParametersBastionHostName"] = None,
        bastion_instance_type: typing.Optional["CfnModulePropsParametersBastionInstanceType"] = None,
        bastion_tenancy: typing.Optional["CfnModulePropsParametersBastionTenancy"] = None,
        enable_banner: typing.Optional["CfnModulePropsParametersEnableBanner"] = None,
        enable_tcp_forwarding: typing.Optional["CfnModulePropsParametersEnableTcpForwarding"] = None,
        enable_x11_forwarding: typing.Optional["CfnModulePropsParametersEnableX11Forwarding"] = None,
        environment_variables: typing.Optional["CfnModulePropsParametersEnvironmentVariables"] = None,
        key_pair_name: typing.Optional["CfnModulePropsParametersKeyPairName"] = None,
        logical_id: typing.Optional["CfnModulePropsParametersLogicalId"] = None,
        num_bastion_hosts: typing.Optional["CfnModulePropsParametersNumBastionHosts"] = None,
        os_image_override: typing.Optional["CfnModulePropsParametersOsImageOverride"] = None,
        public_subnet1_id: typing.Optional["CfnModulePropsParametersPublicSubnet1Id"] = None,
        public_subnet2_id: typing.Optional["CfnModulePropsParametersPublicSubnet2Id"] = None,
        qss3_bucket_name: typing.Optional["CfnModulePropsParametersQss3BucketName"] = None,
        qss3_bucket_region: typing.Optional["CfnModulePropsParametersQss3BucketRegion"] = None,
        qss3_key_prefix: typing.Optional["CfnModulePropsParametersQss3KeyPrefix"] = None,
        remote_access_cidr: typing.Optional["CfnModulePropsParametersRemoteAccessCidr"] = None,
        root_volume_size: typing.Optional["CfnModulePropsParametersRootVolumeSize"] = None,
        vpcid: typing.Optional["CfnModulePropsParametersVpcid"] = None,
    ) -> None:
        '''
        :param alternative_initialization_script: An alternative initialization script to run during setup.
        :param bastion_amios: The Linux distribution for the AMI to be used for the bastion instances.
        :param bastion_banner: Banner text to display upon login.
        :param bastion_host_name: The value used for the name tag of the bastion host.
        :param bastion_instance_type: Amazon EC2 instance type for the bastion instances.
        :param bastion_tenancy: VPC tenancy to launch the bastion in. Options: 'dedicated' or 'default'
        :param enable_banner: To include a banner to be displayed when connecting via SSH to the bastion, choose true.
        :param enable_tcp_forwarding: To enable TCP forwarding, choose true.
        :param enable_x11_forwarding: To enable X11 forwarding, choose true.
        :param environment_variables: A comma-separated list of environment variables for use in bootstrapping. Variables must be in the format KEY=VALUE. VALUE cannot contain commas.
        :param key_pair_name: Name of an existing public/private key pair. If you do not have one in this AWS Region, please create it before continuing.
        :param logical_id: Logical Id of the MODULE.
        :param num_bastion_hosts: The number of bastion hosts to create. The maximum number is four.
        :param os_image_override: The Region-specific image to use for the instance.
        :param public_subnet1_id: ID of the public subnet in Availability Zone 1 of your existing VPC (e.g., subnet-z0376dab).
        :param public_subnet2_id: ID of the public subnet in Availability Zone 1 of your existing VPC (e.g., subnet-z0376dab).
        :param qss3_bucket_name: S3 bucket name for the Quick Start assets. Quick Start bucket name can include numbers, lowercase letters, uppercase letters, and hyphens (-). It cannot start or end with a hyphen (-).
        :param qss3_bucket_region: The AWS Region where the Quick Start S3 bucket (QSS3BucketName) is hosted. When using your own bucket, you must specify this value.
        :param qss3_key_prefix: S3 key prefix for the Quick Start assets. Quick Start key prefix can include numbers, lowercase letters, uppercase letters, hyphens (-), dots (.) and forward slash (/) and it should end with a forward slash (/).
        :param remote_access_cidr: Allowed CIDR block for external SSH access to the bastions.
        :param root_volume_size: The size in GB for the root EBS volume.
        :param vpcid: ID of the VPC (e.g., vpc-0343606e).

        :schema: CfnModulePropsParameters
        '''
        if isinstance(alternative_initialization_script, dict):
            alternative_initialization_script = CfnModulePropsParametersAlternativeInitializationScript(**alternative_initialization_script)
        if isinstance(bastion_amios, dict):
            bastion_amios = CfnModulePropsParametersBastionAmios(**bastion_amios)
        if isinstance(bastion_banner, dict):
            bastion_banner = CfnModulePropsParametersBastionBanner(**bastion_banner)
        if isinstance(bastion_host_name, dict):
            bastion_host_name = CfnModulePropsParametersBastionHostName(**bastion_host_name)
        if isinstance(bastion_instance_type, dict):
            bastion_instance_type = CfnModulePropsParametersBastionInstanceType(**bastion_instance_type)
        if isinstance(bastion_tenancy, dict):
            bastion_tenancy = CfnModulePropsParametersBastionTenancy(**bastion_tenancy)
        if isinstance(enable_banner, dict):
            enable_banner = CfnModulePropsParametersEnableBanner(**enable_banner)
        if isinstance(enable_tcp_forwarding, dict):
            enable_tcp_forwarding = CfnModulePropsParametersEnableTcpForwarding(**enable_tcp_forwarding)
        if isinstance(enable_x11_forwarding, dict):
            enable_x11_forwarding = CfnModulePropsParametersEnableX11Forwarding(**enable_x11_forwarding)
        if isinstance(environment_variables, dict):
            environment_variables = CfnModulePropsParametersEnvironmentVariables(**environment_variables)
        if isinstance(key_pair_name, dict):
            key_pair_name = CfnModulePropsParametersKeyPairName(**key_pair_name)
        if isinstance(logical_id, dict):
            logical_id = CfnModulePropsParametersLogicalId(**logical_id)
        if isinstance(num_bastion_hosts, dict):
            num_bastion_hosts = CfnModulePropsParametersNumBastionHosts(**num_bastion_hosts)
        if isinstance(os_image_override, dict):
            os_image_override = CfnModulePropsParametersOsImageOverride(**os_image_override)
        if isinstance(public_subnet1_id, dict):
            public_subnet1_id = CfnModulePropsParametersPublicSubnet1Id(**public_subnet1_id)
        if isinstance(public_subnet2_id, dict):
            public_subnet2_id = CfnModulePropsParametersPublicSubnet2Id(**public_subnet2_id)
        if isinstance(qss3_bucket_name, dict):
            qss3_bucket_name = CfnModulePropsParametersQss3BucketName(**qss3_bucket_name)
        if isinstance(qss3_bucket_region, dict):
            qss3_bucket_region = CfnModulePropsParametersQss3BucketRegion(**qss3_bucket_region)
        if isinstance(qss3_key_prefix, dict):
            qss3_key_prefix = CfnModulePropsParametersQss3KeyPrefix(**qss3_key_prefix)
        if isinstance(remote_access_cidr, dict):
            remote_access_cidr = CfnModulePropsParametersRemoteAccessCidr(**remote_access_cidr)
        if isinstance(root_volume_size, dict):
            root_volume_size = CfnModulePropsParametersRootVolumeSize(**root_volume_size)
        if isinstance(vpcid, dict):
            vpcid = CfnModulePropsParametersVpcid(**vpcid)
        self._values: typing.Dict[str, typing.Any] = {}
        if alternative_initialization_script is not None:
            self._values["alternative_initialization_script"] = alternative_initialization_script
        if bastion_amios is not None:
            self._values["bastion_amios"] = bastion_amios
        if bastion_banner is not None:
            self._values["bastion_banner"] = bastion_banner
        if bastion_host_name is not None:
            self._values["bastion_host_name"] = bastion_host_name
        if bastion_instance_type is not None:
            self._values["bastion_instance_type"] = bastion_instance_type
        if bastion_tenancy is not None:
            self._values["bastion_tenancy"] = bastion_tenancy
        if enable_banner is not None:
            self._values["enable_banner"] = enable_banner
        if enable_tcp_forwarding is not None:
            self._values["enable_tcp_forwarding"] = enable_tcp_forwarding
        if enable_x11_forwarding is not None:
            self._values["enable_x11_forwarding"] = enable_x11_forwarding
        if environment_variables is not None:
            self._values["environment_variables"] = environment_variables
        if key_pair_name is not None:
            self._values["key_pair_name"] = key_pair_name
        if logical_id is not None:
            self._values["logical_id"] = logical_id
        if num_bastion_hosts is not None:
            self._values["num_bastion_hosts"] = num_bastion_hosts
        if os_image_override is not None:
            self._values["os_image_override"] = os_image_override
        if public_subnet1_id is not None:
            self._values["public_subnet1_id"] = public_subnet1_id
        if public_subnet2_id is not None:
            self._values["public_subnet2_id"] = public_subnet2_id
        if qss3_bucket_name is not None:
            self._values["qss3_bucket_name"] = qss3_bucket_name
        if qss3_bucket_region is not None:
            self._values["qss3_bucket_region"] = qss3_bucket_region
        if qss3_key_prefix is not None:
            self._values["qss3_key_prefix"] = qss3_key_prefix
        if remote_access_cidr is not None:
            self._values["remote_access_cidr"] = remote_access_cidr
        if root_volume_size is not None:
            self._values["root_volume_size"] = root_volume_size
        if vpcid is not None:
            self._values["vpcid"] = vpcid

    @builtins.property
    def alternative_initialization_script(
        self,
    ) -> typing.Optional["CfnModulePropsParametersAlternativeInitializationScript"]:
        '''An alternative initialization script to run during setup.

        :schema: CfnModulePropsParameters#AlternativeInitializationScript
        '''
        result = self._values.get("alternative_initialization_script")
        return typing.cast(typing.Optional["CfnModulePropsParametersAlternativeInitializationScript"], result)

    @builtins.property
    def bastion_amios(self) -> typing.Optional["CfnModulePropsParametersBastionAmios"]:
        '''The Linux distribution for the AMI to be used for the bastion instances.

        :schema: CfnModulePropsParameters#BastionAMIOS
        '''
        result = self._values.get("bastion_amios")
        return typing.cast(typing.Optional["CfnModulePropsParametersBastionAmios"], result)

    @builtins.property
    def bastion_banner(
        self,
    ) -> typing.Optional["CfnModulePropsParametersBastionBanner"]:
        '''Banner text to display upon login.

        :schema: CfnModulePropsParameters#BastionBanner
        '''
        result = self._values.get("bastion_banner")
        return typing.cast(typing.Optional["CfnModulePropsParametersBastionBanner"], result)

    @builtins.property
    def bastion_host_name(
        self,
    ) -> typing.Optional["CfnModulePropsParametersBastionHostName"]:
        '''The value used for the name tag of the bastion host.

        :schema: CfnModulePropsParameters#BastionHostName
        '''
        result = self._values.get("bastion_host_name")
        return typing.cast(typing.Optional["CfnModulePropsParametersBastionHostName"], result)

    @builtins.property
    def bastion_instance_type(
        self,
    ) -> typing.Optional["CfnModulePropsParametersBastionInstanceType"]:
        '''Amazon EC2 instance type for the bastion instances.

        :schema: CfnModulePropsParameters#BastionInstanceType
        '''
        result = self._values.get("bastion_instance_type")
        return typing.cast(typing.Optional["CfnModulePropsParametersBastionInstanceType"], result)

    @builtins.property
    def bastion_tenancy(
        self,
    ) -> typing.Optional["CfnModulePropsParametersBastionTenancy"]:
        '''VPC tenancy to launch the bastion in.

        Options: 'dedicated' or 'default'

        :schema: CfnModulePropsParameters#BastionTenancy
        '''
        result = self._values.get("bastion_tenancy")
        return typing.cast(typing.Optional["CfnModulePropsParametersBastionTenancy"], result)

    @builtins.property
    def enable_banner(self) -> typing.Optional["CfnModulePropsParametersEnableBanner"]:
        '''To include a banner to be displayed when connecting via SSH to the bastion, choose true.

        :schema: CfnModulePropsParameters#EnableBanner
        '''
        result = self._values.get("enable_banner")
        return typing.cast(typing.Optional["CfnModulePropsParametersEnableBanner"], result)

    @builtins.property
    def enable_tcp_forwarding(
        self,
    ) -> typing.Optional["CfnModulePropsParametersEnableTcpForwarding"]:
        '''To enable TCP forwarding, choose true.

        :schema: CfnModulePropsParameters#EnableTCPForwarding
        '''
        result = self._values.get("enable_tcp_forwarding")
        return typing.cast(typing.Optional["CfnModulePropsParametersEnableTcpForwarding"], result)

    @builtins.property
    def enable_x11_forwarding(
        self,
    ) -> typing.Optional["CfnModulePropsParametersEnableX11Forwarding"]:
        '''To enable X11 forwarding, choose true.

        :schema: CfnModulePropsParameters#EnableX11Forwarding
        '''
        result = self._values.get("enable_x11_forwarding")
        return typing.cast(typing.Optional["CfnModulePropsParametersEnableX11Forwarding"], result)

    @builtins.property
    def environment_variables(
        self,
    ) -> typing.Optional["CfnModulePropsParametersEnvironmentVariables"]:
        '''A comma-separated list of environment variables for use in bootstrapping.

        Variables must be in the format KEY=VALUE. VALUE cannot contain commas.

        :schema: CfnModulePropsParameters#EnvironmentVariables
        '''
        result = self._values.get("environment_variables")
        return typing.cast(typing.Optional["CfnModulePropsParametersEnvironmentVariables"], result)

    @builtins.property
    def key_pair_name(self) -> typing.Optional["CfnModulePropsParametersKeyPairName"]:
        '''Name of an existing public/private key pair.

        If you do not have one in this AWS Region, please create it before continuing.

        :schema: CfnModulePropsParameters#KeyPairName
        '''
        result = self._values.get("key_pair_name")
        return typing.cast(typing.Optional["CfnModulePropsParametersKeyPairName"], result)

    @builtins.property
    def logical_id(self) -> typing.Optional["CfnModulePropsParametersLogicalId"]:
        '''Logical Id of the MODULE.

        :schema: CfnModulePropsParameters#LogicalId
        '''
        result = self._values.get("logical_id")
        return typing.cast(typing.Optional["CfnModulePropsParametersLogicalId"], result)

    @builtins.property
    def num_bastion_hosts(
        self,
    ) -> typing.Optional["CfnModulePropsParametersNumBastionHosts"]:
        '''The number of bastion hosts to create.

        The maximum number is four.

        :schema: CfnModulePropsParameters#NumBastionHosts
        '''
        result = self._values.get("num_bastion_hosts")
        return typing.cast(typing.Optional["CfnModulePropsParametersNumBastionHosts"], result)

    @builtins.property
    def os_image_override(
        self,
    ) -> typing.Optional["CfnModulePropsParametersOsImageOverride"]:
        '''The Region-specific image to use for the instance.

        :schema: CfnModulePropsParameters#OSImageOverride
        '''
        result = self._values.get("os_image_override")
        return typing.cast(typing.Optional["CfnModulePropsParametersOsImageOverride"], result)

    @builtins.property
    def public_subnet1_id(
        self,
    ) -> typing.Optional["CfnModulePropsParametersPublicSubnet1Id"]:
        '''ID of the public subnet in Availability Zone 1 of your existing VPC (e.g., subnet-z0376dab).

        :schema: CfnModulePropsParameters#PublicSubnet1Id
        '''
        result = self._values.get("public_subnet1_id")
        return typing.cast(typing.Optional["CfnModulePropsParametersPublicSubnet1Id"], result)

    @builtins.property
    def public_subnet2_id(
        self,
    ) -> typing.Optional["CfnModulePropsParametersPublicSubnet2Id"]:
        '''ID of the public subnet in Availability Zone 1 of your existing VPC (e.g., subnet-z0376dab).

        :schema: CfnModulePropsParameters#PublicSubnet2Id
        '''
        result = self._values.get("public_subnet2_id")
        return typing.cast(typing.Optional["CfnModulePropsParametersPublicSubnet2Id"], result)

    @builtins.property
    def qss3_bucket_name(
        self,
    ) -> typing.Optional["CfnModulePropsParametersQss3BucketName"]:
        '''S3 bucket name for the Quick Start assets.

        Quick Start bucket name can include numbers, lowercase letters, uppercase letters, and hyphens (-). It cannot start or end with a hyphen (-).

        :schema: CfnModulePropsParameters#QSS3BucketName
        '''
        result = self._values.get("qss3_bucket_name")
        return typing.cast(typing.Optional["CfnModulePropsParametersQss3BucketName"], result)

    @builtins.property
    def qss3_bucket_region(
        self,
    ) -> typing.Optional["CfnModulePropsParametersQss3BucketRegion"]:
        '''The AWS Region where the Quick Start S3 bucket (QSS3BucketName) is hosted.

        When using your own bucket, you must specify this value.

        :schema: CfnModulePropsParameters#QSS3BucketRegion
        '''
        result = self._values.get("qss3_bucket_region")
        return typing.cast(typing.Optional["CfnModulePropsParametersQss3BucketRegion"], result)

    @builtins.property
    def qss3_key_prefix(
        self,
    ) -> typing.Optional["CfnModulePropsParametersQss3KeyPrefix"]:
        '''S3 key prefix for the Quick Start assets.

        Quick Start key prefix can include numbers, lowercase letters, uppercase letters, hyphens (-), dots (.) and forward slash (/) and it should end with a forward slash (/).

        :schema: CfnModulePropsParameters#QSS3KeyPrefix
        '''
        result = self._values.get("qss3_key_prefix")
        return typing.cast(typing.Optional["CfnModulePropsParametersQss3KeyPrefix"], result)

    @builtins.property
    def remote_access_cidr(
        self,
    ) -> typing.Optional["CfnModulePropsParametersRemoteAccessCidr"]:
        '''Allowed CIDR block for external SSH access to the bastions.

        :schema: CfnModulePropsParameters#RemoteAccessCIDR
        '''
        result = self._values.get("remote_access_cidr")
        return typing.cast(typing.Optional["CfnModulePropsParametersRemoteAccessCidr"], result)

    @builtins.property
    def root_volume_size(
        self,
    ) -> typing.Optional["CfnModulePropsParametersRootVolumeSize"]:
        '''The size in GB for the root EBS volume.

        :schema: CfnModulePropsParameters#RootVolumeSize
        '''
        result = self._values.get("root_volume_size")
        return typing.cast(typing.Optional["CfnModulePropsParametersRootVolumeSize"], result)

    @builtins.property
    def vpcid(self) -> typing.Optional["CfnModulePropsParametersVpcid"]:
        '''ID of the VPC (e.g., vpc-0343606e).

        :schema: CfnModulePropsParameters#VPCID
        '''
        result = self._values.get("vpcid")
        return typing.cast(typing.Optional["CfnModulePropsParametersVpcid"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-linux-bastion-module.CfnModulePropsParametersAlternativeInitializationScript",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersAlternativeInitializationScript:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''An alternative initialization script to run during setup.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersAlternativeInitializationScript
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersAlternativeInitializationScript#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersAlternativeInitializationScript#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersAlternativeInitializationScript(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-linux-bastion-module.CfnModulePropsParametersBastionAmios",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersBastionAmios:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The Linux distribution for the AMI to be used for the bastion instances.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersBastionAmios
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersBastionAmios#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersBastionAmios#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersBastionAmios(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-linux-bastion-module.CfnModulePropsParametersBastionBanner",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersBastionBanner:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Banner text to display upon login.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersBastionBanner
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersBastionBanner#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersBastionBanner#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersBastionBanner(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-linux-bastion-module.CfnModulePropsParametersBastionHostName",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersBastionHostName:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The value used for the name tag of the bastion host.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersBastionHostName
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersBastionHostName#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersBastionHostName#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersBastionHostName(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-linux-bastion-module.CfnModulePropsParametersBastionInstanceType",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersBastionInstanceType:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Amazon EC2 instance type for the bastion instances.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersBastionInstanceType
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersBastionInstanceType#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersBastionInstanceType#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersBastionInstanceType(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-linux-bastion-module.CfnModulePropsParametersBastionTenancy",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersBastionTenancy:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''VPC tenancy to launch the bastion in.

        Options: 'dedicated' or 'default'

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersBastionTenancy
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersBastionTenancy#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersBastionTenancy#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersBastionTenancy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-linux-bastion-module.CfnModulePropsParametersEnableBanner",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersEnableBanner:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''To include a banner to be displayed when connecting via SSH to the bastion, choose true.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersEnableBanner
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersEnableBanner#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersEnableBanner#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersEnableBanner(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-linux-bastion-module.CfnModulePropsParametersEnableTcpForwarding",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersEnableTcpForwarding:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''To enable TCP forwarding, choose true.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersEnableTcpForwarding
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersEnableTcpForwarding#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersEnableTcpForwarding#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersEnableTcpForwarding(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-linux-bastion-module.CfnModulePropsParametersEnableX11Forwarding",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersEnableX11Forwarding:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''To enable X11 forwarding, choose true.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersEnableX11Forwarding
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersEnableX11Forwarding#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersEnableX11Forwarding#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersEnableX11Forwarding(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-linux-bastion-module.CfnModulePropsParametersEnvironmentVariables",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersEnvironmentVariables:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''A comma-separated list of environment variables for use in bootstrapping.

        Variables must be in the format KEY=VALUE. VALUE cannot contain commas.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersEnvironmentVariables
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersEnvironmentVariables#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersEnvironmentVariables#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersEnvironmentVariables(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-linux-bastion-module.CfnModulePropsParametersKeyPairName",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersKeyPairName:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Name of an existing public/private key pair.

        If you do not have one in this AWS Region, please create it before continuing.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersKeyPairName
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersKeyPairName#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersKeyPairName#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersKeyPairName(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-linux-bastion-module.CfnModulePropsParametersLogicalId",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersLogicalId:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Logical Id of the MODULE.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersLogicalId
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersLogicalId#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersLogicalId#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersLogicalId(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-linux-bastion-module.CfnModulePropsParametersNumBastionHosts",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersNumBastionHosts:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The number of bastion hosts to create.

        The maximum number is four.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersNumBastionHosts
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersNumBastionHosts#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersNumBastionHosts#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersNumBastionHosts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-linux-bastion-module.CfnModulePropsParametersOsImageOverride",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersOsImageOverride:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The Region-specific image to use for the instance.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersOsImageOverride
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersOsImageOverride#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersOsImageOverride#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersOsImageOverride(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-linux-bastion-module.CfnModulePropsParametersPublicSubnet1Id",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersPublicSubnet1Id:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''ID of the public subnet in Availability Zone 1 of your existing VPC (e.g., subnet-z0376dab).

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersPublicSubnet1Id
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersPublicSubnet1Id#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersPublicSubnet1Id#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersPublicSubnet1Id(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-linux-bastion-module.CfnModulePropsParametersPublicSubnet2Id",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersPublicSubnet2Id:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''ID of the public subnet in Availability Zone 1 of your existing VPC (e.g., subnet-z0376dab).

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersPublicSubnet2Id
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersPublicSubnet2Id#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersPublicSubnet2Id#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersPublicSubnet2Id(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-linux-bastion-module.CfnModulePropsParametersQss3BucketName",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersQss3BucketName:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''S3 bucket name for the Quick Start assets.

        Quick Start bucket name can include numbers, lowercase letters, uppercase letters, and hyphens (-). It cannot start or end with a hyphen (-).

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersQss3BucketName
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersQss3BucketName#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersQss3BucketName#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersQss3BucketName(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-linux-bastion-module.CfnModulePropsParametersQss3BucketRegion",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersQss3BucketRegion:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The AWS Region where the Quick Start S3 bucket (QSS3BucketName) is hosted.

        When using your own bucket, you must specify this value.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersQss3BucketRegion
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersQss3BucketRegion#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersQss3BucketRegion#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersQss3BucketRegion(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-linux-bastion-module.CfnModulePropsParametersQss3KeyPrefix",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersQss3KeyPrefix:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''S3 key prefix for the Quick Start assets.

        Quick Start key prefix can include numbers, lowercase letters, uppercase letters, hyphens (-), dots (.) and forward slash (/) and it should end with a forward slash (/).

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersQss3KeyPrefix
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersQss3KeyPrefix#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersQss3KeyPrefix#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersQss3KeyPrefix(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-linux-bastion-module.CfnModulePropsParametersRemoteAccessCidr",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersRemoteAccessCidr:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Allowed CIDR block for external SSH access to the bastions.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersRemoteAccessCidr
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersRemoteAccessCidr#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersRemoteAccessCidr#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersRemoteAccessCidr(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-linux-bastion-module.CfnModulePropsParametersRootVolumeSize",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersRootVolumeSize:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The size in GB for the root EBS volume.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersRootVolumeSize
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersRootVolumeSize#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersRootVolumeSize#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersRootVolumeSize(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-linux-bastion-module.CfnModulePropsParametersVpcid",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersVpcid:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''ID of the VPC (e.g., vpc-0343606e).

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersVpcid
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersVpcid#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersVpcid#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersVpcid(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-linux-bastion-module.CfnModulePropsResources",
    jsii_struct_bases=[],
    name_mapping={
        "bastion_auto_scaling_group": "bastionAutoScalingGroup",
        "bastion_host_policy": "bastionHostPolicy",
        "bastion_host_profile": "bastionHostProfile",
        "bastion_host_role": "bastionHostRole",
        "bastion_launch_configuration": "bastionLaunchConfiguration",
        "bastion_main_log_group": "bastionMainLogGroup",
        "bastion_security_group": "bastionSecurityGroup",
        "eip1": "eip1",
        "eip2": "eip2",
        "eip3": "eip3",
        "eip4": "eip4",
        "ssh_metric_filter": "sshMetricFilter",
    },
)
class CfnModulePropsResources:
    def __init__(
        self,
        *,
        bastion_auto_scaling_group: typing.Optional["CfnModulePropsResourcesBastionAutoScalingGroup"] = None,
        bastion_host_policy: typing.Optional["CfnModulePropsResourcesBastionHostPolicy"] = None,
        bastion_host_profile: typing.Optional["CfnModulePropsResourcesBastionHostProfile"] = None,
        bastion_host_role: typing.Optional["CfnModulePropsResourcesBastionHostRole"] = None,
        bastion_launch_configuration: typing.Optional["CfnModulePropsResourcesBastionLaunchConfiguration"] = None,
        bastion_main_log_group: typing.Optional["CfnModulePropsResourcesBastionMainLogGroup"] = None,
        bastion_security_group: typing.Optional["CfnModulePropsResourcesBastionSecurityGroup"] = None,
        eip1: typing.Optional["CfnModulePropsResourcesEip1"] = None,
        eip2: typing.Optional["CfnModulePropsResourcesEip2"] = None,
        eip3: typing.Optional["CfnModulePropsResourcesEip3"] = None,
        eip4: typing.Optional["CfnModulePropsResourcesEip4"] = None,
        ssh_metric_filter: typing.Optional["CfnModulePropsResourcesSshMetricFilter"] = None,
    ) -> None:
        '''
        :param bastion_auto_scaling_group: 
        :param bastion_host_policy: 
        :param bastion_host_profile: 
        :param bastion_host_role: 
        :param bastion_launch_configuration: 
        :param bastion_main_log_group: 
        :param bastion_security_group: 
        :param eip1: 
        :param eip2: 
        :param eip3: 
        :param eip4: 
        :param ssh_metric_filter: 

        :schema: CfnModulePropsResources
        '''
        if isinstance(bastion_auto_scaling_group, dict):
            bastion_auto_scaling_group = CfnModulePropsResourcesBastionAutoScalingGroup(**bastion_auto_scaling_group)
        if isinstance(bastion_host_policy, dict):
            bastion_host_policy = CfnModulePropsResourcesBastionHostPolicy(**bastion_host_policy)
        if isinstance(bastion_host_profile, dict):
            bastion_host_profile = CfnModulePropsResourcesBastionHostProfile(**bastion_host_profile)
        if isinstance(bastion_host_role, dict):
            bastion_host_role = CfnModulePropsResourcesBastionHostRole(**bastion_host_role)
        if isinstance(bastion_launch_configuration, dict):
            bastion_launch_configuration = CfnModulePropsResourcesBastionLaunchConfiguration(**bastion_launch_configuration)
        if isinstance(bastion_main_log_group, dict):
            bastion_main_log_group = CfnModulePropsResourcesBastionMainLogGroup(**bastion_main_log_group)
        if isinstance(bastion_security_group, dict):
            bastion_security_group = CfnModulePropsResourcesBastionSecurityGroup(**bastion_security_group)
        if isinstance(eip1, dict):
            eip1 = CfnModulePropsResourcesEip1(**eip1)
        if isinstance(eip2, dict):
            eip2 = CfnModulePropsResourcesEip2(**eip2)
        if isinstance(eip3, dict):
            eip3 = CfnModulePropsResourcesEip3(**eip3)
        if isinstance(eip4, dict):
            eip4 = CfnModulePropsResourcesEip4(**eip4)
        if isinstance(ssh_metric_filter, dict):
            ssh_metric_filter = CfnModulePropsResourcesSshMetricFilter(**ssh_metric_filter)
        self._values: typing.Dict[str, typing.Any] = {}
        if bastion_auto_scaling_group is not None:
            self._values["bastion_auto_scaling_group"] = bastion_auto_scaling_group
        if bastion_host_policy is not None:
            self._values["bastion_host_policy"] = bastion_host_policy
        if bastion_host_profile is not None:
            self._values["bastion_host_profile"] = bastion_host_profile
        if bastion_host_role is not None:
            self._values["bastion_host_role"] = bastion_host_role
        if bastion_launch_configuration is not None:
            self._values["bastion_launch_configuration"] = bastion_launch_configuration
        if bastion_main_log_group is not None:
            self._values["bastion_main_log_group"] = bastion_main_log_group
        if bastion_security_group is not None:
            self._values["bastion_security_group"] = bastion_security_group
        if eip1 is not None:
            self._values["eip1"] = eip1
        if eip2 is not None:
            self._values["eip2"] = eip2
        if eip3 is not None:
            self._values["eip3"] = eip3
        if eip4 is not None:
            self._values["eip4"] = eip4
        if ssh_metric_filter is not None:
            self._values["ssh_metric_filter"] = ssh_metric_filter

    @builtins.property
    def bastion_auto_scaling_group(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesBastionAutoScalingGroup"]:
        '''
        :schema: CfnModulePropsResources#BastionAutoScalingGroup
        '''
        result = self._values.get("bastion_auto_scaling_group")
        return typing.cast(typing.Optional["CfnModulePropsResourcesBastionAutoScalingGroup"], result)

    @builtins.property
    def bastion_host_policy(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesBastionHostPolicy"]:
        '''
        :schema: CfnModulePropsResources#BastionHostPolicy
        '''
        result = self._values.get("bastion_host_policy")
        return typing.cast(typing.Optional["CfnModulePropsResourcesBastionHostPolicy"], result)

    @builtins.property
    def bastion_host_profile(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesBastionHostProfile"]:
        '''
        :schema: CfnModulePropsResources#BastionHostProfile
        '''
        result = self._values.get("bastion_host_profile")
        return typing.cast(typing.Optional["CfnModulePropsResourcesBastionHostProfile"], result)

    @builtins.property
    def bastion_host_role(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesBastionHostRole"]:
        '''
        :schema: CfnModulePropsResources#BastionHostRole
        '''
        result = self._values.get("bastion_host_role")
        return typing.cast(typing.Optional["CfnModulePropsResourcesBastionHostRole"], result)

    @builtins.property
    def bastion_launch_configuration(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesBastionLaunchConfiguration"]:
        '''
        :schema: CfnModulePropsResources#BastionLaunchConfiguration
        '''
        result = self._values.get("bastion_launch_configuration")
        return typing.cast(typing.Optional["CfnModulePropsResourcesBastionLaunchConfiguration"], result)

    @builtins.property
    def bastion_main_log_group(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesBastionMainLogGroup"]:
        '''
        :schema: CfnModulePropsResources#BastionMainLogGroup
        '''
        result = self._values.get("bastion_main_log_group")
        return typing.cast(typing.Optional["CfnModulePropsResourcesBastionMainLogGroup"], result)

    @builtins.property
    def bastion_security_group(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesBastionSecurityGroup"]:
        '''
        :schema: CfnModulePropsResources#BastionSecurityGroup
        '''
        result = self._values.get("bastion_security_group")
        return typing.cast(typing.Optional["CfnModulePropsResourcesBastionSecurityGroup"], result)

    @builtins.property
    def eip1(self) -> typing.Optional["CfnModulePropsResourcesEip1"]:
        '''
        :schema: CfnModulePropsResources#EIP1
        '''
        result = self._values.get("eip1")
        return typing.cast(typing.Optional["CfnModulePropsResourcesEip1"], result)

    @builtins.property
    def eip2(self) -> typing.Optional["CfnModulePropsResourcesEip2"]:
        '''
        :schema: CfnModulePropsResources#EIP2
        '''
        result = self._values.get("eip2")
        return typing.cast(typing.Optional["CfnModulePropsResourcesEip2"], result)

    @builtins.property
    def eip3(self) -> typing.Optional["CfnModulePropsResourcesEip3"]:
        '''
        :schema: CfnModulePropsResources#EIP3
        '''
        result = self._values.get("eip3")
        return typing.cast(typing.Optional["CfnModulePropsResourcesEip3"], result)

    @builtins.property
    def eip4(self) -> typing.Optional["CfnModulePropsResourcesEip4"]:
        '''
        :schema: CfnModulePropsResources#EIP4
        '''
        result = self._values.get("eip4")
        return typing.cast(typing.Optional["CfnModulePropsResourcesEip4"], result)

    @builtins.property
    def ssh_metric_filter(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesSshMetricFilter"]:
        '''
        :schema: CfnModulePropsResources#SSHMetricFilter
        '''
        result = self._values.get("ssh_metric_filter")
        return typing.cast(typing.Optional["CfnModulePropsResourcesSshMetricFilter"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResources(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-linux-bastion-module.CfnModulePropsResourcesBastionAutoScalingGroup",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesBastionAutoScalingGroup:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesBastionAutoScalingGroup
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesBastionAutoScalingGroup#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesBastionAutoScalingGroup#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesBastionAutoScalingGroup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-linux-bastion-module.CfnModulePropsResourcesBastionHostPolicy",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesBastionHostPolicy:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesBastionHostPolicy
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesBastionHostPolicy#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesBastionHostPolicy#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesBastionHostPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-linux-bastion-module.CfnModulePropsResourcesBastionHostProfile",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesBastionHostProfile:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesBastionHostProfile
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesBastionHostProfile#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesBastionHostProfile#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesBastionHostProfile(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-linux-bastion-module.CfnModulePropsResourcesBastionHostRole",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesBastionHostRole:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesBastionHostRole
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesBastionHostRole#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesBastionHostRole#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesBastionHostRole(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-linux-bastion-module.CfnModulePropsResourcesBastionLaunchConfiguration",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesBastionLaunchConfiguration:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesBastionLaunchConfiguration
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesBastionLaunchConfiguration#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesBastionLaunchConfiguration#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesBastionLaunchConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-linux-bastion-module.CfnModulePropsResourcesBastionMainLogGroup",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesBastionMainLogGroup:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesBastionMainLogGroup
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesBastionMainLogGroup#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesBastionMainLogGroup#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesBastionMainLogGroup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-linux-bastion-module.CfnModulePropsResourcesBastionSecurityGroup",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesBastionSecurityGroup:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesBastionSecurityGroup
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesBastionSecurityGroup#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesBastionSecurityGroup#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesBastionSecurityGroup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-linux-bastion-module.CfnModulePropsResourcesEip1",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesEip1:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesEip1
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesEip1#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesEip1#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesEip1(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-linux-bastion-module.CfnModulePropsResourcesEip2",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesEip2:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesEip2
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesEip2#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesEip2#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesEip2(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-linux-bastion-module.CfnModulePropsResourcesEip3",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesEip3:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesEip3
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesEip3#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesEip3#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesEip3(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-linux-bastion-module.CfnModulePropsResourcesEip4",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesEip4:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesEip4
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesEip4#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesEip4#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesEip4(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-linux-bastion-module.CfnModulePropsResourcesSshMetricFilter",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesSshMetricFilter:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesSshMetricFilter
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesSshMetricFilter#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesSshMetricFilter#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesSshMetricFilter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnModule",
    "CfnModuleProps",
    "CfnModulePropsParameters",
    "CfnModulePropsParametersAlternativeInitializationScript",
    "CfnModulePropsParametersBastionAmios",
    "CfnModulePropsParametersBastionBanner",
    "CfnModulePropsParametersBastionHostName",
    "CfnModulePropsParametersBastionInstanceType",
    "CfnModulePropsParametersBastionTenancy",
    "CfnModulePropsParametersEnableBanner",
    "CfnModulePropsParametersEnableTcpForwarding",
    "CfnModulePropsParametersEnableX11Forwarding",
    "CfnModulePropsParametersEnvironmentVariables",
    "CfnModulePropsParametersKeyPairName",
    "CfnModulePropsParametersLogicalId",
    "CfnModulePropsParametersNumBastionHosts",
    "CfnModulePropsParametersOsImageOverride",
    "CfnModulePropsParametersPublicSubnet1Id",
    "CfnModulePropsParametersPublicSubnet2Id",
    "CfnModulePropsParametersQss3BucketName",
    "CfnModulePropsParametersQss3BucketRegion",
    "CfnModulePropsParametersQss3KeyPrefix",
    "CfnModulePropsParametersRemoteAccessCidr",
    "CfnModulePropsParametersRootVolumeSize",
    "CfnModulePropsParametersVpcid",
    "CfnModulePropsResources",
    "CfnModulePropsResourcesBastionAutoScalingGroup",
    "CfnModulePropsResourcesBastionHostPolicy",
    "CfnModulePropsResourcesBastionHostProfile",
    "CfnModulePropsResourcesBastionHostRole",
    "CfnModulePropsResourcesBastionLaunchConfiguration",
    "CfnModulePropsResourcesBastionMainLogGroup",
    "CfnModulePropsResourcesBastionSecurityGroup",
    "CfnModulePropsResourcesEip1",
    "CfnModulePropsResourcesEip2",
    "CfnModulePropsResourcesEip3",
    "CfnModulePropsResourcesEip4",
    "CfnModulePropsResourcesSshMetricFilter",
]

publication.publish()
