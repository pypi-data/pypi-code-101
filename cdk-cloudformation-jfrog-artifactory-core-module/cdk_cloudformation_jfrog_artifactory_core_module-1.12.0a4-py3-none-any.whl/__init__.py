'''
# jfrog-artifactory-core-module

> AWS CDK [L1 construct](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html) and data structures for the [AWS CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) type `JFrog::Artifactory::Core::MODULE` v1.12.0.

## Description

Schema for Module Fragment of type JFrog::Artifactory::Core::MODULE

## Usage

In order to use this library, you will need to activate this AWS CloudFormation Registry type in your account. You can do this via the AWS Management Console or using the [AWS CLI](https://aws.amazon.com/cli/) using the following command:

```sh
aws cloudformation activate-type \
  --type-name JFrog::Artifactory::Core::MODULE \
  --publisher-id 06ff50c2e47f57b381f874871d9fac41796c9522 \
  --type MODULE \
  --execution-role-arn ROLE-ARN
```

Alternatively:

```sh
aws cloudformation activate-type \
  --public-type-arn arn:aws:cloudformation:us-east-1::type/module/06ff50c2e47f57b381f874871d9fac41796c9522/JFrog-Artifactory-Core-MODULE \
  --execution-role-arn ROLE-ARN
```

You can find more information about activating this type in the [AWS CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html).

## Feedback

This library is auto-generated and published to all supported programming languages by the [cdklabs/cdk-cloudformation](https://github.com/cdklabs/cdk-cloudformation) project based on the API schema published for `JFrog::Artifactory::Core::MODULE`.

* Issues related to this generated library should be [reported here](https://github.com/cdklabs/cdk-cloudformation/issues/new?title=Issue+with+%40cdk-cloudformation%2Fjfrog-artifactory-core-module+v1.12.0).
* Issues related to `JFrog::Artifactory::Core::MODULE` should be reported to the [publisher](undefined).

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


class CfnCoreModule(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/jfrog-artifactory-core-module.CfnCoreModule",
):
    '''A CloudFormation ``JFrog::Artifactory::Core::MODULE``.

    :cloudformationResource: JFrog::Artifactory::Core::MODULE
    :link: http://unknown-url
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        parameters: typing.Optional["CfnCoreModulePropsParameters"] = None,
        resources: typing.Optional["CfnCoreModulePropsResources"] = None,
    ) -> None:
        '''Create a new ``JFrog::Artifactory::Core::MODULE``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param parameters: 
        :param resources: 
        '''
        props = CfnCoreModuleProps(parameters=parameters, resources=resources)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnCoreModuleProps":
        '''Resource props.'''
        return typing.cast("CfnCoreModuleProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-core-module.CfnCoreModuleProps",
    jsii_struct_bases=[],
    name_mapping={"parameters": "parameters", "resources": "resources"},
)
class CfnCoreModuleProps:
    def __init__(
        self,
        *,
        parameters: typing.Optional["CfnCoreModulePropsParameters"] = None,
        resources: typing.Optional["CfnCoreModulePropsResources"] = None,
    ) -> None:
        '''Schema for Module Fragment of type JFrog::Artifactory::Core::MODULE.

        :param parameters: 
        :param resources: 

        :schema: CfnCoreModuleProps
        '''
        if isinstance(parameters, dict):
            parameters = CfnCoreModulePropsParameters(**parameters)
        if isinstance(resources, dict):
            resources = CfnCoreModulePropsResources(**resources)
        self._values: typing.Dict[str, typing.Any] = {}
        if parameters is not None:
            self._values["parameters"] = parameters
        if resources is not None:
            self._values["resources"] = resources

    @builtins.property
    def parameters(self) -> typing.Optional["CfnCoreModulePropsParameters"]:
        '''
        :schema: CfnCoreModuleProps#Parameters
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional["CfnCoreModulePropsParameters"], result)

    @builtins.property
    def resources(self) -> typing.Optional["CfnCoreModulePropsResources"]:
        '''
        :schema: CfnCoreModuleProps#Resources
        '''
        result = self._values.get("resources")
        return typing.cast(typing.Optional["CfnCoreModulePropsResources"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCoreModuleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-core-module.CfnCoreModulePropsParameters",
    jsii_struct_bases=[],
    name_mapping={
        "artifactory_host_role": "artifactoryHostRole",
        "artifactory_product": "artifactoryProduct",
        "availability_zone1": "availabilityZone1",
        "availability_zone2": "availabilityZone2",
        "database_allocated_storage": "databaseAllocatedStorage",
        "database_engine": "databaseEngine",
        "database_instance": "databaseInstance",
        "database_name": "databaseName",
        "database_password": "databasePassword",
        "database_preferred_az": "databasePreferredAz",
        "database_user": "databaseUser",
        "efs_security_group": "efsSecurityGroup",
        "instance_type": "instanceType",
        "multi_az_database": "multiAzDatabase",
        "private_subnet1_cidr": "privateSubnet1Cidr",
        "private_subnet1_id": "privateSubnet1Id",
        "private_subnet2_cidr": "privateSubnet2Cidr",
        "private_subnet2_id": "privateSubnet2Id",
        "private_subnet3_cidr": "privateSubnet3Cidr",
        "release_stage": "releaseStage",
        "vpc_cidr": "vpcCidr",
        "vpc_id": "vpcId",
    },
)
class CfnCoreModulePropsParameters:
    def __init__(
        self,
        *,
        artifactory_host_role: typing.Optional["CfnCoreModulePropsParametersArtifactoryHostRole"] = None,
        artifactory_product: typing.Optional["CfnCoreModulePropsParametersArtifactoryProduct"] = None,
        availability_zone1: typing.Optional["CfnCoreModulePropsParametersAvailabilityZone1"] = None,
        availability_zone2: typing.Optional["CfnCoreModulePropsParametersAvailabilityZone2"] = None,
        database_allocated_storage: typing.Optional["CfnCoreModulePropsParametersDatabaseAllocatedStorage"] = None,
        database_engine: typing.Optional["CfnCoreModulePropsParametersDatabaseEngine"] = None,
        database_instance: typing.Optional["CfnCoreModulePropsParametersDatabaseInstance"] = None,
        database_name: typing.Optional["CfnCoreModulePropsParametersDatabaseName"] = None,
        database_password: typing.Optional["CfnCoreModulePropsParametersDatabasePassword"] = None,
        database_preferred_az: typing.Optional["CfnCoreModulePropsParametersDatabasePreferredAz"] = None,
        database_user: typing.Optional["CfnCoreModulePropsParametersDatabaseUser"] = None,
        efs_security_group: typing.Optional["CfnCoreModulePropsParametersEfsSecurityGroup"] = None,
        instance_type: typing.Optional["CfnCoreModulePropsParametersInstanceType"] = None,
        multi_az_database: typing.Optional["CfnCoreModulePropsParametersMultiAzDatabase"] = None,
        private_subnet1_cidr: typing.Optional["CfnCoreModulePropsParametersPrivateSubnet1Cidr"] = None,
        private_subnet1_id: typing.Optional["CfnCoreModulePropsParametersPrivateSubnet1Id"] = None,
        private_subnet2_cidr: typing.Optional["CfnCoreModulePropsParametersPrivateSubnet2Cidr"] = None,
        private_subnet2_id: typing.Optional["CfnCoreModulePropsParametersPrivateSubnet2Id"] = None,
        private_subnet3_cidr: typing.Optional["CfnCoreModulePropsParametersPrivateSubnet3Cidr"] = None,
        release_stage: typing.Optional["CfnCoreModulePropsParametersReleaseStage"] = None,
        vpc_cidr: typing.Optional["CfnCoreModulePropsParametersVpcCidr"] = None,
        vpc_id: typing.Optional["CfnCoreModulePropsParametersVpcId"] = None,
    ) -> None:
        '''
        :param artifactory_host_role: 
        :param artifactory_product: 
        :param availability_zone1: Availability Zone 1 to use for the subnets in the VPC. Two Availability Zones are used for this deployment.
        :param availability_zone2: Availability Zone 2 to use for the subnets in the VPC. Two Availability Zones are used for this deployment.
        :param database_allocated_storage: 
        :param database_engine: 
        :param database_instance: 
        :param database_name: 
        :param database_password: 
        :param database_preferred_az: 
        :param database_user: 
        :param efs_security_group: 
        :param instance_type: 
        :param multi_az_database: Choose false to create an Amazon RDS instance in a single Availability Zone.
        :param private_subnet1_cidr: 
        :param private_subnet1_id: ID of the private subnet in Availability Zone 1 of your existing VPC (e.g., subnet-z0376dab).
        :param private_subnet2_cidr: 
        :param private_subnet2_id: ID of the private subnet in Availability Zone 1 of your existing VPC (e.g., subnet-z0376dab).
        :param private_subnet3_cidr: 
        :param release_stage: 
        :param vpc_cidr: CIDR block for the VPC.
        :param vpc_id: 

        :schema: CfnCoreModulePropsParameters
        '''
        if isinstance(artifactory_host_role, dict):
            artifactory_host_role = CfnCoreModulePropsParametersArtifactoryHostRole(**artifactory_host_role)
        if isinstance(artifactory_product, dict):
            artifactory_product = CfnCoreModulePropsParametersArtifactoryProduct(**artifactory_product)
        if isinstance(availability_zone1, dict):
            availability_zone1 = CfnCoreModulePropsParametersAvailabilityZone1(**availability_zone1)
        if isinstance(availability_zone2, dict):
            availability_zone2 = CfnCoreModulePropsParametersAvailabilityZone2(**availability_zone2)
        if isinstance(database_allocated_storage, dict):
            database_allocated_storage = CfnCoreModulePropsParametersDatabaseAllocatedStorage(**database_allocated_storage)
        if isinstance(database_engine, dict):
            database_engine = CfnCoreModulePropsParametersDatabaseEngine(**database_engine)
        if isinstance(database_instance, dict):
            database_instance = CfnCoreModulePropsParametersDatabaseInstance(**database_instance)
        if isinstance(database_name, dict):
            database_name = CfnCoreModulePropsParametersDatabaseName(**database_name)
        if isinstance(database_password, dict):
            database_password = CfnCoreModulePropsParametersDatabasePassword(**database_password)
        if isinstance(database_preferred_az, dict):
            database_preferred_az = CfnCoreModulePropsParametersDatabasePreferredAz(**database_preferred_az)
        if isinstance(database_user, dict):
            database_user = CfnCoreModulePropsParametersDatabaseUser(**database_user)
        if isinstance(efs_security_group, dict):
            efs_security_group = CfnCoreModulePropsParametersEfsSecurityGroup(**efs_security_group)
        if isinstance(instance_type, dict):
            instance_type = CfnCoreModulePropsParametersInstanceType(**instance_type)
        if isinstance(multi_az_database, dict):
            multi_az_database = CfnCoreModulePropsParametersMultiAzDatabase(**multi_az_database)
        if isinstance(private_subnet1_cidr, dict):
            private_subnet1_cidr = CfnCoreModulePropsParametersPrivateSubnet1Cidr(**private_subnet1_cidr)
        if isinstance(private_subnet1_id, dict):
            private_subnet1_id = CfnCoreModulePropsParametersPrivateSubnet1Id(**private_subnet1_id)
        if isinstance(private_subnet2_cidr, dict):
            private_subnet2_cidr = CfnCoreModulePropsParametersPrivateSubnet2Cidr(**private_subnet2_cidr)
        if isinstance(private_subnet2_id, dict):
            private_subnet2_id = CfnCoreModulePropsParametersPrivateSubnet2Id(**private_subnet2_id)
        if isinstance(private_subnet3_cidr, dict):
            private_subnet3_cidr = CfnCoreModulePropsParametersPrivateSubnet3Cidr(**private_subnet3_cidr)
        if isinstance(release_stage, dict):
            release_stage = CfnCoreModulePropsParametersReleaseStage(**release_stage)
        if isinstance(vpc_cidr, dict):
            vpc_cidr = CfnCoreModulePropsParametersVpcCidr(**vpc_cidr)
        if isinstance(vpc_id, dict):
            vpc_id = CfnCoreModulePropsParametersVpcId(**vpc_id)
        self._values: typing.Dict[str, typing.Any] = {}
        if artifactory_host_role is not None:
            self._values["artifactory_host_role"] = artifactory_host_role
        if artifactory_product is not None:
            self._values["artifactory_product"] = artifactory_product
        if availability_zone1 is not None:
            self._values["availability_zone1"] = availability_zone1
        if availability_zone2 is not None:
            self._values["availability_zone2"] = availability_zone2
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
        if efs_security_group is not None:
            self._values["efs_security_group"] = efs_security_group
        if instance_type is not None:
            self._values["instance_type"] = instance_type
        if multi_az_database is not None:
            self._values["multi_az_database"] = multi_az_database
        if private_subnet1_cidr is not None:
            self._values["private_subnet1_cidr"] = private_subnet1_cidr
        if private_subnet1_id is not None:
            self._values["private_subnet1_id"] = private_subnet1_id
        if private_subnet2_cidr is not None:
            self._values["private_subnet2_cidr"] = private_subnet2_cidr
        if private_subnet2_id is not None:
            self._values["private_subnet2_id"] = private_subnet2_id
        if private_subnet3_cidr is not None:
            self._values["private_subnet3_cidr"] = private_subnet3_cidr
        if release_stage is not None:
            self._values["release_stage"] = release_stage
        if vpc_cidr is not None:
            self._values["vpc_cidr"] = vpc_cidr
        if vpc_id is not None:
            self._values["vpc_id"] = vpc_id

    @builtins.property
    def artifactory_host_role(
        self,
    ) -> typing.Optional["CfnCoreModulePropsParametersArtifactoryHostRole"]:
        '''
        :schema: CfnCoreModulePropsParameters#ArtifactoryHostRole
        '''
        result = self._values.get("artifactory_host_role")
        return typing.cast(typing.Optional["CfnCoreModulePropsParametersArtifactoryHostRole"], result)

    @builtins.property
    def artifactory_product(
        self,
    ) -> typing.Optional["CfnCoreModulePropsParametersArtifactoryProduct"]:
        '''
        :schema: CfnCoreModulePropsParameters#ArtifactoryProduct
        '''
        result = self._values.get("artifactory_product")
        return typing.cast(typing.Optional["CfnCoreModulePropsParametersArtifactoryProduct"], result)

    @builtins.property
    def availability_zone1(
        self,
    ) -> typing.Optional["CfnCoreModulePropsParametersAvailabilityZone1"]:
        '''Availability Zone 1 to use for the subnets in the VPC.

        Two Availability Zones are used for this deployment.

        :schema: CfnCoreModulePropsParameters#AvailabilityZone1
        '''
        result = self._values.get("availability_zone1")
        return typing.cast(typing.Optional["CfnCoreModulePropsParametersAvailabilityZone1"], result)

    @builtins.property
    def availability_zone2(
        self,
    ) -> typing.Optional["CfnCoreModulePropsParametersAvailabilityZone2"]:
        '''Availability Zone 2 to use for the subnets in the VPC.

        Two Availability Zones are used for this deployment.

        :schema: CfnCoreModulePropsParameters#AvailabilityZone2
        '''
        result = self._values.get("availability_zone2")
        return typing.cast(typing.Optional["CfnCoreModulePropsParametersAvailabilityZone2"], result)

    @builtins.property
    def database_allocated_storage(
        self,
    ) -> typing.Optional["CfnCoreModulePropsParametersDatabaseAllocatedStorage"]:
        '''
        :schema: CfnCoreModulePropsParameters#DatabaseAllocatedStorage
        '''
        result = self._values.get("database_allocated_storage")
        return typing.cast(typing.Optional["CfnCoreModulePropsParametersDatabaseAllocatedStorage"], result)

    @builtins.property
    def database_engine(
        self,
    ) -> typing.Optional["CfnCoreModulePropsParametersDatabaseEngine"]:
        '''
        :schema: CfnCoreModulePropsParameters#DatabaseEngine
        '''
        result = self._values.get("database_engine")
        return typing.cast(typing.Optional["CfnCoreModulePropsParametersDatabaseEngine"], result)

    @builtins.property
    def database_instance(
        self,
    ) -> typing.Optional["CfnCoreModulePropsParametersDatabaseInstance"]:
        '''
        :schema: CfnCoreModulePropsParameters#DatabaseInstance
        '''
        result = self._values.get("database_instance")
        return typing.cast(typing.Optional["CfnCoreModulePropsParametersDatabaseInstance"], result)

    @builtins.property
    def database_name(
        self,
    ) -> typing.Optional["CfnCoreModulePropsParametersDatabaseName"]:
        '''
        :schema: CfnCoreModulePropsParameters#DatabaseName
        '''
        result = self._values.get("database_name")
        return typing.cast(typing.Optional["CfnCoreModulePropsParametersDatabaseName"], result)

    @builtins.property
    def database_password(
        self,
    ) -> typing.Optional["CfnCoreModulePropsParametersDatabasePassword"]:
        '''
        :schema: CfnCoreModulePropsParameters#DatabasePassword
        '''
        result = self._values.get("database_password")
        return typing.cast(typing.Optional["CfnCoreModulePropsParametersDatabasePassword"], result)

    @builtins.property
    def database_preferred_az(
        self,
    ) -> typing.Optional["CfnCoreModulePropsParametersDatabasePreferredAz"]:
        '''
        :schema: CfnCoreModulePropsParameters#DatabasePreferredAz
        '''
        result = self._values.get("database_preferred_az")
        return typing.cast(typing.Optional["CfnCoreModulePropsParametersDatabasePreferredAz"], result)

    @builtins.property
    def database_user(
        self,
    ) -> typing.Optional["CfnCoreModulePropsParametersDatabaseUser"]:
        '''
        :schema: CfnCoreModulePropsParameters#DatabaseUser
        '''
        result = self._values.get("database_user")
        return typing.cast(typing.Optional["CfnCoreModulePropsParametersDatabaseUser"], result)

    @builtins.property
    def efs_security_group(
        self,
    ) -> typing.Optional["CfnCoreModulePropsParametersEfsSecurityGroup"]:
        '''
        :schema: CfnCoreModulePropsParameters#EfsSecurityGroup
        '''
        result = self._values.get("efs_security_group")
        return typing.cast(typing.Optional["CfnCoreModulePropsParametersEfsSecurityGroup"], result)

    @builtins.property
    def instance_type(
        self,
    ) -> typing.Optional["CfnCoreModulePropsParametersInstanceType"]:
        '''
        :schema: CfnCoreModulePropsParameters#InstanceType
        '''
        result = self._values.get("instance_type")
        return typing.cast(typing.Optional["CfnCoreModulePropsParametersInstanceType"], result)

    @builtins.property
    def multi_az_database(
        self,
    ) -> typing.Optional["CfnCoreModulePropsParametersMultiAzDatabase"]:
        '''Choose false to create an Amazon RDS instance in a single Availability Zone.

        :schema: CfnCoreModulePropsParameters#MultiAzDatabase
        '''
        result = self._values.get("multi_az_database")
        return typing.cast(typing.Optional["CfnCoreModulePropsParametersMultiAzDatabase"], result)

    @builtins.property
    def private_subnet1_cidr(
        self,
    ) -> typing.Optional["CfnCoreModulePropsParametersPrivateSubnet1Cidr"]:
        '''
        :schema: CfnCoreModulePropsParameters#PrivateSubnet1Cidr
        '''
        result = self._values.get("private_subnet1_cidr")
        return typing.cast(typing.Optional["CfnCoreModulePropsParametersPrivateSubnet1Cidr"], result)

    @builtins.property
    def private_subnet1_id(
        self,
    ) -> typing.Optional["CfnCoreModulePropsParametersPrivateSubnet1Id"]:
        '''ID of the private subnet in Availability Zone 1 of your existing VPC (e.g., subnet-z0376dab).

        :schema: CfnCoreModulePropsParameters#PrivateSubnet1Id
        '''
        result = self._values.get("private_subnet1_id")
        return typing.cast(typing.Optional["CfnCoreModulePropsParametersPrivateSubnet1Id"], result)

    @builtins.property
    def private_subnet2_cidr(
        self,
    ) -> typing.Optional["CfnCoreModulePropsParametersPrivateSubnet2Cidr"]:
        '''
        :schema: CfnCoreModulePropsParameters#PrivateSubnet2Cidr
        '''
        result = self._values.get("private_subnet2_cidr")
        return typing.cast(typing.Optional["CfnCoreModulePropsParametersPrivateSubnet2Cidr"], result)

    @builtins.property
    def private_subnet2_id(
        self,
    ) -> typing.Optional["CfnCoreModulePropsParametersPrivateSubnet2Id"]:
        '''ID of the private subnet in Availability Zone 1 of your existing VPC (e.g., subnet-z0376dab).

        :schema: CfnCoreModulePropsParameters#PrivateSubnet2Id
        '''
        result = self._values.get("private_subnet2_id")
        return typing.cast(typing.Optional["CfnCoreModulePropsParametersPrivateSubnet2Id"], result)

    @builtins.property
    def private_subnet3_cidr(
        self,
    ) -> typing.Optional["CfnCoreModulePropsParametersPrivateSubnet3Cidr"]:
        '''
        :schema: CfnCoreModulePropsParameters#PrivateSubnet3Cidr
        '''
        result = self._values.get("private_subnet3_cidr")
        return typing.cast(typing.Optional["CfnCoreModulePropsParametersPrivateSubnet3Cidr"], result)

    @builtins.property
    def release_stage(
        self,
    ) -> typing.Optional["CfnCoreModulePropsParametersReleaseStage"]:
        '''
        :schema: CfnCoreModulePropsParameters#ReleaseStage
        '''
        result = self._values.get("release_stage")
        return typing.cast(typing.Optional["CfnCoreModulePropsParametersReleaseStage"], result)

    @builtins.property
    def vpc_cidr(self) -> typing.Optional["CfnCoreModulePropsParametersVpcCidr"]:
        '''CIDR block for the VPC.

        :schema: CfnCoreModulePropsParameters#VpcCidr
        '''
        result = self._values.get("vpc_cidr")
        return typing.cast(typing.Optional["CfnCoreModulePropsParametersVpcCidr"], result)

    @builtins.property
    def vpc_id(self) -> typing.Optional["CfnCoreModulePropsParametersVpcId"]:
        '''
        :schema: CfnCoreModulePropsParameters#VpcId
        '''
        result = self._values.get("vpc_id")
        return typing.cast(typing.Optional["CfnCoreModulePropsParametersVpcId"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCoreModulePropsParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-core-module.CfnCoreModulePropsParametersArtifactoryHostRole",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnCoreModulePropsParametersArtifactoryHostRole:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnCoreModulePropsParametersArtifactoryHostRole
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCoreModulePropsParametersArtifactoryHostRole#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCoreModulePropsParametersArtifactoryHostRole(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-core-module.CfnCoreModulePropsParametersArtifactoryProduct",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnCoreModulePropsParametersArtifactoryProduct:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnCoreModulePropsParametersArtifactoryProduct
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCoreModulePropsParametersArtifactoryProduct#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCoreModulePropsParametersArtifactoryProduct(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-core-module.CfnCoreModulePropsParametersAvailabilityZone1",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCoreModulePropsParametersAvailabilityZone1:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Availability Zone 1 to use for the subnets in the VPC.

        Two Availability Zones are used for this deployment.

        :param description: 
        :param type: 

        :schema: CfnCoreModulePropsParametersAvailabilityZone1
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCoreModulePropsParametersAvailabilityZone1#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCoreModulePropsParametersAvailabilityZone1#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCoreModulePropsParametersAvailabilityZone1(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-core-module.CfnCoreModulePropsParametersAvailabilityZone2",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCoreModulePropsParametersAvailabilityZone2:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Availability Zone 2 to use for the subnets in the VPC.

        Two Availability Zones are used for this deployment.

        :param description: 
        :param type: 

        :schema: CfnCoreModulePropsParametersAvailabilityZone2
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCoreModulePropsParametersAvailabilityZone2#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCoreModulePropsParametersAvailabilityZone2#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCoreModulePropsParametersAvailabilityZone2(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-core-module.CfnCoreModulePropsParametersDatabaseAllocatedStorage",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnCoreModulePropsParametersDatabaseAllocatedStorage:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnCoreModulePropsParametersDatabaseAllocatedStorage
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCoreModulePropsParametersDatabaseAllocatedStorage#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCoreModulePropsParametersDatabaseAllocatedStorage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-core-module.CfnCoreModulePropsParametersDatabaseEngine",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnCoreModulePropsParametersDatabaseEngine:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnCoreModulePropsParametersDatabaseEngine
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCoreModulePropsParametersDatabaseEngine#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCoreModulePropsParametersDatabaseEngine(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-core-module.CfnCoreModulePropsParametersDatabaseInstance",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnCoreModulePropsParametersDatabaseInstance:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnCoreModulePropsParametersDatabaseInstance
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCoreModulePropsParametersDatabaseInstance#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCoreModulePropsParametersDatabaseInstance(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-core-module.CfnCoreModulePropsParametersDatabaseName",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnCoreModulePropsParametersDatabaseName:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnCoreModulePropsParametersDatabaseName
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCoreModulePropsParametersDatabaseName#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCoreModulePropsParametersDatabaseName(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-core-module.CfnCoreModulePropsParametersDatabasePassword",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnCoreModulePropsParametersDatabasePassword:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnCoreModulePropsParametersDatabasePassword
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCoreModulePropsParametersDatabasePassword#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCoreModulePropsParametersDatabasePassword(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-core-module.CfnCoreModulePropsParametersDatabasePreferredAz",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnCoreModulePropsParametersDatabasePreferredAz:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnCoreModulePropsParametersDatabasePreferredAz
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCoreModulePropsParametersDatabasePreferredAz#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCoreModulePropsParametersDatabasePreferredAz(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-core-module.CfnCoreModulePropsParametersDatabaseUser",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnCoreModulePropsParametersDatabaseUser:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnCoreModulePropsParametersDatabaseUser
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCoreModulePropsParametersDatabaseUser#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCoreModulePropsParametersDatabaseUser(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-core-module.CfnCoreModulePropsParametersEfsSecurityGroup",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnCoreModulePropsParametersEfsSecurityGroup:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnCoreModulePropsParametersEfsSecurityGroup
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCoreModulePropsParametersEfsSecurityGroup#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCoreModulePropsParametersEfsSecurityGroup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-core-module.CfnCoreModulePropsParametersInstanceType",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnCoreModulePropsParametersInstanceType:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnCoreModulePropsParametersInstanceType
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCoreModulePropsParametersInstanceType#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCoreModulePropsParametersInstanceType(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-core-module.CfnCoreModulePropsParametersMultiAzDatabase",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCoreModulePropsParametersMultiAzDatabase:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Choose false to create an Amazon RDS instance in a single Availability Zone.

        :param description: 
        :param type: 

        :schema: CfnCoreModulePropsParametersMultiAzDatabase
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCoreModulePropsParametersMultiAzDatabase#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCoreModulePropsParametersMultiAzDatabase#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCoreModulePropsParametersMultiAzDatabase(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-core-module.CfnCoreModulePropsParametersPrivateSubnet1Cidr",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnCoreModulePropsParametersPrivateSubnet1Cidr:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnCoreModulePropsParametersPrivateSubnet1Cidr
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCoreModulePropsParametersPrivateSubnet1Cidr#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCoreModulePropsParametersPrivateSubnet1Cidr(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-core-module.CfnCoreModulePropsParametersPrivateSubnet1Id",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCoreModulePropsParametersPrivateSubnet1Id:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''ID of the private subnet in Availability Zone 1 of your existing VPC (e.g., subnet-z0376dab).

        :param description: 
        :param type: 

        :schema: CfnCoreModulePropsParametersPrivateSubnet1Id
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCoreModulePropsParametersPrivateSubnet1Id#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCoreModulePropsParametersPrivateSubnet1Id#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCoreModulePropsParametersPrivateSubnet1Id(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-core-module.CfnCoreModulePropsParametersPrivateSubnet2Cidr",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnCoreModulePropsParametersPrivateSubnet2Cidr:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnCoreModulePropsParametersPrivateSubnet2Cidr
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCoreModulePropsParametersPrivateSubnet2Cidr#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCoreModulePropsParametersPrivateSubnet2Cidr(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-core-module.CfnCoreModulePropsParametersPrivateSubnet2Id",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCoreModulePropsParametersPrivateSubnet2Id:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''ID of the private subnet in Availability Zone 1 of your existing VPC (e.g., subnet-z0376dab).

        :param description: 
        :param type: 

        :schema: CfnCoreModulePropsParametersPrivateSubnet2Id
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCoreModulePropsParametersPrivateSubnet2Id#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCoreModulePropsParametersPrivateSubnet2Id#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCoreModulePropsParametersPrivateSubnet2Id(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-core-module.CfnCoreModulePropsParametersPrivateSubnet3Cidr",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnCoreModulePropsParametersPrivateSubnet3Cidr:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnCoreModulePropsParametersPrivateSubnet3Cidr
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCoreModulePropsParametersPrivateSubnet3Cidr#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCoreModulePropsParametersPrivateSubnet3Cidr(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-core-module.CfnCoreModulePropsParametersReleaseStage",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnCoreModulePropsParametersReleaseStage:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnCoreModulePropsParametersReleaseStage
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCoreModulePropsParametersReleaseStage#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCoreModulePropsParametersReleaseStage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-core-module.CfnCoreModulePropsParametersVpcCidr",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCoreModulePropsParametersVpcCidr:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''CIDR block for the VPC.

        :param description: 
        :param type: 

        :schema: CfnCoreModulePropsParametersVpcCidr
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCoreModulePropsParametersVpcCidr#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCoreModulePropsParametersVpcCidr#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCoreModulePropsParametersVpcCidr(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-core-module.CfnCoreModulePropsParametersVpcId",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnCoreModulePropsParametersVpcId:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnCoreModulePropsParametersVpcId
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCoreModulePropsParametersVpcId#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCoreModulePropsParametersVpcId(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-core-module.CfnCoreModulePropsResources",
    jsii_struct_bases=[],
    name_mapping={
        "artifactory_database": "artifactoryDatabase",
        "artifactory_database_sg": "artifactoryDatabaseSg",
        "artifactory_database_subnet_group": "artifactoryDatabaseSubnetGroup",
        "artifactory_efs_file_system": "artifactoryEfsFileSystem",
        "artifactory_efs_mount_target1": "artifactoryEfsMountTarget1",
        "artifactory_efs_mount_target2": "artifactoryEfsMountTarget2",
        "artifactory_s3_bucket": "artifactoryS3Bucket",
        "artifactory_s3_iam_policy": "artifactoryS3IamPolicy",
    },
)
class CfnCoreModulePropsResources:
    def __init__(
        self,
        *,
        artifactory_database: typing.Optional["CfnCoreModulePropsResourcesArtifactoryDatabase"] = None,
        artifactory_database_sg: typing.Optional["CfnCoreModulePropsResourcesArtifactoryDatabaseSg"] = None,
        artifactory_database_subnet_group: typing.Optional["CfnCoreModulePropsResourcesArtifactoryDatabaseSubnetGroup"] = None,
        artifactory_efs_file_system: typing.Optional["CfnCoreModulePropsResourcesArtifactoryEfsFileSystem"] = None,
        artifactory_efs_mount_target1: typing.Optional["CfnCoreModulePropsResourcesArtifactoryEfsMountTarget1"] = None,
        artifactory_efs_mount_target2: typing.Optional["CfnCoreModulePropsResourcesArtifactoryEfsMountTarget2"] = None,
        artifactory_s3_bucket: typing.Optional["CfnCoreModulePropsResourcesArtifactoryS3Bucket"] = None,
        artifactory_s3_iam_policy: typing.Optional["CfnCoreModulePropsResourcesArtifactoryS3IamPolicy"] = None,
    ) -> None:
        '''
        :param artifactory_database: 
        :param artifactory_database_sg: 
        :param artifactory_database_subnet_group: 
        :param artifactory_efs_file_system: 
        :param artifactory_efs_mount_target1: 
        :param artifactory_efs_mount_target2: 
        :param artifactory_s3_bucket: 
        :param artifactory_s3_iam_policy: 

        :schema: CfnCoreModulePropsResources
        '''
        if isinstance(artifactory_database, dict):
            artifactory_database = CfnCoreModulePropsResourcesArtifactoryDatabase(**artifactory_database)
        if isinstance(artifactory_database_sg, dict):
            artifactory_database_sg = CfnCoreModulePropsResourcesArtifactoryDatabaseSg(**artifactory_database_sg)
        if isinstance(artifactory_database_subnet_group, dict):
            artifactory_database_subnet_group = CfnCoreModulePropsResourcesArtifactoryDatabaseSubnetGroup(**artifactory_database_subnet_group)
        if isinstance(artifactory_efs_file_system, dict):
            artifactory_efs_file_system = CfnCoreModulePropsResourcesArtifactoryEfsFileSystem(**artifactory_efs_file_system)
        if isinstance(artifactory_efs_mount_target1, dict):
            artifactory_efs_mount_target1 = CfnCoreModulePropsResourcesArtifactoryEfsMountTarget1(**artifactory_efs_mount_target1)
        if isinstance(artifactory_efs_mount_target2, dict):
            artifactory_efs_mount_target2 = CfnCoreModulePropsResourcesArtifactoryEfsMountTarget2(**artifactory_efs_mount_target2)
        if isinstance(artifactory_s3_bucket, dict):
            artifactory_s3_bucket = CfnCoreModulePropsResourcesArtifactoryS3Bucket(**artifactory_s3_bucket)
        if isinstance(artifactory_s3_iam_policy, dict):
            artifactory_s3_iam_policy = CfnCoreModulePropsResourcesArtifactoryS3IamPolicy(**artifactory_s3_iam_policy)
        self._values: typing.Dict[str, typing.Any] = {}
        if artifactory_database is not None:
            self._values["artifactory_database"] = artifactory_database
        if artifactory_database_sg is not None:
            self._values["artifactory_database_sg"] = artifactory_database_sg
        if artifactory_database_subnet_group is not None:
            self._values["artifactory_database_subnet_group"] = artifactory_database_subnet_group
        if artifactory_efs_file_system is not None:
            self._values["artifactory_efs_file_system"] = artifactory_efs_file_system
        if artifactory_efs_mount_target1 is not None:
            self._values["artifactory_efs_mount_target1"] = artifactory_efs_mount_target1
        if artifactory_efs_mount_target2 is not None:
            self._values["artifactory_efs_mount_target2"] = artifactory_efs_mount_target2
        if artifactory_s3_bucket is not None:
            self._values["artifactory_s3_bucket"] = artifactory_s3_bucket
        if artifactory_s3_iam_policy is not None:
            self._values["artifactory_s3_iam_policy"] = artifactory_s3_iam_policy

    @builtins.property
    def artifactory_database(
        self,
    ) -> typing.Optional["CfnCoreModulePropsResourcesArtifactoryDatabase"]:
        '''
        :schema: CfnCoreModulePropsResources#ArtifactoryDatabase
        '''
        result = self._values.get("artifactory_database")
        return typing.cast(typing.Optional["CfnCoreModulePropsResourcesArtifactoryDatabase"], result)

    @builtins.property
    def artifactory_database_sg(
        self,
    ) -> typing.Optional["CfnCoreModulePropsResourcesArtifactoryDatabaseSg"]:
        '''
        :schema: CfnCoreModulePropsResources#ArtifactoryDatabaseSG
        '''
        result = self._values.get("artifactory_database_sg")
        return typing.cast(typing.Optional["CfnCoreModulePropsResourcesArtifactoryDatabaseSg"], result)

    @builtins.property
    def artifactory_database_subnet_group(
        self,
    ) -> typing.Optional["CfnCoreModulePropsResourcesArtifactoryDatabaseSubnetGroup"]:
        '''
        :schema: CfnCoreModulePropsResources#ArtifactoryDatabaseSubnetGroup
        '''
        result = self._values.get("artifactory_database_subnet_group")
        return typing.cast(typing.Optional["CfnCoreModulePropsResourcesArtifactoryDatabaseSubnetGroup"], result)

    @builtins.property
    def artifactory_efs_file_system(
        self,
    ) -> typing.Optional["CfnCoreModulePropsResourcesArtifactoryEfsFileSystem"]:
        '''
        :schema: CfnCoreModulePropsResources#ArtifactoryEfsFileSystem
        '''
        result = self._values.get("artifactory_efs_file_system")
        return typing.cast(typing.Optional["CfnCoreModulePropsResourcesArtifactoryEfsFileSystem"], result)

    @builtins.property
    def artifactory_efs_mount_target1(
        self,
    ) -> typing.Optional["CfnCoreModulePropsResourcesArtifactoryEfsMountTarget1"]:
        '''
        :schema: CfnCoreModulePropsResources#ArtifactoryEfsMountTarget1
        '''
        result = self._values.get("artifactory_efs_mount_target1")
        return typing.cast(typing.Optional["CfnCoreModulePropsResourcesArtifactoryEfsMountTarget1"], result)

    @builtins.property
    def artifactory_efs_mount_target2(
        self,
    ) -> typing.Optional["CfnCoreModulePropsResourcesArtifactoryEfsMountTarget2"]:
        '''
        :schema: CfnCoreModulePropsResources#ArtifactoryEfsMountTarget2
        '''
        result = self._values.get("artifactory_efs_mount_target2")
        return typing.cast(typing.Optional["CfnCoreModulePropsResourcesArtifactoryEfsMountTarget2"], result)

    @builtins.property
    def artifactory_s3_bucket(
        self,
    ) -> typing.Optional["CfnCoreModulePropsResourcesArtifactoryS3Bucket"]:
        '''
        :schema: CfnCoreModulePropsResources#ArtifactoryS3Bucket
        '''
        result = self._values.get("artifactory_s3_bucket")
        return typing.cast(typing.Optional["CfnCoreModulePropsResourcesArtifactoryS3Bucket"], result)

    @builtins.property
    def artifactory_s3_iam_policy(
        self,
    ) -> typing.Optional["CfnCoreModulePropsResourcesArtifactoryS3IamPolicy"]:
        '''
        :schema: CfnCoreModulePropsResources#ArtifactoryS3IAMPolicy
        '''
        result = self._values.get("artifactory_s3_iam_policy")
        return typing.cast(typing.Optional["CfnCoreModulePropsResourcesArtifactoryS3IamPolicy"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCoreModulePropsResources(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-core-module.CfnCoreModulePropsResourcesArtifactoryDatabase",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnCoreModulePropsResourcesArtifactoryDatabase:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnCoreModulePropsResourcesArtifactoryDatabase
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnCoreModulePropsResourcesArtifactoryDatabase#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnCoreModulePropsResourcesArtifactoryDatabase#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCoreModulePropsResourcesArtifactoryDatabase(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-core-module.CfnCoreModulePropsResourcesArtifactoryDatabaseSg",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnCoreModulePropsResourcesArtifactoryDatabaseSg:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnCoreModulePropsResourcesArtifactoryDatabaseSg
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnCoreModulePropsResourcesArtifactoryDatabaseSg#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnCoreModulePropsResourcesArtifactoryDatabaseSg#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCoreModulePropsResourcesArtifactoryDatabaseSg(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-core-module.CfnCoreModulePropsResourcesArtifactoryDatabaseSubnetGroup",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnCoreModulePropsResourcesArtifactoryDatabaseSubnetGroup:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnCoreModulePropsResourcesArtifactoryDatabaseSubnetGroup
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnCoreModulePropsResourcesArtifactoryDatabaseSubnetGroup#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnCoreModulePropsResourcesArtifactoryDatabaseSubnetGroup#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCoreModulePropsResourcesArtifactoryDatabaseSubnetGroup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-core-module.CfnCoreModulePropsResourcesArtifactoryEfsFileSystem",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnCoreModulePropsResourcesArtifactoryEfsFileSystem:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnCoreModulePropsResourcesArtifactoryEfsFileSystem
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnCoreModulePropsResourcesArtifactoryEfsFileSystem#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnCoreModulePropsResourcesArtifactoryEfsFileSystem#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCoreModulePropsResourcesArtifactoryEfsFileSystem(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-core-module.CfnCoreModulePropsResourcesArtifactoryEfsMountTarget1",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnCoreModulePropsResourcesArtifactoryEfsMountTarget1:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnCoreModulePropsResourcesArtifactoryEfsMountTarget1
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnCoreModulePropsResourcesArtifactoryEfsMountTarget1#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnCoreModulePropsResourcesArtifactoryEfsMountTarget1#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCoreModulePropsResourcesArtifactoryEfsMountTarget1(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-core-module.CfnCoreModulePropsResourcesArtifactoryEfsMountTarget2",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnCoreModulePropsResourcesArtifactoryEfsMountTarget2:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnCoreModulePropsResourcesArtifactoryEfsMountTarget2
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnCoreModulePropsResourcesArtifactoryEfsMountTarget2#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnCoreModulePropsResourcesArtifactoryEfsMountTarget2#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCoreModulePropsResourcesArtifactoryEfsMountTarget2(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-core-module.CfnCoreModulePropsResourcesArtifactoryS3Bucket",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnCoreModulePropsResourcesArtifactoryS3Bucket:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnCoreModulePropsResourcesArtifactoryS3Bucket
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnCoreModulePropsResourcesArtifactoryS3Bucket#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnCoreModulePropsResourcesArtifactoryS3Bucket#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCoreModulePropsResourcesArtifactoryS3Bucket(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-core-module.CfnCoreModulePropsResourcesArtifactoryS3IamPolicy",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnCoreModulePropsResourcesArtifactoryS3IamPolicy:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnCoreModulePropsResourcesArtifactoryS3IamPolicy
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnCoreModulePropsResourcesArtifactoryS3IamPolicy#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnCoreModulePropsResourcesArtifactoryS3IamPolicy#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCoreModulePropsResourcesArtifactoryS3IamPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnCoreModule",
    "CfnCoreModuleProps",
    "CfnCoreModulePropsParameters",
    "CfnCoreModulePropsParametersArtifactoryHostRole",
    "CfnCoreModulePropsParametersArtifactoryProduct",
    "CfnCoreModulePropsParametersAvailabilityZone1",
    "CfnCoreModulePropsParametersAvailabilityZone2",
    "CfnCoreModulePropsParametersDatabaseAllocatedStorage",
    "CfnCoreModulePropsParametersDatabaseEngine",
    "CfnCoreModulePropsParametersDatabaseInstance",
    "CfnCoreModulePropsParametersDatabaseName",
    "CfnCoreModulePropsParametersDatabasePassword",
    "CfnCoreModulePropsParametersDatabasePreferredAz",
    "CfnCoreModulePropsParametersDatabaseUser",
    "CfnCoreModulePropsParametersEfsSecurityGroup",
    "CfnCoreModulePropsParametersInstanceType",
    "CfnCoreModulePropsParametersMultiAzDatabase",
    "CfnCoreModulePropsParametersPrivateSubnet1Cidr",
    "CfnCoreModulePropsParametersPrivateSubnet1Id",
    "CfnCoreModulePropsParametersPrivateSubnet2Cidr",
    "CfnCoreModulePropsParametersPrivateSubnet2Id",
    "CfnCoreModulePropsParametersPrivateSubnet3Cidr",
    "CfnCoreModulePropsParametersReleaseStage",
    "CfnCoreModulePropsParametersVpcCidr",
    "CfnCoreModulePropsParametersVpcId",
    "CfnCoreModulePropsResources",
    "CfnCoreModulePropsResourcesArtifactoryDatabase",
    "CfnCoreModulePropsResourcesArtifactoryDatabaseSg",
    "CfnCoreModulePropsResourcesArtifactoryDatabaseSubnetGroup",
    "CfnCoreModulePropsResourcesArtifactoryEfsFileSystem",
    "CfnCoreModulePropsResourcesArtifactoryEfsMountTarget1",
    "CfnCoreModulePropsResourcesArtifactoryEfsMountTarget2",
    "CfnCoreModulePropsResourcesArtifactoryS3Bucket",
    "CfnCoreModulePropsResourcesArtifactoryS3IamPolicy",
]

publication.publish()
