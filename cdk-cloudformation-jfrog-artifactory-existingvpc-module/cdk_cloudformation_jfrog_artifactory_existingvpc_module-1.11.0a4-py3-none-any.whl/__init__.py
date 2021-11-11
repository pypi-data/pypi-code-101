'''
# jfrog-artifactory-existingvpc-module

> AWS CDK [L1 construct](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html) and data structures for the [AWS CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) type `JFrog::Artifactory::ExistingVpc::MODULE` v1.11.0.

## Description

Schema for Module Fragment of type JFrog::Artifactory::ExistingVpc::MODULE

## Usage

In order to use this library, you will need to activate this AWS CloudFormation Registry type in your account. You can do this via the AWS Management Console or using the [AWS CLI](https://aws.amazon.com/cli/) using the following command:

```sh
aws cloudformation activate-type \
  --type-name JFrog::Artifactory::ExistingVpc::MODULE \
  --publisher-id 06ff50c2e47f57b381f874871d9fac41796c9522 \
  --type MODULE \
  --execution-role-arn ROLE-ARN
```

Alternatively:

```sh
aws cloudformation activate-type \
  --public-type-arn arn:aws:cloudformation:us-east-1::type/module/06ff50c2e47f57b381f874871d9fac41796c9522/JFrog-Artifactory-ExistingVpc-MODULE \
  --execution-role-arn ROLE-ARN
```

You can find more information about activating this type in the [AWS CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html).

## Feedback

This library is auto-generated and published to all supported programming languages by the [cdklabs/cdk-cloudformation](https://github.com/cdklabs/cdk-cloudformation) project based on the API schema published for `JFrog::Artifactory::ExistingVpc::MODULE`.

* Issues related to this generated library should be [reported here](https://github.com/cdklabs/cdk-cloudformation/issues/new?title=Issue+with+%40cdk-cloudformation%2Fjfrog-artifactory-existingvpc-module+v1.11.0).
* Issues related to `JFrog::Artifactory::ExistingVpc::MODULE` should be reported to the [publisher](undefined).

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


class CfnExistingVpcModule(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/jfrog-artifactory-existingvpc-module.CfnExistingVpcModule",
):
    '''A CloudFormation ``JFrog::Artifactory::ExistingVpc::MODULE``.

    :cloudformationResource: JFrog::Artifactory::ExistingVpc::MODULE
    :link: http://unknown-url
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        parameters: typing.Optional["CfnExistingVpcModulePropsParameters"] = None,
        resources: typing.Optional["CfnExistingVpcModulePropsResources"] = None,
    ) -> None:
        '''Create a new ``JFrog::Artifactory::ExistingVpc::MODULE``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param parameters: 
        :param resources: 
        '''
        props = CfnExistingVpcModuleProps(parameters=parameters, resources=resources)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnExistingVpcModuleProps":
        '''Resource props.'''
        return typing.cast("CfnExistingVpcModuleProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-existingvpc-module.CfnExistingVpcModuleProps",
    jsii_struct_bases=[],
    name_mapping={"parameters": "parameters", "resources": "resources"},
)
class CfnExistingVpcModuleProps:
    def __init__(
        self,
        *,
        parameters: typing.Optional["CfnExistingVpcModulePropsParameters"] = None,
        resources: typing.Optional["CfnExistingVpcModulePropsResources"] = None,
    ) -> None:
        '''Schema for Module Fragment of type JFrog::Artifactory::ExistingVpc::MODULE.

        :param parameters: 
        :param resources: 

        :schema: CfnExistingVpcModuleProps
        '''
        if isinstance(parameters, dict):
            parameters = CfnExistingVpcModulePropsParameters(**parameters)
        if isinstance(resources, dict):
            resources = CfnExistingVpcModulePropsResources(**resources)
        self._values: typing.Dict[str, typing.Any] = {}
        if parameters is not None:
            self._values["parameters"] = parameters
        if resources is not None:
            self._values["resources"] = resources

    @builtins.property
    def parameters(self) -> typing.Optional["CfnExistingVpcModulePropsParameters"]:
        '''
        :schema: CfnExistingVpcModuleProps#Parameters
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional["CfnExistingVpcModulePropsParameters"], result)

    @builtins.property
    def resources(self) -> typing.Optional["CfnExistingVpcModulePropsResources"]:
        '''
        :schema: CfnExistingVpcModuleProps#Resources
        '''
        result = self._values.get("resources")
        return typing.cast(typing.Optional["CfnExistingVpcModulePropsResources"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnExistingVpcModuleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-existingvpc-module.CfnExistingVpcModulePropsParameters",
    jsii_struct_bases=[],
    name_mapping={
        "access_cidr": "accessCidr",
        "artifactory_product": "artifactoryProduct",
        "artifactory_server_name": "artifactoryServerName",
        "artifactory_version": "artifactoryVersion",
        "availability_zone1": "availabilityZone1",
        "availability_zone2": "availabilityZone2",
        "bastion_enable_tcp_forwarding": "bastionEnableTcpForwarding",
        "bastion_enable_x11_forwarding": "bastionEnableX11Forwarding",
        "bastion_instance_type": "bastionInstanceType",
        "bastion_os": "bastionOs",
        "bastion_root_volume_size": "bastionRootVolumeSize",
        "database_allocated_storage": "databaseAllocatedStorage",
        "database_engine": "databaseEngine",
        "database_instance": "databaseInstance",
        "database_name": "databaseName",
        "database_password": "databasePassword",
        "database_preferred_az": "databasePreferredAz",
        "database_user": "databaseUser",
        "default_java_mem_settings": "defaultJavaMemSettings",
        "elb_scheme": "elbScheme",
        "enable_bastion": "enableBastion",
        "extra_java_options": "extraJavaOptions",
        "install_xray": "installXray",
        "instance_type": "instanceType",
        "key_pair_name": "keyPairName",
        "logical_id": "logicalId",
        "master_key": "masterKey",
        "multi_az_database": "multiAzDatabase",
        "num_bastion_hosts": "numBastionHosts",
        "number_of_secondary": "numberOfSecondary",
        "private_subnet1_cidr": "privateSubnet1Cidr",
        "private_subnet1_id": "privateSubnet1Id",
        "private_subnet2_cidr": "privateSubnet2Cidr",
        "private_subnet2_id": "privateSubnet2Id",
        "public_subnet1_id": "publicSubnet1Id",
        "public_subnet2_id": "publicSubnet2Id",
        "qs_s3_bucket_name": "qsS3BucketName",
        "qs_s3_bucket_region": "qsS3BucketRegion",
        "qs_s3_key_prefix": "qsS3KeyPrefix",
        "remote_access_cidr": "remoteAccessCidr",
        "sm_cert_name": "smCertName",
        "sm_license_name": "smLicenseName",
        "volume_size": "volumeSize",
        "vpc_cidr": "vpcCidr",
        "vpc_id": "vpcId",
        "xray_database_password": "xrayDatabasePassword",
        "xray_database_user": "xrayDatabaseUser",
        "xray_instance_type": "xrayInstanceType",
        "xray_number_of_instances": "xrayNumberOfInstances",
        "xray_version": "xrayVersion",
    },
)
class CfnExistingVpcModulePropsParameters:
    def __init__(
        self,
        *,
        access_cidr: typing.Optional["CfnExistingVpcModulePropsParametersAccessCidr"] = None,
        artifactory_product: typing.Optional["CfnExistingVpcModulePropsParametersArtifactoryProduct"] = None,
        artifactory_server_name: typing.Optional["CfnExistingVpcModulePropsParametersArtifactoryServerName"] = None,
        artifactory_version: typing.Optional["CfnExistingVpcModulePropsParametersArtifactoryVersion"] = None,
        availability_zone1: typing.Optional["CfnExistingVpcModulePropsParametersAvailabilityZone1"] = None,
        availability_zone2: typing.Optional["CfnExistingVpcModulePropsParametersAvailabilityZone2"] = None,
        bastion_enable_tcp_forwarding: typing.Optional["CfnExistingVpcModulePropsParametersBastionEnableTcpForwarding"] = None,
        bastion_enable_x11_forwarding: typing.Optional["CfnExistingVpcModulePropsParametersBastionEnableX11Forwarding"] = None,
        bastion_instance_type: typing.Optional["CfnExistingVpcModulePropsParametersBastionInstanceType"] = None,
        bastion_os: typing.Optional["CfnExistingVpcModulePropsParametersBastionOs"] = None,
        bastion_root_volume_size: typing.Optional["CfnExistingVpcModulePropsParametersBastionRootVolumeSize"] = None,
        database_allocated_storage: typing.Optional["CfnExistingVpcModulePropsParametersDatabaseAllocatedStorage"] = None,
        database_engine: typing.Optional["CfnExistingVpcModulePropsParametersDatabaseEngine"] = None,
        database_instance: typing.Optional["CfnExistingVpcModulePropsParametersDatabaseInstance"] = None,
        database_name: typing.Optional["CfnExistingVpcModulePropsParametersDatabaseName"] = None,
        database_password: typing.Optional["CfnExistingVpcModulePropsParametersDatabasePassword"] = None,
        database_preferred_az: typing.Optional["CfnExistingVpcModulePropsParametersDatabasePreferredAz"] = None,
        database_user: typing.Optional["CfnExistingVpcModulePropsParametersDatabaseUser"] = None,
        default_java_mem_settings: typing.Optional["CfnExistingVpcModulePropsParametersDefaultJavaMemSettings"] = None,
        elb_scheme: typing.Optional["CfnExistingVpcModulePropsParametersElbScheme"] = None,
        enable_bastion: typing.Optional["CfnExistingVpcModulePropsParametersEnableBastion"] = None,
        extra_java_options: typing.Optional["CfnExistingVpcModulePropsParametersExtraJavaOptions"] = None,
        install_xray: typing.Optional["CfnExistingVpcModulePropsParametersInstallXray"] = None,
        instance_type: typing.Optional["CfnExistingVpcModulePropsParametersInstanceType"] = None,
        key_pair_name: typing.Optional["CfnExistingVpcModulePropsParametersKeyPairName"] = None,
        logical_id: typing.Optional["CfnExistingVpcModulePropsParametersLogicalId"] = None,
        master_key: typing.Optional["CfnExistingVpcModulePropsParametersMasterKey"] = None,
        multi_az_database: typing.Optional["CfnExistingVpcModulePropsParametersMultiAzDatabase"] = None,
        num_bastion_hosts: typing.Optional["CfnExistingVpcModulePropsParametersNumBastionHosts"] = None,
        number_of_secondary: typing.Optional["CfnExistingVpcModulePropsParametersNumberOfSecondary"] = None,
        private_subnet1_cidr: typing.Optional["CfnExistingVpcModulePropsParametersPrivateSubnet1Cidr"] = None,
        private_subnet1_id: typing.Optional["CfnExistingVpcModulePropsParametersPrivateSubnet1Id"] = None,
        private_subnet2_cidr: typing.Optional["CfnExistingVpcModulePropsParametersPrivateSubnet2Cidr"] = None,
        private_subnet2_id: typing.Optional["CfnExistingVpcModulePropsParametersPrivateSubnet2Id"] = None,
        public_subnet1_id: typing.Optional["CfnExistingVpcModulePropsParametersPublicSubnet1Id"] = None,
        public_subnet2_id: typing.Optional["CfnExistingVpcModulePropsParametersPublicSubnet2Id"] = None,
        qs_s3_bucket_name: typing.Optional["CfnExistingVpcModulePropsParametersQsS3BucketName"] = None,
        qs_s3_bucket_region: typing.Optional["CfnExistingVpcModulePropsParametersQsS3BucketRegion"] = None,
        qs_s3_key_prefix: typing.Optional["CfnExistingVpcModulePropsParametersQsS3KeyPrefix"] = None,
        remote_access_cidr: typing.Optional["CfnExistingVpcModulePropsParametersRemoteAccessCidr"] = None,
        sm_cert_name: typing.Optional["CfnExistingVpcModulePropsParametersSmCertName"] = None,
        sm_license_name: typing.Optional["CfnExistingVpcModulePropsParametersSmLicenseName"] = None,
        volume_size: typing.Optional["CfnExistingVpcModulePropsParametersVolumeSize"] = None,
        vpc_cidr: typing.Optional["CfnExistingVpcModulePropsParametersVpcCidr"] = None,
        vpc_id: typing.Optional["CfnExistingVpcModulePropsParametersVpcId"] = None,
        xray_database_password: typing.Optional["CfnExistingVpcModulePropsParametersXrayDatabasePassword"] = None,
        xray_database_user: typing.Optional["CfnExistingVpcModulePropsParametersXrayDatabaseUser"] = None,
        xray_instance_type: typing.Optional["CfnExistingVpcModulePropsParametersXrayInstanceType"] = None,
        xray_number_of_instances: typing.Optional["CfnExistingVpcModulePropsParametersXrayNumberOfInstances"] = None,
        xray_version: typing.Optional["CfnExistingVpcModulePropsParametersXrayVersion"] = None,
    ) -> None:
        '''
        :param access_cidr: CIDR IP range that is permitted to access Artifactory. We recommend that you set this value to a trusted IP range. For example, you might want to grant only your corporate network access to the software.
        :param artifactory_product: JFrog Artifactory product you want to install into an AMI.
        :param artifactory_server_name: Name of your Artifactory server. Ensure that this matches your certificate.
        :param artifactory_version: Version of Artifactory that you want to deploy into the Quick Start. See the release notes to select the version you want to deploy at https://www.jfrog.com/confluence/display/RTF/Release+Notes.
        :param availability_zone1: Availability Zone 1 to use for the subnets in the VPC. Two Availability Zones are used for this deployment.
        :param availability_zone2: Availability Zone 2 to use for the subnets in the VPC. Two Availability Zones are used for this deployment.
        :param bastion_enable_tcp_forwarding: Choose whether to enable TCPForwarding via the bootstrapping of the bastion instance or not.
        :param bastion_enable_x11_forwarding: Choose true to enable X11 via the bootstrapping of the bastion host. Setting this value to true will enable X Windows over SSH. X11 forwarding can be useful, but it is also a security risk, so it's recommended that you keep the default (false) setting.
        :param bastion_instance_type: Size of the bastion instances.
        :param bastion_os: Linux distribution for the Amazon Machine Image (AMI) to be used for the bastion instances.
        :param bastion_root_volume_size: Size of the root volume on the bastion instances.
        :param database_allocated_storage: Size in gigabytes of the available storage for the database instance.
        :param database_engine: Database engine that you want to run, which is currently locked to MySQL.
        :param database_instance: Size of the database to be deployed as part of the Quick Start.
        :param database_name: Name of your database instance. The name must be unique across all instances owned by your AWS account in the current Region. The database instance identifier is case-insensitive, but it's stored in lowercase (as in "mydbinstance").
        :param database_password: Password for the Artifactory database user.
        :param database_preferred_az: Preferred availability zone for Amazon RDS primary instance.
        :param database_user: Login ID for the master user of your database instance.
        :param default_java_mem_settings: Choose false to overwrite the standard memory-calculation options to pass to the Artifactory JVM. If you plan to overwrite them, ensure they are added to the ExtraJavaOptions to prevent the stack provision from failing.
        :param elb_scheme: Choose whether this is internet facing or internal.
        :param enable_bastion: If set to true, a bastion host will be created.
        :param extra_java_options: Set Java options to pass to the JVM for Artifactory. For more information, see the Artifactory system requirements at https://www.jfrog.com/confluence/display/RTF/System+Requirements#SystemRequirements-RecommendedHardware. Do not add Xms or Xmx settings without disabling DefaultJavaMemSettings.
        :param install_xray: Choose true to install JFrog Xray instance(s).
        :param instance_type: EC2 type for the Artifactory instances.
        :param key_pair_name: Name of an existing key pair, which allows you to connect securely to your instance after it launches. This is the key pair you created in your preferred Region.
        :param logical_id: Logical Id of the MODULE.
        :param master_key: Master key for the Artifactory cluster. Generate a master key by using the command '$openssl rand -hex 16'.
        :param multi_az_database: Choose false to create an Amazon RDS instance in a single Availability Zone.
        :param num_bastion_hosts: Number of bastion instances to create.
        :param number_of_secondary: Number of secondary Artifactory servers to complete your HA deployment. To align with Artifactory best practices, the minimum number is two and the maximum is seven. Do not select more instances than you have licenses for.
        :param private_subnet1_cidr: CIDR of the private subnet in Availability Zone 1 of your existing VPC (e.g., 10.0.0.0/19).
        :param private_subnet1_id: ID of the private subnet in Availability Zone 1 of your existing VPC (e.g., subnet-z0376dab).
        :param private_subnet2_cidr: CIDR of the private subnet in Availability Zone 2 of your existing VPC (e.g., 10.0.32.0/19).
        :param private_subnet2_id: ID of the private subnet in Availability Zone 2 of your existing VPC (e.g., subnet-z0376dab).
        :param public_subnet1_id: ID of the public subnet in Availability Zone 1 of your existing VPC (e.g., subnet-z0376dab).
        :param public_subnet2_id: ID of the public subnet in Availability Zone 1 of your existing VPC (e.g., subnet-z0376dab).
        :param qs_s3_bucket_name: S3 bucket name for the Quick Start assets. This string can include numbers, lowercase letters, and hyphens (-). It cannot start or end with a hyphen (-).
        :param qs_s3_bucket_region: AWS Region where the Quick Start S3 bucket (QSS3BucketName) is hosted. If you use your own bucket, you must specify your own value.
        :param qs_s3_key_prefix: S3 key prefix for the Quick Start assets. Quick Start key prefix can include numbers, lowercase letters, uppercase letters, hyphens (-), and forward slash (/).
        :param remote_access_cidr: Remote CIDR range that allows you to connect to the bastion instance by using SSH. We recommend that you set this value to a trusted IP range. For example, you might want to grant specific ranges inside your corporate network SSH access.
        :param sm_cert_name: Secret name created in AWS Secrets Manager, which contains the SSL certificate and certificate key.
        :param sm_license_name: Secret name created in AWS Secrets Manager, which contains the Artifactory licenses.
        :param volume_size: Size in gigabytes of the available storage (min 10GB); the Quick Start will create an Amazon Elastic Block Store (Amazon EBS) volumes of this size.
        :param vpc_cidr: CIDR block for the VPC.
        :param vpc_id: ID of your existing VPC (e.g., vpc-0343606e).
        :param xray_database_password: The password for the Xray database user.
        :param xray_database_user: The login ID for the Xray database user.
        :param xray_instance_type: The EC2 instance type for the Xray instances.
        :param xray_number_of_instances: The number of Xray instances servers to complete your HA deployment. The minimum number is one; the maximum is seven. Do not select more than instances than you have licenses for.
        :param xray_version: The version of Xray that you want to deploy into the Quick Start.

        :schema: CfnExistingVpcModulePropsParameters
        '''
        if isinstance(access_cidr, dict):
            access_cidr = CfnExistingVpcModulePropsParametersAccessCidr(**access_cidr)
        if isinstance(artifactory_product, dict):
            artifactory_product = CfnExistingVpcModulePropsParametersArtifactoryProduct(**artifactory_product)
        if isinstance(artifactory_server_name, dict):
            artifactory_server_name = CfnExistingVpcModulePropsParametersArtifactoryServerName(**artifactory_server_name)
        if isinstance(artifactory_version, dict):
            artifactory_version = CfnExistingVpcModulePropsParametersArtifactoryVersion(**artifactory_version)
        if isinstance(availability_zone1, dict):
            availability_zone1 = CfnExistingVpcModulePropsParametersAvailabilityZone1(**availability_zone1)
        if isinstance(availability_zone2, dict):
            availability_zone2 = CfnExistingVpcModulePropsParametersAvailabilityZone2(**availability_zone2)
        if isinstance(bastion_enable_tcp_forwarding, dict):
            bastion_enable_tcp_forwarding = CfnExistingVpcModulePropsParametersBastionEnableTcpForwarding(**bastion_enable_tcp_forwarding)
        if isinstance(bastion_enable_x11_forwarding, dict):
            bastion_enable_x11_forwarding = CfnExistingVpcModulePropsParametersBastionEnableX11Forwarding(**bastion_enable_x11_forwarding)
        if isinstance(bastion_instance_type, dict):
            bastion_instance_type = CfnExistingVpcModulePropsParametersBastionInstanceType(**bastion_instance_type)
        if isinstance(bastion_os, dict):
            bastion_os = CfnExistingVpcModulePropsParametersBastionOs(**bastion_os)
        if isinstance(bastion_root_volume_size, dict):
            bastion_root_volume_size = CfnExistingVpcModulePropsParametersBastionRootVolumeSize(**bastion_root_volume_size)
        if isinstance(database_allocated_storage, dict):
            database_allocated_storage = CfnExistingVpcModulePropsParametersDatabaseAllocatedStorage(**database_allocated_storage)
        if isinstance(database_engine, dict):
            database_engine = CfnExistingVpcModulePropsParametersDatabaseEngine(**database_engine)
        if isinstance(database_instance, dict):
            database_instance = CfnExistingVpcModulePropsParametersDatabaseInstance(**database_instance)
        if isinstance(database_name, dict):
            database_name = CfnExistingVpcModulePropsParametersDatabaseName(**database_name)
        if isinstance(database_password, dict):
            database_password = CfnExistingVpcModulePropsParametersDatabasePassword(**database_password)
        if isinstance(database_preferred_az, dict):
            database_preferred_az = CfnExistingVpcModulePropsParametersDatabasePreferredAz(**database_preferred_az)
        if isinstance(database_user, dict):
            database_user = CfnExistingVpcModulePropsParametersDatabaseUser(**database_user)
        if isinstance(default_java_mem_settings, dict):
            default_java_mem_settings = CfnExistingVpcModulePropsParametersDefaultJavaMemSettings(**default_java_mem_settings)
        if isinstance(elb_scheme, dict):
            elb_scheme = CfnExistingVpcModulePropsParametersElbScheme(**elb_scheme)
        if isinstance(enable_bastion, dict):
            enable_bastion = CfnExistingVpcModulePropsParametersEnableBastion(**enable_bastion)
        if isinstance(extra_java_options, dict):
            extra_java_options = CfnExistingVpcModulePropsParametersExtraJavaOptions(**extra_java_options)
        if isinstance(install_xray, dict):
            install_xray = CfnExistingVpcModulePropsParametersInstallXray(**install_xray)
        if isinstance(instance_type, dict):
            instance_type = CfnExistingVpcModulePropsParametersInstanceType(**instance_type)
        if isinstance(key_pair_name, dict):
            key_pair_name = CfnExistingVpcModulePropsParametersKeyPairName(**key_pair_name)
        if isinstance(logical_id, dict):
            logical_id = CfnExistingVpcModulePropsParametersLogicalId(**logical_id)
        if isinstance(master_key, dict):
            master_key = CfnExistingVpcModulePropsParametersMasterKey(**master_key)
        if isinstance(multi_az_database, dict):
            multi_az_database = CfnExistingVpcModulePropsParametersMultiAzDatabase(**multi_az_database)
        if isinstance(num_bastion_hosts, dict):
            num_bastion_hosts = CfnExistingVpcModulePropsParametersNumBastionHosts(**num_bastion_hosts)
        if isinstance(number_of_secondary, dict):
            number_of_secondary = CfnExistingVpcModulePropsParametersNumberOfSecondary(**number_of_secondary)
        if isinstance(private_subnet1_cidr, dict):
            private_subnet1_cidr = CfnExistingVpcModulePropsParametersPrivateSubnet1Cidr(**private_subnet1_cidr)
        if isinstance(private_subnet1_id, dict):
            private_subnet1_id = CfnExistingVpcModulePropsParametersPrivateSubnet1Id(**private_subnet1_id)
        if isinstance(private_subnet2_cidr, dict):
            private_subnet2_cidr = CfnExistingVpcModulePropsParametersPrivateSubnet2Cidr(**private_subnet2_cidr)
        if isinstance(private_subnet2_id, dict):
            private_subnet2_id = CfnExistingVpcModulePropsParametersPrivateSubnet2Id(**private_subnet2_id)
        if isinstance(public_subnet1_id, dict):
            public_subnet1_id = CfnExistingVpcModulePropsParametersPublicSubnet1Id(**public_subnet1_id)
        if isinstance(public_subnet2_id, dict):
            public_subnet2_id = CfnExistingVpcModulePropsParametersPublicSubnet2Id(**public_subnet2_id)
        if isinstance(qs_s3_bucket_name, dict):
            qs_s3_bucket_name = CfnExistingVpcModulePropsParametersQsS3BucketName(**qs_s3_bucket_name)
        if isinstance(qs_s3_bucket_region, dict):
            qs_s3_bucket_region = CfnExistingVpcModulePropsParametersQsS3BucketRegion(**qs_s3_bucket_region)
        if isinstance(qs_s3_key_prefix, dict):
            qs_s3_key_prefix = CfnExistingVpcModulePropsParametersQsS3KeyPrefix(**qs_s3_key_prefix)
        if isinstance(remote_access_cidr, dict):
            remote_access_cidr = CfnExistingVpcModulePropsParametersRemoteAccessCidr(**remote_access_cidr)
        if isinstance(sm_cert_name, dict):
            sm_cert_name = CfnExistingVpcModulePropsParametersSmCertName(**sm_cert_name)
        if isinstance(sm_license_name, dict):
            sm_license_name = CfnExistingVpcModulePropsParametersSmLicenseName(**sm_license_name)
        if isinstance(volume_size, dict):
            volume_size = CfnExistingVpcModulePropsParametersVolumeSize(**volume_size)
        if isinstance(vpc_cidr, dict):
            vpc_cidr = CfnExistingVpcModulePropsParametersVpcCidr(**vpc_cidr)
        if isinstance(vpc_id, dict):
            vpc_id = CfnExistingVpcModulePropsParametersVpcId(**vpc_id)
        if isinstance(xray_database_password, dict):
            xray_database_password = CfnExistingVpcModulePropsParametersXrayDatabasePassword(**xray_database_password)
        if isinstance(xray_database_user, dict):
            xray_database_user = CfnExistingVpcModulePropsParametersXrayDatabaseUser(**xray_database_user)
        if isinstance(xray_instance_type, dict):
            xray_instance_type = CfnExistingVpcModulePropsParametersXrayInstanceType(**xray_instance_type)
        if isinstance(xray_number_of_instances, dict):
            xray_number_of_instances = CfnExistingVpcModulePropsParametersXrayNumberOfInstances(**xray_number_of_instances)
        if isinstance(xray_version, dict):
            xray_version = CfnExistingVpcModulePropsParametersXrayVersion(**xray_version)
        self._values: typing.Dict[str, typing.Any] = {}
        if access_cidr is not None:
            self._values["access_cidr"] = access_cidr
        if artifactory_product is not None:
            self._values["artifactory_product"] = artifactory_product
        if artifactory_server_name is not None:
            self._values["artifactory_server_name"] = artifactory_server_name
        if artifactory_version is not None:
            self._values["artifactory_version"] = artifactory_version
        if availability_zone1 is not None:
            self._values["availability_zone1"] = availability_zone1
        if availability_zone2 is not None:
            self._values["availability_zone2"] = availability_zone2
        if bastion_enable_tcp_forwarding is not None:
            self._values["bastion_enable_tcp_forwarding"] = bastion_enable_tcp_forwarding
        if bastion_enable_x11_forwarding is not None:
            self._values["bastion_enable_x11_forwarding"] = bastion_enable_x11_forwarding
        if bastion_instance_type is not None:
            self._values["bastion_instance_type"] = bastion_instance_type
        if bastion_os is not None:
            self._values["bastion_os"] = bastion_os
        if bastion_root_volume_size is not None:
            self._values["bastion_root_volume_size"] = bastion_root_volume_size
        if database_allocated_storage is not None:
            self._values["database_allocated_storage"] = database_allocated_storage
        if database_engine is not None:
            self._values["database_engine"] = database_engine
        if database_instance is not None:
            self._values["database_instance"] = database_instance
        if database_name is not None:
            self._values["database_name"] = database_name
        if database_password is not None:
            self._values["database_password"] = database_password
        if database_preferred_az is not None:
            self._values["database_preferred_az"] = database_preferred_az
        if database_user is not None:
            self._values["database_user"] = database_user
        if default_java_mem_settings is not None:
            self._values["default_java_mem_settings"] = default_java_mem_settings
        if elb_scheme is not None:
            self._values["elb_scheme"] = elb_scheme
        if enable_bastion is not None:
            self._values["enable_bastion"] = enable_bastion
        if extra_java_options is not None:
            self._values["extra_java_options"] = extra_java_options
        if install_xray is not None:
            self._values["install_xray"] = install_xray
        if instance_type is not None:
            self._values["instance_type"] = instance_type
        if key_pair_name is not None:
            self._values["key_pair_name"] = key_pair_name
        if logical_id is not None:
            self._values["logical_id"] = logical_id
        if master_key is not None:
            self._values["master_key"] = master_key
        if multi_az_database is not None:
            self._values["multi_az_database"] = multi_az_database
        if num_bastion_hosts is not None:
            self._values["num_bastion_hosts"] = num_bastion_hosts
        if number_of_secondary is not None:
            self._values["number_of_secondary"] = number_of_secondary
        if private_subnet1_cidr is not None:
            self._values["private_subnet1_cidr"] = private_subnet1_cidr
        if private_subnet1_id is not None:
            self._values["private_subnet1_id"] = private_subnet1_id
        if private_subnet2_cidr is not None:
            self._values["private_subnet2_cidr"] = private_subnet2_cidr
        if private_subnet2_id is not None:
            self._values["private_subnet2_id"] = private_subnet2_id
        if public_subnet1_id is not None:
            self._values["public_subnet1_id"] = public_subnet1_id
        if public_subnet2_id is not None:
            self._values["public_subnet2_id"] = public_subnet2_id
        if qs_s3_bucket_name is not None:
            self._values["qs_s3_bucket_name"] = qs_s3_bucket_name
        if qs_s3_bucket_region is not None:
            self._values["qs_s3_bucket_region"] = qs_s3_bucket_region
        if qs_s3_key_prefix is not None:
            self._values["qs_s3_key_prefix"] = qs_s3_key_prefix
        if remote_access_cidr is not None:
            self._values["remote_access_cidr"] = remote_access_cidr
        if sm_cert_name is not None:
            self._values["sm_cert_name"] = sm_cert_name
        if sm_license_name is not None:
            self._values["sm_license_name"] = sm_license_name
        if volume_size is not None:
            self._values["volume_size"] = volume_size
        if vpc_cidr is not None:
            self._values["vpc_cidr"] = vpc_cidr
        if vpc_id is not None:
            self._values["vpc_id"] = vpc_id
        if xray_database_password is not None:
            self._values["xray_database_password"] = xray_database_password
        if xray_database_user is not None:
            self._values["xray_database_user"] = xray_database_user
        if xray_instance_type is not None:
            self._values["xray_instance_type"] = xray_instance_type
        if xray_number_of_instances is not None:
            self._values["xray_number_of_instances"] = xray_number_of_instances
        if xray_version is not None:
            self._values["xray_version"] = xray_version

    @builtins.property
    def access_cidr(
        self,
    ) -> typing.Optional["CfnExistingVpcModulePropsParametersAccessCidr"]:
        '''CIDR IP range that is permitted to access Artifactory.

        We recommend that you set this value to a trusted IP range. For example, you might want to grant only your corporate network access to the software.

        :schema: CfnExistingVpcModulePropsParameters#AccessCidr
        '''
        result = self._values.get("access_cidr")
        return typing.cast(typing.Optional["CfnExistingVpcModulePropsParametersAccessCidr"], result)

    @builtins.property
    def artifactory_product(
        self,
    ) -> typing.Optional["CfnExistingVpcModulePropsParametersArtifactoryProduct"]:
        '''JFrog Artifactory product you want to install into an AMI.

        :schema: CfnExistingVpcModulePropsParameters#ArtifactoryProduct
        '''
        result = self._values.get("artifactory_product")
        return typing.cast(typing.Optional["CfnExistingVpcModulePropsParametersArtifactoryProduct"], result)

    @builtins.property
    def artifactory_server_name(
        self,
    ) -> typing.Optional["CfnExistingVpcModulePropsParametersArtifactoryServerName"]:
        '''Name of your Artifactory server.

        Ensure that this matches your certificate.

        :schema: CfnExistingVpcModulePropsParameters#ArtifactoryServerName
        '''
        result = self._values.get("artifactory_server_name")
        return typing.cast(typing.Optional["CfnExistingVpcModulePropsParametersArtifactoryServerName"], result)

    @builtins.property
    def artifactory_version(
        self,
    ) -> typing.Optional["CfnExistingVpcModulePropsParametersArtifactoryVersion"]:
        '''Version of Artifactory that you want to deploy into the Quick Start.

        See the release notes to select the version you want to deploy at https://www.jfrog.com/confluence/display/RTF/Release+Notes.

        :schema: CfnExistingVpcModulePropsParameters#ArtifactoryVersion
        '''
        result = self._values.get("artifactory_version")
        return typing.cast(typing.Optional["CfnExistingVpcModulePropsParametersArtifactoryVersion"], result)

    @builtins.property
    def availability_zone1(
        self,
    ) -> typing.Optional["CfnExistingVpcModulePropsParametersAvailabilityZone1"]:
        '''Availability Zone 1 to use for the subnets in the VPC.

        Two Availability Zones are used for this deployment.

        :schema: CfnExistingVpcModulePropsParameters#AvailabilityZone1
        '''
        result = self._values.get("availability_zone1")
        return typing.cast(typing.Optional["CfnExistingVpcModulePropsParametersAvailabilityZone1"], result)

    @builtins.property
    def availability_zone2(
        self,
    ) -> typing.Optional["CfnExistingVpcModulePropsParametersAvailabilityZone2"]:
        '''Availability Zone 2 to use for the subnets in the VPC.

        Two Availability Zones are used for this deployment.

        :schema: CfnExistingVpcModulePropsParameters#AvailabilityZone2
        '''
        result = self._values.get("availability_zone2")
        return typing.cast(typing.Optional["CfnExistingVpcModulePropsParametersAvailabilityZone2"], result)

    @builtins.property
    def bastion_enable_tcp_forwarding(
        self,
    ) -> typing.Optional["CfnExistingVpcModulePropsParametersBastionEnableTcpForwarding"]:
        '''Choose whether to enable TCPForwarding via the bootstrapping of the bastion instance or not.

        :schema: CfnExistingVpcModulePropsParameters#BastionEnableTcpForwarding
        '''
        result = self._values.get("bastion_enable_tcp_forwarding")
        return typing.cast(typing.Optional["CfnExistingVpcModulePropsParametersBastionEnableTcpForwarding"], result)

    @builtins.property
    def bastion_enable_x11_forwarding(
        self,
    ) -> typing.Optional["CfnExistingVpcModulePropsParametersBastionEnableX11Forwarding"]:
        '''Choose true to enable X11 via the bootstrapping of the bastion host.

        Setting this value to true will enable X Windows over SSH. X11 forwarding can be useful, but it is also a security risk, so it's recommended that you keep the default (false) setting.

        :schema: CfnExistingVpcModulePropsParameters#BastionEnableX11Forwarding
        '''
        result = self._values.get("bastion_enable_x11_forwarding")
        return typing.cast(typing.Optional["CfnExistingVpcModulePropsParametersBastionEnableX11Forwarding"], result)

    @builtins.property
    def bastion_instance_type(
        self,
    ) -> typing.Optional["CfnExistingVpcModulePropsParametersBastionInstanceType"]:
        '''Size of the bastion instances.

        :schema: CfnExistingVpcModulePropsParameters#BastionInstanceType
        '''
        result = self._values.get("bastion_instance_type")
        return typing.cast(typing.Optional["CfnExistingVpcModulePropsParametersBastionInstanceType"], result)

    @builtins.property
    def bastion_os(
        self,
    ) -> typing.Optional["CfnExistingVpcModulePropsParametersBastionOs"]:
        '''Linux distribution for the Amazon Machine Image (AMI) to be used for the bastion instances.

        :schema: CfnExistingVpcModulePropsParameters#BastionOs
        '''
        result = self._values.get("bastion_os")
        return typing.cast(typing.Optional["CfnExistingVpcModulePropsParametersBastionOs"], result)

    @builtins.property
    def bastion_root_volume_size(
        self,
    ) -> typing.Optional["CfnExistingVpcModulePropsParametersBastionRootVolumeSize"]:
        '''Size of the root volume on the bastion instances.

        :schema: CfnExistingVpcModulePropsParameters#BastionRootVolumeSize
        '''
        result = self._values.get("bastion_root_volume_size")
        return typing.cast(typing.Optional["CfnExistingVpcModulePropsParametersBastionRootVolumeSize"], result)

    @builtins.property
    def database_allocated_storage(
        self,
    ) -> typing.Optional["CfnExistingVpcModulePropsParametersDatabaseAllocatedStorage"]:
        '''Size in gigabytes of the available storage for the database instance.

        :schema: CfnExistingVpcModulePropsParameters#DatabaseAllocatedStorage
        '''
        result = self._values.get("database_allocated_storage")
        return typing.cast(typing.Optional["CfnExistingVpcModulePropsParametersDatabaseAllocatedStorage"], result)

    @builtins.property
    def database_engine(
        self,
    ) -> typing.Optional["CfnExistingVpcModulePropsParametersDatabaseEngine"]:
        '''Database engine that you want to run, which is currently locked to MySQL.

        :schema: CfnExistingVpcModulePropsParameters#DatabaseEngine
        '''
        result = self._values.get("database_engine")
        return typing.cast(typing.Optional["CfnExistingVpcModulePropsParametersDatabaseEngine"], result)

    @builtins.property
    def database_instance(
        self,
    ) -> typing.Optional["CfnExistingVpcModulePropsParametersDatabaseInstance"]:
        '''Size of the database to be deployed as part of the Quick Start.

        :schema: CfnExistingVpcModulePropsParameters#DatabaseInstance
        '''
        result = self._values.get("database_instance")
        return typing.cast(typing.Optional["CfnExistingVpcModulePropsParametersDatabaseInstance"], result)

    @builtins.property
    def database_name(
        self,
    ) -> typing.Optional["CfnExistingVpcModulePropsParametersDatabaseName"]:
        '''Name of your database instance.

        The name must be unique across all instances owned by your AWS account in the current Region. The database instance identifier is case-insensitive, but it's stored in lowercase (as in "mydbinstance").

        :schema: CfnExistingVpcModulePropsParameters#DatabaseName
        '''
        result = self._values.get("database_name")
        return typing.cast(typing.Optional["CfnExistingVpcModulePropsParametersDatabaseName"], result)

    @builtins.property
    def database_password(
        self,
    ) -> typing.Optional["CfnExistingVpcModulePropsParametersDatabasePassword"]:
        '''Password for the Artifactory database user.

        :schema: CfnExistingVpcModulePropsParameters#DatabasePassword
        '''
        result = self._values.get("database_password")
        return typing.cast(typing.Optional["CfnExistingVpcModulePropsParametersDatabasePassword"], result)

    @builtins.property
    def database_preferred_az(
        self,
    ) -> typing.Optional["CfnExistingVpcModulePropsParametersDatabasePreferredAz"]:
        '''Preferred availability zone for Amazon RDS primary instance.

        :schema: CfnExistingVpcModulePropsParameters#DatabasePreferredAz
        '''
        result = self._values.get("database_preferred_az")
        return typing.cast(typing.Optional["CfnExistingVpcModulePropsParametersDatabasePreferredAz"], result)

    @builtins.property
    def database_user(
        self,
    ) -> typing.Optional["CfnExistingVpcModulePropsParametersDatabaseUser"]:
        '''Login ID for the master user of your database instance.

        :schema: CfnExistingVpcModulePropsParameters#DatabaseUser
        '''
        result = self._values.get("database_user")
        return typing.cast(typing.Optional["CfnExistingVpcModulePropsParametersDatabaseUser"], result)

    @builtins.property
    def default_java_mem_settings(
        self,
    ) -> typing.Optional["CfnExistingVpcModulePropsParametersDefaultJavaMemSettings"]:
        '''Choose false to overwrite the standard memory-calculation options to pass to the Artifactory JVM.

        If you plan to overwrite them, ensure they are added to the ExtraJavaOptions to prevent the stack provision from failing.

        :schema: CfnExistingVpcModulePropsParameters#DefaultJavaMemSettings
        '''
        result = self._values.get("default_java_mem_settings")
        return typing.cast(typing.Optional["CfnExistingVpcModulePropsParametersDefaultJavaMemSettings"], result)

    @builtins.property
    def elb_scheme(
        self,
    ) -> typing.Optional["CfnExistingVpcModulePropsParametersElbScheme"]:
        '''Choose whether this is internet facing or internal.

        :schema: CfnExistingVpcModulePropsParameters#ELBScheme
        '''
        result = self._values.get("elb_scheme")
        return typing.cast(typing.Optional["CfnExistingVpcModulePropsParametersElbScheme"], result)

    @builtins.property
    def enable_bastion(
        self,
    ) -> typing.Optional["CfnExistingVpcModulePropsParametersEnableBastion"]:
        '''If set to true, a bastion host will be created.

        :schema: CfnExistingVpcModulePropsParameters#EnableBastion
        '''
        result = self._values.get("enable_bastion")
        return typing.cast(typing.Optional["CfnExistingVpcModulePropsParametersEnableBastion"], result)

    @builtins.property
    def extra_java_options(
        self,
    ) -> typing.Optional["CfnExistingVpcModulePropsParametersExtraJavaOptions"]:
        '''Set Java options to pass to the JVM for Artifactory.

        For more information, see the Artifactory system requirements at https://www.jfrog.com/confluence/display/RTF/System+Requirements#SystemRequirements-RecommendedHardware. Do not add Xms or Xmx settings without disabling DefaultJavaMemSettings.

        :schema: CfnExistingVpcModulePropsParameters#ExtraJavaOptions
        '''
        result = self._values.get("extra_java_options")
        return typing.cast(typing.Optional["CfnExistingVpcModulePropsParametersExtraJavaOptions"], result)

    @builtins.property
    def install_xray(
        self,
    ) -> typing.Optional["CfnExistingVpcModulePropsParametersInstallXray"]:
        '''Choose true to install JFrog Xray instance(s).

        :schema: CfnExistingVpcModulePropsParameters#InstallXray
        '''
        result = self._values.get("install_xray")
        return typing.cast(typing.Optional["CfnExistingVpcModulePropsParametersInstallXray"], result)

    @builtins.property
    def instance_type(
        self,
    ) -> typing.Optional["CfnExistingVpcModulePropsParametersInstanceType"]:
        '''EC2 type for the Artifactory instances.

        :schema: CfnExistingVpcModulePropsParameters#InstanceType
        '''
        result = self._values.get("instance_type")
        return typing.cast(typing.Optional["CfnExistingVpcModulePropsParametersInstanceType"], result)

    @builtins.property
    def key_pair_name(
        self,
    ) -> typing.Optional["CfnExistingVpcModulePropsParametersKeyPairName"]:
        '''Name of an existing key pair, which allows you to connect securely to your instance after it launches.

        This is the key pair you created in your preferred Region.

        :schema: CfnExistingVpcModulePropsParameters#KeyPairName
        '''
        result = self._values.get("key_pair_name")
        return typing.cast(typing.Optional["CfnExistingVpcModulePropsParametersKeyPairName"], result)

    @builtins.property
    def logical_id(
        self,
    ) -> typing.Optional["CfnExistingVpcModulePropsParametersLogicalId"]:
        '''Logical Id of the MODULE.

        :schema: CfnExistingVpcModulePropsParameters#LogicalId
        '''
        result = self._values.get("logical_id")
        return typing.cast(typing.Optional["CfnExistingVpcModulePropsParametersLogicalId"], result)

    @builtins.property
    def master_key(
        self,
    ) -> typing.Optional["CfnExistingVpcModulePropsParametersMasterKey"]:
        '''Master key for the Artifactory cluster.

        Generate a master key by using the command '$openssl rand -hex 16'.

        :schema: CfnExistingVpcModulePropsParameters#MasterKey
        '''
        result = self._values.get("master_key")
        return typing.cast(typing.Optional["CfnExistingVpcModulePropsParametersMasterKey"], result)

    @builtins.property
    def multi_az_database(
        self,
    ) -> typing.Optional["CfnExistingVpcModulePropsParametersMultiAzDatabase"]:
        '''Choose false to create an Amazon RDS instance in a single Availability Zone.

        :schema: CfnExistingVpcModulePropsParameters#MultiAzDatabase
        '''
        result = self._values.get("multi_az_database")
        return typing.cast(typing.Optional["CfnExistingVpcModulePropsParametersMultiAzDatabase"], result)

    @builtins.property
    def num_bastion_hosts(
        self,
    ) -> typing.Optional["CfnExistingVpcModulePropsParametersNumBastionHosts"]:
        '''Number of bastion instances to create.

        :schema: CfnExistingVpcModulePropsParameters#NumBastionHosts
        '''
        result = self._values.get("num_bastion_hosts")
        return typing.cast(typing.Optional["CfnExistingVpcModulePropsParametersNumBastionHosts"], result)

    @builtins.property
    def number_of_secondary(
        self,
    ) -> typing.Optional["CfnExistingVpcModulePropsParametersNumberOfSecondary"]:
        '''Number of secondary Artifactory servers to complete your HA deployment.

        To align with Artifactory best practices, the minimum number is two and the maximum is seven. Do not select more instances than you have licenses for.

        :schema: CfnExistingVpcModulePropsParameters#NumberOfSecondary
        '''
        result = self._values.get("number_of_secondary")
        return typing.cast(typing.Optional["CfnExistingVpcModulePropsParametersNumberOfSecondary"], result)

    @builtins.property
    def private_subnet1_cidr(
        self,
    ) -> typing.Optional["CfnExistingVpcModulePropsParametersPrivateSubnet1Cidr"]:
        '''CIDR of the private subnet in Availability Zone 1 of your existing VPC (e.g., 10.0.0.0/19).

        :schema: CfnExistingVpcModulePropsParameters#PrivateSubnet1Cidr
        '''
        result = self._values.get("private_subnet1_cidr")
        return typing.cast(typing.Optional["CfnExistingVpcModulePropsParametersPrivateSubnet1Cidr"], result)

    @builtins.property
    def private_subnet1_id(
        self,
    ) -> typing.Optional["CfnExistingVpcModulePropsParametersPrivateSubnet1Id"]:
        '''ID of the private subnet in Availability Zone 1 of your existing VPC (e.g., subnet-z0376dab).

        :schema: CfnExistingVpcModulePropsParameters#PrivateSubnet1Id
        '''
        result = self._values.get("private_subnet1_id")
        return typing.cast(typing.Optional["CfnExistingVpcModulePropsParametersPrivateSubnet1Id"], result)

    @builtins.property
    def private_subnet2_cidr(
        self,
    ) -> typing.Optional["CfnExistingVpcModulePropsParametersPrivateSubnet2Cidr"]:
        '''CIDR of the private subnet in Availability Zone 2 of your existing VPC (e.g., 10.0.32.0/19).

        :schema: CfnExistingVpcModulePropsParameters#PrivateSubnet2Cidr
        '''
        result = self._values.get("private_subnet2_cidr")
        return typing.cast(typing.Optional["CfnExistingVpcModulePropsParametersPrivateSubnet2Cidr"], result)

    @builtins.property
    def private_subnet2_id(
        self,
    ) -> typing.Optional["CfnExistingVpcModulePropsParametersPrivateSubnet2Id"]:
        '''ID of the private subnet in Availability Zone 2 of your existing VPC (e.g., subnet-z0376dab).

        :schema: CfnExistingVpcModulePropsParameters#PrivateSubnet2Id
        '''
        result = self._values.get("private_subnet2_id")
        return typing.cast(typing.Optional["CfnExistingVpcModulePropsParametersPrivateSubnet2Id"], result)

    @builtins.property
    def public_subnet1_id(
        self,
    ) -> typing.Optional["CfnExistingVpcModulePropsParametersPublicSubnet1Id"]:
        '''ID of the public subnet in Availability Zone 1 of your existing VPC (e.g., subnet-z0376dab).

        :schema: CfnExistingVpcModulePropsParameters#PublicSubnet1Id
        '''
        result = self._values.get("public_subnet1_id")
        return typing.cast(typing.Optional["CfnExistingVpcModulePropsParametersPublicSubnet1Id"], result)

    @builtins.property
    def public_subnet2_id(
        self,
    ) -> typing.Optional["CfnExistingVpcModulePropsParametersPublicSubnet2Id"]:
        '''ID of the public subnet in Availability Zone 1 of your existing VPC (e.g., subnet-z0376dab).

        :schema: CfnExistingVpcModulePropsParameters#PublicSubnet2Id
        '''
        result = self._values.get("public_subnet2_id")
        return typing.cast(typing.Optional["CfnExistingVpcModulePropsParametersPublicSubnet2Id"], result)

    @builtins.property
    def qs_s3_bucket_name(
        self,
    ) -> typing.Optional["CfnExistingVpcModulePropsParametersQsS3BucketName"]:
        '''S3 bucket name for the Quick Start assets.

        This string can include numbers, lowercase letters, and hyphens (-). It cannot start or end with a hyphen (-).

        :schema: CfnExistingVpcModulePropsParameters#QsS3BucketName
        '''
        result = self._values.get("qs_s3_bucket_name")
        return typing.cast(typing.Optional["CfnExistingVpcModulePropsParametersQsS3BucketName"], result)

    @builtins.property
    def qs_s3_bucket_region(
        self,
    ) -> typing.Optional["CfnExistingVpcModulePropsParametersQsS3BucketRegion"]:
        '''AWS Region where the Quick Start S3 bucket (QSS3BucketName) is hosted.

        If you use your own bucket, you must specify your own value.

        :schema: CfnExistingVpcModulePropsParameters#QsS3BucketRegion
        '''
        result = self._values.get("qs_s3_bucket_region")
        return typing.cast(typing.Optional["CfnExistingVpcModulePropsParametersQsS3BucketRegion"], result)

    @builtins.property
    def qs_s3_key_prefix(
        self,
    ) -> typing.Optional["CfnExistingVpcModulePropsParametersQsS3KeyPrefix"]:
        '''S3 key prefix for the Quick Start assets.

        Quick Start key prefix can include numbers, lowercase letters, uppercase letters, hyphens (-), and forward slash (/).

        :schema: CfnExistingVpcModulePropsParameters#QsS3KeyPrefix
        '''
        result = self._values.get("qs_s3_key_prefix")
        return typing.cast(typing.Optional["CfnExistingVpcModulePropsParametersQsS3KeyPrefix"], result)

    @builtins.property
    def remote_access_cidr(
        self,
    ) -> typing.Optional["CfnExistingVpcModulePropsParametersRemoteAccessCidr"]:
        '''Remote CIDR range that allows you to connect to the bastion instance by using SSH.

        We recommend that you set this value to a trusted IP range. For example, you might want to grant specific ranges inside your corporate network SSH access.

        :schema: CfnExistingVpcModulePropsParameters#RemoteAccessCidr
        '''
        result = self._values.get("remote_access_cidr")
        return typing.cast(typing.Optional["CfnExistingVpcModulePropsParametersRemoteAccessCidr"], result)

    @builtins.property
    def sm_cert_name(
        self,
    ) -> typing.Optional["CfnExistingVpcModulePropsParametersSmCertName"]:
        '''Secret name created in AWS Secrets Manager, which contains the SSL certificate and certificate key.

        :schema: CfnExistingVpcModulePropsParameters#SmCertName
        '''
        result = self._values.get("sm_cert_name")
        return typing.cast(typing.Optional["CfnExistingVpcModulePropsParametersSmCertName"], result)

    @builtins.property
    def sm_license_name(
        self,
    ) -> typing.Optional["CfnExistingVpcModulePropsParametersSmLicenseName"]:
        '''Secret name created in AWS Secrets Manager, which contains the Artifactory licenses.

        :schema: CfnExistingVpcModulePropsParameters#SmLicenseName
        '''
        result = self._values.get("sm_license_name")
        return typing.cast(typing.Optional["CfnExistingVpcModulePropsParametersSmLicenseName"], result)

    @builtins.property
    def volume_size(
        self,
    ) -> typing.Optional["CfnExistingVpcModulePropsParametersVolumeSize"]:
        '''Size in gigabytes of the available storage (min 10GB);

        the Quick Start will create an Amazon Elastic Block Store (Amazon EBS) volumes of this size.

        :schema: CfnExistingVpcModulePropsParameters#VolumeSize
        '''
        result = self._values.get("volume_size")
        return typing.cast(typing.Optional["CfnExistingVpcModulePropsParametersVolumeSize"], result)

    @builtins.property
    def vpc_cidr(self) -> typing.Optional["CfnExistingVpcModulePropsParametersVpcCidr"]:
        '''CIDR block for the VPC.

        :schema: CfnExistingVpcModulePropsParameters#VpcCidr
        '''
        result = self._values.get("vpc_cidr")
        return typing.cast(typing.Optional["CfnExistingVpcModulePropsParametersVpcCidr"], result)

    @builtins.property
    def vpc_id(self) -> typing.Optional["CfnExistingVpcModulePropsParametersVpcId"]:
        '''ID of your existing VPC (e.g., vpc-0343606e).

        :schema: CfnExistingVpcModulePropsParameters#VpcId
        '''
        result = self._values.get("vpc_id")
        return typing.cast(typing.Optional["CfnExistingVpcModulePropsParametersVpcId"], result)

    @builtins.property
    def xray_database_password(
        self,
    ) -> typing.Optional["CfnExistingVpcModulePropsParametersXrayDatabasePassword"]:
        '''The password for the Xray database user.

        :schema: CfnExistingVpcModulePropsParameters#XrayDatabasePassword
        '''
        result = self._values.get("xray_database_password")
        return typing.cast(typing.Optional["CfnExistingVpcModulePropsParametersXrayDatabasePassword"], result)

    @builtins.property
    def xray_database_user(
        self,
    ) -> typing.Optional["CfnExistingVpcModulePropsParametersXrayDatabaseUser"]:
        '''The login ID for the Xray database user.

        :schema: CfnExistingVpcModulePropsParameters#XrayDatabaseUser
        '''
        result = self._values.get("xray_database_user")
        return typing.cast(typing.Optional["CfnExistingVpcModulePropsParametersXrayDatabaseUser"], result)

    @builtins.property
    def xray_instance_type(
        self,
    ) -> typing.Optional["CfnExistingVpcModulePropsParametersXrayInstanceType"]:
        '''The EC2 instance type for the Xray instances.

        :schema: CfnExistingVpcModulePropsParameters#XrayInstanceType
        '''
        result = self._values.get("xray_instance_type")
        return typing.cast(typing.Optional["CfnExistingVpcModulePropsParametersXrayInstanceType"], result)

    @builtins.property
    def xray_number_of_instances(
        self,
    ) -> typing.Optional["CfnExistingVpcModulePropsParametersXrayNumberOfInstances"]:
        '''The number of Xray instances servers to complete your HA deployment.

        The minimum number is one; the maximum is seven. Do not select more than instances than you have licenses for.

        :schema: CfnExistingVpcModulePropsParameters#XrayNumberOfInstances
        '''
        result = self._values.get("xray_number_of_instances")
        return typing.cast(typing.Optional["CfnExistingVpcModulePropsParametersXrayNumberOfInstances"], result)

    @builtins.property
    def xray_version(
        self,
    ) -> typing.Optional["CfnExistingVpcModulePropsParametersXrayVersion"]:
        '''The version of Xray that you want to deploy into the Quick Start.

        :schema: CfnExistingVpcModulePropsParameters#XrayVersion
        '''
        result = self._values.get("xray_version")
        return typing.cast(typing.Optional["CfnExistingVpcModulePropsParametersXrayVersion"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnExistingVpcModulePropsParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-existingvpc-module.CfnExistingVpcModulePropsParametersAccessCidr",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnExistingVpcModulePropsParametersAccessCidr:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''CIDR IP range that is permitted to access Artifactory.

        We recommend that you set this value to a trusted IP range. For example, you might want to grant only your corporate network access to the software.

        :param description: 
        :param type: 

        :schema: CfnExistingVpcModulePropsParametersAccessCidr
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnExistingVpcModulePropsParametersAccessCidr#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnExistingVpcModulePropsParametersAccessCidr#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnExistingVpcModulePropsParametersAccessCidr(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-existingvpc-module.CfnExistingVpcModulePropsParametersArtifactoryProduct",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnExistingVpcModulePropsParametersArtifactoryProduct:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''JFrog Artifactory product you want to install into an AMI.

        :param description: 
        :param type: 

        :schema: CfnExistingVpcModulePropsParametersArtifactoryProduct
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnExistingVpcModulePropsParametersArtifactoryProduct#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnExistingVpcModulePropsParametersArtifactoryProduct#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnExistingVpcModulePropsParametersArtifactoryProduct(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-existingvpc-module.CfnExistingVpcModulePropsParametersArtifactoryServerName",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnExistingVpcModulePropsParametersArtifactoryServerName:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Name of your Artifactory server.

        Ensure that this matches your certificate.

        :param description: 
        :param type: 

        :schema: CfnExistingVpcModulePropsParametersArtifactoryServerName
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnExistingVpcModulePropsParametersArtifactoryServerName#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnExistingVpcModulePropsParametersArtifactoryServerName#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnExistingVpcModulePropsParametersArtifactoryServerName(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-existingvpc-module.CfnExistingVpcModulePropsParametersArtifactoryVersion",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnExistingVpcModulePropsParametersArtifactoryVersion:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Version of Artifactory that you want to deploy into the Quick Start.

        See the release notes to select the version you want to deploy at https://www.jfrog.com/confluence/display/RTF/Release+Notes.

        :param description: 
        :param type: 

        :schema: CfnExistingVpcModulePropsParametersArtifactoryVersion
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnExistingVpcModulePropsParametersArtifactoryVersion#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnExistingVpcModulePropsParametersArtifactoryVersion#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnExistingVpcModulePropsParametersArtifactoryVersion(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-existingvpc-module.CfnExistingVpcModulePropsParametersAvailabilityZone1",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnExistingVpcModulePropsParametersAvailabilityZone1:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Availability Zone 1 to use for the subnets in the VPC.

        Two Availability Zones are used for this deployment.

        :param description: 
        :param type: 

        :schema: CfnExistingVpcModulePropsParametersAvailabilityZone1
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnExistingVpcModulePropsParametersAvailabilityZone1#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnExistingVpcModulePropsParametersAvailabilityZone1#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnExistingVpcModulePropsParametersAvailabilityZone1(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-existingvpc-module.CfnExistingVpcModulePropsParametersAvailabilityZone2",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnExistingVpcModulePropsParametersAvailabilityZone2:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Availability Zone 2 to use for the subnets in the VPC.

        Two Availability Zones are used for this deployment.

        :param description: 
        :param type: 

        :schema: CfnExistingVpcModulePropsParametersAvailabilityZone2
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnExistingVpcModulePropsParametersAvailabilityZone2#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnExistingVpcModulePropsParametersAvailabilityZone2#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnExistingVpcModulePropsParametersAvailabilityZone2(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-existingvpc-module.CfnExistingVpcModulePropsParametersBastionEnableTcpForwarding",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnExistingVpcModulePropsParametersBastionEnableTcpForwarding:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Choose whether to enable TCPForwarding via the bootstrapping of the bastion instance or not.

        :param description: 
        :param type: 

        :schema: CfnExistingVpcModulePropsParametersBastionEnableTcpForwarding
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnExistingVpcModulePropsParametersBastionEnableTcpForwarding#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnExistingVpcModulePropsParametersBastionEnableTcpForwarding#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnExistingVpcModulePropsParametersBastionEnableTcpForwarding(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-existingvpc-module.CfnExistingVpcModulePropsParametersBastionEnableX11Forwarding",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnExistingVpcModulePropsParametersBastionEnableX11Forwarding:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Choose true to enable X11 via the bootstrapping of the bastion host.

        Setting this value to true will enable X Windows over SSH. X11 forwarding can be useful, but it is also a security risk, so it's recommended that you keep the default (false) setting.

        :param description: 
        :param type: 

        :schema: CfnExistingVpcModulePropsParametersBastionEnableX11Forwarding
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnExistingVpcModulePropsParametersBastionEnableX11Forwarding#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnExistingVpcModulePropsParametersBastionEnableX11Forwarding#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnExistingVpcModulePropsParametersBastionEnableX11Forwarding(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-existingvpc-module.CfnExistingVpcModulePropsParametersBastionInstanceType",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnExistingVpcModulePropsParametersBastionInstanceType:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Size of the bastion instances.

        :param description: 
        :param type: 

        :schema: CfnExistingVpcModulePropsParametersBastionInstanceType
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnExistingVpcModulePropsParametersBastionInstanceType#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnExistingVpcModulePropsParametersBastionInstanceType#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnExistingVpcModulePropsParametersBastionInstanceType(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-existingvpc-module.CfnExistingVpcModulePropsParametersBastionOs",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnExistingVpcModulePropsParametersBastionOs:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Linux distribution for the Amazon Machine Image (AMI) to be used for the bastion instances.

        :param description: 
        :param type: 

        :schema: CfnExistingVpcModulePropsParametersBastionOs
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnExistingVpcModulePropsParametersBastionOs#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnExistingVpcModulePropsParametersBastionOs#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnExistingVpcModulePropsParametersBastionOs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-existingvpc-module.CfnExistingVpcModulePropsParametersBastionRootVolumeSize",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnExistingVpcModulePropsParametersBastionRootVolumeSize:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Size of the root volume on the bastion instances.

        :param description: 
        :param type: 

        :schema: CfnExistingVpcModulePropsParametersBastionRootVolumeSize
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnExistingVpcModulePropsParametersBastionRootVolumeSize#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnExistingVpcModulePropsParametersBastionRootVolumeSize#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnExistingVpcModulePropsParametersBastionRootVolumeSize(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-existingvpc-module.CfnExistingVpcModulePropsParametersDatabaseAllocatedStorage",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnExistingVpcModulePropsParametersDatabaseAllocatedStorage:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Size in gigabytes of the available storage for the database instance.

        :param description: 
        :param type: 

        :schema: CfnExistingVpcModulePropsParametersDatabaseAllocatedStorage
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnExistingVpcModulePropsParametersDatabaseAllocatedStorage#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnExistingVpcModulePropsParametersDatabaseAllocatedStorage#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnExistingVpcModulePropsParametersDatabaseAllocatedStorage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-existingvpc-module.CfnExistingVpcModulePropsParametersDatabaseEngine",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnExistingVpcModulePropsParametersDatabaseEngine:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Database engine that you want to run, which is currently locked to MySQL.

        :param description: 
        :param type: 

        :schema: CfnExistingVpcModulePropsParametersDatabaseEngine
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnExistingVpcModulePropsParametersDatabaseEngine#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnExistingVpcModulePropsParametersDatabaseEngine#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnExistingVpcModulePropsParametersDatabaseEngine(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-existingvpc-module.CfnExistingVpcModulePropsParametersDatabaseInstance",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnExistingVpcModulePropsParametersDatabaseInstance:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Size of the database to be deployed as part of the Quick Start.

        :param description: 
        :param type: 

        :schema: CfnExistingVpcModulePropsParametersDatabaseInstance
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnExistingVpcModulePropsParametersDatabaseInstance#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnExistingVpcModulePropsParametersDatabaseInstance#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnExistingVpcModulePropsParametersDatabaseInstance(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-existingvpc-module.CfnExistingVpcModulePropsParametersDatabaseName",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnExistingVpcModulePropsParametersDatabaseName:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Name of your database instance.

        The name must be unique across all instances owned by your AWS account in the current Region. The database instance identifier is case-insensitive, but it's stored in lowercase (as in "mydbinstance").

        :param description: 
        :param type: 

        :schema: CfnExistingVpcModulePropsParametersDatabaseName
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnExistingVpcModulePropsParametersDatabaseName#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnExistingVpcModulePropsParametersDatabaseName#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnExistingVpcModulePropsParametersDatabaseName(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-existingvpc-module.CfnExistingVpcModulePropsParametersDatabasePassword",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnExistingVpcModulePropsParametersDatabasePassword:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Password for the Artifactory database user.

        :param description: 
        :param type: 

        :schema: CfnExistingVpcModulePropsParametersDatabasePassword
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnExistingVpcModulePropsParametersDatabasePassword#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnExistingVpcModulePropsParametersDatabasePassword#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnExistingVpcModulePropsParametersDatabasePassword(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-existingvpc-module.CfnExistingVpcModulePropsParametersDatabasePreferredAz",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnExistingVpcModulePropsParametersDatabasePreferredAz:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Preferred availability zone for Amazon RDS primary instance.

        :param description: 
        :param type: 

        :schema: CfnExistingVpcModulePropsParametersDatabasePreferredAz
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnExistingVpcModulePropsParametersDatabasePreferredAz#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnExistingVpcModulePropsParametersDatabasePreferredAz#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnExistingVpcModulePropsParametersDatabasePreferredAz(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-existingvpc-module.CfnExistingVpcModulePropsParametersDatabaseUser",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnExistingVpcModulePropsParametersDatabaseUser:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Login ID for the master user of your database instance.

        :param description: 
        :param type: 

        :schema: CfnExistingVpcModulePropsParametersDatabaseUser
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnExistingVpcModulePropsParametersDatabaseUser#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnExistingVpcModulePropsParametersDatabaseUser#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnExistingVpcModulePropsParametersDatabaseUser(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-existingvpc-module.CfnExistingVpcModulePropsParametersDefaultJavaMemSettings",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnExistingVpcModulePropsParametersDefaultJavaMemSettings:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Choose false to overwrite the standard memory-calculation options to pass to the Artifactory JVM.

        If you plan to overwrite them, ensure they are added to the ExtraJavaOptions to prevent the stack provision from failing.

        :param description: 
        :param type: 

        :schema: CfnExistingVpcModulePropsParametersDefaultJavaMemSettings
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnExistingVpcModulePropsParametersDefaultJavaMemSettings#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnExistingVpcModulePropsParametersDefaultJavaMemSettings#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnExistingVpcModulePropsParametersDefaultJavaMemSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-existingvpc-module.CfnExistingVpcModulePropsParametersElbScheme",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnExistingVpcModulePropsParametersElbScheme:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Choose whether this is internet facing or internal.

        :param description: 
        :param type: 

        :schema: CfnExistingVpcModulePropsParametersElbScheme
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnExistingVpcModulePropsParametersElbScheme#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnExistingVpcModulePropsParametersElbScheme#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnExistingVpcModulePropsParametersElbScheme(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-existingvpc-module.CfnExistingVpcModulePropsParametersEnableBastion",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnExistingVpcModulePropsParametersEnableBastion:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''If set to true, a bastion host will be created.

        :param description: 
        :param type: 

        :schema: CfnExistingVpcModulePropsParametersEnableBastion
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnExistingVpcModulePropsParametersEnableBastion#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnExistingVpcModulePropsParametersEnableBastion#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnExistingVpcModulePropsParametersEnableBastion(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-existingvpc-module.CfnExistingVpcModulePropsParametersExtraJavaOptions",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnExistingVpcModulePropsParametersExtraJavaOptions:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Set Java options to pass to the JVM for Artifactory.

        For more information, see the Artifactory system requirements at https://www.jfrog.com/confluence/display/RTF/System+Requirements#SystemRequirements-RecommendedHardware. Do not add Xms or Xmx settings without disabling DefaultJavaMemSettings.

        :param description: 
        :param type: 

        :schema: CfnExistingVpcModulePropsParametersExtraJavaOptions
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnExistingVpcModulePropsParametersExtraJavaOptions#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnExistingVpcModulePropsParametersExtraJavaOptions#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnExistingVpcModulePropsParametersExtraJavaOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-existingvpc-module.CfnExistingVpcModulePropsParametersInstallXray",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnExistingVpcModulePropsParametersInstallXray:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Choose true to install JFrog Xray instance(s).

        :param description: 
        :param type: 

        :schema: CfnExistingVpcModulePropsParametersInstallXray
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnExistingVpcModulePropsParametersInstallXray#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnExistingVpcModulePropsParametersInstallXray#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnExistingVpcModulePropsParametersInstallXray(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-existingvpc-module.CfnExistingVpcModulePropsParametersInstanceType",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnExistingVpcModulePropsParametersInstanceType:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''EC2 type for the Artifactory instances.

        :param description: 
        :param type: 

        :schema: CfnExistingVpcModulePropsParametersInstanceType
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnExistingVpcModulePropsParametersInstanceType#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnExistingVpcModulePropsParametersInstanceType#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnExistingVpcModulePropsParametersInstanceType(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-existingvpc-module.CfnExistingVpcModulePropsParametersKeyPairName",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnExistingVpcModulePropsParametersKeyPairName:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Name of an existing key pair, which allows you to connect securely to your instance after it launches.

        This is the key pair you created in your preferred Region.

        :param description: 
        :param type: 

        :schema: CfnExistingVpcModulePropsParametersKeyPairName
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnExistingVpcModulePropsParametersKeyPairName#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnExistingVpcModulePropsParametersKeyPairName#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnExistingVpcModulePropsParametersKeyPairName(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-existingvpc-module.CfnExistingVpcModulePropsParametersLogicalId",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnExistingVpcModulePropsParametersLogicalId:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Logical Id of the MODULE.

        :param description: 
        :param type: 

        :schema: CfnExistingVpcModulePropsParametersLogicalId
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnExistingVpcModulePropsParametersLogicalId#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnExistingVpcModulePropsParametersLogicalId#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnExistingVpcModulePropsParametersLogicalId(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-existingvpc-module.CfnExistingVpcModulePropsParametersMasterKey",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnExistingVpcModulePropsParametersMasterKey:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Master key for the Artifactory cluster.

        Generate a master key by using the command '$openssl rand -hex 16'.

        :param description: 
        :param type: 

        :schema: CfnExistingVpcModulePropsParametersMasterKey
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnExistingVpcModulePropsParametersMasterKey#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnExistingVpcModulePropsParametersMasterKey#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnExistingVpcModulePropsParametersMasterKey(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-existingvpc-module.CfnExistingVpcModulePropsParametersMultiAzDatabase",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnExistingVpcModulePropsParametersMultiAzDatabase:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Choose false to create an Amazon RDS instance in a single Availability Zone.

        :param description: 
        :param type: 

        :schema: CfnExistingVpcModulePropsParametersMultiAzDatabase
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnExistingVpcModulePropsParametersMultiAzDatabase#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnExistingVpcModulePropsParametersMultiAzDatabase#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnExistingVpcModulePropsParametersMultiAzDatabase(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-existingvpc-module.CfnExistingVpcModulePropsParametersNumBastionHosts",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnExistingVpcModulePropsParametersNumBastionHosts:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Number of bastion instances to create.

        :param description: 
        :param type: 

        :schema: CfnExistingVpcModulePropsParametersNumBastionHosts
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnExistingVpcModulePropsParametersNumBastionHosts#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnExistingVpcModulePropsParametersNumBastionHosts#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnExistingVpcModulePropsParametersNumBastionHosts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-existingvpc-module.CfnExistingVpcModulePropsParametersNumberOfSecondary",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnExistingVpcModulePropsParametersNumberOfSecondary:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Number of secondary Artifactory servers to complete your HA deployment.

        To align with Artifactory best practices, the minimum number is two and the maximum is seven. Do not select more instances than you have licenses for.

        :param description: 
        :param type: 

        :schema: CfnExistingVpcModulePropsParametersNumberOfSecondary
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnExistingVpcModulePropsParametersNumberOfSecondary#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnExistingVpcModulePropsParametersNumberOfSecondary#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnExistingVpcModulePropsParametersNumberOfSecondary(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-existingvpc-module.CfnExistingVpcModulePropsParametersPrivateSubnet1Cidr",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnExistingVpcModulePropsParametersPrivateSubnet1Cidr:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''CIDR of the private subnet in Availability Zone 1 of your existing VPC (e.g., 10.0.0.0/19).

        :param description: 
        :param type: 

        :schema: CfnExistingVpcModulePropsParametersPrivateSubnet1Cidr
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnExistingVpcModulePropsParametersPrivateSubnet1Cidr#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnExistingVpcModulePropsParametersPrivateSubnet1Cidr#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnExistingVpcModulePropsParametersPrivateSubnet1Cidr(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-existingvpc-module.CfnExistingVpcModulePropsParametersPrivateSubnet1Id",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnExistingVpcModulePropsParametersPrivateSubnet1Id:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''ID of the private subnet in Availability Zone 1 of your existing VPC (e.g., subnet-z0376dab).

        :param description: 
        :param type: 

        :schema: CfnExistingVpcModulePropsParametersPrivateSubnet1Id
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnExistingVpcModulePropsParametersPrivateSubnet1Id#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnExistingVpcModulePropsParametersPrivateSubnet1Id#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnExistingVpcModulePropsParametersPrivateSubnet1Id(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-existingvpc-module.CfnExistingVpcModulePropsParametersPrivateSubnet2Cidr",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnExistingVpcModulePropsParametersPrivateSubnet2Cidr:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''CIDR of the private subnet in Availability Zone 2 of your existing VPC (e.g., 10.0.32.0/19).

        :param description: 
        :param type: 

        :schema: CfnExistingVpcModulePropsParametersPrivateSubnet2Cidr
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnExistingVpcModulePropsParametersPrivateSubnet2Cidr#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnExistingVpcModulePropsParametersPrivateSubnet2Cidr#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnExistingVpcModulePropsParametersPrivateSubnet2Cidr(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-existingvpc-module.CfnExistingVpcModulePropsParametersPrivateSubnet2Id",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnExistingVpcModulePropsParametersPrivateSubnet2Id:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''ID of the private subnet in Availability Zone 2 of your existing VPC (e.g., subnet-z0376dab).

        :param description: 
        :param type: 

        :schema: CfnExistingVpcModulePropsParametersPrivateSubnet2Id
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnExistingVpcModulePropsParametersPrivateSubnet2Id#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnExistingVpcModulePropsParametersPrivateSubnet2Id#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnExistingVpcModulePropsParametersPrivateSubnet2Id(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-existingvpc-module.CfnExistingVpcModulePropsParametersPublicSubnet1Id",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnExistingVpcModulePropsParametersPublicSubnet1Id:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''ID of the public subnet in Availability Zone 1 of your existing VPC (e.g., subnet-z0376dab).

        :param description: 
        :param type: 

        :schema: CfnExistingVpcModulePropsParametersPublicSubnet1Id
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnExistingVpcModulePropsParametersPublicSubnet1Id#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnExistingVpcModulePropsParametersPublicSubnet1Id#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnExistingVpcModulePropsParametersPublicSubnet1Id(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-existingvpc-module.CfnExistingVpcModulePropsParametersPublicSubnet2Id",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnExistingVpcModulePropsParametersPublicSubnet2Id:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''ID of the public subnet in Availability Zone 1 of your existing VPC (e.g., subnet-z0376dab).

        :param description: 
        :param type: 

        :schema: CfnExistingVpcModulePropsParametersPublicSubnet2Id
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnExistingVpcModulePropsParametersPublicSubnet2Id#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnExistingVpcModulePropsParametersPublicSubnet2Id#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnExistingVpcModulePropsParametersPublicSubnet2Id(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-existingvpc-module.CfnExistingVpcModulePropsParametersQsS3BucketName",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnExistingVpcModulePropsParametersQsS3BucketName:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''S3 bucket name for the Quick Start assets.

        This string can include numbers, lowercase letters, and hyphens (-). It cannot start or end with a hyphen (-).

        :param description: 
        :param type: 

        :schema: CfnExistingVpcModulePropsParametersQsS3BucketName
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnExistingVpcModulePropsParametersQsS3BucketName#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnExistingVpcModulePropsParametersQsS3BucketName#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnExistingVpcModulePropsParametersQsS3BucketName(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-existingvpc-module.CfnExistingVpcModulePropsParametersQsS3BucketRegion",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnExistingVpcModulePropsParametersQsS3BucketRegion:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''AWS Region where the Quick Start S3 bucket (QSS3BucketName) is hosted.

        If you use your own bucket, you must specify your own value.

        :param description: 
        :param type: 

        :schema: CfnExistingVpcModulePropsParametersQsS3BucketRegion
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnExistingVpcModulePropsParametersQsS3BucketRegion#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnExistingVpcModulePropsParametersQsS3BucketRegion#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnExistingVpcModulePropsParametersQsS3BucketRegion(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-existingvpc-module.CfnExistingVpcModulePropsParametersQsS3KeyPrefix",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnExistingVpcModulePropsParametersQsS3KeyPrefix:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''S3 key prefix for the Quick Start assets.

        Quick Start key prefix can include numbers, lowercase letters, uppercase letters, hyphens (-), and forward slash (/).

        :param description: 
        :param type: 

        :schema: CfnExistingVpcModulePropsParametersQsS3KeyPrefix
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnExistingVpcModulePropsParametersQsS3KeyPrefix#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnExistingVpcModulePropsParametersQsS3KeyPrefix#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnExistingVpcModulePropsParametersQsS3KeyPrefix(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-existingvpc-module.CfnExistingVpcModulePropsParametersRemoteAccessCidr",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnExistingVpcModulePropsParametersRemoteAccessCidr:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Remote CIDR range that allows you to connect to the bastion instance by using SSH.

        We recommend that you set this value to a trusted IP range. For example, you might want to grant specific ranges inside your corporate network SSH access.

        :param description: 
        :param type: 

        :schema: CfnExistingVpcModulePropsParametersRemoteAccessCidr
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnExistingVpcModulePropsParametersRemoteAccessCidr#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnExistingVpcModulePropsParametersRemoteAccessCidr#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnExistingVpcModulePropsParametersRemoteAccessCidr(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-existingvpc-module.CfnExistingVpcModulePropsParametersSmCertName",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnExistingVpcModulePropsParametersSmCertName:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Secret name created in AWS Secrets Manager, which contains the SSL certificate and certificate key.

        :param description: 
        :param type: 

        :schema: CfnExistingVpcModulePropsParametersSmCertName
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnExistingVpcModulePropsParametersSmCertName#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnExistingVpcModulePropsParametersSmCertName#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnExistingVpcModulePropsParametersSmCertName(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-existingvpc-module.CfnExistingVpcModulePropsParametersSmLicenseName",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnExistingVpcModulePropsParametersSmLicenseName:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Secret name created in AWS Secrets Manager, which contains the Artifactory licenses.

        :param description: 
        :param type: 

        :schema: CfnExistingVpcModulePropsParametersSmLicenseName
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnExistingVpcModulePropsParametersSmLicenseName#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnExistingVpcModulePropsParametersSmLicenseName#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnExistingVpcModulePropsParametersSmLicenseName(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-existingvpc-module.CfnExistingVpcModulePropsParametersVolumeSize",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnExistingVpcModulePropsParametersVolumeSize:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Size in gigabytes of the available storage (min 10GB);

        the Quick Start will create an Amazon Elastic Block Store (Amazon EBS) volumes of this size.

        :param description: 
        :param type: 

        :schema: CfnExistingVpcModulePropsParametersVolumeSize
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnExistingVpcModulePropsParametersVolumeSize#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnExistingVpcModulePropsParametersVolumeSize#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnExistingVpcModulePropsParametersVolumeSize(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-existingvpc-module.CfnExistingVpcModulePropsParametersVpcCidr",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnExistingVpcModulePropsParametersVpcCidr:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''CIDR block for the VPC.

        :param description: 
        :param type: 

        :schema: CfnExistingVpcModulePropsParametersVpcCidr
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnExistingVpcModulePropsParametersVpcCidr#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnExistingVpcModulePropsParametersVpcCidr#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnExistingVpcModulePropsParametersVpcCidr(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-existingvpc-module.CfnExistingVpcModulePropsParametersVpcId",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnExistingVpcModulePropsParametersVpcId:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''ID of your existing VPC (e.g., vpc-0343606e).

        :param description: 
        :param type: 

        :schema: CfnExistingVpcModulePropsParametersVpcId
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnExistingVpcModulePropsParametersVpcId#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnExistingVpcModulePropsParametersVpcId#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnExistingVpcModulePropsParametersVpcId(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-existingvpc-module.CfnExistingVpcModulePropsParametersXrayDatabasePassword",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnExistingVpcModulePropsParametersXrayDatabasePassword:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The password for the Xray database user.

        :param description: 
        :param type: 

        :schema: CfnExistingVpcModulePropsParametersXrayDatabasePassword
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnExistingVpcModulePropsParametersXrayDatabasePassword#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnExistingVpcModulePropsParametersXrayDatabasePassword#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnExistingVpcModulePropsParametersXrayDatabasePassword(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-existingvpc-module.CfnExistingVpcModulePropsParametersXrayDatabaseUser",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnExistingVpcModulePropsParametersXrayDatabaseUser:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The login ID for the Xray database user.

        :param description: 
        :param type: 

        :schema: CfnExistingVpcModulePropsParametersXrayDatabaseUser
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnExistingVpcModulePropsParametersXrayDatabaseUser#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnExistingVpcModulePropsParametersXrayDatabaseUser#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnExistingVpcModulePropsParametersXrayDatabaseUser(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-existingvpc-module.CfnExistingVpcModulePropsParametersXrayInstanceType",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnExistingVpcModulePropsParametersXrayInstanceType:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The EC2 instance type for the Xray instances.

        :param description: 
        :param type: 

        :schema: CfnExistingVpcModulePropsParametersXrayInstanceType
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnExistingVpcModulePropsParametersXrayInstanceType#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnExistingVpcModulePropsParametersXrayInstanceType#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnExistingVpcModulePropsParametersXrayInstanceType(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-existingvpc-module.CfnExistingVpcModulePropsParametersXrayNumberOfInstances",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnExistingVpcModulePropsParametersXrayNumberOfInstances:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The number of Xray instances servers to complete your HA deployment.

        The minimum number is one; the maximum is seven. Do not select more than instances than you have licenses for.

        :param description: 
        :param type: 

        :schema: CfnExistingVpcModulePropsParametersXrayNumberOfInstances
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnExistingVpcModulePropsParametersXrayNumberOfInstances#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnExistingVpcModulePropsParametersXrayNumberOfInstances#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnExistingVpcModulePropsParametersXrayNumberOfInstances(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-existingvpc-module.CfnExistingVpcModulePropsParametersXrayVersion",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnExistingVpcModulePropsParametersXrayVersion:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The version of Xray that you want to deploy into the Quick Start.

        :param description: 
        :param type: 

        :schema: CfnExistingVpcModulePropsParametersXrayVersion
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnExistingVpcModulePropsParametersXrayVersion#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnExistingVpcModulePropsParametersXrayVersion#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnExistingVpcModulePropsParametersXrayVersion(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-existingvpc-module.CfnExistingVpcModulePropsResources",
    jsii_struct_bases=[],
    name_mapping={
        "artifactory_core_infra_stack": "artifactoryCoreInfraStack",
        "artifactory_ec2_sg": "artifactoryEc2Sg",
        "artifactory_elb": "artifactoryElb",
        "artifactory_elb_listener": "artifactoryElbListener",
        "artifactory_host_profile": "artifactoryHostProfile",
        "artifactory_host_role": "artifactoryHostRole",
        "artifactory_internal_elb": "artifactoryInternalElb",
        "artifactory_internal_elb_listener": "artifactoryInternalElbListener",
        "artifactory_internal_target_group": "artifactoryInternalTargetGroup",
        "artifactory_primary": "artifactoryPrimary",
        "artifactory_secondary": "artifactorySecondary",
        "artifactory_ssl_elb_listener": "artifactorySslElbListener",
        "artifactory_ssl_target_group": "artifactorySslTargetGroup",
        "artifactory_target_group": "artifactoryTargetGroup",
        "bastion_stack": "bastionStack",
        "xray_existing_vpc_stack": "xrayExistingVpcStack",
        "xray_host_profile": "xrayHostProfile",
        "xray_host_role": "xrayHostRole",
    },
)
class CfnExistingVpcModulePropsResources:
    def __init__(
        self,
        *,
        artifactory_core_infra_stack: typing.Optional["CfnExistingVpcModulePropsResourcesArtifactoryCoreInfraStack"] = None,
        artifactory_ec2_sg: typing.Optional["CfnExistingVpcModulePropsResourcesArtifactoryEc2Sg"] = None,
        artifactory_elb: typing.Optional["CfnExistingVpcModulePropsResourcesArtifactoryElb"] = None,
        artifactory_elb_listener: typing.Optional["CfnExistingVpcModulePropsResourcesArtifactoryElbListener"] = None,
        artifactory_host_profile: typing.Optional["CfnExistingVpcModulePropsResourcesArtifactoryHostProfile"] = None,
        artifactory_host_role: typing.Optional["CfnExistingVpcModulePropsResourcesArtifactoryHostRole"] = None,
        artifactory_internal_elb: typing.Optional["CfnExistingVpcModulePropsResourcesArtifactoryInternalElb"] = None,
        artifactory_internal_elb_listener: typing.Optional["CfnExistingVpcModulePropsResourcesArtifactoryInternalElbListener"] = None,
        artifactory_internal_target_group: typing.Optional["CfnExistingVpcModulePropsResourcesArtifactoryInternalTargetGroup"] = None,
        artifactory_primary: typing.Optional["CfnExistingVpcModulePropsResourcesArtifactoryPrimary"] = None,
        artifactory_secondary: typing.Optional["CfnExistingVpcModulePropsResourcesArtifactorySecondary"] = None,
        artifactory_ssl_elb_listener: typing.Optional["CfnExistingVpcModulePropsResourcesArtifactorySslElbListener"] = None,
        artifactory_ssl_target_group: typing.Optional["CfnExistingVpcModulePropsResourcesArtifactorySslTargetGroup"] = None,
        artifactory_target_group: typing.Optional["CfnExistingVpcModulePropsResourcesArtifactoryTargetGroup"] = None,
        bastion_stack: typing.Optional["CfnExistingVpcModulePropsResourcesBastionStack"] = None,
        xray_existing_vpc_stack: typing.Optional["CfnExistingVpcModulePropsResourcesXrayExistingVpcStack"] = None,
        xray_host_profile: typing.Optional["CfnExistingVpcModulePropsResourcesXrayHostProfile"] = None,
        xray_host_role: typing.Optional["CfnExistingVpcModulePropsResourcesXrayHostRole"] = None,
    ) -> None:
        '''
        :param artifactory_core_infra_stack: 
        :param artifactory_ec2_sg: 
        :param artifactory_elb: 
        :param artifactory_elb_listener: 
        :param artifactory_host_profile: 
        :param artifactory_host_role: 
        :param artifactory_internal_elb: 
        :param artifactory_internal_elb_listener: 
        :param artifactory_internal_target_group: 
        :param artifactory_primary: 
        :param artifactory_secondary: 
        :param artifactory_ssl_elb_listener: 
        :param artifactory_ssl_target_group: 
        :param artifactory_target_group: 
        :param bastion_stack: 
        :param xray_existing_vpc_stack: 
        :param xray_host_profile: 
        :param xray_host_role: 

        :schema: CfnExistingVpcModulePropsResources
        '''
        if isinstance(artifactory_core_infra_stack, dict):
            artifactory_core_infra_stack = CfnExistingVpcModulePropsResourcesArtifactoryCoreInfraStack(**artifactory_core_infra_stack)
        if isinstance(artifactory_ec2_sg, dict):
            artifactory_ec2_sg = CfnExistingVpcModulePropsResourcesArtifactoryEc2Sg(**artifactory_ec2_sg)
        if isinstance(artifactory_elb, dict):
            artifactory_elb = CfnExistingVpcModulePropsResourcesArtifactoryElb(**artifactory_elb)
        if isinstance(artifactory_elb_listener, dict):
            artifactory_elb_listener = CfnExistingVpcModulePropsResourcesArtifactoryElbListener(**artifactory_elb_listener)
        if isinstance(artifactory_host_profile, dict):
            artifactory_host_profile = CfnExistingVpcModulePropsResourcesArtifactoryHostProfile(**artifactory_host_profile)
        if isinstance(artifactory_host_role, dict):
            artifactory_host_role = CfnExistingVpcModulePropsResourcesArtifactoryHostRole(**artifactory_host_role)
        if isinstance(artifactory_internal_elb, dict):
            artifactory_internal_elb = CfnExistingVpcModulePropsResourcesArtifactoryInternalElb(**artifactory_internal_elb)
        if isinstance(artifactory_internal_elb_listener, dict):
            artifactory_internal_elb_listener = CfnExistingVpcModulePropsResourcesArtifactoryInternalElbListener(**artifactory_internal_elb_listener)
        if isinstance(artifactory_internal_target_group, dict):
            artifactory_internal_target_group = CfnExistingVpcModulePropsResourcesArtifactoryInternalTargetGroup(**artifactory_internal_target_group)
        if isinstance(artifactory_primary, dict):
            artifactory_primary = CfnExistingVpcModulePropsResourcesArtifactoryPrimary(**artifactory_primary)
        if isinstance(artifactory_secondary, dict):
            artifactory_secondary = CfnExistingVpcModulePropsResourcesArtifactorySecondary(**artifactory_secondary)
        if isinstance(artifactory_ssl_elb_listener, dict):
            artifactory_ssl_elb_listener = CfnExistingVpcModulePropsResourcesArtifactorySslElbListener(**artifactory_ssl_elb_listener)
        if isinstance(artifactory_ssl_target_group, dict):
            artifactory_ssl_target_group = CfnExistingVpcModulePropsResourcesArtifactorySslTargetGroup(**artifactory_ssl_target_group)
        if isinstance(artifactory_target_group, dict):
            artifactory_target_group = CfnExistingVpcModulePropsResourcesArtifactoryTargetGroup(**artifactory_target_group)
        if isinstance(bastion_stack, dict):
            bastion_stack = CfnExistingVpcModulePropsResourcesBastionStack(**bastion_stack)
        if isinstance(xray_existing_vpc_stack, dict):
            xray_existing_vpc_stack = CfnExistingVpcModulePropsResourcesXrayExistingVpcStack(**xray_existing_vpc_stack)
        if isinstance(xray_host_profile, dict):
            xray_host_profile = CfnExistingVpcModulePropsResourcesXrayHostProfile(**xray_host_profile)
        if isinstance(xray_host_role, dict):
            xray_host_role = CfnExistingVpcModulePropsResourcesXrayHostRole(**xray_host_role)
        self._values: typing.Dict[str, typing.Any] = {}
        if artifactory_core_infra_stack is not None:
            self._values["artifactory_core_infra_stack"] = artifactory_core_infra_stack
        if artifactory_ec2_sg is not None:
            self._values["artifactory_ec2_sg"] = artifactory_ec2_sg
        if artifactory_elb is not None:
            self._values["artifactory_elb"] = artifactory_elb
        if artifactory_elb_listener is not None:
            self._values["artifactory_elb_listener"] = artifactory_elb_listener
        if artifactory_host_profile is not None:
            self._values["artifactory_host_profile"] = artifactory_host_profile
        if artifactory_host_role is not None:
            self._values["artifactory_host_role"] = artifactory_host_role
        if artifactory_internal_elb is not None:
            self._values["artifactory_internal_elb"] = artifactory_internal_elb
        if artifactory_internal_elb_listener is not None:
            self._values["artifactory_internal_elb_listener"] = artifactory_internal_elb_listener
        if artifactory_internal_target_group is not None:
            self._values["artifactory_internal_target_group"] = artifactory_internal_target_group
        if artifactory_primary is not None:
            self._values["artifactory_primary"] = artifactory_primary
        if artifactory_secondary is not None:
            self._values["artifactory_secondary"] = artifactory_secondary
        if artifactory_ssl_elb_listener is not None:
            self._values["artifactory_ssl_elb_listener"] = artifactory_ssl_elb_listener
        if artifactory_ssl_target_group is not None:
            self._values["artifactory_ssl_target_group"] = artifactory_ssl_target_group
        if artifactory_target_group is not None:
            self._values["artifactory_target_group"] = artifactory_target_group
        if bastion_stack is not None:
            self._values["bastion_stack"] = bastion_stack
        if xray_existing_vpc_stack is not None:
            self._values["xray_existing_vpc_stack"] = xray_existing_vpc_stack
        if xray_host_profile is not None:
            self._values["xray_host_profile"] = xray_host_profile
        if xray_host_role is not None:
            self._values["xray_host_role"] = xray_host_role

    @builtins.property
    def artifactory_core_infra_stack(
        self,
    ) -> typing.Optional["CfnExistingVpcModulePropsResourcesArtifactoryCoreInfraStack"]:
        '''
        :schema: CfnExistingVpcModulePropsResources#ArtifactoryCoreInfraStack
        '''
        result = self._values.get("artifactory_core_infra_stack")
        return typing.cast(typing.Optional["CfnExistingVpcModulePropsResourcesArtifactoryCoreInfraStack"], result)

    @builtins.property
    def artifactory_ec2_sg(
        self,
    ) -> typing.Optional["CfnExistingVpcModulePropsResourcesArtifactoryEc2Sg"]:
        '''
        :schema: CfnExistingVpcModulePropsResources#ArtifactoryEc2Sg
        '''
        result = self._values.get("artifactory_ec2_sg")
        return typing.cast(typing.Optional["CfnExistingVpcModulePropsResourcesArtifactoryEc2Sg"], result)

    @builtins.property
    def artifactory_elb(
        self,
    ) -> typing.Optional["CfnExistingVpcModulePropsResourcesArtifactoryElb"]:
        '''
        :schema: CfnExistingVpcModulePropsResources#ArtifactoryElb
        '''
        result = self._values.get("artifactory_elb")
        return typing.cast(typing.Optional["CfnExistingVpcModulePropsResourcesArtifactoryElb"], result)

    @builtins.property
    def artifactory_elb_listener(
        self,
    ) -> typing.Optional["CfnExistingVpcModulePropsResourcesArtifactoryElbListener"]:
        '''
        :schema: CfnExistingVpcModulePropsResources#ArtifactoryElbListener
        '''
        result = self._values.get("artifactory_elb_listener")
        return typing.cast(typing.Optional["CfnExistingVpcModulePropsResourcesArtifactoryElbListener"], result)

    @builtins.property
    def artifactory_host_profile(
        self,
    ) -> typing.Optional["CfnExistingVpcModulePropsResourcesArtifactoryHostProfile"]:
        '''
        :schema: CfnExistingVpcModulePropsResources#ArtifactoryHostProfile
        '''
        result = self._values.get("artifactory_host_profile")
        return typing.cast(typing.Optional["CfnExistingVpcModulePropsResourcesArtifactoryHostProfile"], result)

    @builtins.property
    def artifactory_host_role(
        self,
    ) -> typing.Optional["CfnExistingVpcModulePropsResourcesArtifactoryHostRole"]:
        '''
        :schema: CfnExistingVpcModulePropsResources#ArtifactoryHostRole
        '''
        result = self._values.get("artifactory_host_role")
        return typing.cast(typing.Optional["CfnExistingVpcModulePropsResourcesArtifactoryHostRole"], result)

    @builtins.property
    def artifactory_internal_elb(
        self,
    ) -> typing.Optional["CfnExistingVpcModulePropsResourcesArtifactoryInternalElb"]:
        '''
        :schema: CfnExistingVpcModulePropsResources#ArtifactoryInternalElb
        '''
        result = self._values.get("artifactory_internal_elb")
        return typing.cast(typing.Optional["CfnExistingVpcModulePropsResourcesArtifactoryInternalElb"], result)

    @builtins.property
    def artifactory_internal_elb_listener(
        self,
    ) -> typing.Optional["CfnExistingVpcModulePropsResourcesArtifactoryInternalElbListener"]:
        '''
        :schema: CfnExistingVpcModulePropsResources#ArtifactoryInternalElbListener
        '''
        result = self._values.get("artifactory_internal_elb_listener")
        return typing.cast(typing.Optional["CfnExistingVpcModulePropsResourcesArtifactoryInternalElbListener"], result)

    @builtins.property
    def artifactory_internal_target_group(
        self,
    ) -> typing.Optional["CfnExistingVpcModulePropsResourcesArtifactoryInternalTargetGroup"]:
        '''
        :schema: CfnExistingVpcModulePropsResources#ArtifactoryInternalTargetGroup
        '''
        result = self._values.get("artifactory_internal_target_group")
        return typing.cast(typing.Optional["CfnExistingVpcModulePropsResourcesArtifactoryInternalTargetGroup"], result)

    @builtins.property
    def artifactory_primary(
        self,
    ) -> typing.Optional["CfnExistingVpcModulePropsResourcesArtifactoryPrimary"]:
        '''
        :schema: CfnExistingVpcModulePropsResources#ArtifactoryPrimary
        '''
        result = self._values.get("artifactory_primary")
        return typing.cast(typing.Optional["CfnExistingVpcModulePropsResourcesArtifactoryPrimary"], result)

    @builtins.property
    def artifactory_secondary(
        self,
    ) -> typing.Optional["CfnExistingVpcModulePropsResourcesArtifactorySecondary"]:
        '''
        :schema: CfnExistingVpcModulePropsResources#ArtifactorySecondary
        '''
        result = self._values.get("artifactory_secondary")
        return typing.cast(typing.Optional["CfnExistingVpcModulePropsResourcesArtifactorySecondary"], result)

    @builtins.property
    def artifactory_ssl_elb_listener(
        self,
    ) -> typing.Optional["CfnExistingVpcModulePropsResourcesArtifactorySslElbListener"]:
        '''
        :schema: CfnExistingVpcModulePropsResources#ArtifactorySslElbListener
        '''
        result = self._values.get("artifactory_ssl_elb_listener")
        return typing.cast(typing.Optional["CfnExistingVpcModulePropsResourcesArtifactorySslElbListener"], result)

    @builtins.property
    def artifactory_ssl_target_group(
        self,
    ) -> typing.Optional["CfnExistingVpcModulePropsResourcesArtifactorySslTargetGroup"]:
        '''
        :schema: CfnExistingVpcModulePropsResources#ArtifactorySslTargetGroup
        '''
        result = self._values.get("artifactory_ssl_target_group")
        return typing.cast(typing.Optional["CfnExistingVpcModulePropsResourcesArtifactorySslTargetGroup"], result)

    @builtins.property
    def artifactory_target_group(
        self,
    ) -> typing.Optional["CfnExistingVpcModulePropsResourcesArtifactoryTargetGroup"]:
        '''
        :schema: CfnExistingVpcModulePropsResources#ArtifactoryTargetGroup
        '''
        result = self._values.get("artifactory_target_group")
        return typing.cast(typing.Optional["CfnExistingVpcModulePropsResourcesArtifactoryTargetGroup"], result)

    @builtins.property
    def bastion_stack(
        self,
    ) -> typing.Optional["CfnExistingVpcModulePropsResourcesBastionStack"]:
        '''
        :schema: CfnExistingVpcModulePropsResources#BastionStack
        '''
        result = self._values.get("bastion_stack")
        return typing.cast(typing.Optional["CfnExistingVpcModulePropsResourcesBastionStack"], result)

    @builtins.property
    def xray_existing_vpc_stack(
        self,
    ) -> typing.Optional["CfnExistingVpcModulePropsResourcesXrayExistingVpcStack"]:
        '''
        :schema: CfnExistingVpcModulePropsResources#XrayExistingVpcStack
        '''
        result = self._values.get("xray_existing_vpc_stack")
        return typing.cast(typing.Optional["CfnExistingVpcModulePropsResourcesXrayExistingVpcStack"], result)

    @builtins.property
    def xray_host_profile(
        self,
    ) -> typing.Optional["CfnExistingVpcModulePropsResourcesXrayHostProfile"]:
        '''
        :schema: CfnExistingVpcModulePropsResources#XrayHostProfile
        '''
        result = self._values.get("xray_host_profile")
        return typing.cast(typing.Optional["CfnExistingVpcModulePropsResourcesXrayHostProfile"], result)

    @builtins.property
    def xray_host_role(
        self,
    ) -> typing.Optional["CfnExistingVpcModulePropsResourcesXrayHostRole"]:
        '''
        :schema: CfnExistingVpcModulePropsResources#XrayHostRole
        '''
        result = self._values.get("xray_host_role")
        return typing.cast(typing.Optional["CfnExistingVpcModulePropsResourcesXrayHostRole"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnExistingVpcModulePropsResources(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-existingvpc-module.CfnExistingVpcModulePropsResourcesArtifactoryCoreInfraStack",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnExistingVpcModulePropsResourcesArtifactoryCoreInfraStack:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnExistingVpcModulePropsResourcesArtifactoryCoreInfraStack
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnExistingVpcModulePropsResourcesArtifactoryCoreInfraStack#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnExistingVpcModulePropsResourcesArtifactoryCoreInfraStack#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnExistingVpcModulePropsResourcesArtifactoryCoreInfraStack(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-existingvpc-module.CfnExistingVpcModulePropsResourcesArtifactoryEc2Sg",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnExistingVpcModulePropsResourcesArtifactoryEc2Sg:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnExistingVpcModulePropsResourcesArtifactoryEc2Sg
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnExistingVpcModulePropsResourcesArtifactoryEc2Sg#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnExistingVpcModulePropsResourcesArtifactoryEc2Sg#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnExistingVpcModulePropsResourcesArtifactoryEc2Sg(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-existingvpc-module.CfnExistingVpcModulePropsResourcesArtifactoryElb",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnExistingVpcModulePropsResourcesArtifactoryElb:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnExistingVpcModulePropsResourcesArtifactoryElb
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnExistingVpcModulePropsResourcesArtifactoryElb#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnExistingVpcModulePropsResourcesArtifactoryElb#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnExistingVpcModulePropsResourcesArtifactoryElb(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-existingvpc-module.CfnExistingVpcModulePropsResourcesArtifactoryElbListener",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnExistingVpcModulePropsResourcesArtifactoryElbListener:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnExistingVpcModulePropsResourcesArtifactoryElbListener
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnExistingVpcModulePropsResourcesArtifactoryElbListener#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnExistingVpcModulePropsResourcesArtifactoryElbListener#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnExistingVpcModulePropsResourcesArtifactoryElbListener(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-existingvpc-module.CfnExistingVpcModulePropsResourcesArtifactoryHostProfile",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnExistingVpcModulePropsResourcesArtifactoryHostProfile:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnExistingVpcModulePropsResourcesArtifactoryHostProfile
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnExistingVpcModulePropsResourcesArtifactoryHostProfile#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnExistingVpcModulePropsResourcesArtifactoryHostProfile#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnExistingVpcModulePropsResourcesArtifactoryHostProfile(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-existingvpc-module.CfnExistingVpcModulePropsResourcesArtifactoryHostRole",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnExistingVpcModulePropsResourcesArtifactoryHostRole:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnExistingVpcModulePropsResourcesArtifactoryHostRole
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnExistingVpcModulePropsResourcesArtifactoryHostRole#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnExistingVpcModulePropsResourcesArtifactoryHostRole#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnExistingVpcModulePropsResourcesArtifactoryHostRole(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-existingvpc-module.CfnExistingVpcModulePropsResourcesArtifactoryInternalElb",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnExistingVpcModulePropsResourcesArtifactoryInternalElb:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnExistingVpcModulePropsResourcesArtifactoryInternalElb
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnExistingVpcModulePropsResourcesArtifactoryInternalElb#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnExistingVpcModulePropsResourcesArtifactoryInternalElb#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnExistingVpcModulePropsResourcesArtifactoryInternalElb(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-existingvpc-module.CfnExistingVpcModulePropsResourcesArtifactoryInternalElbListener",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnExistingVpcModulePropsResourcesArtifactoryInternalElbListener:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnExistingVpcModulePropsResourcesArtifactoryInternalElbListener
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnExistingVpcModulePropsResourcesArtifactoryInternalElbListener#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnExistingVpcModulePropsResourcesArtifactoryInternalElbListener#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnExistingVpcModulePropsResourcesArtifactoryInternalElbListener(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-existingvpc-module.CfnExistingVpcModulePropsResourcesArtifactoryInternalTargetGroup",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnExistingVpcModulePropsResourcesArtifactoryInternalTargetGroup:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnExistingVpcModulePropsResourcesArtifactoryInternalTargetGroup
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnExistingVpcModulePropsResourcesArtifactoryInternalTargetGroup#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnExistingVpcModulePropsResourcesArtifactoryInternalTargetGroup#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnExistingVpcModulePropsResourcesArtifactoryInternalTargetGroup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-existingvpc-module.CfnExistingVpcModulePropsResourcesArtifactoryPrimary",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnExistingVpcModulePropsResourcesArtifactoryPrimary:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnExistingVpcModulePropsResourcesArtifactoryPrimary
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnExistingVpcModulePropsResourcesArtifactoryPrimary#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnExistingVpcModulePropsResourcesArtifactoryPrimary#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnExistingVpcModulePropsResourcesArtifactoryPrimary(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-existingvpc-module.CfnExistingVpcModulePropsResourcesArtifactorySecondary",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnExistingVpcModulePropsResourcesArtifactorySecondary:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnExistingVpcModulePropsResourcesArtifactorySecondary
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnExistingVpcModulePropsResourcesArtifactorySecondary#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnExistingVpcModulePropsResourcesArtifactorySecondary#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnExistingVpcModulePropsResourcesArtifactorySecondary(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-existingvpc-module.CfnExistingVpcModulePropsResourcesArtifactorySslElbListener",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnExistingVpcModulePropsResourcesArtifactorySslElbListener:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnExistingVpcModulePropsResourcesArtifactorySslElbListener
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnExistingVpcModulePropsResourcesArtifactorySslElbListener#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnExistingVpcModulePropsResourcesArtifactorySslElbListener#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnExistingVpcModulePropsResourcesArtifactorySslElbListener(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-existingvpc-module.CfnExistingVpcModulePropsResourcesArtifactorySslTargetGroup",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnExistingVpcModulePropsResourcesArtifactorySslTargetGroup:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnExistingVpcModulePropsResourcesArtifactorySslTargetGroup
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnExistingVpcModulePropsResourcesArtifactorySslTargetGroup#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnExistingVpcModulePropsResourcesArtifactorySslTargetGroup#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnExistingVpcModulePropsResourcesArtifactorySslTargetGroup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-existingvpc-module.CfnExistingVpcModulePropsResourcesArtifactoryTargetGroup",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnExistingVpcModulePropsResourcesArtifactoryTargetGroup:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnExistingVpcModulePropsResourcesArtifactoryTargetGroup
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnExistingVpcModulePropsResourcesArtifactoryTargetGroup#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnExistingVpcModulePropsResourcesArtifactoryTargetGroup#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnExistingVpcModulePropsResourcesArtifactoryTargetGroup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-existingvpc-module.CfnExistingVpcModulePropsResourcesBastionStack",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnExistingVpcModulePropsResourcesBastionStack:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnExistingVpcModulePropsResourcesBastionStack
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnExistingVpcModulePropsResourcesBastionStack#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnExistingVpcModulePropsResourcesBastionStack#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnExistingVpcModulePropsResourcesBastionStack(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-existingvpc-module.CfnExistingVpcModulePropsResourcesXrayExistingVpcStack",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnExistingVpcModulePropsResourcesXrayExistingVpcStack:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnExistingVpcModulePropsResourcesXrayExistingVpcStack
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnExistingVpcModulePropsResourcesXrayExistingVpcStack#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnExistingVpcModulePropsResourcesXrayExistingVpcStack#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnExistingVpcModulePropsResourcesXrayExistingVpcStack(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-existingvpc-module.CfnExistingVpcModulePropsResourcesXrayHostProfile",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnExistingVpcModulePropsResourcesXrayHostProfile:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnExistingVpcModulePropsResourcesXrayHostProfile
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnExistingVpcModulePropsResourcesXrayHostProfile#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnExistingVpcModulePropsResourcesXrayHostProfile#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnExistingVpcModulePropsResourcesXrayHostProfile(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-existingvpc-module.CfnExistingVpcModulePropsResourcesXrayHostRole",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnExistingVpcModulePropsResourcesXrayHostRole:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnExistingVpcModulePropsResourcesXrayHostRole
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnExistingVpcModulePropsResourcesXrayHostRole#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnExistingVpcModulePropsResourcesXrayHostRole#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnExistingVpcModulePropsResourcesXrayHostRole(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnExistingVpcModule",
    "CfnExistingVpcModuleProps",
    "CfnExistingVpcModulePropsParameters",
    "CfnExistingVpcModulePropsParametersAccessCidr",
    "CfnExistingVpcModulePropsParametersArtifactoryProduct",
    "CfnExistingVpcModulePropsParametersArtifactoryServerName",
    "CfnExistingVpcModulePropsParametersArtifactoryVersion",
    "CfnExistingVpcModulePropsParametersAvailabilityZone1",
    "CfnExistingVpcModulePropsParametersAvailabilityZone2",
    "CfnExistingVpcModulePropsParametersBastionEnableTcpForwarding",
    "CfnExistingVpcModulePropsParametersBastionEnableX11Forwarding",
    "CfnExistingVpcModulePropsParametersBastionInstanceType",
    "CfnExistingVpcModulePropsParametersBastionOs",
    "CfnExistingVpcModulePropsParametersBastionRootVolumeSize",
    "CfnExistingVpcModulePropsParametersDatabaseAllocatedStorage",
    "CfnExistingVpcModulePropsParametersDatabaseEngine",
    "CfnExistingVpcModulePropsParametersDatabaseInstance",
    "CfnExistingVpcModulePropsParametersDatabaseName",
    "CfnExistingVpcModulePropsParametersDatabasePassword",
    "CfnExistingVpcModulePropsParametersDatabasePreferredAz",
    "CfnExistingVpcModulePropsParametersDatabaseUser",
    "CfnExistingVpcModulePropsParametersDefaultJavaMemSettings",
    "CfnExistingVpcModulePropsParametersElbScheme",
    "CfnExistingVpcModulePropsParametersEnableBastion",
    "CfnExistingVpcModulePropsParametersExtraJavaOptions",
    "CfnExistingVpcModulePropsParametersInstallXray",
    "CfnExistingVpcModulePropsParametersInstanceType",
    "CfnExistingVpcModulePropsParametersKeyPairName",
    "CfnExistingVpcModulePropsParametersLogicalId",
    "CfnExistingVpcModulePropsParametersMasterKey",
    "CfnExistingVpcModulePropsParametersMultiAzDatabase",
    "CfnExistingVpcModulePropsParametersNumBastionHosts",
    "CfnExistingVpcModulePropsParametersNumberOfSecondary",
    "CfnExistingVpcModulePropsParametersPrivateSubnet1Cidr",
    "CfnExistingVpcModulePropsParametersPrivateSubnet1Id",
    "CfnExistingVpcModulePropsParametersPrivateSubnet2Cidr",
    "CfnExistingVpcModulePropsParametersPrivateSubnet2Id",
    "CfnExistingVpcModulePropsParametersPublicSubnet1Id",
    "CfnExistingVpcModulePropsParametersPublicSubnet2Id",
    "CfnExistingVpcModulePropsParametersQsS3BucketName",
    "CfnExistingVpcModulePropsParametersQsS3BucketRegion",
    "CfnExistingVpcModulePropsParametersQsS3KeyPrefix",
    "CfnExistingVpcModulePropsParametersRemoteAccessCidr",
    "CfnExistingVpcModulePropsParametersSmCertName",
    "CfnExistingVpcModulePropsParametersSmLicenseName",
    "CfnExistingVpcModulePropsParametersVolumeSize",
    "CfnExistingVpcModulePropsParametersVpcCidr",
    "CfnExistingVpcModulePropsParametersVpcId",
    "CfnExistingVpcModulePropsParametersXrayDatabasePassword",
    "CfnExistingVpcModulePropsParametersXrayDatabaseUser",
    "CfnExistingVpcModulePropsParametersXrayInstanceType",
    "CfnExistingVpcModulePropsParametersXrayNumberOfInstances",
    "CfnExistingVpcModulePropsParametersXrayVersion",
    "CfnExistingVpcModulePropsResources",
    "CfnExistingVpcModulePropsResourcesArtifactoryCoreInfraStack",
    "CfnExistingVpcModulePropsResourcesArtifactoryEc2Sg",
    "CfnExistingVpcModulePropsResourcesArtifactoryElb",
    "CfnExistingVpcModulePropsResourcesArtifactoryElbListener",
    "CfnExistingVpcModulePropsResourcesArtifactoryHostProfile",
    "CfnExistingVpcModulePropsResourcesArtifactoryHostRole",
    "CfnExistingVpcModulePropsResourcesArtifactoryInternalElb",
    "CfnExistingVpcModulePropsResourcesArtifactoryInternalElbListener",
    "CfnExistingVpcModulePropsResourcesArtifactoryInternalTargetGroup",
    "CfnExistingVpcModulePropsResourcesArtifactoryPrimary",
    "CfnExistingVpcModulePropsResourcesArtifactorySecondary",
    "CfnExistingVpcModulePropsResourcesArtifactorySslElbListener",
    "CfnExistingVpcModulePropsResourcesArtifactorySslTargetGroup",
    "CfnExistingVpcModulePropsResourcesArtifactoryTargetGroup",
    "CfnExistingVpcModulePropsResourcesBastionStack",
    "CfnExistingVpcModulePropsResourcesXrayExistingVpcStack",
    "CfnExistingVpcModulePropsResourcesXrayHostProfile",
    "CfnExistingVpcModulePropsResourcesXrayHostRole",
]

publication.publish()
