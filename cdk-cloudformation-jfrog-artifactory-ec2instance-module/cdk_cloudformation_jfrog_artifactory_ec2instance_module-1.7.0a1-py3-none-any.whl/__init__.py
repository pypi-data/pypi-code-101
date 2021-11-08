'''
# AWS CDK CloudFormation Constructs for JFrog::Artifactory::EC2Instance::MODULE

Schema for Module Fragment of type JFrog::Artifactory::EC2Instance::MODULE

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
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnModule",
):
    '''A CloudFormation ``JFrog::Artifactory::EC2Instance::MODULE``.

    :cloudformationResource: JFrog::Artifactory::EC2Instance::MODULE
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
        '''Create a new ``JFrog::Artifactory::EC2Instance::MODULE``.

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
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnModuleProps",
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
        '''Schema for Module Fragment of type JFrog::Artifactory::EC2Instance::MODULE.

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
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnModulePropsParameters",
    jsii_struct_bases=[],
    name_mapping={
        "artifactory_efs_file_system": "artifactoryEfsFileSystem",
        "artifactory_licenses_secret_name": "artifactoryLicensesSecretName",
        "artifactory_primary": "artifactoryPrimary",
        "artifactory_product": "artifactoryProduct",
        "artifactory_s3_bucket": "artifactoryS3Bucket",
        "artifactory_server_name": "artifactoryServerName",
        "artifactory_version": "artifactoryVersion",
        "database_driver": "databaseDriver",
        "database_password": "databasePassword",
        "database_plugin": "databasePlugin",
        "database_plugin_url": "databasePluginUrl",
        "database_type": "databaseType",
        "database_url": "databaseUrl",
        "database_user": "databaseUser",
        "deployment_tag": "deploymentTag",
        "extra_java_options": "extraJavaOptions",
        "host_profile": "hostProfile",
        "host_role": "hostRole",
        "instance_type": "instanceType",
        "internal_target_group_arn": "internalTargetGroupArn",
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
        "sm_cert_name": "smCertName",
        "ssl_target_group_arn": "sslTargetGroupArn",
        "target_group_arn": "targetGroupArn",
        "user_data_directory": "userDataDirectory",
    },
)
class CfnModulePropsParameters:
    def __init__(
        self,
        *,
        artifactory_efs_file_system: typing.Optional["CfnModulePropsParametersArtifactoryEfsFileSystem"] = None,
        artifactory_licenses_secret_name: typing.Optional["CfnModulePropsParametersArtifactoryLicensesSecretName"] = None,
        artifactory_primary: typing.Optional["CfnModulePropsParametersArtifactoryPrimary"] = None,
        artifactory_product: typing.Optional["CfnModulePropsParametersArtifactoryProduct"] = None,
        artifactory_s3_bucket: typing.Optional["CfnModulePropsParametersArtifactoryS3Bucket"] = None,
        artifactory_server_name: typing.Optional["CfnModulePropsParametersArtifactoryServerName"] = None,
        artifactory_version: typing.Optional["CfnModulePropsParametersArtifactoryVersion"] = None,
        database_driver: typing.Optional["CfnModulePropsParametersDatabaseDriver"] = None,
        database_password: typing.Optional["CfnModulePropsParametersDatabasePassword"] = None,
        database_plugin: typing.Optional["CfnModulePropsParametersDatabasePlugin"] = None,
        database_plugin_url: typing.Optional["CfnModulePropsParametersDatabasePluginUrl"] = None,
        database_type: typing.Optional["CfnModulePropsParametersDatabaseType"] = None,
        database_url: typing.Optional["CfnModulePropsParametersDatabaseUrl"] = None,
        database_user: typing.Optional["CfnModulePropsParametersDatabaseUser"] = None,
        deployment_tag: typing.Optional["CfnModulePropsParametersDeploymentTag"] = None,
        extra_java_options: typing.Optional["CfnModulePropsParametersExtraJavaOptions"] = None,
        host_profile: typing.Optional["CfnModulePropsParametersHostProfile"] = None,
        host_role: typing.Optional["CfnModulePropsParametersHostRole"] = None,
        instance_type: typing.Optional["CfnModulePropsParametersInstanceType"] = None,
        internal_target_group_arn: typing.Optional["CfnModulePropsParametersInternalTargetGroupArn"] = None,
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
        sm_cert_name: typing.Optional["CfnModulePropsParametersSmCertName"] = None,
        ssl_target_group_arn: typing.Optional["CfnModulePropsParametersSslTargetGroupArn"] = None,
        target_group_arn: typing.Optional["CfnModulePropsParametersTargetGroupArn"] = None,
        user_data_directory: typing.Optional["CfnModulePropsParametersUserDataDirectory"] = None,
    ) -> None:
        '''
        :param artifactory_efs_file_system: 
        :param artifactory_licenses_secret_name: 
        :param artifactory_primary: 
        :param artifactory_product: JFrog Artifactory product you want to install into an AMI.
        :param artifactory_s3_bucket: 
        :param artifactory_server_name: 
        :param artifactory_version: 
        :param database_driver: 
        :param database_password: 
        :param database_plugin: 
        :param database_plugin_url: 
        :param database_type: 
        :param database_url: 
        :param database_user: 
        :param deployment_tag: 
        :param extra_java_options: 
        :param host_profile: 
        :param host_role: 
        :param instance_type: 
        :param internal_target_group_arn: 
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
        :param sm_cert_name: Secret name created in AWS Secrets Manager, which contains the SSL certificate and certificate key.
        :param ssl_target_group_arn: 
        :param target_group_arn: 
        :param user_data_directory: Directory to store Artifactory data. Can be used to store data (via symlink) in detachable volume

        :schema: CfnModulePropsParameters
        '''
        if isinstance(artifactory_efs_file_system, dict):
            artifactory_efs_file_system = CfnModulePropsParametersArtifactoryEfsFileSystem(**artifactory_efs_file_system)
        if isinstance(artifactory_licenses_secret_name, dict):
            artifactory_licenses_secret_name = CfnModulePropsParametersArtifactoryLicensesSecretName(**artifactory_licenses_secret_name)
        if isinstance(artifactory_primary, dict):
            artifactory_primary = CfnModulePropsParametersArtifactoryPrimary(**artifactory_primary)
        if isinstance(artifactory_product, dict):
            artifactory_product = CfnModulePropsParametersArtifactoryProduct(**artifactory_product)
        if isinstance(artifactory_s3_bucket, dict):
            artifactory_s3_bucket = CfnModulePropsParametersArtifactoryS3Bucket(**artifactory_s3_bucket)
        if isinstance(artifactory_server_name, dict):
            artifactory_server_name = CfnModulePropsParametersArtifactoryServerName(**artifactory_server_name)
        if isinstance(artifactory_version, dict):
            artifactory_version = CfnModulePropsParametersArtifactoryVersion(**artifactory_version)
        if isinstance(database_driver, dict):
            database_driver = CfnModulePropsParametersDatabaseDriver(**database_driver)
        if isinstance(database_password, dict):
            database_password = CfnModulePropsParametersDatabasePassword(**database_password)
        if isinstance(database_plugin, dict):
            database_plugin = CfnModulePropsParametersDatabasePlugin(**database_plugin)
        if isinstance(database_plugin_url, dict):
            database_plugin_url = CfnModulePropsParametersDatabasePluginUrl(**database_plugin_url)
        if isinstance(database_type, dict):
            database_type = CfnModulePropsParametersDatabaseType(**database_type)
        if isinstance(database_url, dict):
            database_url = CfnModulePropsParametersDatabaseUrl(**database_url)
        if isinstance(database_user, dict):
            database_user = CfnModulePropsParametersDatabaseUser(**database_user)
        if isinstance(deployment_tag, dict):
            deployment_tag = CfnModulePropsParametersDeploymentTag(**deployment_tag)
        if isinstance(extra_java_options, dict):
            extra_java_options = CfnModulePropsParametersExtraJavaOptions(**extra_java_options)
        if isinstance(host_profile, dict):
            host_profile = CfnModulePropsParametersHostProfile(**host_profile)
        if isinstance(host_role, dict):
            host_role = CfnModulePropsParametersHostRole(**host_role)
        if isinstance(instance_type, dict):
            instance_type = CfnModulePropsParametersInstanceType(**instance_type)
        if isinstance(internal_target_group_arn, dict):
            internal_target_group_arn = CfnModulePropsParametersInternalTargetGroupArn(**internal_target_group_arn)
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
        if isinstance(sm_cert_name, dict):
            sm_cert_name = CfnModulePropsParametersSmCertName(**sm_cert_name)
        if isinstance(ssl_target_group_arn, dict):
            ssl_target_group_arn = CfnModulePropsParametersSslTargetGroupArn(**ssl_target_group_arn)
        if isinstance(target_group_arn, dict):
            target_group_arn = CfnModulePropsParametersTargetGroupArn(**target_group_arn)
        if isinstance(user_data_directory, dict):
            user_data_directory = CfnModulePropsParametersUserDataDirectory(**user_data_directory)
        self._values: typing.Dict[str, typing.Any] = {}
        if artifactory_efs_file_system is not None:
            self._values["artifactory_efs_file_system"] = artifactory_efs_file_system
        if artifactory_licenses_secret_name is not None:
            self._values["artifactory_licenses_secret_name"] = artifactory_licenses_secret_name
        if artifactory_primary is not None:
            self._values["artifactory_primary"] = artifactory_primary
        if artifactory_product is not None:
            self._values["artifactory_product"] = artifactory_product
        if artifactory_s3_bucket is not None:
            self._values["artifactory_s3_bucket"] = artifactory_s3_bucket
        if artifactory_server_name is not None:
            self._values["artifactory_server_name"] = artifactory_server_name
        if artifactory_version is not None:
            self._values["artifactory_version"] = artifactory_version
        if database_driver is not None:
            self._values["database_driver"] = database_driver
        if database_password is not None:
            self._values["database_password"] = database_password
        if database_plugin is not None:
            self._values["database_plugin"] = database_plugin
        if database_plugin_url is not None:
            self._values["database_plugin_url"] = database_plugin_url
        if database_type is not None:
            self._values["database_type"] = database_type
        if database_url is not None:
            self._values["database_url"] = database_url
        if database_user is not None:
            self._values["database_user"] = database_user
        if deployment_tag is not None:
            self._values["deployment_tag"] = deployment_tag
        if extra_java_options is not None:
            self._values["extra_java_options"] = extra_java_options
        if host_profile is not None:
            self._values["host_profile"] = host_profile
        if host_role is not None:
            self._values["host_role"] = host_role
        if instance_type is not None:
            self._values["instance_type"] = instance_type
        if internal_target_group_arn is not None:
            self._values["internal_target_group_arn"] = internal_target_group_arn
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
        if sm_cert_name is not None:
            self._values["sm_cert_name"] = sm_cert_name
        if ssl_target_group_arn is not None:
            self._values["ssl_target_group_arn"] = ssl_target_group_arn
        if target_group_arn is not None:
            self._values["target_group_arn"] = target_group_arn
        if user_data_directory is not None:
            self._values["user_data_directory"] = user_data_directory

    @builtins.property
    def artifactory_efs_file_system(
        self,
    ) -> typing.Optional["CfnModulePropsParametersArtifactoryEfsFileSystem"]:
        '''
        :schema: CfnModulePropsParameters#ArtifactoryEfsFileSystem
        '''
        result = self._values.get("artifactory_efs_file_system")
        return typing.cast(typing.Optional["CfnModulePropsParametersArtifactoryEfsFileSystem"], result)

    @builtins.property
    def artifactory_licenses_secret_name(
        self,
    ) -> typing.Optional["CfnModulePropsParametersArtifactoryLicensesSecretName"]:
        '''
        :schema: CfnModulePropsParameters#ArtifactoryLicensesSecretName
        '''
        result = self._values.get("artifactory_licenses_secret_name")
        return typing.cast(typing.Optional["CfnModulePropsParametersArtifactoryLicensesSecretName"], result)

    @builtins.property
    def artifactory_primary(
        self,
    ) -> typing.Optional["CfnModulePropsParametersArtifactoryPrimary"]:
        '''
        :schema: CfnModulePropsParameters#ArtifactoryPrimary
        '''
        result = self._values.get("artifactory_primary")
        return typing.cast(typing.Optional["CfnModulePropsParametersArtifactoryPrimary"], result)

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
    def artifactory_s3_bucket(
        self,
    ) -> typing.Optional["CfnModulePropsParametersArtifactoryS3Bucket"]:
        '''
        :schema: CfnModulePropsParameters#ArtifactoryS3Bucket
        '''
        result = self._values.get("artifactory_s3_bucket")
        return typing.cast(typing.Optional["CfnModulePropsParametersArtifactoryS3Bucket"], result)

    @builtins.property
    def artifactory_server_name(
        self,
    ) -> typing.Optional["CfnModulePropsParametersArtifactoryServerName"]:
        '''
        :schema: CfnModulePropsParameters#ArtifactoryServerName
        '''
        result = self._values.get("artifactory_server_name")
        return typing.cast(typing.Optional["CfnModulePropsParametersArtifactoryServerName"], result)

    @builtins.property
    def artifactory_version(
        self,
    ) -> typing.Optional["CfnModulePropsParametersArtifactoryVersion"]:
        '''
        :schema: CfnModulePropsParameters#ArtifactoryVersion
        '''
        result = self._values.get("artifactory_version")
        return typing.cast(typing.Optional["CfnModulePropsParametersArtifactoryVersion"], result)

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
    def database_plugin(
        self,
    ) -> typing.Optional["CfnModulePropsParametersDatabasePlugin"]:
        '''
        :schema: CfnModulePropsParameters#DatabasePlugin
        '''
        result = self._values.get("database_plugin")
        return typing.cast(typing.Optional["CfnModulePropsParametersDatabasePlugin"], result)

    @builtins.property
    def database_plugin_url(
        self,
    ) -> typing.Optional["CfnModulePropsParametersDatabasePluginUrl"]:
        '''
        :schema: CfnModulePropsParameters#DatabasePluginUrl
        '''
        result = self._values.get("database_plugin_url")
        return typing.cast(typing.Optional["CfnModulePropsParametersDatabasePluginUrl"], result)

    @builtins.property
    def database_type(self) -> typing.Optional["CfnModulePropsParametersDatabaseType"]:
        '''
        :schema: CfnModulePropsParameters#DatabaseType
        '''
        result = self._values.get("database_type")
        return typing.cast(typing.Optional["CfnModulePropsParametersDatabaseType"], result)

    @builtins.property
    def database_url(self) -> typing.Optional["CfnModulePropsParametersDatabaseUrl"]:
        '''
        :schema: CfnModulePropsParameters#DatabaseUrl
        '''
        result = self._values.get("database_url")
        return typing.cast(typing.Optional["CfnModulePropsParametersDatabaseUrl"], result)

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
    def host_profile(self) -> typing.Optional["CfnModulePropsParametersHostProfile"]:
        '''
        :schema: CfnModulePropsParameters#HostProfile
        '''
        result = self._values.get("host_profile")
        return typing.cast(typing.Optional["CfnModulePropsParametersHostProfile"], result)

    @builtins.property
    def host_role(self) -> typing.Optional["CfnModulePropsParametersHostRole"]:
        '''
        :schema: CfnModulePropsParameters#HostRole
        '''
        result = self._values.get("host_role")
        return typing.cast(typing.Optional["CfnModulePropsParametersHostRole"], result)

    @builtins.property
    def instance_type(self) -> typing.Optional["CfnModulePropsParametersInstanceType"]:
        '''
        :schema: CfnModulePropsParameters#InstanceType
        '''
        result = self._values.get("instance_type")
        return typing.cast(typing.Optional["CfnModulePropsParametersInstanceType"], result)

    @builtins.property
    def internal_target_group_arn(
        self,
    ) -> typing.Optional["CfnModulePropsParametersInternalTargetGroupArn"]:
        '''
        :schema: CfnModulePropsParameters#InternalTargetGroupARN
        '''
        result = self._values.get("internal_target_group_arn")
        return typing.cast(typing.Optional["CfnModulePropsParametersInternalTargetGroupArn"], result)

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
    def sm_cert_name(self) -> typing.Optional["CfnModulePropsParametersSmCertName"]:
        '''Secret name created in AWS Secrets Manager, which contains the SSL certificate and certificate key.

        :schema: CfnModulePropsParameters#SmCertName
        '''
        result = self._values.get("sm_cert_name")
        return typing.cast(typing.Optional["CfnModulePropsParametersSmCertName"], result)

    @builtins.property
    def ssl_target_group_arn(
        self,
    ) -> typing.Optional["CfnModulePropsParametersSslTargetGroupArn"]:
        '''
        :schema: CfnModulePropsParameters#SSLTargetGroupARN
        '''
        result = self._values.get("ssl_target_group_arn")
        return typing.cast(typing.Optional["CfnModulePropsParametersSslTargetGroupArn"], result)

    @builtins.property
    def target_group_arn(
        self,
    ) -> typing.Optional["CfnModulePropsParametersTargetGroupArn"]:
        '''
        :schema: CfnModulePropsParameters#TargetGroupARN
        '''
        result = self._values.get("target_group_arn")
        return typing.cast(typing.Optional["CfnModulePropsParametersTargetGroupArn"], result)

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

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnModulePropsParametersArtifactoryEfsFileSystem",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnModulePropsParametersArtifactoryEfsFileSystem:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnModulePropsParametersArtifactoryEfsFileSystem
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersArtifactoryEfsFileSystem#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersArtifactoryEfsFileSystem(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnModulePropsParametersArtifactoryLicensesSecretName",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnModulePropsParametersArtifactoryLicensesSecretName:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnModulePropsParametersArtifactoryLicensesSecretName
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersArtifactoryLicensesSecretName#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersArtifactoryLicensesSecretName(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnModulePropsParametersArtifactoryPrimary",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnModulePropsParametersArtifactoryPrimary:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnModulePropsParametersArtifactoryPrimary
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersArtifactoryPrimary#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersArtifactoryPrimary(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnModulePropsParametersArtifactoryProduct",
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
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnModulePropsParametersArtifactoryS3Bucket",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnModulePropsParametersArtifactoryS3Bucket:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnModulePropsParametersArtifactoryS3Bucket
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersArtifactoryS3Bucket#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersArtifactoryS3Bucket(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnModulePropsParametersArtifactoryServerName",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnModulePropsParametersArtifactoryServerName:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnModulePropsParametersArtifactoryServerName
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersArtifactoryServerName#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersArtifactoryServerName(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnModulePropsParametersArtifactoryVersion",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnModulePropsParametersArtifactoryVersion:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnModulePropsParametersArtifactoryVersion
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersArtifactoryVersion#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersArtifactoryVersion(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnModulePropsParametersDatabaseDriver",
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
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnModulePropsParametersDatabasePassword",
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
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnModulePropsParametersDatabasePlugin",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnModulePropsParametersDatabasePlugin:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnModulePropsParametersDatabasePlugin
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersDatabasePlugin#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersDatabasePlugin(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnModulePropsParametersDatabasePluginUrl",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnModulePropsParametersDatabasePluginUrl:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnModulePropsParametersDatabasePluginUrl
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersDatabasePluginUrl#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersDatabasePluginUrl(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnModulePropsParametersDatabaseType",
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
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnModulePropsParametersDatabaseUrl",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnModulePropsParametersDatabaseUrl:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnModulePropsParametersDatabaseUrl
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersDatabaseUrl#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersDatabaseUrl(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnModulePropsParametersDatabaseUser",
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
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnModulePropsParametersDeploymentTag",
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
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnModulePropsParametersExtraJavaOptions",
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
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnModulePropsParametersHostProfile",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnModulePropsParametersHostProfile:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnModulePropsParametersHostProfile
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersHostProfile#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersHostProfile(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnModulePropsParametersHostRole",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnModulePropsParametersHostRole:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnModulePropsParametersHostRole
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersHostRole#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersHostRole(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnModulePropsParametersInstanceType",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnModulePropsParametersInstanceType:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnModulePropsParametersInstanceType
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersInstanceType#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersInstanceType(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnModulePropsParametersInternalTargetGroupArn",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnModulePropsParametersInternalTargetGroupArn:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnModulePropsParametersInternalTargetGroupArn
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersInternalTargetGroupArn#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersInternalTargetGroupArn(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnModulePropsParametersKeyPairName",
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
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnModulePropsParametersLogicalId",
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
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnModulePropsParametersMasterKey",
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
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnModulePropsParametersMaxScalingNodes",
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
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnModulePropsParametersMinScalingNodes",
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
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnModulePropsParametersPrivateSubnet1Id",
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
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnModulePropsParametersPrivateSubnet2Id",
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
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnModulePropsParametersQsS3BucketName",
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
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnModulePropsParametersQsS3KeyPrefix",
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
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnModulePropsParametersQsS3Uri",
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
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnModulePropsParametersSecurityGroups",
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
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnModulePropsParametersSmCertName",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersSmCertName:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Secret name created in AWS Secrets Manager, which contains the SSL certificate and certificate key.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersSmCertName
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersSmCertName#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersSmCertName#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersSmCertName(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnModulePropsParametersSslTargetGroupArn",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnModulePropsParametersSslTargetGroupArn:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnModulePropsParametersSslTargetGroupArn
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersSslTargetGroupArn#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersSslTargetGroupArn(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnModulePropsParametersTargetGroupArn",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnModulePropsParametersTargetGroupArn:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnModulePropsParametersTargetGroupArn
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersTargetGroupArn#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersTargetGroupArn(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnModulePropsParametersUserDataDirectory",
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
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnModulePropsResources",
    jsii_struct_bases=[],
    name_mapping={
        "artifactory_launch_configuration": "artifactoryLaunchConfiguration",
        "artifactory_scaling_group": "artifactoryScalingGroup",
    },
)
class CfnModulePropsResources:
    def __init__(
        self,
        *,
        artifactory_launch_configuration: typing.Optional["CfnModulePropsResourcesArtifactoryLaunchConfiguration"] = None,
        artifactory_scaling_group: typing.Optional["CfnModulePropsResourcesArtifactoryScalingGroup"] = None,
    ) -> None:
        '''
        :param artifactory_launch_configuration: 
        :param artifactory_scaling_group: 

        :schema: CfnModulePropsResources
        '''
        if isinstance(artifactory_launch_configuration, dict):
            artifactory_launch_configuration = CfnModulePropsResourcesArtifactoryLaunchConfiguration(**artifactory_launch_configuration)
        if isinstance(artifactory_scaling_group, dict):
            artifactory_scaling_group = CfnModulePropsResourcesArtifactoryScalingGroup(**artifactory_scaling_group)
        self._values: typing.Dict[str, typing.Any] = {}
        if artifactory_launch_configuration is not None:
            self._values["artifactory_launch_configuration"] = artifactory_launch_configuration
        if artifactory_scaling_group is not None:
            self._values["artifactory_scaling_group"] = artifactory_scaling_group

    @builtins.property
    def artifactory_launch_configuration(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesArtifactoryLaunchConfiguration"]:
        '''
        :schema: CfnModulePropsResources#ArtifactoryLaunchConfiguration
        '''
        result = self._values.get("artifactory_launch_configuration")
        return typing.cast(typing.Optional["CfnModulePropsResourcesArtifactoryLaunchConfiguration"], result)

    @builtins.property
    def artifactory_scaling_group(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesArtifactoryScalingGroup"]:
        '''
        :schema: CfnModulePropsResources#ArtifactoryScalingGroup
        '''
        result = self._values.get("artifactory_scaling_group")
        return typing.cast(typing.Optional["CfnModulePropsResourcesArtifactoryScalingGroup"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResources(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnModulePropsResourcesArtifactoryLaunchConfiguration",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesArtifactoryLaunchConfiguration:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesArtifactoryLaunchConfiguration
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesArtifactoryLaunchConfiguration#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesArtifactoryLaunchConfiguration#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesArtifactoryLaunchConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnModulePropsResourcesArtifactoryScalingGroup",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesArtifactoryScalingGroup:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesArtifactoryScalingGroup
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesArtifactoryScalingGroup#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesArtifactoryScalingGroup#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesArtifactoryScalingGroup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnModule",
    "CfnModuleProps",
    "CfnModulePropsParameters",
    "CfnModulePropsParametersArtifactoryEfsFileSystem",
    "CfnModulePropsParametersArtifactoryLicensesSecretName",
    "CfnModulePropsParametersArtifactoryPrimary",
    "CfnModulePropsParametersArtifactoryProduct",
    "CfnModulePropsParametersArtifactoryS3Bucket",
    "CfnModulePropsParametersArtifactoryServerName",
    "CfnModulePropsParametersArtifactoryVersion",
    "CfnModulePropsParametersDatabaseDriver",
    "CfnModulePropsParametersDatabasePassword",
    "CfnModulePropsParametersDatabasePlugin",
    "CfnModulePropsParametersDatabasePluginUrl",
    "CfnModulePropsParametersDatabaseType",
    "CfnModulePropsParametersDatabaseUrl",
    "CfnModulePropsParametersDatabaseUser",
    "CfnModulePropsParametersDeploymentTag",
    "CfnModulePropsParametersExtraJavaOptions",
    "CfnModulePropsParametersHostProfile",
    "CfnModulePropsParametersHostRole",
    "CfnModulePropsParametersInstanceType",
    "CfnModulePropsParametersInternalTargetGroupArn",
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
    "CfnModulePropsParametersSmCertName",
    "CfnModulePropsParametersSslTargetGroupArn",
    "CfnModulePropsParametersTargetGroupArn",
    "CfnModulePropsParametersUserDataDirectory",
    "CfnModulePropsResources",
    "CfnModulePropsResourcesArtifactoryLaunchConfiguration",
    "CfnModulePropsResourcesArtifactoryScalingGroup",
]

publication.publish()
