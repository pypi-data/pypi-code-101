'''
# AWS CDK CloudFormation Constructs for JFrog::Xray::EC2Instance::MODULE

Schema for Module Fragment of type JFrog::Xray::EC2Instance::MODULE

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
    jsii_type="@cdk-cloudformation/jfrog-xray-ec2instance-module.CfnModule",
):
    '''A CloudFormation ``JFrog::Xray::EC2Instance::MODULE``.

    :cloudformationResource: JFrog::Xray::EC2Instance::MODULE
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
        '''Create a new ``JFrog::Xray::EC2Instance::MODULE``.

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
    jsii_type="@cdk-cloudformation/jfrog-xray-ec2instance-module.CfnModuleProps",
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
        '''Schema for Module Fragment of type JFrog::Xray::EC2Instance::MODULE.

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
    jsii_type="@cdk-cloudformation/jfrog-xray-ec2instance-module.CfnModulePropsParameters",
    jsii_struct_bases=[],
    name_mapping={
        "artifactory_product": "artifactoryProduct",
        "database_driver": "databaseDriver",
        "database_password": "databasePassword",
        "database_type": "databaseType",
        "database_user": "databaseUser",
        "deployment_tag": "deploymentTag",
        "extra_java_options": "extraJavaOptions",
        "jfrog_internal_url": "jfrogInternalUrl",
        "key_pair_name": "keyPairName",
        "logical_id": "logicalId",
        "master_key": "masterKey",
        "max_scaling_nodes": "maxScalingNodes",
        "min_scaling_nodes": "minScalingNodes",
        "private_subnet1_id": "privateSubnet1Id",
        "private_subnet2_id": "privateSubnet2Id",
        "qs_s3_bucket_name": "qsS3BucketName",
        "qs_s3_key_prefix": "qsS3KeyPrefix",
        "qs_s3_uri": "qsS3Uri",
        "security_groups": "securityGroups",
        "user_data_directory": "userDataDirectory",
        "volume_size": "volumeSize",
        "xray_database_password": "xrayDatabasePassword",
        "xray_database_url": "xrayDatabaseUrl",
        "xray_database_user": "xrayDatabaseUser",
        "xray_host_profile": "xrayHostProfile",
        "xray_host_role": "xrayHostRole",
        "xray_instance_type": "xrayInstanceType",
        "xray_master_database_url": "xrayMasterDatabaseUrl",
        "xray_version": "xrayVersion",
    },
)
class CfnModulePropsParameters:
    def __init__(
        self,
        *,
        artifactory_product: typing.Optional["CfnModulePropsParametersArtifactoryProduct"] = None,
        database_driver: typing.Optional["CfnModulePropsParametersDatabaseDriver"] = None,
        database_password: typing.Optional["CfnModulePropsParametersDatabasePassword"] = None,
        database_type: typing.Optional["CfnModulePropsParametersDatabaseType"] = None,
        database_user: typing.Optional["CfnModulePropsParametersDatabaseUser"] = None,
        deployment_tag: typing.Optional["CfnModulePropsParametersDeploymentTag"] = None,
        extra_java_options: typing.Optional["CfnModulePropsParametersExtraJavaOptions"] = None,
        jfrog_internal_url: typing.Optional["CfnModulePropsParametersJfrogInternalUrl"] = None,
        key_pair_name: typing.Optional["CfnModulePropsParametersKeyPairName"] = None,
        logical_id: typing.Optional["CfnModulePropsParametersLogicalId"] = None,
        master_key: typing.Optional["CfnModulePropsParametersMasterKey"] = None,
        max_scaling_nodes: typing.Optional["CfnModulePropsParametersMaxScalingNodes"] = None,
        min_scaling_nodes: typing.Optional["CfnModulePropsParametersMinScalingNodes"] = None,
        private_subnet1_id: typing.Optional["CfnModulePropsParametersPrivateSubnet1Id"] = None,
        private_subnet2_id: typing.Optional["CfnModulePropsParametersPrivateSubnet2Id"] = None,
        qs_s3_bucket_name: typing.Optional["CfnModulePropsParametersQsS3BucketName"] = None,
        qs_s3_key_prefix: typing.Optional["CfnModulePropsParametersQsS3KeyPrefix"] = None,
        qs_s3_uri: typing.Optional["CfnModulePropsParametersQsS3Uri"] = None,
        security_groups: typing.Optional["CfnModulePropsParametersSecurityGroups"] = None,
        user_data_directory: typing.Optional["CfnModulePropsParametersUserDataDirectory"] = None,
        volume_size: typing.Optional["CfnModulePropsParametersVolumeSize"] = None,
        xray_database_password: typing.Optional["CfnModulePropsParametersXrayDatabasePassword"] = None,
        xray_database_url: typing.Optional["CfnModulePropsParametersXrayDatabaseUrl"] = None,
        xray_database_user: typing.Optional["CfnModulePropsParametersXrayDatabaseUser"] = None,
        xray_host_profile: typing.Optional["CfnModulePropsParametersXrayHostProfile"] = None,
        xray_host_role: typing.Optional["CfnModulePropsParametersXrayHostRole"] = None,
        xray_instance_type: typing.Optional["CfnModulePropsParametersXrayInstanceType"] = None,
        xray_master_database_url: typing.Optional["CfnModulePropsParametersXrayMasterDatabaseUrl"] = None,
        xray_version: typing.Optional["CfnModulePropsParametersXrayVersion"] = None,
    ) -> None:
        '''
        :param artifactory_product: JFrog Artifactory product you want to install into an AMI.
        :param database_driver: 
        :param database_password: 
        :param database_type: 
        :param database_user: 
        :param deployment_tag: 
        :param extra_java_options: 
        :param jfrog_internal_url: 
        :param key_pair_name: 
        :param logical_id: Logical Id of the MODULE.
        :param master_key: 
        :param max_scaling_nodes: 
        :param min_scaling_nodes: 
        :param private_subnet1_id: ID of the private subnet in Availability Zone 1 of your existing VPC (e.g., subnet-z0376dab).
        :param private_subnet2_id: ID of the private subnet in Availability Zone 2 of your existing VPC (e.g., subnet-z0376dab).
        :param qs_s3_bucket_name: 
        :param qs_s3_key_prefix: 
        :param qs_s3_uri: 
        :param security_groups: 
        :param user_data_directory: Directory to store Artifactory data. Can be used to store data (via symlink) in detachable volume
        :param volume_size: 
        :param xray_database_password: 
        :param xray_database_url: 
        :param xray_database_user: 
        :param xray_host_profile: 
        :param xray_host_role: 
        :param xray_instance_type: 
        :param xray_master_database_url: 
        :param xray_version: 

        :schema: CfnModulePropsParameters
        '''
        if isinstance(artifactory_product, dict):
            artifactory_product = CfnModulePropsParametersArtifactoryProduct(**artifactory_product)
        if isinstance(database_driver, dict):
            database_driver = CfnModulePropsParametersDatabaseDriver(**database_driver)
        if isinstance(database_password, dict):
            database_password = CfnModulePropsParametersDatabasePassword(**database_password)
        if isinstance(database_type, dict):
            database_type = CfnModulePropsParametersDatabaseType(**database_type)
        if isinstance(database_user, dict):
            database_user = CfnModulePropsParametersDatabaseUser(**database_user)
        if isinstance(deployment_tag, dict):
            deployment_tag = CfnModulePropsParametersDeploymentTag(**deployment_tag)
        if isinstance(extra_java_options, dict):
            extra_java_options = CfnModulePropsParametersExtraJavaOptions(**extra_java_options)
        if isinstance(jfrog_internal_url, dict):
            jfrog_internal_url = CfnModulePropsParametersJfrogInternalUrl(**jfrog_internal_url)
        if isinstance(key_pair_name, dict):
            key_pair_name = CfnModulePropsParametersKeyPairName(**key_pair_name)
        if isinstance(logical_id, dict):
            logical_id = CfnModulePropsParametersLogicalId(**logical_id)
        if isinstance(master_key, dict):
            master_key = CfnModulePropsParametersMasterKey(**master_key)
        if isinstance(max_scaling_nodes, dict):
            max_scaling_nodes = CfnModulePropsParametersMaxScalingNodes(**max_scaling_nodes)
        if isinstance(min_scaling_nodes, dict):
            min_scaling_nodes = CfnModulePropsParametersMinScalingNodes(**min_scaling_nodes)
        if isinstance(private_subnet1_id, dict):
            private_subnet1_id = CfnModulePropsParametersPrivateSubnet1Id(**private_subnet1_id)
        if isinstance(private_subnet2_id, dict):
            private_subnet2_id = CfnModulePropsParametersPrivateSubnet2Id(**private_subnet2_id)
        if isinstance(qs_s3_bucket_name, dict):
            qs_s3_bucket_name = CfnModulePropsParametersQsS3BucketName(**qs_s3_bucket_name)
        if isinstance(qs_s3_key_prefix, dict):
            qs_s3_key_prefix = CfnModulePropsParametersQsS3KeyPrefix(**qs_s3_key_prefix)
        if isinstance(qs_s3_uri, dict):
            qs_s3_uri = CfnModulePropsParametersQsS3Uri(**qs_s3_uri)
        if isinstance(security_groups, dict):
            security_groups = CfnModulePropsParametersSecurityGroups(**security_groups)
        if isinstance(user_data_directory, dict):
            user_data_directory = CfnModulePropsParametersUserDataDirectory(**user_data_directory)
        if isinstance(volume_size, dict):
            volume_size = CfnModulePropsParametersVolumeSize(**volume_size)
        if isinstance(xray_database_password, dict):
            xray_database_password = CfnModulePropsParametersXrayDatabasePassword(**xray_database_password)
        if isinstance(xray_database_url, dict):
            xray_database_url = CfnModulePropsParametersXrayDatabaseUrl(**xray_database_url)
        if isinstance(xray_database_user, dict):
            xray_database_user = CfnModulePropsParametersXrayDatabaseUser(**xray_database_user)
        if isinstance(xray_host_profile, dict):
            xray_host_profile = CfnModulePropsParametersXrayHostProfile(**xray_host_profile)
        if isinstance(xray_host_role, dict):
            xray_host_role = CfnModulePropsParametersXrayHostRole(**xray_host_role)
        if isinstance(xray_instance_type, dict):
            xray_instance_type = CfnModulePropsParametersXrayInstanceType(**xray_instance_type)
        if isinstance(xray_master_database_url, dict):
            xray_master_database_url = CfnModulePropsParametersXrayMasterDatabaseUrl(**xray_master_database_url)
        if isinstance(xray_version, dict):
            xray_version = CfnModulePropsParametersXrayVersion(**xray_version)
        self._values: typing.Dict[str, typing.Any] = {}
        if artifactory_product is not None:
            self._values["artifactory_product"] = artifactory_product
        if database_driver is not None:
            self._values["database_driver"] = database_driver
        if database_password is not None:
            self._values["database_password"] = database_password
        if database_type is not None:
            self._values["database_type"] = database_type
        if database_user is not None:
            self._values["database_user"] = database_user
        if deployment_tag is not None:
            self._values["deployment_tag"] = deployment_tag
        if extra_java_options is not None:
            self._values["extra_java_options"] = extra_java_options
        if jfrog_internal_url is not None:
            self._values["jfrog_internal_url"] = jfrog_internal_url
        if key_pair_name is not None:
            self._values["key_pair_name"] = key_pair_name
        if logical_id is not None:
            self._values["logical_id"] = logical_id
        if master_key is not None:
            self._values["master_key"] = master_key
        if max_scaling_nodes is not None:
            self._values["max_scaling_nodes"] = max_scaling_nodes
        if min_scaling_nodes is not None:
            self._values["min_scaling_nodes"] = min_scaling_nodes
        if private_subnet1_id is not None:
            self._values["private_subnet1_id"] = private_subnet1_id
        if private_subnet2_id is not None:
            self._values["private_subnet2_id"] = private_subnet2_id
        if qs_s3_bucket_name is not None:
            self._values["qs_s3_bucket_name"] = qs_s3_bucket_name
        if qs_s3_key_prefix is not None:
            self._values["qs_s3_key_prefix"] = qs_s3_key_prefix
        if qs_s3_uri is not None:
            self._values["qs_s3_uri"] = qs_s3_uri
        if security_groups is not None:
            self._values["security_groups"] = security_groups
        if user_data_directory is not None:
            self._values["user_data_directory"] = user_data_directory
        if volume_size is not None:
            self._values["volume_size"] = volume_size
        if xray_database_password is not None:
            self._values["xray_database_password"] = xray_database_password
        if xray_database_url is not None:
            self._values["xray_database_url"] = xray_database_url
        if xray_database_user is not None:
            self._values["xray_database_user"] = xray_database_user
        if xray_host_profile is not None:
            self._values["xray_host_profile"] = xray_host_profile
        if xray_host_role is not None:
            self._values["xray_host_role"] = xray_host_role
        if xray_instance_type is not None:
            self._values["xray_instance_type"] = xray_instance_type
        if xray_master_database_url is not None:
            self._values["xray_master_database_url"] = xray_master_database_url
        if xray_version is not None:
            self._values["xray_version"] = xray_version

    @builtins.property
    def artifactory_product(
        self,
    ) -> typing.Optional["CfnModulePropsParametersArtifactoryProduct"]:
        '''JFrog Artifactory product you want to install into an AMI.

        :schema: CfnModulePropsParameters#ArtifactoryProduct
        '''
        result = self._values.get("artifactory_product")
        return typing.cast(typing.Optional["CfnModulePropsParametersArtifactoryProduct"], result)

    @builtins.property
    def database_driver(
        self,
    ) -> typing.Optional["CfnModulePropsParametersDatabaseDriver"]:
        '''
        :schema: CfnModulePropsParameters#DatabaseDriver
        '''
        result = self._values.get("database_driver")
        return typing.cast(typing.Optional["CfnModulePropsParametersDatabaseDriver"], result)

    @builtins.property
    def database_password(
        self,
    ) -> typing.Optional["CfnModulePropsParametersDatabasePassword"]:
        '''
        :schema: CfnModulePropsParameters#DatabasePassword
        '''
        result = self._values.get("database_password")
        return typing.cast(typing.Optional["CfnModulePropsParametersDatabasePassword"], result)

    @builtins.property
    def database_type(self) -> typing.Optional["CfnModulePropsParametersDatabaseType"]:
        '''
        :schema: CfnModulePropsParameters#DatabaseType
        '''
        result = self._values.get("database_type")
        return typing.cast(typing.Optional["CfnModulePropsParametersDatabaseType"], result)

    @builtins.property
    def database_user(self) -> typing.Optional["CfnModulePropsParametersDatabaseUser"]:
        '''
        :schema: CfnModulePropsParameters#DatabaseUser
        '''
        result = self._values.get("database_user")
        return typing.cast(typing.Optional["CfnModulePropsParametersDatabaseUser"], result)

    @builtins.property
    def deployment_tag(
        self,
    ) -> typing.Optional["CfnModulePropsParametersDeploymentTag"]:
        '''
        :schema: CfnModulePropsParameters#DeploymentTag
        '''
        result = self._values.get("deployment_tag")
        return typing.cast(typing.Optional["CfnModulePropsParametersDeploymentTag"], result)

    @builtins.property
    def extra_java_options(
        self,
    ) -> typing.Optional["CfnModulePropsParametersExtraJavaOptions"]:
        '''
        :schema: CfnModulePropsParameters#ExtraJavaOptions
        '''
        result = self._values.get("extra_java_options")
        return typing.cast(typing.Optional["CfnModulePropsParametersExtraJavaOptions"], result)

    @builtins.property
    def jfrog_internal_url(
        self,
    ) -> typing.Optional["CfnModulePropsParametersJfrogInternalUrl"]:
        '''
        :schema: CfnModulePropsParameters#JfrogInternalUrl
        '''
        result = self._values.get("jfrog_internal_url")
        return typing.cast(typing.Optional["CfnModulePropsParametersJfrogInternalUrl"], result)

    @builtins.property
    def key_pair_name(self) -> typing.Optional["CfnModulePropsParametersKeyPairName"]:
        '''
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
    def master_key(self) -> typing.Optional["CfnModulePropsParametersMasterKey"]:
        '''
        :schema: CfnModulePropsParameters#MasterKey
        '''
        result = self._values.get("master_key")
        return typing.cast(typing.Optional["CfnModulePropsParametersMasterKey"], result)

    @builtins.property
    def max_scaling_nodes(
        self,
    ) -> typing.Optional["CfnModulePropsParametersMaxScalingNodes"]:
        '''
        :schema: CfnModulePropsParameters#MaxScalingNodes
        '''
        result = self._values.get("max_scaling_nodes")
        return typing.cast(typing.Optional["CfnModulePropsParametersMaxScalingNodes"], result)

    @builtins.property
    def min_scaling_nodes(
        self,
    ) -> typing.Optional["CfnModulePropsParametersMinScalingNodes"]:
        '''
        :schema: CfnModulePropsParameters#MinScalingNodes
        '''
        result = self._values.get("min_scaling_nodes")
        return typing.cast(typing.Optional["CfnModulePropsParametersMinScalingNodes"], result)

    @builtins.property
    def private_subnet1_id(
        self,
    ) -> typing.Optional["CfnModulePropsParametersPrivateSubnet1Id"]:
        '''ID of the private subnet in Availability Zone 1 of your existing VPC (e.g., subnet-z0376dab).

        :schema: CfnModulePropsParameters#PrivateSubnet1Id
        '''
        result = self._values.get("private_subnet1_id")
        return typing.cast(typing.Optional["CfnModulePropsParametersPrivateSubnet1Id"], result)

    @builtins.property
    def private_subnet2_id(
        self,
    ) -> typing.Optional["CfnModulePropsParametersPrivateSubnet2Id"]:
        '''ID of the private subnet in Availability Zone 2 of your existing VPC (e.g., subnet-z0376dab).

        :schema: CfnModulePropsParameters#PrivateSubnet2Id
        '''
        result = self._values.get("private_subnet2_id")
        return typing.cast(typing.Optional["CfnModulePropsParametersPrivateSubnet2Id"], result)

    @builtins.property
    def qs_s3_bucket_name(
        self,
    ) -> typing.Optional["CfnModulePropsParametersQsS3BucketName"]:
        '''
        :schema: CfnModulePropsParameters#QsS3BucketName
        '''
        result = self._values.get("qs_s3_bucket_name")
        return typing.cast(typing.Optional["CfnModulePropsParametersQsS3BucketName"], result)

    @builtins.property
    def qs_s3_key_prefix(
        self,
    ) -> typing.Optional["CfnModulePropsParametersQsS3KeyPrefix"]:
        '''
        :schema: CfnModulePropsParameters#QsS3KeyPrefix
        '''
        result = self._values.get("qs_s3_key_prefix")
        return typing.cast(typing.Optional["CfnModulePropsParametersQsS3KeyPrefix"], result)

    @builtins.property
    def qs_s3_uri(self) -> typing.Optional["CfnModulePropsParametersQsS3Uri"]:
        '''
        :schema: CfnModulePropsParameters#QsS3Uri
        '''
        result = self._values.get("qs_s3_uri")
        return typing.cast(typing.Optional["CfnModulePropsParametersQsS3Uri"], result)

    @builtins.property
    def security_groups(
        self,
    ) -> typing.Optional["CfnModulePropsParametersSecurityGroups"]:
        '''
        :schema: CfnModulePropsParameters#SecurityGroups
        '''
        result = self._values.get("security_groups")
        return typing.cast(typing.Optional["CfnModulePropsParametersSecurityGroups"], result)

    @builtins.property
    def user_data_directory(
        self,
    ) -> typing.Optional["CfnModulePropsParametersUserDataDirectory"]:
        '''Directory to store Artifactory data.

        Can be used to store data (via symlink) in detachable volume

        :schema: CfnModulePropsParameters#UserDataDirectory
        '''
        result = self._values.get("user_data_directory")
        return typing.cast(typing.Optional["CfnModulePropsParametersUserDataDirectory"], result)

    @builtins.property
    def volume_size(self) -> typing.Optional["CfnModulePropsParametersVolumeSize"]:
        '''
        :schema: CfnModulePropsParameters#VolumeSize
        '''
        result = self._values.get("volume_size")
        return typing.cast(typing.Optional["CfnModulePropsParametersVolumeSize"], result)

    @builtins.property
    def xray_database_password(
        self,
    ) -> typing.Optional["CfnModulePropsParametersXrayDatabasePassword"]:
        '''
        :schema: CfnModulePropsParameters#XrayDatabasePassword
        '''
        result = self._values.get("xray_database_password")
        return typing.cast(typing.Optional["CfnModulePropsParametersXrayDatabasePassword"], result)

    @builtins.property
    def xray_database_url(
        self,
    ) -> typing.Optional["CfnModulePropsParametersXrayDatabaseUrl"]:
        '''
        :schema: CfnModulePropsParameters#XrayDatabaseUrl
        '''
        result = self._values.get("xray_database_url")
        return typing.cast(typing.Optional["CfnModulePropsParametersXrayDatabaseUrl"], result)

    @builtins.property
    def xray_database_user(
        self,
    ) -> typing.Optional["CfnModulePropsParametersXrayDatabaseUser"]:
        '''
        :schema: CfnModulePropsParameters#XrayDatabaseUser
        '''
        result = self._values.get("xray_database_user")
        return typing.cast(typing.Optional["CfnModulePropsParametersXrayDatabaseUser"], result)

    @builtins.property
    def xray_host_profile(
        self,
    ) -> typing.Optional["CfnModulePropsParametersXrayHostProfile"]:
        '''
        :schema: CfnModulePropsParameters#XrayHostProfile
        '''
        result = self._values.get("xray_host_profile")
        return typing.cast(typing.Optional["CfnModulePropsParametersXrayHostProfile"], result)

    @builtins.property
    def xray_host_role(self) -> typing.Optional["CfnModulePropsParametersXrayHostRole"]:
        '''
        :schema: CfnModulePropsParameters#XrayHostRole
        '''
        result = self._values.get("xray_host_role")
        return typing.cast(typing.Optional["CfnModulePropsParametersXrayHostRole"], result)

    @builtins.property
    def xray_instance_type(
        self,
    ) -> typing.Optional["CfnModulePropsParametersXrayInstanceType"]:
        '''
        :schema: CfnModulePropsParameters#XrayInstanceType
        '''
        result = self._values.get("xray_instance_type")
        return typing.cast(typing.Optional["CfnModulePropsParametersXrayInstanceType"], result)

    @builtins.property
    def xray_master_database_url(
        self,
    ) -> typing.Optional["CfnModulePropsParametersXrayMasterDatabaseUrl"]:
        '''
        :schema: CfnModulePropsParameters#XrayMasterDatabaseUrl
        '''
        result = self._values.get("xray_master_database_url")
        return typing.cast(typing.Optional["CfnModulePropsParametersXrayMasterDatabaseUrl"], result)

    @builtins.property
    def xray_version(self) -> typing.Optional["CfnModulePropsParametersXrayVersion"]:
        '''
        :schema: CfnModulePropsParameters#XrayVersion
        '''
        result = self._values.get("xray_version")
        return typing.cast(typing.Optional["CfnModulePropsParametersXrayVersion"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-xray-ec2instance-module.CfnModulePropsParametersArtifactoryProduct",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersArtifactoryProduct:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''JFrog Artifactory product you want to install into an AMI.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersArtifactoryProduct
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersArtifactoryProduct#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersArtifactoryProduct#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersArtifactoryProduct(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-xray-ec2instance-module.CfnModulePropsParametersDatabaseDriver",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnModulePropsParametersDatabaseDriver:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnModulePropsParametersDatabaseDriver
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersDatabaseDriver#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersDatabaseDriver(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-xray-ec2instance-module.CfnModulePropsParametersDatabasePassword",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnModulePropsParametersDatabasePassword:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnModulePropsParametersDatabasePassword
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersDatabasePassword#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersDatabasePassword(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-xray-ec2instance-module.CfnModulePropsParametersDatabaseType",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnModulePropsParametersDatabaseType:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnModulePropsParametersDatabaseType
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersDatabaseType#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersDatabaseType(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-xray-ec2instance-module.CfnModulePropsParametersDatabaseUser",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnModulePropsParametersDatabaseUser:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnModulePropsParametersDatabaseUser
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersDatabaseUser#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersDatabaseUser(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-xray-ec2instance-module.CfnModulePropsParametersDeploymentTag",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnModulePropsParametersDeploymentTag:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnModulePropsParametersDeploymentTag
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersDeploymentTag#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersDeploymentTag(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-xray-ec2instance-module.CfnModulePropsParametersExtraJavaOptions",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnModulePropsParametersExtraJavaOptions:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnModulePropsParametersExtraJavaOptions
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersExtraJavaOptions#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersExtraJavaOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-xray-ec2instance-module.CfnModulePropsParametersJfrogInternalUrl",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnModulePropsParametersJfrogInternalUrl:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnModulePropsParametersJfrogInternalUrl
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersJfrogInternalUrl#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersJfrogInternalUrl(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-xray-ec2instance-module.CfnModulePropsParametersKeyPairName",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnModulePropsParametersKeyPairName:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnModulePropsParametersKeyPairName
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

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
    jsii_type="@cdk-cloudformation/jfrog-xray-ec2instance-module.CfnModulePropsParametersLogicalId",
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
    jsii_type="@cdk-cloudformation/jfrog-xray-ec2instance-module.CfnModulePropsParametersMasterKey",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnModulePropsParametersMasterKey:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnModulePropsParametersMasterKey
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersMasterKey#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersMasterKey(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-xray-ec2instance-module.CfnModulePropsParametersMaxScalingNodes",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnModulePropsParametersMaxScalingNodes:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnModulePropsParametersMaxScalingNodes
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersMaxScalingNodes#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersMaxScalingNodes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-xray-ec2instance-module.CfnModulePropsParametersMinScalingNodes",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnModulePropsParametersMinScalingNodes:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnModulePropsParametersMinScalingNodes
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersMinScalingNodes#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersMinScalingNodes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-xray-ec2instance-module.CfnModulePropsParametersPrivateSubnet1Id",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersPrivateSubnet1Id:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''ID of the private subnet in Availability Zone 1 of your existing VPC (e.g., subnet-z0376dab).

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersPrivateSubnet1Id
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersPrivateSubnet1Id#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersPrivateSubnet1Id#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersPrivateSubnet1Id(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-xray-ec2instance-module.CfnModulePropsParametersPrivateSubnet2Id",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersPrivateSubnet2Id:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''ID of the private subnet in Availability Zone 2 of your existing VPC (e.g., subnet-z0376dab).

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersPrivateSubnet2Id
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersPrivateSubnet2Id#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersPrivateSubnet2Id#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersPrivateSubnet2Id(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-xray-ec2instance-module.CfnModulePropsParametersQsS3BucketName",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnModulePropsParametersQsS3BucketName:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnModulePropsParametersQsS3BucketName
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersQsS3BucketName#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersQsS3BucketName(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-xray-ec2instance-module.CfnModulePropsParametersQsS3KeyPrefix",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnModulePropsParametersQsS3KeyPrefix:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnModulePropsParametersQsS3KeyPrefix
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersQsS3KeyPrefix#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersQsS3KeyPrefix(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-xray-ec2instance-module.CfnModulePropsParametersQsS3Uri",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnModulePropsParametersQsS3Uri:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnModulePropsParametersQsS3Uri
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersQsS3Uri#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersQsS3Uri(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-xray-ec2instance-module.CfnModulePropsParametersSecurityGroups",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnModulePropsParametersSecurityGroups:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnModulePropsParametersSecurityGroups
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersSecurityGroups#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersSecurityGroups(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-xray-ec2instance-module.CfnModulePropsParametersUserDataDirectory",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersUserDataDirectory:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Directory to store Artifactory data.

        Can be used to store data (via symlink) in detachable volume

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersUserDataDirectory
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersUserDataDirectory#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersUserDataDirectory#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersUserDataDirectory(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-xray-ec2instance-module.CfnModulePropsParametersVolumeSize",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnModulePropsParametersVolumeSize:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnModulePropsParametersVolumeSize
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersVolumeSize#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersVolumeSize(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-xray-ec2instance-module.CfnModulePropsParametersXrayDatabasePassword",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnModulePropsParametersXrayDatabasePassword:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnModulePropsParametersXrayDatabasePassword
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersXrayDatabasePassword#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersXrayDatabasePassword(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-xray-ec2instance-module.CfnModulePropsParametersXrayDatabaseUrl",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnModulePropsParametersXrayDatabaseUrl:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnModulePropsParametersXrayDatabaseUrl
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersXrayDatabaseUrl#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersXrayDatabaseUrl(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-xray-ec2instance-module.CfnModulePropsParametersXrayDatabaseUser",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnModulePropsParametersXrayDatabaseUser:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnModulePropsParametersXrayDatabaseUser
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersXrayDatabaseUser#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersXrayDatabaseUser(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-xray-ec2instance-module.CfnModulePropsParametersXrayHostProfile",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnModulePropsParametersXrayHostProfile:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnModulePropsParametersXrayHostProfile
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersXrayHostProfile#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersXrayHostProfile(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-xray-ec2instance-module.CfnModulePropsParametersXrayHostRole",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnModulePropsParametersXrayHostRole:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnModulePropsParametersXrayHostRole
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersXrayHostRole#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersXrayHostRole(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-xray-ec2instance-module.CfnModulePropsParametersXrayInstanceType",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnModulePropsParametersXrayInstanceType:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnModulePropsParametersXrayInstanceType
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersXrayInstanceType#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersXrayInstanceType(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-xray-ec2instance-module.CfnModulePropsParametersXrayMasterDatabaseUrl",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnModulePropsParametersXrayMasterDatabaseUrl:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnModulePropsParametersXrayMasterDatabaseUrl
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersXrayMasterDatabaseUrl#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersXrayMasterDatabaseUrl(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-xray-ec2instance-module.CfnModulePropsParametersXrayVersion",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnModulePropsParametersXrayVersion:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnModulePropsParametersXrayVersion
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersXrayVersion#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersXrayVersion(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-xray-ec2instance-module.CfnModulePropsResources",
    jsii_struct_bases=[],
    name_mapping={
        "xray_launch_configuration": "xrayLaunchConfiguration",
        "xray_scaling_group": "xrayScalingGroup",
    },
)
class CfnModulePropsResources:
    def __init__(
        self,
        *,
        xray_launch_configuration: typing.Optional["CfnModulePropsResourcesXrayLaunchConfiguration"] = None,
        xray_scaling_group: typing.Optional["CfnModulePropsResourcesXrayScalingGroup"] = None,
    ) -> None:
        '''
        :param xray_launch_configuration: 
        :param xray_scaling_group: 

        :schema: CfnModulePropsResources
        '''
        if isinstance(xray_launch_configuration, dict):
            xray_launch_configuration = CfnModulePropsResourcesXrayLaunchConfiguration(**xray_launch_configuration)
        if isinstance(xray_scaling_group, dict):
            xray_scaling_group = CfnModulePropsResourcesXrayScalingGroup(**xray_scaling_group)
        self._values: typing.Dict[str, typing.Any] = {}
        if xray_launch_configuration is not None:
            self._values["xray_launch_configuration"] = xray_launch_configuration
        if xray_scaling_group is not None:
            self._values["xray_scaling_group"] = xray_scaling_group

    @builtins.property
    def xray_launch_configuration(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesXrayLaunchConfiguration"]:
        '''
        :schema: CfnModulePropsResources#XrayLaunchConfiguration
        '''
        result = self._values.get("xray_launch_configuration")
        return typing.cast(typing.Optional["CfnModulePropsResourcesXrayLaunchConfiguration"], result)

    @builtins.property
    def xray_scaling_group(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesXrayScalingGroup"]:
        '''
        :schema: CfnModulePropsResources#XrayScalingGroup
        '''
        result = self._values.get("xray_scaling_group")
        return typing.cast(typing.Optional["CfnModulePropsResourcesXrayScalingGroup"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResources(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-xray-ec2instance-module.CfnModulePropsResourcesXrayLaunchConfiguration",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesXrayLaunchConfiguration:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesXrayLaunchConfiguration
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesXrayLaunchConfiguration#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesXrayLaunchConfiguration#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesXrayLaunchConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-xray-ec2instance-module.CfnModulePropsResourcesXrayScalingGroup",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesXrayScalingGroup:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesXrayScalingGroup
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesXrayScalingGroup#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesXrayScalingGroup#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesXrayScalingGroup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnModule",
    "CfnModuleProps",
    "CfnModulePropsParameters",
    "CfnModulePropsParametersArtifactoryProduct",
    "CfnModulePropsParametersDatabaseDriver",
    "CfnModulePropsParametersDatabasePassword",
    "CfnModulePropsParametersDatabaseType",
    "CfnModulePropsParametersDatabaseUser",
    "CfnModulePropsParametersDeploymentTag",
    "CfnModulePropsParametersExtraJavaOptions",
    "CfnModulePropsParametersJfrogInternalUrl",
    "CfnModulePropsParametersKeyPairName",
    "CfnModulePropsParametersLogicalId",
    "CfnModulePropsParametersMasterKey",
    "CfnModulePropsParametersMaxScalingNodes",
    "CfnModulePropsParametersMinScalingNodes",
    "CfnModulePropsParametersPrivateSubnet1Id",
    "CfnModulePropsParametersPrivateSubnet2Id",
    "CfnModulePropsParametersQsS3BucketName",
    "CfnModulePropsParametersQsS3KeyPrefix",
    "CfnModulePropsParametersQsS3Uri",
    "CfnModulePropsParametersSecurityGroups",
    "CfnModulePropsParametersUserDataDirectory",
    "CfnModulePropsParametersVolumeSize",
    "CfnModulePropsParametersXrayDatabasePassword",
    "CfnModulePropsParametersXrayDatabaseUrl",
    "CfnModulePropsParametersXrayDatabaseUser",
    "CfnModulePropsParametersXrayHostProfile",
    "CfnModulePropsParametersXrayHostRole",
    "CfnModulePropsParametersXrayInstanceType",
    "CfnModulePropsParametersXrayMasterDatabaseUrl",
    "CfnModulePropsParametersXrayVersion",
    "CfnModulePropsResources",
    "CfnModulePropsResourcesXrayLaunchConfiguration",
    "CfnModulePropsResourcesXrayScalingGroup",
]

publication.publish()
