'''
# jfrog-artifactory-ec2instance-module

> AWS CDK [L1 construct](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html) and data structures for the [AWS CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) type `JFrog::Artifactory::EC2Instance::MODULE` v1.7.0.

## Description

Schema for Module Fragment of type JFrog::Artifactory::EC2Instance::MODULE

## Usage

In order to use this library, you will need to activate this AWS CloudFormation Registry type in your account. You can do this via the AWS Management Console or using the [AWS CLI](https://aws.amazon.com/cli/) using the following command:

```sh
aws cloudformation activate-type \
  --type-name JFrog::Artifactory::EC2Instance::MODULE \
  --publisher-id 06ff50c2e47f57b381f874871d9fac41796c9522 \
  --type MODULE \
  --execution-role-arn ROLE-ARN
```

Alternatively:

```sh
aws cloudformation activate-type \
  --public-type-arn arn:aws:cloudformation:us-east-1::type/module/06ff50c2e47f57b381f874871d9fac41796c9522/JFrog-Artifactory-EC2Instance-MODULE \
  --execution-role-arn ROLE-ARN
```

You can find more information about activating this type in the [AWS CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html).

## Feedback

This library is auto-generated and published to all supported programming languages by the [cdklabs/cdk-cloudformation](https://github.com/cdklabs/cdk-cloudformation) project based on the API schema published for `JFrog::Artifactory::EC2Instance::MODULE`.

* Issues related to this generated library should be [reported here](https://github.com/cdklabs/cdk-cloudformation/issues/new?title=Issue+with+%40cdk-cloudformation%2Fjfrog-artifactory-ec2instance-module+v1.7.0).
* Issues related to `JFrog::Artifactory::EC2Instance::MODULE` should be reported to the [publisher](undefined).

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


class CfnEc2InstanceModule(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnEc2InstanceModule",
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
        parameters: typing.Optional["CfnEc2InstanceModulePropsParameters"] = None,
        resources: typing.Optional["CfnEc2InstanceModulePropsResources"] = None,
    ) -> None:
        '''Create a new ``JFrog::Artifactory::EC2Instance::MODULE``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param parameters: 
        :param resources: 
        '''
        props = CfnEc2InstanceModuleProps(parameters=parameters, resources=resources)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnEc2InstanceModuleProps":
        '''Resource props.'''
        return typing.cast("CfnEc2InstanceModuleProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnEc2InstanceModuleProps",
    jsii_struct_bases=[],
    name_mapping={"parameters": "parameters", "resources": "resources"},
)
class CfnEc2InstanceModuleProps:
    def __init__(
        self,
        *,
        parameters: typing.Optional["CfnEc2InstanceModulePropsParameters"] = None,
        resources: typing.Optional["CfnEc2InstanceModulePropsResources"] = None,
    ) -> None:
        '''Schema for Module Fragment of type JFrog::Artifactory::EC2Instance::MODULE.

        :param parameters: 
        :param resources: 

        :schema: CfnEc2InstanceModuleProps
        '''
        if isinstance(parameters, dict):
            parameters = CfnEc2InstanceModulePropsParameters(**parameters)
        if isinstance(resources, dict):
            resources = CfnEc2InstanceModulePropsResources(**resources)
        self._values: typing.Dict[str, typing.Any] = {}
        if parameters is not None:
            self._values["parameters"] = parameters
        if resources is not None:
            self._values["resources"] = resources

    @builtins.property
    def parameters(self) -> typing.Optional["CfnEc2InstanceModulePropsParameters"]:
        '''
        :schema: CfnEc2InstanceModuleProps#Parameters
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional["CfnEc2InstanceModulePropsParameters"], result)

    @builtins.property
    def resources(self) -> typing.Optional["CfnEc2InstanceModulePropsResources"]:
        '''
        :schema: CfnEc2InstanceModuleProps#Resources
        '''
        result = self._values.get("resources")
        return typing.cast(typing.Optional["CfnEc2InstanceModulePropsResources"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEc2InstanceModuleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnEc2InstanceModulePropsParameters",
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
class CfnEc2InstanceModulePropsParameters:
    def __init__(
        self,
        *,
        artifactory_efs_file_system: typing.Optional["CfnEc2InstanceModulePropsParametersArtifactoryEfsFileSystem"] = None,
        artifactory_licenses_secret_name: typing.Optional["CfnEc2InstanceModulePropsParametersArtifactoryLicensesSecretName"] = None,
        artifactory_primary: typing.Optional["CfnEc2InstanceModulePropsParametersArtifactoryPrimary"] = None,
        artifactory_product: typing.Optional["CfnEc2InstanceModulePropsParametersArtifactoryProduct"] = None,
        artifactory_s3_bucket: typing.Optional["CfnEc2InstanceModulePropsParametersArtifactoryS3Bucket"] = None,
        artifactory_server_name: typing.Optional["CfnEc2InstanceModulePropsParametersArtifactoryServerName"] = None,
        artifactory_version: typing.Optional["CfnEc2InstanceModulePropsParametersArtifactoryVersion"] = None,
        database_driver: typing.Optional["CfnEc2InstanceModulePropsParametersDatabaseDriver"] = None,
        database_password: typing.Optional["CfnEc2InstanceModulePropsParametersDatabasePassword"] = None,
        database_plugin: typing.Optional["CfnEc2InstanceModulePropsParametersDatabasePlugin"] = None,
        database_plugin_url: typing.Optional["CfnEc2InstanceModulePropsParametersDatabasePluginUrl"] = None,
        database_type: typing.Optional["CfnEc2InstanceModulePropsParametersDatabaseType"] = None,
        database_url: typing.Optional["CfnEc2InstanceModulePropsParametersDatabaseUrl"] = None,
        database_user: typing.Optional["CfnEc2InstanceModulePropsParametersDatabaseUser"] = None,
        deployment_tag: typing.Optional["CfnEc2InstanceModulePropsParametersDeploymentTag"] = None,
        extra_java_options: typing.Optional["CfnEc2InstanceModulePropsParametersExtraJavaOptions"] = None,
        host_profile: typing.Optional["CfnEc2InstanceModulePropsParametersHostProfile"] = None,
        host_role: typing.Optional["CfnEc2InstanceModulePropsParametersHostRole"] = None,
        instance_type: typing.Optional["CfnEc2InstanceModulePropsParametersInstanceType"] = None,
        internal_target_group_arn: typing.Optional["CfnEc2InstanceModulePropsParametersInternalTargetGroupArn"] = None,
        key_pair_name: typing.Optional["CfnEc2InstanceModulePropsParametersKeyPairName"] = None,
        logical_id: typing.Optional["CfnEc2InstanceModulePropsParametersLogicalId"] = None,
        master_key: typing.Optional["CfnEc2InstanceModulePropsParametersMasterKey"] = None,
        max_scaling_nodes: typing.Optional["CfnEc2InstanceModulePropsParametersMaxScalingNodes"] = None,
        min_scaling_nodes: typing.Optional["CfnEc2InstanceModulePropsParametersMinScalingNodes"] = None,
        private_subnet1_id: typing.Optional["CfnEc2InstanceModulePropsParametersPrivateSubnet1Id"] = None,
        private_subnet2_id: typing.Optional["CfnEc2InstanceModulePropsParametersPrivateSubnet2Id"] = None,
        qs_s3_bucket_name: typing.Optional["CfnEc2InstanceModulePropsParametersQsS3BucketName"] = None,
        qs_s3_key_prefix: typing.Optional["CfnEc2InstanceModulePropsParametersQsS3KeyPrefix"] = None,
        qs_s3_uri: typing.Optional["CfnEc2InstanceModulePropsParametersQsS3Uri"] = None,
        security_groups: typing.Optional["CfnEc2InstanceModulePropsParametersSecurityGroups"] = None,
        sm_cert_name: typing.Optional["CfnEc2InstanceModulePropsParametersSmCertName"] = None,
        ssl_target_group_arn: typing.Optional["CfnEc2InstanceModulePropsParametersSslTargetGroupArn"] = None,
        target_group_arn: typing.Optional["CfnEc2InstanceModulePropsParametersTargetGroupArn"] = None,
        user_data_directory: typing.Optional["CfnEc2InstanceModulePropsParametersUserDataDirectory"] = None,
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

        :schema: CfnEc2InstanceModulePropsParameters
        '''
        if isinstance(artifactory_efs_file_system, dict):
            artifactory_efs_file_system = CfnEc2InstanceModulePropsParametersArtifactoryEfsFileSystem(**artifactory_efs_file_system)
        if isinstance(artifactory_licenses_secret_name, dict):
            artifactory_licenses_secret_name = CfnEc2InstanceModulePropsParametersArtifactoryLicensesSecretName(**artifactory_licenses_secret_name)
        if isinstance(artifactory_primary, dict):
            artifactory_primary = CfnEc2InstanceModulePropsParametersArtifactoryPrimary(**artifactory_primary)
        if isinstance(artifactory_product, dict):
            artifactory_product = CfnEc2InstanceModulePropsParametersArtifactoryProduct(**artifactory_product)
        if isinstance(artifactory_s3_bucket, dict):
            artifactory_s3_bucket = CfnEc2InstanceModulePropsParametersArtifactoryS3Bucket(**artifactory_s3_bucket)
        if isinstance(artifactory_server_name, dict):
            artifactory_server_name = CfnEc2InstanceModulePropsParametersArtifactoryServerName(**artifactory_server_name)
        if isinstance(artifactory_version, dict):
            artifactory_version = CfnEc2InstanceModulePropsParametersArtifactoryVersion(**artifactory_version)
        if isinstance(database_driver, dict):
            database_driver = CfnEc2InstanceModulePropsParametersDatabaseDriver(**database_driver)
        if isinstance(database_password, dict):
            database_password = CfnEc2InstanceModulePropsParametersDatabasePassword(**database_password)
        if isinstance(database_plugin, dict):
            database_plugin = CfnEc2InstanceModulePropsParametersDatabasePlugin(**database_plugin)
        if isinstance(database_plugin_url, dict):
            database_plugin_url = CfnEc2InstanceModulePropsParametersDatabasePluginUrl(**database_plugin_url)
        if isinstance(database_type, dict):
            database_type = CfnEc2InstanceModulePropsParametersDatabaseType(**database_type)
        if isinstance(database_url, dict):
            database_url = CfnEc2InstanceModulePropsParametersDatabaseUrl(**database_url)
        if isinstance(database_user, dict):
            database_user = CfnEc2InstanceModulePropsParametersDatabaseUser(**database_user)
        if isinstance(deployment_tag, dict):
            deployment_tag = CfnEc2InstanceModulePropsParametersDeploymentTag(**deployment_tag)
        if isinstance(extra_java_options, dict):
            extra_java_options = CfnEc2InstanceModulePropsParametersExtraJavaOptions(**extra_java_options)
        if isinstance(host_profile, dict):
            host_profile = CfnEc2InstanceModulePropsParametersHostProfile(**host_profile)
        if isinstance(host_role, dict):
            host_role = CfnEc2InstanceModulePropsParametersHostRole(**host_role)
        if isinstance(instance_type, dict):
            instance_type = CfnEc2InstanceModulePropsParametersInstanceType(**instance_type)
        if isinstance(internal_target_group_arn, dict):
            internal_target_group_arn = CfnEc2InstanceModulePropsParametersInternalTargetGroupArn(**internal_target_group_arn)
        if isinstance(key_pair_name, dict):
            key_pair_name = CfnEc2InstanceModulePropsParametersKeyPairName(**key_pair_name)
        if isinstance(logical_id, dict):
            logical_id = CfnEc2InstanceModulePropsParametersLogicalId(**logical_id)
        if isinstance(master_key, dict):
            master_key = CfnEc2InstanceModulePropsParametersMasterKey(**master_key)
        if isinstance(max_scaling_nodes, dict):
            max_scaling_nodes = CfnEc2InstanceModulePropsParametersMaxScalingNodes(**max_scaling_nodes)
        if isinstance(min_scaling_nodes, dict):
            min_scaling_nodes = CfnEc2InstanceModulePropsParametersMinScalingNodes(**min_scaling_nodes)
        if isinstance(private_subnet1_id, dict):
            private_subnet1_id = CfnEc2InstanceModulePropsParametersPrivateSubnet1Id(**private_subnet1_id)
        if isinstance(private_subnet2_id, dict):
            private_subnet2_id = CfnEc2InstanceModulePropsParametersPrivateSubnet2Id(**private_subnet2_id)
        if isinstance(qs_s3_bucket_name, dict):
            qs_s3_bucket_name = CfnEc2InstanceModulePropsParametersQsS3BucketName(**qs_s3_bucket_name)
        if isinstance(qs_s3_key_prefix, dict):
            qs_s3_key_prefix = CfnEc2InstanceModulePropsParametersQsS3KeyPrefix(**qs_s3_key_prefix)
        if isinstance(qs_s3_uri, dict):
            qs_s3_uri = CfnEc2InstanceModulePropsParametersQsS3Uri(**qs_s3_uri)
        if isinstance(security_groups, dict):
            security_groups = CfnEc2InstanceModulePropsParametersSecurityGroups(**security_groups)
        if isinstance(sm_cert_name, dict):
            sm_cert_name = CfnEc2InstanceModulePropsParametersSmCertName(**sm_cert_name)
        if isinstance(ssl_target_group_arn, dict):
            ssl_target_group_arn = CfnEc2InstanceModulePropsParametersSslTargetGroupArn(**ssl_target_group_arn)
        if isinstance(target_group_arn, dict):
            target_group_arn = CfnEc2InstanceModulePropsParametersTargetGroupArn(**target_group_arn)
        if isinstance(user_data_directory, dict):
            user_data_directory = CfnEc2InstanceModulePropsParametersUserDataDirectory(**user_data_directory)
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
    ) -> typing.Optional["CfnEc2InstanceModulePropsParametersArtifactoryEfsFileSystem"]:
        '''
        :schema: CfnEc2InstanceModulePropsParameters#ArtifactoryEfsFileSystem
        '''
        result = self._values.get("artifactory_efs_file_system")
        return typing.cast(typing.Optional["CfnEc2InstanceModulePropsParametersArtifactoryEfsFileSystem"], result)

    @builtins.property
    def artifactory_licenses_secret_name(
        self,
    ) -> typing.Optional["CfnEc2InstanceModulePropsParametersArtifactoryLicensesSecretName"]:
        '''
        :schema: CfnEc2InstanceModulePropsParameters#ArtifactoryLicensesSecretName
        '''
        result = self._values.get("artifactory_licenses_secret_name")
        return typing.cast(typing.Optional["CfnEc2InstanceModulePropsParametersArtifactoryLicensesSecretName"], result)

    @builtins.property
    def artifactory_primary(
        self,
    ) -> typing.Optional["CfnEc2InstanceModulePropsParametersArtifactoryPrimary"]:
        '''
        :schema: CfnEc2InstanceModulePropsParameters#ArtifactoryPrimary
        '''
        result = self._values.get("artifactory_primary")
        return typing.cast(typing.Optional["CfnEc2InstanceModulePropsParametersArtifactoryPrimary"], result)

    @builtins.property
    def artifactory_product(
        self,
    ) -> typing.Optional["CfnEc2InstanceModulePropsParametersArtifactoryProduct"]:
        '''JFrog Artifactory product you want to install into an AMI.

        :schema: CfnEc2InstanceModulePropsParameters#ArtifactoryProduct
        '''
        result = self._values.get("artifactory_product")
        return typing.cast(typing.Optional["CfnEc2InstanceModulePropsParametersArtifactoryProduct"], result)

    @builtins.property
    def artifactory_s3_bucket(
        self,
    ) -> typing.Optional["CfnEc2InstanceModulePropsParametersArtifactoryS3Bucket"]:
        '''
        :schema: CfnEc2InstanceModulePropsParameters#ArtifactoryS3Bucket
        '''
        result = self._values.get("artifactory_s3_bucket")
        return typing.cast(typing.Optional["CfnEc2InstanceModulePropsParametersArtifactoryS3Bucket"], result)

    @builtins.property
    def artifactory_server_name(
        self,
    ) -> typing.Optional["CfnEc2InstanceModulePropsParametersArtifactoryServerName"]:
        '''
        :schema: CfnEc2InstanceModulePropsParameters#ArtifactoryServerName
        '''
        result = self._values.get("artifactory_server_name")
        return typing.cast(typing.Optional["CfnEc2InstanceModulePropsParametersArtifactoryServerName"], result)

    @builtins.property
    def artifactory_version(
        self,
    ) -> typing.Optional["CfnEc2InstanceModulePropsParametersArtifactoryVersion"]:
        '''
        :schema: CfnEc2InstanceModulePropsParameters#ArtifactoryVersion
        '''
        result = self._values.get("artifactory_version")
        return typing.cast(typing.Optional["CfnEc2InstanceModulePropsParametersArtifactoryVersion"], result)

    @builtins.property
    def database_driver(
        self,
    ) -> typing.Optional["CfnEc2InstanceModulePropsParametersDatabaseDriver"]:
        '''
        :schema: CfnEc2InstanceModulePropsParameters#DatabaseDriver
        '''
        result = self._values.get("database_driver")
        return typing.cast(typing.Optional["CfnEc2InstanceModulePropsParametersDatabaseDriver"], result)

    @builtins.property
    def database_password(
        self,
    ) -> typing.Optional["CfnEc2InstanceModulePropsParametersDatabasePassword"]:
        '''
        :schema: CfnEc2InstanceModulePropsParameters#DatabasePassword
        '''
        result = self._values.get("database_password")
        return typing.cast(typing.Optional["CfnEc2InstanceModulePropsParametersDatabasePassword"], result)

    @builtins.property
    def database_plugin(
        self,
    ) -> typing.Optional["CfnEc2InstanceModulePropsParametersDatabasePlugin"]:
        '''
        :schema: CfnEc2InstanceModulePropsParameters#DatabasePlugin
        '''
        result = self._values.get("database_plugin")
        return typing.cast(typing.Optional["CfnEc2InstanceModulePropsParametersDatabasePlugin"], result)

    @builtins.property
    def database_plugin_url(
        self,
    ) -> typing.Optional["CfnEc2InstanceModulePropsParametersDatabasePluginUrl"]:
        '''
        :schema: CfnEc2InstanceModulePropsParameters#DatabasePluginUrl
        '''
        result = self._values.get("database_plugin_url")
        return typing.cast(typing.Optional["CfnEc2InstanceModulePropsParametersDatabasePluginUrl"], result)

    @builtins.property
    def database_type(
        self,
    ) -> typing.Optional["CfnEc2InstanceModulePropsParametersDatabaseType"]:
        '''
        :schema: CfnEc2InstanceModulePropsParameters#DatabaseType
        '''
        result = self._values.get("database_type")
        return typing.cast(typing.Optional["CfnEc2InstanceModulePropsParametersDatabaseType"], result)

    @builtins.property
    def database_url(
        self,
    ) -> typing.Optional["CfnEc2InstanceModulePropsParametersDatabaseUrl"]:
        '''
        :schema: CfnEc2InstanceModulePropsParameters#DatabaseUrl
        '''
        result = self._values.get("database_url")
        return typing.cast(typing.Optional["CfnEc2InstanceModulePropsParametersDatabaseUrl"], result)

    @builtins.property
    def database_user(
        self,
    ) -> typing.Optional["CfnEc2InstanceModulePropsParametersDatabaseUser"]:
        '''
        :schema: CfnEc2InstanceModulePropsParameters#DatabaseUser
        '''
        result = self._values.get("database_user")
        return typing.cast(typing.Optional["CfnEc2InstanceModulePropsParametersDatabaseUser"], result)

    @builtins.property
    def deployment_tag(
        self,
    ) -> typing.Optional["CfnEc2InstanceModulePropsParametersDeploymentTag"]:
        '''
        :schema: CfnEc2InstanceModulePropsParameters#DeploymentTag
        '''
        result = self._values.get("deployment_tag")
        return typing.cast(typing.Optional["CfnEc2InstanceModulePropsParametersDeploymentTag"], result)

    @builtins.property
    def extra_java_options(
        self,
    ) -> typing.Optional["CfnEc2InstanceModulePropsParametersExtraJavaOptions"]:
        '''
        :schema: CfnEc2InstanceModulePropsParameters#ExtraJavaOptions
        '''
        result = self._values.get("extra_java_options")
        return typing.cast(typing.Optional["CfnEc2InstanceModulePropsParametersExtraJavaOptions"], result)

    @builtins.property
    def host_profile(
        self,
    ) -> typing.Optional["CfnEc2InstanceModulePropsParametersHostProfile"]:
        '''
        :schema: CfnEc2InstanceModulePropsParameters#HostProfile
        '''
        result = self._values.get("host_profile")
        return typing.cast(typing.Optional["CfnEc2InstanceModulePropsParametersHostProfile"], result)

    @builtins.property
    def host_role(
        self,
    ) -> typing.Optional["CfnEc2InstanceModulePropsParametersHostRole"]:
        '''
        :schema: CfnEc2InstanceModulePropsParameters#HostRole
        '''
        result = self._values.get("host_role")
        return typing.cast(typing.Optional["CfnEc2InstanceModulePropsParametersHostRole"], result)

    @builtins.property
    def instance_type(
        self,
    ) -> typing.Optional["CfnEc2InstanceModulePropsParametersInstanceType"]:
        '''
        :schema: CfnEc2InstanceModulePropsParameters#InstanceType
        '''
        result = self._values.get("instance_type")
        return typing.cast(typing.Optional["CfnEc2InstanceModulePropsParametersInstanceType"], result)

    @builtins.property
    def internal_target_group_arn(
        self,
    ) -> typing.Optional["CfnEc2InstanceModulePropsParametersInternalTargetGroupArn"]:
        '''
        :schema: CfnEc2InstanceModulePropsParameters#InternalTargetGroupARN
        '''
        result = self._values.get("internal_target_group_arn")
        return typing.cast(typing.Optional["CfnEc2InstanceModulePropsParametersInternalTargetGroupArn"], result)

    @builtins.property
    def key_pair_name(
        self,
    ) -> typing.Optional["CfnEc2InstanceModulePropsParametersKeyPairName"]:
        '''
        :schema: CfnEc2InstanceModulePropsParameters#KeyPairName
        '''
        result = self._values.get("key_pair_name")
        return typing.cast(typing.Optional["CfnEc2InstanceModulePropsParametersKeyPairName"], result)

    @builtins.property
    def logical_id(
        self,
    ) -> typing.Optional["CfnEc2InstanceModulePropsParametersLogicalId"]:
        '''Logical Id of the MODULE.

        :schema: CfnEc2InstanceModulePropsParameters#LogicalId
        '''
        result = self._values.get("logical_id")
        return typing.cast(typing.Optional["CfnEc2InstanceModulePropsParametersLogicalId"], result)

    @builtins.property
    def master_key(
        self,
    ) -> typing.Optional["CfnEc2InstanceModulePropsParametersMasterKey"]:
        '''
        :schema: CfnEc2InstanceModulePropsParameters#MasterKey
        '''
        result = self._values.get("master_key")
        return typing.cast(typing.Optional["CfnEc2InstanceModulePropsParametersMasterKey"], result)

    @builtins.property
    def max_scaling_nodes(
        self,
    ) -> typing.Optional["CfnEc2InstanceModulePropsParametersMaxScalingNodes"]:
        '''
        :schema: CfnEc2InstanceModulePropsParameters#MaxScalingNodes
        '''
        result = self._values.get("max_scaling_nodes")
        return typing.cast(typing.Optional["CfnEc2InstanceModulePropsParametersMaxScalingNodes"], result)

    @builtins.property
    def min_scaling_nodes(
        self,
    ) -> typing.Optional["CfnEc2InstanceModulePropsParametersMinScalingNodes"]:
        '''
        :schema: CfnEc2InstanceModulePropsParameters#MinScalingNodes
        '''
        result = self._values.get("min_scaling_nodes")
        return typing.cast(typing.Optional["CfnEc2InstanceModulePropsParametersMinScalingNodes"], result)

    @builtins.property
    def private_subnet1_id(
        self,
    ) -> typing.Optional["CfnEc2InstanceModulePropsParametersPrivateSubnet1Id"]:
        '''ID of the private subnet in Availability Zone 1 of your existing VPC (e.g., subnet-z0376dab).

        :schema: CfnEc2InstanceModulePropsParameters#PrivateSubnet1Id
        '''
        result = self._values.get("private_subnet1_id")
        return typing.cast(typing.Optional["CfnEc2InstanceModulePropsParametersPrivateSubnet1Id"], result)

    @builtins.property
    def private_subnet2_id(
        self,
    ) -> typing.Optional["CfnEc2InstanceModulePropsParametersPrivateSubnet2Id"]:
        '''ID of the private subnet in Availability Zone 2 of your existing VPC (e.g., subnet-z0376dab).

        :schema: CfnEc2InstanceModulePropsParameters#PrivateSubnet2Id
        '''
        result = self._values.get("private_subnet2_id")
        return typing.cast(typing.Optional["CfnEc2InstanceModulePropsParametersPrivateSubnet2Id"], result)

    @builtins.property
    def qs_s3_bucket_name(
        self,
    ) -> typing.Optional["CfnEc2InstanceModulePropsParametersQsS3BucketName"]:
        '''
        :schema: CfnEc2InstanceModulePropsParameters#QsS3BucketName
        '''
        result = self._values.get("qs_s3_bucket_name")
        return typing.cast(typing.Optional["CfnEc2InstanceModulePropsParametersQsS3BucketName"], result)

    @builtins.property
    def qs_s3_key_prefix(
        self,
    ) -> typing.Optional["CfnEc2InstanceModulePropsParametersQsS3KeyPrefix"]:
        '''
        :schema: CfnEc2InstanceModulePropsParameters#QsS3KeyPrefix
        '''
        result = self._values.get("qs_s3_key_prefix")
        return typing.cast(typing.Optional["CfnEc2InstanceModulePropsParametersQsS3KeyPrefix"], result)

    @builtins.property
    def qs_s3_uri(
        self,
    ) -> typing.Optional["CfnEc2InstanceModulePropsParametersQsS3Uri"]:
        '''
        :schema: CfnEc2InstanceModulePropsParameters#QsS3Uri
        '''
        result = self._values.get("qs_s3_uri")
        return typing.cast(typing.Optional["CfnEc2InstanceModulePropsParametersQsS3Uri"], result)

    @builtins.property
    def security_groups(
        self,
    ) -> typing.Optional["CfnEc2InstanceModulePropsParametersSecurityGroups"]:
        '''
        :schema: CfnEc2InstanceModulePropsParameters#SecurityGroups
        '''
        result = self._values.get("security_groups")
        return typing.cast(typing.Optional["CfnEc2InstanceModulePropsParametersSecurityGroups"], result)

    @builtins.property
    def sm_cert_name(
        self,
    ) -> typing.Optional["CfnEc2InstanceModulePropsParametersSmCertName"]:
        '''Secret name created in AWS Secrets Manager, which contains the SSL certificate and certificate key.

        :schema: CfnEc2InstanceModulePropsParameters#SmCertName
        '''
        result = self._values.get("sm_cert_name")
        return typing.cast(typing.Optional["CfnEc2InstanceModulePropsParametersSmCertName"], result)

    @builtins.property
    def ssl_target_group_arn(
        self,
    ) -> typing.Optional["CfnEc2InstanceModulePropsParametersSslTargetGroupArn"]:
        '''
        :schema: CfnEc2InstanceModulePropsParameters#SSLTargetGroupARN
        '''
        result = self._values.get("ssl_target_group_arn")
        return typing.cast(typing.Optional["CfnEc2InstanceModulePropsParametersSslTargetGroupArn"], result)

    @builtins.property
    def target_group_arn(
        self,
    ) -> typing.Optional["CfnEc2InstanceModulePropsParametersTargetGroupArn"]:
        '''
        :schema: CfnEc2InstanceModulePropsParameters#TargetGroupARN
        '''
        result = self._values.get("target_group_arn")
        return typing.cast(typing.Optional["CfnEc2InstanceModulePropsParametersTargetGroupArn"], result)

    @builtins.property
    def user_data_directory(
        self,
    ) -> typing.Optional["CfnEc2InstanceModulePropsParametersUserDataDirectory"]:
        '''Directory to store Artifactory data.

        Can be used to store data (via symlink) in detachable volume

        :schema: CfnEc2InstanceModulePropsParameters#UserDataDirectory
        '''
        result = self._values.get("user_data_directory")
        return typing.cast(typing.Optional["CfnEc2InstanceModulePropsParametersUserDataDirectory"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEc2InstanceModulePropsParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnEc2InstanceModulePropsParametersArtifactoryEfsFileSystem",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnEc2InstanceModulePropsParametersArtifactoryEfsFileSystem:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnEc2InstanceModulePropsParametersArtifactoryEfsFileSystem
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnEc2InstanceModulePropsParametersArtifactoryEfsFileSystem#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEc2InstanceModulePropsParametersArtifactoryEfsFileSystem(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnEc2InstanceModulePropsParametersArtifactoryLicensesSecretName",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnEc2InstanceModulePropsParametersArtifactoryLicensesSecretName:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnEc2InstanceModulePropsParametersArtifactoryLicensesSecretName
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnEc2InstanceModulePropsParametersArtifactoryLicensesSecretName#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEc2InstanceModulePropsParametersArtifactoryLicensesSecretName(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnEc2InstanceModulePropsParametersArtifactoryPrimary",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnEc2InstanceModulePropsParametersArtifactoryPrimary:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnEc2InstanceModulePropsParametersArtifactoryPrimary
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnEc2InstanceModulePropsParametersArtifactoryPrimary#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEc2InstanceModulePropsParametersArtifactoryPrimary(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnEc2InstanceModulePropsParametersArtifactoryProduct",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnEc2InstanceModulePropsParametersArtifactoryProduct:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''JFrog Artifactory product you want to install into an AMI.

        :param description: 
        :param type: 

        :schema: CfnEc2InstanceModulePropsParametersArtifactoryProduct
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnEc2InstanceModulePropsParametersArtifactoryProduct#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnEc2InstanceModulePropsParametersArtifactoryProduct#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEc2InstanceModulePropsParametersArtifactoryProduct(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnEc2InstanceModulePropsParametersArtifactoryS3Bucket",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnEc2InstanceModulePropsParametersArtifactoryS3Bucket:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnEc2InstanceModulePropsParametersArtifactoryS3Bucket
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnEc2InstanceModulePropsParametersArtifactoryS3Bucket#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEc2InstanceModulePropsParametersArtifactoryS3Bucket(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnEc2InstanceModulePropsParametersArtifactoryServerName",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnEc2InstanceModulePropsParametersArtifactoryServerName:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnEc2InstanceModulePropsParametersArtifactoryServerName
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnEc2InstanceModulePropsParametersArtifactoryServerName#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEc2InstanceModulePropsParametersArtifactoryServerName(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnEc2InstanceModulePropsParametersArtifactoryVersion",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnEc2InstanceModulePropsParametersArtifactoryVersion:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnEc2InstanceModulePropsParametersArtifactoryVersion
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnEc2InstanceModulePropsParametersArtifactoryVersion#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEc2InstanceModulePropsParametersArtifactoryVersion(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnEc2InstanceModulePropsParametersDatabaseDriver",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnEc2InstanceModulePropsParametersDatabaseDriver:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnEc2InstanceModulePropsParametersDatabaseDriver
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnEc2InstanceModulePropsParametersDatabaseDriver#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEc2InstanceModulePropsParametersDatabaseDriver(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnEc2InstanceModulePropsParametersDatabasePassword",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnEc2InstanceModulePropsParametersDatabasePassword:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnEc2InstanceModulePropsParametersDatabasePassword
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnEc2InstanceModulePropsParametersDatabasePassword#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEc2InstanceModulePropsParametersDatabasePassword(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnEc2InstanceModulePropsParametersDatabasePlugin",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnEc2InstanceModulePropsParametersDatabasePlugin:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnEc2InstanceModulePropsParametersDatabasePlugin
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnEc2InstanceModulePropsParametersDatabasePlugin#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEc2InstanceModulePropsParametersDatabasePlugin(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnEc2InstanceModulePropsParametersDatabasePluginUrl",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnEc2InstanceModulePropsParametersDatabasePluginUrl:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnEc2InstanceModulePropsParametersDatabasePluginUrl
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnEc2InstanceModulePropsParametersDatabasePluginUrl#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEc2InstanceModulePropsParametersDatabasePluginUrl(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnEc2InstanceModulePropsParametersDatabaseType",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnEc2InstanceModulePropsParametersDatabaseType:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnEc2InstanceModulePropsParametersDatabaseType
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnEc2InstanceModulePropsParametersDatabaseType#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEc2InstanceModulePropsParametersDatabaseType(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnEc2InstanceModulePropsParametersDatabaseUrl",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnEc2InstanceModulePropsParametersDatabaseUrl:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnEc2InstanceModulePropsParametersDatabaseUrl
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnEc2InstanceModulePropsParametersDatabaseUrl#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEc2InstanceModulePropsParametersDatabaseUrl(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnEc2InstanceModulePropsParametersDatabaseUser",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnEc2InstanceModulePropsParametersDatabaseUser:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnEc2InstanceModulePropsParametersDatabaseUser
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnEc2InstanceModulePropsParametersDatabaseUser#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEc2InstanceModulePropsParametersDatabaseUser(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnEc2InstanceModulePropsParametersDeploymentTag",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnEc2InstanceModulePropsParametersDeploymentTag:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnEc2InstanceModulePropsParametersDeploymentTag
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnEc2InstanceModulePropsParametersDeploymentTag#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEc2InstanceModulePropsParametersDeploymentTag(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnEc2InstanceModulePropsParametersExtraJavaOptions",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnEc2InstanceModulePropsParametersExtraJavaOptions:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnEc2InstanceModulePropsParametersExtraJavaOptions
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnEc2InstanceModulePropsParametersExtraJavaOptions#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEc2InstanceModulePropsParametersExtraJavaOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnEc2InstanceModulePropsParametersHostProfile",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnEc2InstanceModulePropsParametersHostProfile:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnEc2InstanceModulePropsParametersHostProfile
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnEc2InstanceModulePropsParametersHostProfile#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEc2InstanceModulePropsParametersHostProfile(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnEc2InstanceModulePropsParametersHostRole",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnEc2InstanceModulePropsParametersHostRole:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnEc2InstanceModulePropsParametersHostRole
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnEc2InstanceModulePropsParametersHostRole#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEc2InstanceModulePropsParametersHostRole(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnEc2InstanceModulePropsParametersInstanceType",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnEc2InstanceModulePropsParametersInstanceType:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnEc2InstanceModulePropsParametersInstanceType
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnEc2InstanceModulePropsParametersInstanceType#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEc2InstanceModulePropsParametersInstanceType(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnEc2InstanceModulePropsParametersInternalTargetGroupArn",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnEc2InstanceModulePropsParametersInternalTargetGroupArn:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnEc2InstanceModulePropsParametersInternalTargetGroupArn
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnEc2InstanceModulePropsParametersInternalTargetGroupArn#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEc2InstanceModulePropsParametersInternalTargetGroupArn(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnEc2InstanceModulePropsParametersKeyPairName",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnEc2InstanceModulePropsParametersKeyPairName:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnEc2InstanceModulePropsParametersKeyPairName
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnEc2InstanceModulePropsParametersKeyPairName#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEc2InstanceModulePropsParametersKeyPairName(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnEc2InstanceModulePropsParametersLogicalId",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnEc2InstanceModulePropsParametersLogicalId:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Logical Id of the MODULE.

        :param description: 
        :param type: 

        :schema: CfnEc2InstanceModulePropsParametersLogicalId
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnEc2InstanceModulePropsParametersLogicalId#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnEc2InstanceModulePropsParametersLogicalId#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEc2InstanceModulePropsParametersLogicalId(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnEc2InstanceModulePropsParametersMasterKey",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnEc2InstanceModulePropsParametersMasterKey:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnEc2InstanceModulePropsParametersMasterKey
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnEc2InstanceModulePropsParametersMasterKey#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEc2InstanceModulePropsParametersMasterKey(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnEc2InstanceModulePropsParametersMaxScalingNodes",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnEc2InstanceModulePropsParametersMaxScalingNodes:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnEc2InstanceModulePropsParametersMaxScalingNodes
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnEc2InstanceModulePropsParametersMaxScalingNodes#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEc2InstanceModulePropsParametersMaxScalingNodes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnEc2InstanceModulePropsParametersMinScalingNodes",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnEc2InstanceModulePropsParametersMinScalingNodes:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnEc2InstanceModulePropsParametersMinScalingNodes
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnEc2InstanceModulePropsParametersMinScalingNodes#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEc2InstanceModulePropsParametersMinScalingNodes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnEc2InstanceModulePropsParametersPrivateSubnet1Id",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnEc2InstanceModulePropsParametersPrivateSubnet1Id:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''ID of the private subnet in Availability Zone 1 of your existing VPC (e.g., subnet-z0376dab).

        :param description: 
        :param type: 

        :schema: CfnEc2InstanceModulePropsParametersPrivateSubnet1Id
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnEc2InstanceModulePropsParametersPrivateSubnet1Id#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnEc2InstanceModulePropsParametersPrivateSubnet1Id#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEc2InstanceModulePropsParametersPrivateSubnet1Id(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnEc2InstanceModulePropsParametersPrivateSubnet2Id",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnEc2InstanceModulePropsParametersPrivateSubnet2Id:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''ID of the private subnet in Availability Zone 2 of your existing VPC (e.g., subnet-z0376dab).

        :param description: 
        :param type: 

        :schema: CfnEc2InstanceModulePropsParametersPrivateSubnet2Id
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnEc2InstanceModulePropsParametersPrivateSubnet2Id#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnEc2InstanceModulePropsParametersPrivateSubnet2Id#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEc2InstanceModulePropsParametersPrivateSubnet2Id(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnEc2InstanceModulePropsParametersQsS3BucketName",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnEc2InstanceModulePropsParametersQsS3BucketName:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnEc2InstanceModulePropsParametersQsS3BucketName
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnEc2InstanceModulePropsParametersQsS3BucketName#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEc2InstanceModulePropsParametersQsS3BucketName(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnEc2InstanceModulePropsParametersQsS3KeyPrefix",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnEc2InstanceModulePropsParametersQsS3KeyPrefix:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnEc2InstanceModulePropsParametersQsS3KeyPrefix
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnEc2InstanceModulePropsParametersQsS3KeyPrefix#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEc2InstanceModulePropsParametersQsS3KeyPrefix(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnEc2InstanceModulePropsParametersQsS3Uri",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnEc2InstanceModulePropsParametersQsS3Uri:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnEc2InstanceModulePropsParametersQsS3Uri
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnEc2InstanceModulePropsParametersQsS3Uri#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEc2InstanceModulePropsParametersQsS3Uri(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnEc2InstanceModulePropsParametersSecurityGroups",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnEc2InstanceModulePropsParametersSecurityGroups:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnEc2InstanceModulePropsParametersSecurityGroups
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnEc2InstanceModulePropsParametersSecurityGroups#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEc2InstanceModulePropsParametersSecurityGroups(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnEc2InstanceModulePropsParametersSmCertName",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnEc2InstanceModulePropsParametersSmCertName:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Secret name created in AWS Secrets Manager, which contains the SSL certificate and certificate key.

        :param description: 
        :param type: 

        :schema: CfnEc2InstanceModulePropsParametersSmCertName
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnEc2InstanceModulePropsParametersSmCertName#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnEc2InstanceModulePropsParametersSmCertName#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEc2InstanceModulePropsParametersSmCertName(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnEc2InstanceModulePropsParametersSslTargetGroupArn",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnEc2InstanceModulePropsParametersSslTargetGroupArn:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnEc2InstanceModulePropsParametersSslTargetGroupArn
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnEc2InstanceModulePropsParametersSslTargetGroupArn#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEc2InstanceModulePropsParametersSslTargetGroupArn(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnEc2InstanceModulePropsParametersTargetGroupArn",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnEc2InstanceModulePropsParametersTargetGroupArn:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnEc2InstanceModulePropsParametersTargetGroupArn
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnEc2InstanceModulePropsParametersTargetGroupArn#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEc2InstanceModulePropsParametersTargetGroupArn(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnEc2InstanceModulePropsParametersUserDataDirectory",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnEc2InstanceModulePropsParametersUserDataDirectory:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Directory to store Artifactory data.

        Can be used to store data (via symlink) in detachable volume

        :param description: 
        :param type: 

        :schema: CfnEc2InstanceModulePropsParametersUserDataDirectory
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnEc2InstanceModulePropsParametersUserDataDirectory#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnEc2InstanceModulePropsParametersUserDataDirectory#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEc2InstanceModulePropsParametersUserDataDirectory(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnEc2InstanceModulePropsResources",
    jsii_struct_bases=[],
    name_mapping={
        "artifactory_launch_configuration": "artifactoryLaunchConfiguration",
        "artifactory_scaling_group": "artifactoryScalingGroup",
    },
)
class CfnEc2InstanceModulePropsResources:
    def __init__(
        self,
        *,
        artifactory_launch_configuration: typing.Optional["CfnEc2InstanceModulePropsResourcesArtifactoryLaunchConfiguration"] = None,
        artifactory_scaling_group: typing.Optional["CfnEc2InstanceModulePropsResourcesArtifactoryScalingGroup"] = None,
    ) -> None:
        '''
        :param artifactory_launch_configuration: 
        :param artifactory_scaling_group: 

        :schema: CfnEc2InstanceModulePropsResources
        '''
        if isinstance(artifactory_launch_configuration, dict):
            artifactory_launch_configuration = CfnEc2InstanceModulePropsResourcesArtifactoryLaunchConfiguration(**artifactory_launch_configuration)
        if isinstance(artifactory_scaling_group, dict):
            artifactory_scaling_group = CfnEc2InstanceModulePropsResourcesArtifactoryScalingGroup(**artifactory_scaling_group)
        self._values: typing.Dict[str, typing.Any] = {}
        if artifactory_launch_configuration is not None:
            self._values["artifactory_launch_configuration"] = artifactory_launch_configuration
        if artifactory_scaling_group is not None:
            self._values["artifactory_scaling_group"] = artifactory_scaling_group

    @builtins.property
    def artifactory_launch_configuration(
        self,
    ) -> typing.Optional["CfnEc2InstanceModulePropsResourcesArtifactoryLaunchConfiguration"]:
        '''
        :schema: CfnEc2InstanceModulePropsResources#ArtifactoryLaunchConfiguration
        '''
        result = self._values.get("artifactory_launch_configuration")
        return typing.cast(typing.Optional["CfnEc2InstanceModulePropsResourcesArtifactoryLaunchConfiguration"], result)

    @builtins.property
    def artifactory_scaling_group(
        self,
    ) -> typing.Optional["CfnEc2InstanceModulePropsResourcesArtifactoryScalingGroup"]:
        '''
        :schema: CfnEc2InstanceModulePropsResources#ArtifactoryScalingGroup
        '''
        result = self._values.get("artifactory_scaling_group")
        return typing.cast(typing.Optional["CfnEc2InstanceModulePropsResourcesArtifactoryScalingGroup"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEc2InstanceModulePropsResources(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnEc2InstanceModulePropsResourcesArtifactoryLaunchConfiguration",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnEc2InstanceModulePropsResourcesArtifactoryLaunchConfiguration:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnEc2InstanceModulePropsResourcesArtifactoryLaunchConfiguration
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnEc2InstanceModulePropsResourcesArtifactoryLaunchConfiguration#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnEc2InstanceModulePropsResourcesArtifactoryLaunchConfiguration#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEc2InstanceModulePropsResourcesArtifactoryLaunchConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-ec2instance-module.CfnEc2InstanceModulePropsResourcesArtifactoryScalingGroup",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnEc2InstanceModulePropsResourcesArtifactoryScalingGroup:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnEc2InstanceModulePropsResourcesArtifactoryScalingGroup
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnEc2InstanceModulePropsResourcesArtifactoryScalingGroup#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnEc2InstanceModulePropsResourcesArtifactoryScalingGroup#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEc2InstanceModulePropsResourcesArtifactoryScalingGroup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnEc2InstanceModule",
    "CfnEc2InstanceModuleProps",
    "CfnEc2InstanceModulePropsParameters",
    "CfnEc2InstanceModulePropsParametersArtifactoryEfsFileSystem",
    "CfnEc2InstanceModulePropsParametersArtifactoryLicensesSecretName",
    "CfnEc2InstanceModulePropsParametersArtifactoryPrimary",
    "CfnEc2InstanceModulePropsParametersArtifactoryProduct",
    "CfnEc2InstanceModulePropsParametersArtifactoryS3Bucket",
    "CfnEc2InstanceModulePropsParametersArtifactoryServerName",
    "CfnEc2InstanceModulePropsParametersArtifactoryVersion",
    "CfnEc2InstanceModulePropsParametersDatabaseDriver",
    "CfnEc2InstanceModulePropsParametersDatabasePassword",
    "CfnEc2InstanceModulePropsParametersDatabasePlugin",
    "CfnEc2InstanceModulePropsParametersDatabasePluginUrl",
    "CfnEc2InstanceModulePropsParametersDatabaseType",
    "CfnEc2InstanceModulePropsParametersDatabaseUrl",
    "CfnEc2InstanceModulePropsParametersDatabaseUser",
    "CfnEc2InstanceModulePropsParametersDeploymentTag",
    "CfnEc2InstanceModulePropsParametersExtraJavaOptions",
    "CfnEc2InstanceModulePropsParametersHostProfile",
    "CfnEc2InstanceModulePropsParametersHostRole",
    "CfnEc2InstanceModulePropsParametersInstanceType",
    "CfnEc2InstanceModulePropsParametersInternalTargetGroupArn",
    "CfnEc2InstanceModulePropsParametersKeyPairName",
    "CfnEc2InstanceModulePropsParametersLogicalId",
    "CfnEc2InstanceModulePropsParametersMasterKey",
    "CfnEc2InstanceModulePropsParametersMaxScalingNodes",
    "CfnEc2InstanceModulePropsParametersMinScalingNodes",
    "CfnEc2InstanceModulePropsParametersPrivateSubnet1Id",
    "CfnEc2InstanceModulePropsParametersPrivateSubnet2Id",
    "CfnEc2InstanceModulePropsParametersQsS3BucketName",
    "CfnEc2InstanceModulePropsParametersQsS3KeyPrefix",
    "CfnEc2InstanceModulePropsParametersQsS3Uri",
    "CfnEc2InstanceModulePropsParametersSecurityGroups",
    "CfnEc2InstanceModulePropsParametersSmCertName",
    "CfnEc2InstanceModulePropsParametersSslTargetGroupArn",
    "CfnEc2InstanceModulePropsParametersTargetGroupArn",
    "CfnEc2InstanceModulePropsParametersUserDataDirectory",
    "CfnEc2InstanceModulePropsResources",
    "CfnEc2InstanceModulePropsResourcesArtifactoryLaunchConfiguration",
    "CfnEc2InstanceModulePropsResourcesArtifactoryScalingGroup",
]

publication.publish()
