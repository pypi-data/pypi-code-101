'''
# AWS CDK CloudFormation Constructs for JFrog::Artifactory::NewVpc::MODULE

Schema for Module Fragment of type JFrog::Artifactory::NewVpc::MODULE

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
    jsii_type="@cdk-cloudformation/jfrog-artifactory-newvpc-module.CfnModule",
):
    '''A CloudFormation ``JFrog::Artifactory::NewVpc::MODULE``.

    :cloudformationResource: JFrog::Artifactory::NewVpc::MODULE
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
        '''Create a new ``JFrog::Artifactory::NewVpc::MODULE``.

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
    jsii_type="@cdk-cloudformation/jfrog-artifactory-newvpc-module.CfnModuleProps",
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
        '''Schema for Module Fragment of type JFrog::Artifactory::NewVpc::MODULE.

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
    jsii_type="@cdk-cloudformation/jfrog-artifactory-newvpc-module.CfnModulePropsParameters",
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
        "private_subnet2_cidr": "privateSubnet2Cidr",
        "public_subnet1_cidr": "publicSubnet1Cidr",
        "public_subnet2_cidr": "publicSubnet2Cidr",
        "qs_s3_bucket_name": "qsS3BucketName",
        "qs_s3_bucket_region": "qsS3BucketRegion",
        "qs_s3_key_prefix": "qsS3KeyPrefix",
        "remote_access_cidr": "remoteAccessCidr",
        "sm_cert_name": "smCertName",
        "sm_license_name": "smLicenseName",
        "volume_size": "volumeSize",
        "vpc_cidr": "vpcCidr",
        "xray_database_password": "xrayDatabasePassword",
        "xray_database_user": "xrayDatabaseUser",
        "xray_instance_type": "xrayInstanceType",
        "xray_number_of_instances": "xrayNumberOfInstances",
        "xray_version": "xrayVersion",
    },
)
class CfnModulePropsParameters:
    def __init__(
        self,
        *,
        access_cidr: typing.Optional["CfnModulePropsParametersAccessCidr"] = None,
        artifactory_product: typing.Optional["CfnModulePropsParametersArtifactoryProduct"] = None,
        artifactory_server_name: typing.Optional["CfnModulePropsParametersArtifactoryServerName"] = None,
        artifactory_version: typing.Optional["CfnModulePropsParametersArtifactoryVersion"] = None,
        availability_zone1: typing.Optional["CfnModulePropsParametersAvailabilityZone1"] = None,
        availability_zone2: typing.Optional["CfnModulePropsParametersAvailabilityZone2"] = None,
        bastion_enable_tcp_forwarding: typing.Optional["CfnModulePropsParametersBastionEnableTcpForwarding"] = None,
        bastion_enable_x11_forwarding: typing.Optional["CfnModulePropsParametersBastionEnableX11Forwarding"] = None,
        bastion_instance_type: typing.Optional["CfnModulePropsParametersBastionInstanceType"] = None,
        bastion_os: typing.Optional["CfnModulePropsParametersBastionOs"] = None,
        bastion_root_volume_size: typing.Optional["CfnModulePropsParametersBastionRootVolumeSize"] = None,
        database_allocated_storage: typing.Optional["CfnModulePropsParametersDatabaseAllocatedStorage"] = None,
        database_engine: typing.Optional["CfnModulePropsParametersDatabaseEngine"] = None,
        database_instance: typing.Optional["CfnModulePropsParametersDatabaseInstance"] = None,
        database_name: typing.Optional["CfnModulePropsParametersDatabaseName"] = None,
        database_password: typing.Optional["CfnModulePropsParametersDatabasePassword"] = None,
        database_preferred_az: typing.Optional["CfnModulePropsParametersDatabasePreferredAz"] = None,
        database_user: typing.Optional["CfnModulePropsParametersDatabaseUser"] = None,
        default_java_mem_settings: typing.Optional["CfnModulePropsParametersDefaultJavaMemSettings"] = None,
        enable_bastion: typing.Optional["CfnModulePropsParametersEnableBastion"] = None,
        extra_java_options: typing.Optional["CfnModulePropsParametersExtraJavaOptions"] = None,
        install_xray: typing.Optional["CfnModulePropsParametersInstallXray"] = None,
        instance_type: typing.Optional["CfnModulePropsParametersInstanceType"] = None,
        key_pair_name: typing.Optional["CfnModulePropsParametersKeyPairName"] = None,
        logical_id: typing.Optional["CfnModulePropsParametersLogicalId"] = None,
        master_key: typing.Optional["CfnModulePropsParametersMasterKey"] = None,
        multi_az_database: typing.Optional["CfnModulePropsParametersMultiAzDatabase"] = None,
        num_bastion_hosts: typing.Optional["CfnModulePropsParametersNumBastionHosts"] = None,
        number_of_secondary: typing.Optional["CfnModulePropsParametersNumberOfSecondary"] = None,
        private_subnet1_cidr: typing.Optional["CfnModulePropsParametersPrivateSubnet1Cidr"] = None,
        private_subnet2_cidr: typing.Optional["CfnModulePropsParametersPrivateSubnet2Cidr"] = None,
        public_subnet1_cidr: typing.Optional["CfnModulePropsParametersPublicSubnet1Cidr"] = None,
        public_subnet2_cidr: typing.Optional["CfnModulePropsParametersPublicSubnet2Cidr"] = None,
        qs_s3_bucket_name: typing.Optional["CfnModulePropsParametersQsS3BucketName"] = None,
        qs_s3_bucket_region: typing.Optional["CfnModulePropsParametersQsS3BucketRegion"] = None,
        qs_s3_key_prefix: typing.Optional["CfnModulePropsParametersQsS3KeyPrefix"] = None,
        remote_access_cidr: typing.Optional["CfnModulePropsParametersRemoteAccessCidr"] = None,
        sm_cert_name: typing.Optional["CfnModulePropsParametersSmCertName"] = None,
        sm_license_name: typing.Optional["CfnModulePropsParametersSmLicenseName"] = None,
        volume_size: typing.Optional["CfnModulePropsParametersVolumeSize"] = None,
        vpc_cidr: typing.Optional["CfnModulePropsParametersVpcCidr"] = None,
        xray_database_password: typing.Optional["CfnModulePropsParametersXrayDatabasePassword"] = None,
        xray_database_user: typing.Optional["CfnModulePropsParametersXrayDatabaseUser"] = None,
        xray_instance_type: typing.Optional["CfnModulePropsParametersXrayInstanceType"] = None,
        xray_number_of_instances: typing.Optional["CfnModulePropsParametersXrayNumberOfInstances"] = None,
        xray_version: typing.Optional["CfnModulePropsParametersXrayVersion"] = None,
    ) -> None:
        '''
        :param access_cidr: CIDR IP range permitted to access Artifactory. It is recommended that you set this value to a trusted IP range. For example, you may want to limit software access to your corporate network.
        :param artifactory_product: JFrog Artifactory product you want to install into an AMI.
        :param artifactory_server_name: Name of your Artifactory server. Ensure that this matches your certificate.
        :param artifactory_version: Version of Artifactory that you want to deploy into the Quick Start. To select the correct version, see the release notes at https://www.jfrog.com/confluence/display/RTF/Release+Notes.
        :param availability_zone1: Availability Zone 1 to use for the subnets in the VPC. Two Availability Zones are used for this deployment.
        :param availability_zone2: Availability Zone 2 to use for the subnets in the VPC. Two Availability Zones are used for this deployment.
        :param bastion_enable_tcp_forwarding: Choose whether to enable TCP forwarding via bootstrapping of the bastion instance.
        :param bastion_enable_x11_forwarding: Choose true to enable X11 via bootstrapping of the bastion host. Setting this value to true enables X Windows over SSH. X11 forwarding can be useful, but it is also a security risk, so it's recommended that you keep the default (false) setting.
        :param bastion_instance_type: Size of the bastion instances.
        :param bastion_os: Linux distribution for the Amazon Machine Image (AMI) to be used for the bastion instances.
        :param bastion_root_volume_size: Size of the root volume in the bastion instances.
        :param database_allocated_storage: Size in gigabytes of available storage for the database instance.
        :param database_engine: Database engine that you want to run.
        :param database_instance: Size of the database to be deployed as part of the Quick Start.
        :param database_name: Name of your database instance. The name must be unique across all instances owned by your AWS account in the current Region. The database instance identifier is case-insensitive, but it's stored in lowercase (as in "mydbinstance").
        :param database_password: Password for the Artifactory database user.
        :param database_preferred_az: Preferred availability zone for Amazon RDS primary instance.
        :param database_user: Login ID for the master user of your database instance.
        :param default_java_mem_settings: Choose false to overwrite the standard memory-calculation options to pass to the Artifactory JVM. If you plan to overwrite them, ensure they are added to the ExtraJavaOptions to prevent the stack provision from failing.
        :param enable_bastion: If set to true, a bastion host will be created.
        :param extra_java_options: Set Java options to pass to the JVM for Artifactory. For more information, see the Artifactory system requirements at https://www.jfrog.com/confluence/display/RTF/System+Requirements#SystemRequirements-RecommendedHardware. Do not add Xms or Xmx settings without disabling DefaultJavaMemSettings.
        :param install_xray: Choose true to install JFrog Xray instance(s).
        :param instance_type: EC2 instance type for the Artifactory instances.
        :param key_pair_name: Name of an existing key pair, which allows you to connect securely to your instance after it launches. This is the key pair you created in your preferred Region.
        :param logical_id: Logical Id of the MODULE.
        :param master_key: Master key for the Artifactory cluster. Generate a master key by using the command '$openssl rand -hex 16'.
        :param multi_az_database: Choose false to create an Amazon RDS instance in a single Availability Zone.
        :param num_bastion_hosts: Number of bastion instances to create.
        :param number_of_secondary: Number of secondary Artifactory servers to complete your HA deployment. To align with Artifactory best practices, the minimum number is two, and the maximum is seven. Do not select more instances than you have licenses for.
        :param private_subnet1_cidr: CIDR block for private subnet 1 located in Availability Zone 1.
        :param private_subnet2_cidr: CIDR block for private subnet 2 located in Availability Zone 2.
        :param public_subnet1_cidr: CIDR block for the public (DMZ) subnet 1 located in Availability Zone 1.
        :param public_subnet2_cidr: CIDR block for the public (DMZ) subnet 2 located in Availability Zone 2.
        :param qs_s3_bucket_name: S3 bucket name for the Quick Start assets. This string can include numbers, lowercase letters, and hyphens (-). It cannot start or end with a hyphen (-).
        :param qs_s3_bucket_region: AWS Region where the Quick Start S3 bucket (QSS3BucketName) is hosted. If you use your own bucket, you must specify your own value.
        :param qs_s3_key_prefix: S3 key prefix for the Quick Start assets. Quick Start key prefix can include numbers, lowercase letters, uppercase letters, hyphens (-), and forward slash (/).
        :param remote_access_cidr: Remote CIDR range that allows you to connect to the bastion instance by using SSH. It is recommended that you set this value to a trusted IP range. For example, you may want to grant specific ranges from within your corporate network that use the SSH protocol.
        :param sm_cert_name: Secret name created in AWS Secrets Manager, which contains the SSL certificate and certificate key.
        :param sm_license_name: Secret name created in AWS Secrets Manager, which contains the Artifactory licenses.
        :param volume_size: Size in gigabytes of available storage (min 10GB). The Quick Start creates an Amazon Elastic Block Store (Amazon EBS) volumes of this size.
        :param vpc_cidr: CIDR block for the VPC.
        :param xray_database_password: The password for the Xray database user.
        :param xray_database_user: The login ID for the Xray database user.
        :param xray_instance_type: The EC2 instance type for the Xray instances.
        :param xray_number_of_instances: The number of Xray instances servers to complete your HA deployment. The minimum number is one; the maximum is seven. Do not select more than instances than you have licenses for.
        :param xray_version: The version of Xray that you want to deploy into the Quick Start.

        :schema: CfnModulePropsParameters
        '''
        if isinstance(access_cidr, dict):
            access_cidr = CfnModulePropsParametersAccessCidr(**access_cidr)
        if isinstance(artifactory_product, dict):
            artifactory_product = CfnModulePropsParametersArtifactoryProduct(**artifactory_product)
        if isinstance(artifactory_server_name, dict):
            artifactory_server_name = CfnModulePropsParametersArtifactoryServerName(**artifactory_server_name)
        if isinstance(artifactory_version, dict):
            artifactory_version = CfnModulePropsParametersArtifactoryVersion(**artifactory_version)
        if isinstance(availability_zone1, dict):
            availability_zone1 = CfnModulePropsParametersAvailabilityZone1(**availability_zone1)
        if isinstance(availability_zone2, dict):
            availability_zone2 = CfnModulePropsParametersAvailabilityZone2(**availability_zone2)
        if isinstance(bastion_enable_tcp_forwarding, dict):
            bastion_enable_tcp_forwarding = CfnModulePropsParametersBastionEnableTcpForwarding(**bastion_enable_tcp_forwarding)
        if isinstance(bastion_enable_x11_forwarding, dict):
            bastion_enable_x11_forwarding = CfnModulePropsParametersBastionEnableX11Forwarding(**bastion_enable_x11_forwarding)
        if isinstance(bastion_instance_type, dict):
            bastion_instance_type = CfnModulePropsParametersBastionInstanceType(**bastion_instance_type)
        if isinstance(bastion_os, dict):
            bastion_os = CfnModulePropsParametersBastionOs(**bastion_os)
        if isinstance(bastion_root_volume_size, dict):
            bastion_root_volume_size = CfnModulePropsParametersBastionRootVolumeSize(**bastion_root_volume_size)
        if isinstance(database_allocated_storage, dict):
            database_allocated_storage = CfnModulePropsParametersDatabaseAllocatedStorage(**database_allocated_storage)
        if isinstance(database_engine, dict):
            database_engine = CfnModulePropsParametersDatabaseEngine(**database_engine)
        if isinstance(database_instance, dict):
            database_instance = CfnModulePropsParametersDatabaseInstance(**database_instance)
        if isinstance(database_name, dict):
            database_name = CfnModulePropsParametersDatabaseName(**database_name)
        if isinstance(database_password, dict):
            database_password = CfnModulePropsParametersDatabasePassword(**database_password)
        if isinstance(database_preferred_az, dict):
            database_preferred_az = CfnModulePropsParametersDatabasePreferredAz(**database_preferred_az)
        if isinstance(database_user, dict):
            database_user = CfnModulePropsParametersDatabaseUser(**database_user)
        if isinstance(default_java_mem_settings, dict):
            default_java_mem_settings = CfnModulePropsParametersDefaultJavaMemSettings(**default_java_mem_settings)
        if isinstance(enable_bastion, dict):
            enable_bastion = CfnModulePropsParametersEnableBastion(**enable_bastion)
        if isinstance(extra_java_options, dict):
            extra_java_options = CfnModulePropsParametersExtraJavaOptions(**extra_java_options)
        if isinstance(install_xray, dict):
            install_xray = CfnModulePropsParametersInstallXray(**install_xray)
        if isinstance(instance_type, dict):
            instance_type = CfnModulePropsParametersInstanceType(**instance_type)
        if isinstance(key_pair_name, dict):
            key_pair_name = CfnModulePropsParametersKeyPairName(**key_pair_name)
        if isinstance(logical_id, dict):
            logical_id = CfnModulePropsParametersLogicalId(**logical_id)
        if isinstance(master_key, dict):
            master_key = CfnModulePropsParametersMasterKey(**master_key)
        if isinstance(multi_az_database, dict):
            multi_az_database = CfnModulePropsParametersMultiAzDatabase(**multi_az_database)
        if isinstance(num_bastion_hosts, dict):
            num_bastion_hosts = CfnModulePropsParametersNumBastionHosts(**num_bastion_hosts)
        if isinstance(number_of_secondary, dict):
            number_of_secondary = CfnModulePropsParametersNumberOfSecondary(**number_of_secondary)
        if isinstance(private_subnet1_cidr, dict):
            private_subnet1_cidr = CfnModulePropsParametersPrivateSubnet1Cidr(**private_subnet1_cidr)
        if isinstance(private_subnet2_cidr, dict):
            private_subnet2_cidr = CfnModulePropsParametersPrivateSubnet2Cidr(**private_subnet2_cidr)
        if isinstance(public_subnet1_cidr, dict):
            public_subnet1_cidr = CfnModulePropsParametersPublicSubnet1Cidr(**public_subnet1_cidr)
        if isinstance(public_subnet2_cidr, dict):
            public_subnet2_cidr = CfnModulePropsParametersPublicSubnet2Cidr(**public_subnet2_cidr)
        if isinstance(qs_s3_bucket_name, dict):
            qs_s3_bucket_name = CfnModulePropsParametersQsS3BucketName(**qs_s3_bucket_name)
        if isinstance(qs_s3_bucket_region, dict):
            qs_s3_bucket_region = CfnModulePropsParametersQsS3BucketRegion(**qs_s3_bucket_region)
        if isinstance(qs_s3_key_prefix, dict):
            qs_s3_key_prefix = CfnModulePropsParametersQsS3KeyPrefix(**qs_s3_key_prefix)
        if isinstance(remote_access_cidr, dict):
            remote_access_cidr = CfnModulePropsParametersRemoteAccessCidr(**remote_access_cidr)
        if isinstance(sm_cert_name, dict):
            sm_cert_name = CfnModulePropsParametersSmCertName(**sm_cert_name)
        if isinstance(sm_license_name, dict):
            sm_license_name = CfnModulePropsParametersSmLicenseName(**sm_license_name)
        if isinstance(volume_size, dict):
            volume_size = CfnModulePropsParametersVolumeSize(**volume_size)
        if isinstance(vpc_cidr, dict):
            vpc_cidr = CfnModulePropsParametersVpcCidr(**vpc_cidr)
        if isinstance(xray_database_password, dict):
            xray_database_password = CfnModulePropsParametersXrayDatabasePassword(**xray_database_password)
        if isinstance(xray_database_user, dict):
            xray_database_user = CfnModulePropsParametersXrayDatabaseUser(**xray_database_user)
        if isinstance(xray_instance_type, dict):
            xray_instance_type = CfnModulePropsParametersXrayInstanceType(**xray_instance_type)
        if isinstance(xray_number_of_instances, dict):
            xray_number_of_instances = CfnModulePropsParametersXrayNumberOfInstances(**xray_number_of_instances)
        if isinstance(xray_version, dict):
            xray_version = CfnModulePropsParametersXrayVersion(**xray_version)
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
        if private_subnet2_cidr is not None:
            self._values["private_subnet2_cidr"] = private_subnet2_cidr
        if public_subnet1_cidr is not None:
            self._values["public_subnet1_cidr"] = public_subnet1_cidr
        if public_subnet2_cidr is not None:
            self._values["public_subnet2_cidr"] = public_subnet2_cidr
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
    def access_cidr(self) -> typing.Optional["CfnModulePropsParametersAccessCidr"]:
        '''CIDR IP range permitted to access Artifactory.

        It is recommended that you set this value to a trusted IP range. For example, you may want to limit software access to your corporate network.

        :schema: CfnModulePropsParameters#AccessCidr
        '''
        result = self._values.get("access_cidr")
        return typing.cast(typing.Optional["CfnModulePropsParametersAccessCidr"], result)

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
    def artifactory_server_name(
        self,
    ) -> typing.Optional["CfnModulePropsParametersArtifactoryServerName"]:
        '''Name of your Artifactory server.

        Ensure that this matches your certificate.

        :schema: CfnModulePropsParameters#ArtifactoryServerName
        '''
        result = self._values.get("artifactory_server_name")
        return typing.cast(typing.Optional["CfnModulePropsParametersArtifactoryServerName"], result)

    @builtins.property
    def artifactory_version(
        self,
    ) -> typing.Optional["CfnModulePropsParametersArtifactoryVersion"]:
        '''Version of Artifactory that you want to deploy into the Quick Start.

        To select the correct version, see the release notes at https://www.jfrog.com/confluence/display/RTF/Release+Notes.

        :schema: CfnModulePropsParameters#ArtifactoryVersion
        '''
        result = self._values.get("artifactory_version")
        return typing.cast(typing.Optional["CfnModulePropsParametersArtifactoryVersion"], result)

    @builtins.property
    def availability_zone1(
        self,
    ) -> typing.Optional["CfnModulePropsParametersAvailabilityZone1"]:
        '''Availability Zone 1 to use for the subnets in the VPC.

        Two Availability Zones are used for this deployment.

        :schema: CfnModulePropsParameters#AvailabilityZone1
        '''
        result = self._values.get("availability_zone1")
        return typing.cast(typing.Optional["CfnModulePropsParametersAvailabilityZone1"], result)

    @builtins.property
    def availability_zone2(
        self,
    ) -> typing.Optional["CfnModulePropsParametersAvailabilityZone2"]:
        '''Availability Zone 2 to use for the subnets in the VPC.

        Two Availability Zones are used for this deployment.

        :schema: CfnModulePropsParameters#AvailabilityZone2
        '''
        result = self._values.get("availability_zone2")
        return typing.cast(typing.Optional["CfnModulePropsParametersAvailabilityZone2"], result)

    @builtins.property
    def bastion_enable_tcp_forwarding(
        self,
    ) -> typing.Optional["CfnModulePropsParametersBastionEnableTcpForwarding"]:
        '''Choose whether to enable TCP forwarding via bootstrapping of the bastion instance.

        :schema: CfnModulePropsParameters#BastionEnableTcpForwarding
        '''
        result = self._values.get("bastion_enable_tcp_forwarding")
        return typing.cast(typing.Optional["CfnModulePropsParametersBastionEnableTcpForwarding"], result)

    @builtins.property
    def bastion_enable_x11_forwarding(
        self,
    ) -> typing.Optional["CfnModulePropsParametersBastionEnableX11Forwarding"]:
        '''Choose true to enable X11 via bootstrapping of the bastion host.

        Setting this value to true enables X Windows over SSH. X11 forwarding can be useful, but it is also a security risk, so it's recommended that you keep the default (false) setting.

        :schema: CfnModulePropsParameters#BastionEnableX11Forwarding
        '''
        result = self._values.get("bastion_enable_x11_forwarding")
        return typing.cast(typing.Optional["CfnModulePropsParametersBastionEnableX11Forwarding"], result)

    @builtins.property
    def bastion_instance_type(
        self,
    ) -> typing.Optional["CfnModulePropsParametersBastionInstanceType"]:
        '''Size of the bastion instances.

        :schema: CfnModulePropsParameters#BastionInstanceType
        '''
        result = self._values.get("bastion_instance_type")
        return typing.cast(typing.Optional["CfnModulePropsParametersBastionInstanceType"], result)

    @builtins.property
    def bastion_os(self) -> typing.Optional["CfnModulePropsParametersBastionOs"]:
        '''Linux distribution for the Amazon Machine Image (AMI) to be used for the bastion instances.

        :schema: CfnModulePropsParameters#BastionOs
        '''
        result = self._values.get("bastion_os")
        return typing.cast(typing.Optional["CfnModulePropsParametersBastionOs"], result)

    @builtins.property
    def bastion_root_volume_size(
        self,
    ) -> typing.Optional["CfnModulePropsParametersBastionRootVolumeSize"]:
        '''Size of the root volume in the bastion instances.

        :schema: CfnModulePropsParameters#BastionRootVolumeSize
        '''
        result = self._values.get("bastion_root_volume_size")
        return typing.cast(typing.Optional["CfnModulePropsParametersBastionRootVolumeSize"], result)

    @builtins.property
    def database_allocated_storage(
        self,
    ) -> typing.Optional["CfnModulePropsParametersDatabaseAllocatedStorage"]:
        '''Size in gigabytes of available storage for the database instance.

        :schema: CfnModulePropsParameters#DatabaseAllocatedStorage
        '''
        result = self._values.get("database_allocated_storage")
        return typing.cast(typing.Optional["CfnModulePropsParametersDatabaseAllocatedStorage"], result)

    @builtins.property
    def database_engine(
        self,
    ) -> typing.Optional["CfnModulePropsParametersDatabaseEngine"]:
        '''Database engine that you want to run.

        :schema: CfnModulePropsParameters#DatabaseEngine
        '''
        result = self._values.get("database_engine")
        return typing.cast(typing.Optional["CfnModulePropsParametersDatabaseEngine"], result)

    @builtins.property
    def database_instance(
        self,
    ) -> typing.Optional["CfnModulePropsParametersDatabaseInstance"]:
        '''Size of the database to be deployed as part of the Quick Start.

        :schema: CfnModulePropsParameters#DatabaseInstance
        '''
        result = self._values.get("database_instance")
        return typing.cast(typing.Optional["CfnModulePropsParametersDatabaseInstance"], result)

    @builtins.property
    def database_name(self) -> typing.Optional["CfnModulePropsParametersDatabaseName"]:
        '''Name of your database instance.

        The name must be unique across all instances owned by your AWS account in the current Region. The database instance identifier is case-insensitive, but it's stored in lowercase (as in "mydbinstance").

        :schema: CfnModulePropsParameters#DatabaseName
        '''
        result = self._values.get("database_name")
        return typing.cast(typing.Optional["CfnModulePropsParametersDatabaseName"], result)

    @builtins.property
    def database_password(
        self,
    ) -> typing.Optional["CfnModulePropsParametersDatabasePassword"]:
        '''Password for the Artifactory database user.

        :schema: CfnModulePropsParameters#DatabasePassword
        '''
        result = self._values.get("database_password")
        return typing.cast(typing.Optional["CfnModulePropsParametersDatabasePassword"], result)

    @builtins.property
    def database_preferred_az(
        self,
    ) -> typing.Optional["CfnModulePropsParametersDatabasePreferredAz"]:
        '''Preferred availability zone for Amazon RDS primary instance.

        :schema: CfnModulePropsParameters#DatabasePreferredAz
        '''
        result = self._values.get("database_preferred_az")
        return typing.cast(typing.Optional["CfnModulePropsParametersDatabasePreferredAz"], result)

    @builtins.property
    def database_user(self) -> typing.Optional["CfnModulePropsParametersDatabaseUser"]:
        '''Login ID for the master user of your database instance.

        :schema: CfnModulePropsParameters#DatabaseUser
        '''
        result = self._values.get("database_user")
        return typing.cast(typing.Optional["CfnModulePropsParametersDatabaseUser"], result)

    @builtins.property
    def default_java_mem_settings(
        self,
    ) -> typing.Optional["CfnModulePropsParametersDefaultJavaMemSettings"]:
        '''Choose false to overwrite the standard memory-calculation options to pass to the Artifactory JVM.

        If you plan to overwrite them, ensure they are added to the ExtraJavaOptions to prevent the stack provision from failing.

        :schema: CfnModulePropsParameters#DefaultJavaMemSettings
        '''
        result = self._values.get("default_java_mem_settings")
        return typing.cast(typing.Optional["CfnModulePropsParametersDefaultJavaMemSettings"], result)

    @builtins.property
    def enable_bastion(
        self,
    ) -> typing.Optional["CfnModulePropsParametersEnableBastion"]:
        '''If set to true, a bastion host will be created.

        :schema: CfnModulePropsParameters#EnableBastion
        '''
        result = self._values.get("enable_bastion")
        return typing.cast(typing.Optional["CfnModulePropsParametersEnableBastion"], result)

    @builtins.property
    def extra_java_options(
        self,
    ) -> typing.Optional["CfnModulePropsParametersExtraJavaOptions"]:
        '''Set Java options to pass to the JVM for Artifactory.

        For more information, see the Artifactory system requirements at https://www.jfrog.com/confluence/display/RTF/System+Requirements#SystemRequirements-RecommendedHardware. Do not add Xms or Xmx settings without disabling DefaultJavaMemSettings.

        :schema: CfnModulePropsParameters#ExtraJavaOptions
        '''
        result = self._values.get("extra_java_options")
        return typing.cast(typing.Optional["CfnModulePropsParametersExtraJavaOptions"], result)

    @builtins.property
    def install_xray(self) -> typing.Optional["CfnModulePropsParametersInstallXray"]:
        '''Choose true to install JFrog Xray instance(s).

        :schema: CfnModulePropsParameters#InstallXray
        '''
        result = self._values.get("install_xray")
        return typing.cast(typing.Optional["CfnModulePropsParametersInstallXray"], result)

    @builtins.property
    def instance_type(self) -> typing.Optional["CfnModulePropsParametersInstanceType"]:
        '''EC2 instance type for the Artifactory instances.

        :schema: CfnModulePropsParameters#InstanceType
        '''
        result = self._values.get("instance_type")
        return typing.cast(typing.Optional["CfnModulePropsParametersInstanceType"], result)

    @builtins.property
    def key_pair_name(self) -> typing.Optional["CfnModulePropsParametersKeyPairName"]:
        '''Name of an existing key pair, which allows you to connect securely to your instance after it launches.

        This is the key pair you created in your preferred Region.

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
        '''Master key for the Artifactory cluster.

        Generate a master key by using the command '$openssl rand -hex 16'.

        :schema: CfnModulePropsParameters#MasterKey
        '''
        result = self._values.get("master_key")
        return typing.cast(typing.Optional["CfnModulePropsParametersMasterKey"], result)

    @builtins.property
    def multi_az_database(
        self,
    ) -> typing.Optional["CfnModulePropsParametersMultiAzDatabase"]:
        '''Choose false to create an Amazon RDS instance in a single Availability Zone.

        :schema: CfnModulePropsParameters#MultiAzDatabase
        '''
        result = self._values.get("multi_az_database")
        return typing.cast(typing.Optional["CfnModulePropsParametersMultiAzDatabase"], result)

    @builtins.property
    def num_bastion_hosts(
        self,
    ) -> typing.Optional["CfnModulePropsParametersNumBastionHosts"]:
        '''Number of bastion instances to create.

        :schema: CfnModulePropsParameters#NumBastionHosts
        '''
        result = self._values.get("num_bastion_hosts")
        return typing.cast(typing.Optional["CfnModulePropsParametersNumBastionHosts"], result)

    @builtins.property
    def number_of_secondary(
        self,
    ) -> typing.Optional["CfnModulePropsParametersNumberOfSecondary"]:
        '''Number of secondary Artifactory servers to complete your HA deployment.

        To align with Artifactory best practices, the minimum number is two, and the maximum is seven. Do not select more instances than you have licenses for.

        :schema: CfnModulePropsParameters#NumberOfSecondary
        '''
        result = self._values.get("number_of_secondary")
        return typing.cast(typing.Optional["CfnModulePropsParametersNumberOfSecondary"], result)

    @builtins.property
    def private_subnet1_cidr(
        self,
    ) -> typing.Optional["CfnModulePropsParametersPrivateSubnet1Cidr"]:
        '''CIDR block for private subnet 1 located in Availability Zone 1.

        :schema: CfnModulePropsParameters#PrivateSubnet1Cidr
        '''
        result = self._values.get("private_subnet1_cidr")
        return typing.cast(typing.Optional["CfnModulePropsParametersPrivateSubnet1Cidr"], result)

    @builtins.property
    def private_subnet2_cidr(
        self,
    ) -> typing.Optional["CfnModulePropsParametersPrivateSubnet2Cidr"]:
        '''CIDR block for private subnet 2 located in Availability Zone 2.

        :schema: CfnModulePropsParameters#PrivateSubnet2Cidr
        '''
        result = self._values.get("private_subnet2_cidr")
        return typing.cast(typing.Optional["CfnModulePropsParametersPrivateSubnet2Cidr"], result)

    @builtins.property
    def public_subnet1_cidr(
        self,
    ) -> typing.Optional["CfnModulePropsParametersPublicSubnet1Cidr"]:
        '''CIDR block for the public (DMZ) subnet 1 located in Availability Zone 1.

        :schema: CfnModulePropsParameters#PublicSubnet1Cidr
        '''
        result = self._values.get("public_subnet1_cidr")
        return typing.cast(typing.Optional["CfnModulePropsParametersPublicSubnet1Cidr"], result)

    @builtins.property
    def public_subnet2_cidr(
        self,
    ) -> typing.Optional["CfnModulePropsParametersPublicSubnet2Cidr"]:
        '''CIDR block for the public (DMZ) subnet 2 located in Availability Zone 2.

        :schema: CfnModulePropsParameters#PublicSubnet2Cidr
        '''
        result = self._values.get("public_subnet2_cidr")
        return typing.cast(typing.Optional["CfnModulePropsParametersPublicSubnet2Cidr"], result)

    @builtins.property
    def qs_s3_bucket_name(
        self,
    ) -> typing.Optional["CfnModulePropsParametersQsS3BucketName"]:
        '''S3 bucket name for the Quick Start assets.

        This string can include numbers, lowercase letters, and hyphens (-). It cannot start or end with a hyphen (-).

        :schema: CfnModulePropsParameters#QsS3BucketName
        '''
        result = self._values.get("qs_s3_bucket_name")
        return typing.cast(typing.Optional["CfnModulePropsParametersQsS3BucketName"], result)

    @builtins.property
    def qs_s3_bucket_region(
        self,
    ) -> typing.Optional["CfnModulePropsParametersQsS3BucketRegion"]:
        '''AWS Region where the Quick Start S3 bucket (QSS3BucketName) is hosted.

        If you use your own bucket, you must specify your own value.

        :schema: CfnModulePropsParameters#QsS3BucketRegion
        '''
        result = self._values.get("qs_s3_bucket_region")
        return typing.cast(typing.Optional["CfnModulePropsParametersQsS3BucketRegion"], result)

    @builtins.property
    def qs_s3_key_prefix(
        self,
    ) -> typing.Optional["CfnModulePropsParametersQsS3KeyPrefix"]:
        '''S3 key prefix for the Quick Start assets.

        Quick Start key prefix can include numbers, lowercase letters, uppercase letters, hyphens (-), and forward slash (/).

        :schema: CfnModulePropsParameters#QsS3KeyPrefix
        '''
        result = self._values.get("qs_s3_key_prefix")
        return typing.cast(typing.Optional["CfnModulePropsParametersQsS3KeyPrefix"], result)

    @builtins.property
    def remote_access_cidr(
        self,
    ) -> typing.Optional["CfnModulePropsParametersRemoteAccessCidr"]:
        '''Remote CIDR range that allows you to connect to the bastion instance by using SSH.

        It is recommended that you set this value to a trusted IP range. For example, you may want to grant specific ranges from within your corporate network that use the SSH protocol.

        :schema: CfnModulePropsParameters#RemoteAccessCidr
        '''
        result = self._values.get("remote_access_cidr")
        return typing.cast(typing.Optional["CfnModulePropsParametersRemoteAccessCidr"], result)

    @builtins.property
    def sm_cert_name(self) -> typing.Optional["CfnModulePropsParametersSmCertName"]:
        '''Secret name created in AWS Secrets Manager, which contains the SSL certificate and certificate key.

        :schema: CfnModulePropsParameters#SmCertName
        '''
        result = self._values.get("sm_cert_name")
        return typing.cast(typing.Optional["CfnModulePropsParametersSmCertName"], result)

    @builtins.property
    def sm_license_name(
        self,
    ) -> typing.Optional["CfnModulePropsParametersSmLicenseName"]:
        '''Secret name created in AWS Secrets Manager, which contains the Artifactory licenses.

        :schema: CfnModulePropsParameters#SmLicenseName
        '''
        result = self._values.get("sm_license_name")
        return typing.cast(typing.Optional["CfnModulePropsParametersSmLicenseName"], result)

    @builtins.property
    def volume_size(self) -> typing.Optional["CfnModulePropsParametersVolumeSize"]:
        '''Size in gigabytes of available storage (min 10GB).

        The Quick Start creates an Amazon Elastic Block Store (Amazon EBS) volumes of this size.

        :schema: CfnModulePropsParameters#VolumeSize
        '''
        result = self._values.get("volume_size")
        return typing.cast(typing.Optional["CfnModulePropsParametersVolumeSize"], result)

    @builtins.property
    def vpc_cidr(self) -> typing.Optional["CfnModulePropsParametersVpcCidr"]:
        '''CIDR block for the VPC.

        :schema: CfnModulePropsParameters#VpcCidr
        '''
        result = self._values.get("vpc_cidr")
        return typing.cast(typing.Optional["CfnModulePropsParametersVpcCidr"], result)

    @builtins.property
    def xray_database_password(
        self,
    ) -> typing.Optional["CfnModulePropsParametersXrayDatabasePassword"]:
        '''The password for the Xray database user.

        :schema: CfnModulePropsParameters#XrayDatabasePassword
        '''
        result = self._values.get("xray_database_password")
        return typing.cast(typing.Optional["CfnModulePropsParametersXrayDatabasePassword"], result)

    @builtins.property
    def xray_database_user(
        self,
    ) -> typing.Optional["CfnModulePropsParametersXrayDatabaseUser"]:
        '''The login ID for the Xray database user.

        :schema: CfnModulePropsParameters#XrayDatabaseUser
        '''
        result = self._values.get("xray_database_user")
        return typing.cast(typing.Optional["CfnModulePropsParametersXrayDatabaseUser"], result)

    @builtins.property
    def xray_instance_type(
        self,
    ) -> typing.Optional["CfnModulePropsParametersXrayInstanceType"]:
        '''The EC2 instance type for the Xray instances.

        :schema: CfnModulePropsParameters#XrayInstanceType
        '''
        result = self._values.get("xray_instance_type")
        return typing.cast(typing.Optional["CfnModulePropsParametersXrayInstanceType"], result)

    @builtins.property
    def xray_number_of_instances(
        self,
    ) -> typing.Optional["CfnModulePropsParametersXrayNumberOfInstances"]:
        '''The number of Xray instances servers to complete your HA deployment.

        The minimum number is one; the maximum is seven. Do not select more than instances than you have licenses for.

        :schema: CfnModulePropsParameters#XrayNumberOfInstances
        '''
        result = self._values.get("xray_number_of_instances")
        return typing.cast(typing.Optional["CfnModulePropsParametersXrayNumberOfInstances"], result)

    @builtins.property
    def xray_version(self) -> typing.Optional["CfnModulePropsParametersXrayVersion"]:
        '''The version of Xray that you want to deploy into the Quick Start.

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
    jsii_type="@cdk-cloudformation/jfrog-artifactory-newvpc-module.CfnModulePropsParametersAccessCidr",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersAccessCidr:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''CIDR IP range permitted to access Artifactory.

        It is recommended that you set this value to a trusted IP range. For example, you may want to limit software access to your corporate network.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersAccessCidr
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersAccessCidr#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersAccessCidr#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersAccessCidr(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-newvpc-module.CfnModulePropsParametersArtifactoryProduct",
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
    jsii_type="@cdk-cloudformation/jfrog-artifactory-newvpc-module.CfnModulePropsParametersArtifactoryServerName",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersArtifactoryServerName:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Name of your Artifactory server.

        Ensure that this matches your certificate.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersArtifactoryServerName
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersArtifactoryServerName#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

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
    jsii_type="@cdk-cloudformation/jfrog-artifactory-newvpc-module.CfnModulePropsParametersArtifactoryVersion",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersArtifactoryVersion:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Version of Artifactory that you want to deploy into the Quick Start.

        To select the correct version, see the release notes at https://www.jfrog.com/confluence/display/RTF/Release+Notes.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersArtifactoryVersion
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersArtifactoryVersion#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

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
    jsii_type="@cdk-cloudformation/jfrog-artifactory-newvpc-module.CfnModulePropsParametersAvailabilityZone1",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersAvailabilityZone1:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Availability Zone 1 to use for the subnets in the VPC.

        Two Availability Zones are used for this deployment.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersAvailabilityZone1
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersAvailabilityZone1#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersAvailabilityZone1#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersAvailabilityZone1(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-newvpc-module.CfnModulePropsParametersAvailabilityZone2",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersAvailabilityZone2:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Availability Zone 2 to use for the subnets in the VPC.

        Two Availability Zones are used for this deployment.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersAvailabilityZone2
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersAvailabilityZone2#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersAvailabilityZone2#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersAvailabilityZone2(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-newvpc-module.CfnModulePropsParametersBastionEnableTcpForwarding",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersBastionEnableTcpForwarding:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Choose whether to enable TCP forwarding via bootstrapping of the bastion instance.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersBastionEnableTcpForwarding
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersBastionEnableTcpForwarding#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersBastionEnableTcpForwarding#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersBastionEnableTcpForwarding(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-newvpc-module.CfnModulePropsParametersBastionEnableX11Forwarding",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersBastionEnableX11Forwarding:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Choose true to enable X11 via bootstrapping of the bastion host.

        Setting this value to true enables X Windows over SSH. X11 forwarding can be useful, but it is also a security risk, so it's recommended that you keep the default (false) setting.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersBastionEnableX11Forwarding
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersBastionEnableX11Forwarding#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersBastionEnableX11Forwarding#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersBastionEnableX11Forwarding(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-newvpc-module.CfnModulePropsParametersBastionInstanceType",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersBastionInstanceType:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Size of the bastion instances.

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
    jsii_type="@cdk-cloudformation/jfrog-artifactory-newvpc-module.CfnModulePropsParametersBastionOs",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersBastionOs:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Linux distribution for the Amazon Machine Image (AMI) to be used for the bastion instances.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersBastionOs
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersBastionOs#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersBastionOs#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersBastionOs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-newvpc-module.CfnModulePropsParametersBastionRootVolumeSize",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersBastionRootVolumeSize:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Size of the root volume in the bastion instances.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersBastionRootVolumeSize
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersBastionRootVolumeSize#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersBastionRootVolumeSize#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersBastionRootVolumeSize(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-newvpc-module.CfnModulePropsParametersDatabaseAllocatedStorage",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersDatabaseAllocatedStorage:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Size in gigabytes of available storage for the database instance.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersDatabaseAllocatedStorage
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersDatabaseAllocatedStorage#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersDatabaseAllocatedStorage#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersDatabaseAllocatedStorage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-newvpc-module.CfnModulePropsParametersDatabaseEngine",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersDatabaseEngine:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Database engine that you want to run.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersDatabaseEngine
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersDatabaseEngine#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersDatabaseEngine#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersDatabaseEngine(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-newvpc-module.CfnModulePropsParametersDatabaseInstance",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersDatabaseInstance:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Size of the database to be deployed as part of the Quick Start.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersDatabaseInstance
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersDatabaseInstance#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersDatabaseInstance#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersDatabaseInstance(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-newvpc-module.CfnModulePropsParametersDatabaseName",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersDatabaseName:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Name of your database instance.

        The name must be unique across all instances owned by your AWS account in the current Region. The database instance identifier is case-insensitive, but it's stored in lowercase (as in "mydbinstance").

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersDatabaseName
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersDatabaseName#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersDatabaseName#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersDatabaseName(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-newvpc-module.CfnModulePropsParametersDatabasePassword",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersDatabasePassword:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Password for the Artifactory database user.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersDatabasePassword
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersDatabasePassword#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

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
    jsii_type="@cdk-cloudformation/jfrog-artifactory-newvpc-module.CfnModulePropsParametersDatabasePreferredAz",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersDatabasePreferredAz:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Preferred availability zone for Amazon RDS primary instance.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersDatabasePreferredAz
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersDatabasePreferredAz#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersDatabasePreferredAz#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersDatabasePreferredAz(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-newvpc-module.CfnModulePropsParametersDatabaseUser",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersDatabaseUser:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Login ID for the master user of your database instance.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersDatabaseUser
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersDatabaseUser#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

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
    jsii_type="@cdk-cloudformation/jfrog-artifactory-newvpc-module.CfnModulePropsParametersDefaultJavaMemSettings",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersDefaultJavaMemSettings:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Choose false to overwrite the standard memory-calculation options to pass to the Artifactory JVM.

        If you plan to overwrite them, ensure they are added to the ExtraJavaOptions to prevent the stack provision from failing.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersDefaultJavaMemSettings
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersDefaultJavaMemSettings#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersDefaultJavaMemSettings#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersDefaultJavaMemSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-newvpc-module.CfnModulePropsParametersEnableBastion",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersEnableBastion:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''If set to true, a bastion host will be created.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersEnableBastion
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersEnableBastion#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersEnableBastion#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersEnableBastion(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-newvpc-module.CfnModulePropsParametersExtraJavaOptions",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersExtraJavaOptions:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Set Java options to pass to the JVM for Artifactory.

        For more information, see the Artifactory system requirements at https://www.jfrog.com/confluence/display/RTF/System+Requirements#SystemRequirements-RecommendedHardware. Do not add Xms or Xmx settings without disabling DefaultJavaMemSettings.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersExtraJavaOptions
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersExtraJavaOptions#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

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
    jsii_type="@cdk-cloudformation/jfrog-artifactory-newvpc-module.CfnModulePropsParametersInstallXray",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersInstallXray:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Choose true to install JFrog Xray instance(s).

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersInstallXray
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersInstallXray#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersInstallXray#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersInstallXray(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-newvpc-module.CfnModulePropsParametersInstanceType",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersInstanceType:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''EC2 instance type for the Artifactory instances.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersInstanceType
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersInstanceType#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

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
    jsii_type="@cdk-cloudformation/jfrog-artifactory-newvpc-module.CfnModulePropsParametersKeyPairName",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersKeyPairName:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Name of an existing key pair, which allows you to connect securely to your instance after it launches.

        This is the key pair you created in your preferred Region.

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
    jsii_type="@cdk-cloudformation/jfrog-artifactory-newvpc-module.CfnModulePropsParametersLogicalId",
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
    jsii_type="@cdk-cloudformation/jfrog-artifactory-newvpc-module.CfnModulePropsParametersMasterKey",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersMasterKey:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Master key for the Artifactory cluster.

        Generate a master key by using the command '$openssl rand -hex 16'.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersMasterKey
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersMasterKey#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

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
    jsii_type="@cdk-cloudformation/jfrog-artifactory-newvpc-module.CfnModulePropsParametersMultiAzDatabase",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersMultiAzDatabase:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Choose false to create an Amazon RDS instance in a single Availability Zone.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersMultiAzDatabase
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersMultiAzDatabase#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersMultiAzDatabase#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersMultiAzDatabase(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-newvpc-module.CfnModulePropsParametersNumBastionHosts",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersNumBastionHosts:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Number of bastion instances to create.

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
    jsii_type="@cdk-cloudformation/jfrog-artifactory-newvpc-module.CfnModulePropsParametersNumberOfSecondary",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersNumberOfSecondary:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Number of secondary Artifactory servers to complete your HA deployment.

        To align with Artifactory best practices, the minimum number is two, and the maximum is seven. Do not select more instances than you have licenses for.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersNumberOfSecondary
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersNumberOfSecondary#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersNumberOfSecondary#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersNumberOfSecondary(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-newvpc-module.CfnModulePropsParametersPrivateSubnet1Cidr",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersPrivateSubnet1Cidr:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''CIDR block for private subnet 1 located in Availability Zone 1.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersPrivateSubnet1Cidr
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersPrivateSubnet1Cidr#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersPrivateSubnet1Cidr#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersPrivateSubnet1Cidr(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-newvpc-module.CfnModulePropsParametersPrivateSubnet2Cidr",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersPrivateSubnet2Cidr:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''CIDR block for private subnet 2 located in Availability Zone 2.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersPrivateSubnet2Cidr
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersPrivateSubnet2Cidr#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersPrivateSubnet2Cidr#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersPrivateSubnet2Cidr(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-newvpc-module.CfnModulePropsParametersPublicSubnet1Cidr",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersPublicSubnet1Cidr:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''CIDR block for the public (DMZ) subnet 1 located in Availability Zone 1.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersPublicSubnet1Cidr
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersPublicSubnet1Cidr#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

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
    jsii_type="@cdk-cloudformation/jfrog-artifactory-newvpc-module.CfnModulePropsParametersPublicSubnet2Cidr",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersPublicSubnet2Cidr:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''CIDR block for the public (DMZ) subnet 2 located in Availability Zone 2.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersPublicSubnet2Cidr
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersPublicSubnet2Cidr#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

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
    jsii_type="@cdk-cloudformation/jfrog-artifactory-newvpc-module.CfnModulePropsParametersQsS3BucketName",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersQsS3BucketName:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''S3 bucket name for the Quick Start assets.

        This string can include numbers, lowercase letters, and hyphens (-). It cannot start or end with a hyphen (-).

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersQsS3BucketName
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersQsS3BucketName#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

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
    jsii_type="@cdk-cloudformation/jfrog-artifactory-newvpc-module.CfnModulePropsParametersQsS3BucketRegion",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersQsS3BucketRegion:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''AWS Region where the Quick Start S3 bucket (QSS3BucketName) is hosted.

        If you use your own bucket, you must specify your own value.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersQsS3BucketRegion
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersQsS3BucketRegion#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersQsS3BucketRegion#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersQsS3BucketRegion(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-newvpc-module.CfnModulePropsParametersQsS3KeyPrefix",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersQsS3KeyPrefix:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''S3 key prefix for the Quick Start assets.

        Quick Start key prefix can include numbers, lowercase letters, uppercase letters, hyphens (-), and forward slash (/).

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersQsS3KeyPrefix
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersQsS3KeyPrefix#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

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
    jsii_type="@cdk-cloudformation/jfrog-artifactory-newvpc-module.CfnModulePropsParametersRemoteAccessCidr",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersRemoteAccessCidr:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Remote CIDR range that allows you to connect to the bastion instance by using SSH.

        It is recommended that you set this value to a trusted IP range. For example, you may want to grant specific ranges from within your corporate network that use the SSH protocol.

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
    jsii_type="@cdk-cloudformation/jfrog-artifactory-newvpc-module.CfnModulePropsParametersSmCertName",
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
    jsii_type="@cdk-cloudformation/jfrog-artifactory-newvpc-module.CfnModulePropsParametersSmLicenseName",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersSmLicenseName:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Secret name created in AWS Secrets Manager, which contains the Artifactory licenses.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersSmLicenseName
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersSmLicenseName#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersSmLicenseName#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersSmLicenseName(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-newvpc-module.CfnModulePropsParametersVolumeSize",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersVolumeSize:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Size in gigabytes of available storage (min 10GB).

        The Quick Start creates an Amazon Elastic Block Store (Amazon EBS) volumes of this size.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersVolumeSize
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersVolumeSize#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

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
    jsii_type="@cdk-cloudformation/jfrog-artifactory-newvpc-module.CfnModulePropsParametersVpcCidr",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersVpcCidr:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''CIDR block for the VPC.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersVpcCidr
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersVpcCidr#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersVpcCidr#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersVpcCidr(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-newvpc-module.CfnModulePropsParametersXrayDatabasePassword",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersXrayDatabasePassword:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The password for the Xray database user.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersXrayDatabasePassword
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersXrayDatabasePassword#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

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
    jsii_type="@cdk-cloudformation/jfrog-artifactory-newvpc-module.CfnModulePropsParametersXrayDatabaseUser",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersXrayDatabaseUser:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The login ID for the Xray database user.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersXrayDatabaseUser
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersXrayDatabaseUser#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

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
    jsii_type="@cdk-cloudformation/jfrog-artifactory-newvpc-module.CfnModulePropsParametersXrayInstanceType",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersXrayInstanceType:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The EC2 instance type for the Xray instances.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersXrayInstanceType
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersXrayInstanceType#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

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
    jsii_type="@cdk-cloudformation/jfrog-artifactory-newvpc-module.CfnModulePropsParametersXrayNumberOfInstances",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersXrayNumberOfInstances:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The number of Xray instances servers to complete your HA deployment.

        The minimum number is one; the maximum is seven. Do not select more than instances than you have licenses for.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersXrayNumberOfInstances
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersXrayNumberOfInstances#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersXrayNumberOfInstances#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersXrayNumberOfInstances(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-newvpc-module.CfnModulePropsParametersXrayVersion",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersXrayVersion:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The version of Xray that you want to deploy into the Quick Start.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersXrayVersion
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersXrayVersion#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

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
    jsii_type="@cdk-cloudformation/jfrog-artifactory-newvpc-module.CfnModulePropsResources",
    jsii_struct_bases=[],
    name_mapping={
        "artifactory_existing_vpc_stack": "artifactoryExistingVpcStack",
        "artifactory_vpc_stack": "artifactoryVpcStack",
    },
)
class CfnModulePropsResources:
    def __init__(
        self,
        *,
        artifactory_existing_vpc_stack: typing.Optional["CfnModulePropsResourcesArtifactoryExistingVpcStack"] = None,
        artifactory_vpc_stack: typing.Optional["CfnModulePropsResourcesArtifactoryVpcStack"] = None,
    ) -> None:
        '''
        :param artifactory_existing_vpc_stack: 
        :param artifactory_vpc_stack: 

        :schema: CfnModulePropsResources
        '''
        if isinstance(artifactory_existing_vpc_stack, dict):
            artifactory_existing_vpc_stack = CfnModulePropsResourcesArtifactoryExistingVpcStack(**artifactory_existing_vpc_stack)
        if isinstance(artifactory_vpc_stack, dict):
            artifactory_vpc_stack = CfnModulePropsResourcesArtifactoryVpcStack(**artifactory_vpc_stack)
        self._values: typing.Dict[str, typing.Any] = {}
        if artifactory_existing_vpc_stack is not None:
            self._values["artifactory_existing_vpc_stack"] = artifactory_existing_vpc_stack
        if artifactory_vpc_stack is not None:
            self._values["artifactory_vpc_stack"] = artifactory_vpc_stack

    @builtins.property
    def artifactory_existing_vpc_stack(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesArtifactoryExistingVpcStack"]:
        '''
        :schema: CfnModulePropsResources#ArtifactoryExistingVpcStack
        '''
        result = self._values.get("artifactory_existing_vpc_stack")
        return typing.cast(typing.Optional["CfnModulePropsResourcesArtifactoryExistingVpcStack"], result)

    @builtins.property
    def artifactory_vpc_stack(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesArtifactoryVpcStack"]:
        '''
        :schema: CfnModulePropsResources#ArtifactoryVpcStack
        '''
        result = self._values.get("artifactory_vpc_stack")
        return typing.cast(typing.Optional["CfnModulePropsResourcesArtifactoryVpcStack"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResources(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-newvpc-module.CfnModulePropsResourcesArtifactoryExistingVpcStack",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesArtifactoryExistingVpcStack:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesArtifactoryExistingVpcStack
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesArtifactoryExistingVpcStack#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesArtifactoryExistingVpcStack#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesArtifactoryExistingVpcStack(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-newvpc-module.CfnModulePropsResourcesArtifactoryVpcStack",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesArtifactoryVpcStack:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesArtifactoryVpcStack
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesArtifactoryVpcStack#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesArtifactoryVpcStack#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesArtifactoryVpcStack(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnModule",
    "CfnModuleProps",
    "CfnModulePropsParameters",
    "CfnModulePropsParametersAccessCidr",
    "CfnModulePropsParametersArtifactoryProduct",
    "CfnModulePropsParametersArtifactoryServerName",
    "CfnModulePropsParametersArtifactoryVersion",
    "CfnModulePropsParametersAvailabilityZone1",
    "CfnModulePropsParametersAvailabilityZone2",
    "CfnModulePropsParametersBastionEnableTcpForwarding",
    "CfnModulePropsParametersBastionEnableX11Forwarding",
    "CfnModulePropsParametersBastionInstanceType",
    "CfnModulePropsParametersBastionOs",
    "CfnModulePropsParametersBastionRootVolumeSize",
    "CfnModulePropsParametersDatabaseAllocatedStorage",
    "CfnModulePropsParametersDatabaseEngine",
    "CfnModulePropsParametersDatabaseInstance",
    "CfnModulePropsParametersDatabaseName",
    "CfnModulePropsParametersDatabasePassword",
    "CfnModulePropsParametersDatabasePreferredAz",
    "CfnModulePropsParametersDatabaseUser",
    "CfnModulePropsParametersDefaultJavaMemSettings",
    "CfnModulePropsParametersEnableBastion",
    "CfnModulePropsParametersExtraJavaOptions",
    "CfnModulePropsParametersInstallXray",
    "CfnModulePropsParametersInstanceType",
    "CfnModulePropsParametersKeyPairName",
    "CfnModulePropsParametersLogicalId",
    "CfnModulePropsParametersMasterKey",
    "CfnModulePropsParametersMultiAzDatabase",
    "CfnModulePropsParametersNumBastionHosts",
    "CfnModulePropsParametersNumberOfSecondary",
    "CfnModulePropsParametersPrivateSubnet1Cidr",
    "CfnModulePropsParametersPrivateSubnet2Cidr",
    "CfnModulePropsParametersPublicSubnet1Cidr",
    "CfnModulePropsParametersPublicSubnet2Cidr",
    "CfnModulePropsParametersQsS3BucketName",
    "CfnModulePropsParametersQsS3BucketRegion",
    "CfnModulePropsParametersQsS3KeyPrefix",
    "CfnModulePropsParametersRemoteAccessCidr",
    "CfnModulePropsParametersSmCertName",
    "CfnModulePropsParametersSmLicenseName",
    "CfnModulePropsParametersVolumeSize",
    "CfnModulePropsParametersVpcCidr",
    "CfnModulePropsParametersXrayDatabasePassword",
    "CfnModulePropsParametersXrayDatabaseUser",
    "CfnModulePropsParametersXrayInstanceType",
    "CfnModulePropsParametersXrayNumberOfInstances",
    "CfnModulePropsParametersXrayVersion",
    "CfnModulePropsResources",
    "CfnModulePropsResourcesArtifactoryExistingVpcStack",
    "CfnModulePropsResourcesArtifactoryVpcStack",
]

publication.publish()
