'''
# AWS CDK CloudFormation Constructs for JFrog::Artifactory::Core::MODULE

Schema for Module Fragment of type JFrog::Artifactory::Core::MODULE

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
    jsii_type="@cdk-cloudformation/jfrog-artifactory-core-module.CfnModule",
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
        parameters: typing.Optional["CfnModulePropsParameters"] = None,
        resources: typing.Optional["CfnModulePropsResources"] = None,
    ) -> None:
        '''Create a new ``JFrog::Artifactory::Core::MODULE``.

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
    jsii_type="@cdk-cloudformation/jfrog-artifactory-core-module.CfnModuleProps",
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
        '''Schema for Module Fragment of type JFrog::Artifactory::Core::MODULE.

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
    jsii_type="@cdk-cloudformation/jfrog-artifactory-core-module.CfnModulePropsParameters",
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
class CfnModulePropsParameters:
    def __init__(
        self,
        *,
        artifactory_host_role: typing.Optional["CfnModulePropsParametersArtifactoryHostRole"] = None,
        artifactory_product: typing.Optional["CfnModulePropsParametersArtifactoryProduct"] = None,
        availability_zone1: typing.Optional["CfnModulePropsParametersAvailabilityZone1"] = None,
        availability_zone2: typing.Optional["CfnModulePropsParametersAvailabilityZone2"] = None,
        database_allocated_storage: typing.Optional["CfnModulePropsParametersDatabaseAllocatedStorage"] = None,
        database_engine: typing.Optional["CfnModulePropsParametersDatabaseEngine"] = None,
        database_instance: typing.Optional["CfnModulePropsParametersDatabaseInstance"] = None,
        database_name: typing.Optional["CfnModulePropsParametersDatabaseName"] = None,
        database_password: typing.Optional["CfnModulePropsParametersDatabasePassword"] = None,
        database_preferred_az: typing.Optional["CfnModulePropsParametersDatabasePreferredAz"] = None,
        database_user: typing.Optional["CfnModulePropsParametersDatabaseUser"] = None,
        efs_security_group: typing.Optional["CfnModulePropsParametersEfsSecurityGroup"] = None,
        instance_type: typing.Optional["CfnModulePropsParametersInstanceType"] = None,
        multi_az_database: typing.Optional["CfnModulePropsParametersMultiAzDatabase"] = None,
        private_subnet1_cidr: typing.Optional["CfnModulePropsParametersPrivateSubnet1Cidr"] = None,
        private_subnet1_id: typing.Optional["CfnModulePropsParametersPrivateSubnet1Id"] = None,
        private_subnet2_cidr: typing.Optional["CfnModulePropsParametersPrivateSubnet2Cidr"] = None,
        private_subnet2_id: typing.Optional["CfnModulePropsParametersPrivateSubnet2Id"] = None,
        private_subnet3_cidr: typing.Optional["CfnModulePropsParametersPrivateSubnet3Cidr"] = None,
        release_stage: typing.Optional["CfnModulePropsParametersReleaseStage"] = None,
        vpc_cidr: typing.Optional["CfnModulePropsParametersVpcCidr"] = None,
        vpc_id: typing.Optional["CfnModulePropsParametersVpcId"] = None,
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

        :schema: CfnModulePropsParameters
        '''
        if isinstance(artifactory_host_role, dict):
            artifactory_host_role = CfnModulePropsParametersArtifactoryHostRole(**artifactory_host_role)
        if isinstance(artifactory_product, dict):
            artifactory_product = CfnModulePropsParametersArtifactoryProduct(**artifactory_product)
        if isinstance(availability_zone1, dict):
            availability_zone1 = CfnModulePropsParametersAvailabilityZone1(**availability_zone1)
        if isinstance(availability_zone2, dict):
            availability_zone2 = CfnModulePropsParametersAvailabilityZone2(**availability_zone2)
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
        if isinstance(efs_security_group, dict):
            efs_security_group = CfnModulePropsParametersEfsSecurityGroup(**efs_security_group)
        if isinstance(instance_type, dict):
            instance_type = CfnModulePropsParametersInstanceType(**instance_type)
        if isinstance(multi_az_database, dict):
            multi_az_database = CfnModulePropsParametersMultiAzDatabase(**multi_az_database)
        if isinstance(private_subnet1_cidr, dict):
            private_subnet1_cidr = CfnModulePropsParametersPrivateSubnet1Cidr(**private_subnet1_cidr)
        if isinstance(private_subnet1_id, dict):
            private_subnet1_id = CfnModulePropsParametersPrivateSubnet1Id(**private_subnet1_id)
        if isinstance(private_subnet2_cidr, dict):
            private_subnet2_cidr = CfnModulePropsParametersPrivateSubnet2Cidr(**private_subnet2_cidr)
        if isinstance(private_subnet2_id, dict):
            private_subnet2_id = CfnModulePropsParametersPrivateSubnet2Id(**private_subnet2_id)
        if isinstance(private_subnet3_cidr, dict):
            private_subnet3_cidr = CfnModulePropsParametersPrivateSubnet3Cidr(**private_subnet3_cidr)
        if isinstance(release_stage, dict):
            release_stage = CfnModulePropsParametersReleaseStage(**release_stage)
        if isinstance(vpc_cidr, dict):
            vpc_cidr = CfnModulePropsParametersVpcCidr(**vpc_cidr)
        if isinstance(vpc_id, dict):
            vpc_id = CfnModulePropsParametersVpcId(**vpc_id)
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
    ) -> typing.Optional["CfnModulePropsParametersArtifactoryHostRole"]:
        '''
        :schema: CfnModulePropsParameters#ArtifactoryHostRole
        '''
        result = self._values.get("artifactory_host_role")
        return typing.cast(typing.Optional["CfnModulePropsParametersArtifactoryHostRole"], result)

    @builtins.property
    def artifactory_product(
        self,
    ) -> typing.Optional["CfnModulePropsParametersArtifactoryProduct"]:
        '''
        :schema: CfnModulePropsParameters#ArtifactoryProduct
        '''
        result = self._values.get("artifactory_product")
        return typing.cast(typing.Optional["CfnModulePropsParametersArtifactoryProduct"], result)

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
    def database_allocated_storage(
        self,
    ) -> typing.Optional["CfnModulePropsParametersDatabaseAllocatedStorage"]:
        '''
        :schema: CfnModulePropsParameters#DatabaseAllocatedStorage
        '''
        result = self._values.get("database_allocated_storage")
        return typing.cast(typing.Optional["CfnModulePropsParametersDatabaseAllocatedStorage"], result)

    @builtins.property
    def database_engine(
        self,
    ) -> typing.Optional["CfnModulePropsParametersDatabaseEngine"]:
        '''
        :schema: CfnModulePropsParameters#DatabaseEngine
        '''
        result = self._values.get("database_engine")
        return typing.cast(typing.Optional["CfnModulePropsParametersDatabaseEngine"], result)

    @builtins.property
    def database_instance(
        self,
    ) -> typing.Optional["CfnModulePropsParametersDatabaseInstance"]:
        '''
        :schema: CfnModulePropsParameters#DatabaseInstance
        '''
        result = self._values.get("database_instance")
        return typing.cast(typing.Optional["CfnModulePropsParametersDatabaseInstance"], result)

    @builtins.property
    def database_name(self) -> typing.Optional["CfnModulePropsParametersDatabaseName"]:
        '''
        :schema: CfnModulePropsParameters#DatabaseName
        '''
        result = self._values.get("database_name")
        return typing.cast(typing.Optional["CfnModulePropsParametersDatabaseName"], result)

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
    def database_preferred_az(
        self,
    ) -> typing.Optional["CfnModulePropsParametersDatabasePreferredAz"]:
        '''
        :schema: CfnModulePropsParameters#DatabasePreferredAz
        '''
        result = self._values.get("database_preferred_az")
        return typing.cast(typing.Optional["CfnModulePropsParametersDatabasePreferredAz"], result)

    @builtins.property
    def database_user(self) -> typing.Optional["CfnModulePropsParametersDatabaseUser"]:
        '''
        :schema: CfnModulePropsParameters#DatabaseUser
        '''
        result = self._values.get("database_user")
        return typing.cast(typing.Optional["CfnModulePropsParametersDatabaseUser"], result)

    @builtins.property
    def efs_security_group(
        self,
    ) -> typing.Optional["CfnModulePropsParametersEfsSecurityGroup"]:
        '''
        :schema: CfnModulePropsParameters#EfsSecurityGroup
        '''
        result = self._values.get("efs_security_group")
        return typing.cast(typing.Optional["CfnModulePropsParametersEfsSecurityGroup"], result)

    @builtins.property
    def instance_type(self) -> typing.Optional["CfnModulePropsParametersInstanceType"]:
        '''
        :schema: CfnModulePropsParameters#InstanceType
        '''
        result = self._values.get("instance_type")
        return typing.cast(typing.Optional["CfnModulePropsParametersInstanceType"], result)

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
    def private_subnet1_cidr(
        self,
    ) -> typing.Optional["CfnModulePropsParametersPrivateSubnet1Cidr"]:
        '''
        :schema: CfnModulePropsParameters#PrivateSubnet1Cidr
        '''
        result = self._values.get("private_subnet1_cidr")
        return typing.cast(typing.Optional["CfnModulePropsParametersPrivateSubnet1Cidr"], result)

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
    def private_subnet2_cidr(
        self,
    ) -> typing.Optional["CfnModulePropsParametersPrivateSubnet2Cidr"]:
        '''
        :schema: CfnModulePropsParameters#PrivateSubnet2Cidr
        '''
        result = self._values.get("private_subnet2_cidr")
        return typing.cast(typing.Optional["CfnModulePropsParametersPrivateSubnet2Cidr"], result)

    @builtins.property
    def private_subnet2_id(
        self,
    ) -> typing.Optional["CfnModulePropsParametersPrivateSubnet2Id"]:
        '''ID of the private subnet in Availability Zone 1 of your existing VPC (e.g., subnet-z0376dab).

        :schema: CfnModulePropsParameters#PrivateSubnet2Id
        '''
        result = self._values.get("private_subnet2_id")
        return typing.cast(typing.Optional["CfnModulePropsParametersPrivateSubnet2Id"], result)

    @builtins.property
    def private_subnet3_cidr(
        self,
    ) -> typing.Optional["CfnModulePropsParametersPrivateSubnet3Cidr"]:
        '''
        :schema: CfnModulePropsParameters#PrivateSubnet3Cidr
        '''
        result = self._values.get("private_subnet3_cidr")
        return typing.cast(typing.Optional["CfnModulePropsParametersPrivateSubnet3Cidr"], result)

    @builtins.property
    def release_stage(self) -> typing.Optional["CfnModulePropsParametersReleaseStage"]:
        '''
        :schema: CfnModulePropsParameters#ReleaseStage
        '''
        result = self._values.get("release_stage")
        return typing.cast(typing.Optional["CfnModulePropsParametersReleaseStage"], result)

    @builtins.property
    def vpc_cidr(self) -> typing.Optional["CfnModulePropsParametersVpcCidr"]:
        '''CIDR block for the VPC.

        :schema: CfnModulePropsParameters#VpcCidr
        '''
        result = self._values.get("vpc_cidr")
        return typing.cast(typing.Optional["CfnModulePropsParametersVpcCidr"], result)

    @builtins.property
    def vpc_id(self) -> typing.Optional["CfnModulePropsParametersVpcId"]:
        '''
        :schema: CfnModulePropsParameters#VpcId
        '''
        result = self._values.get("vpc_id")
        return typing.cast(typing.Optional["CfnModulePropsParametersVpcId"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-core-module.CfnModulePropsParametersArtifactoryHostRole",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnModulePropsParametersArtifactoryHostRole:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnModulePropsParametersArtifactoryHostRole
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersArtifactoryHostRole#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersArtifactoryHostRole(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-core-module.CfnModulePropsParametersArtifactoryProduct",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnModulePropsParametersArtifactoryProduct:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnModulePropsParametersArtifactoryProduct
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

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
    jsii_type="@cdk-cloudformation/jfrog-artifactory-core-module.CfnModulePropsParametersAvailabilityZone1",
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
    jsii_type="@cdk-cloudformation/jfrog-artifactory-core-module.CfnModulePropsParametersAvailabilityZone2",
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
    jsii_type="@cdk-cloudformation/jfrog-artifactory-core-module.CfnModulePropsParametersDatabaseAllocatedStorage",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnModulePropsParametersDatabaseAllocatedStorage:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnModulePropsParametersDatabaseAllocatedStorage
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

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
    jsii_type="@cdk-cloudformation/jfrog-artifactory-core-module.CfnModulePropsParametersDatabaseEngine",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnModulePropsParametersDatabaseEngine:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnModulePropsParametersDatabaseEngine
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

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
    jsii_type="@cdk-cloudformation/jfrog-artifactory-core-module.CfnModulePropsParametersDatabaseInstance",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnModulePropsParametersDatabaseInstance:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnModulePropsParametersDatabaseInstance
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

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
    jsii_type="@cdk-cloudformation/jfrog-artifactory-core-module.CfnModulePropsParametersDatabaseName",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnModulePropsParametersDatabaseName:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnModulePropsParametersDatabaseName
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

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
    jsii_type="@cdk-cloudformation/jfrog-artifactory-core-module.CfnModulePropsParametersDatabasePassword",
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
    jsii_type="@cdk-cloudformation/jfrog-artifactory-core-module.CfnModulePropsParametersDatabasePreferredAz",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnModulePropsParametersDatabasePreferredAz:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnModulePropsParametersDatabasePreferredAz
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

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
    jsii_type="@cdk-cloudformation/jfrog-artifactory-core-module.CfnModulePropsParametersDatabaseUser",
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
    jsii_type="@cdk-cloudformation/jfrog-artifactory-core-module.CfnModulePropsParametersEfsSecurityGroup",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnModulePropsParametersEfsSecurityGroup:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnModulePropsParametersEfsSecurityGroup
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersEfsSecurityGroup#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersEfsSecurityGroup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-core-module.CfnModulePropsParametersInstanceType",
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
    jsii_type="@cdk-cloudformation/jfrog-artifactory-core-module.CfnModulePropsParametersMultiAzDatabase",
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
    jsii_type="@cdk-cloudformation/jfrog-artifactory-core-module.CfnModulePropsParametersPrivateSubnet1Cidr",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnModulePropsParametersPrivateSubnet1Cidr:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnModulePropsParametersPrivateSubnet1Cidr
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

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
    jsii_type="@cdk-cloudformation/jfrog-artifactory-core-module.CfnModulePropsParametersPrivateSubnet1Id",
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
    jsii_type="@cdk-cloudformation/jfrog-artifactory-core-module.CfnModulePropsParametersPrivateSubnet2Cidr",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnModulePropsParametersPrivateSubnet2Cidr:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnModulePropsParametersPrivateSubnet2Cidr
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

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
    jsii_type="@cdk-cloudformation/jfrog-artifactory-core-module.CfnModulePropsParametersPrivateSubnet2Id",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersPrivateSubnet2Id:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''ID of the private subnet in Availability Zone 1 of your existing VPC (e.g., subnet-z0376dab).

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
    jsii_type="@cdk-cloudformation/jfrog-artifactory-core-module.CfnModulePropsParametersPrivateSubnet3Cidr",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnModulePropsParametersPrivateSubnet3Cidr:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnModulePropsParametersPrivateSubnet3Cidr
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersPrivateSubnet3Cidr#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersPrivateSubnet3Cidr(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-core-module.CfnModulePropsParametersReleaseStage",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnModulePropsParametersReleaseStage:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnModulePropsParametersReleaseStage
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersReleaseStage#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersReleaseStage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-core-module.CfnModulePropsParametersVpcCidr",
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
    jsii_type="@cdk-cloudformation/jfrog-artifactory-core-module.CfnModulePropsParametersVpcId",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class CfnModulePropsParametersVpcId:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: 

        :schema: CfnModulePropsParametersVpcId
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersVpcId#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersVpcId(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-core-module.CfnModulePropsResources",
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
class CfnModulePropsResources:
    def __init__(
        self,
        *,
        artifactory_database: typing.Optional["CfnModulePropsResourcesArtifactoryDatabase"] = None,
        artifactory_database_sg: typing.Optional["CfnModulePropsResourcesArtifactoryDatabaseSg"] = None,
        artifactory_database_subnet_group: typing.Optional["CfnModulePropsResourcesArtifactoryDatabaseSubnetGroup"] = None,
        artifactory_efs_file_system: typing.Optional["CfnModulePropsResourcesArtifactoryEfsFileSystem"] = None,
        artifactory_efs_mount_target1: typing.Optional["CfnModulePropsResourcesArtifactoryEfsMountTarget1"] = None,
        artifactory_efs_mount_target2: typing.Optional["CfnModulePropsResourcesArtifactoryEfsMountTarget2"] = None,
        artifactory_s3_bucket: typing.Optional["CfnModulePropsResourcesArtifactoryS3Bucket"] = None,
        artifactory_s3_iam_policy: typing.Optional["CfnModulePropsResourcesArtifactoryS3IamPolicy"] = None,
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

        :schema: CfnModulePropsResources
        '''
        if isinstance(artifactory_database, dict):
            artifactory_database = CfnModulePropsResourcesArtifactoryDatabase(**artifactory_database)
        if isinstance(artifactory_database_sg, dict):
            artifactory_database_sg = CfnModulePropsResourcesArtifactoryDatabaseSg(**artifactory_database_sg)
        if isinstance(artifactory_database_subnet_group, dict):
            artifactory_database_subnet_group = CfnModulePropsResourcesArtifactoryDatabaseSubnetGroup(**artifactory_database_subnet_group)
        if isinstance(artifactory_efs_file_system, dict):
            artifactory_efs_file_system = CfnModulePropsResourcesArtifactoryEfsFileSystem(**artifactory_efs_file_system)
        if isinstance(artifactory_efs_mount_target1, dict):
            artifactory_efs_mount_target1 = CfnModulePropsResourcesArtifactoryEfsMountTarget1(**artifactory_efs_mount_target1)
        if isinstance(artifactory_efs_mount_target2, dict):
            artifactory_efs_mount_target2 = CfnModulePropsResourcesArtifactoryEfsMountTarget2(**artifactory_efs_mount_target2)
        if isinstance(artifactory_s3_bucket, dict):
            artifactory_s3_bucket = CfnModulePropsResourcesArtifactoryS3Bucket(**artifactory_s3_bucket)
        if isinstance(artifactory_s3_iam_policy, dict):
            artifactory_s3_iam_policy = CfnModulePropsResourcesArtifactoryS3IamPolicy(**artifactory_s3_iam_policy)
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
    ) -> typing.Optional["CfnModulePropsResourcesArtifactoryDatabase"]:
        '''
        :schema: CfnModulePropsResources#ArtifactoryDatabase
        '''
        result = self._values.get("artifactory_database")
        return typing.cast(typing.Optional["CfnModulePropsResourcesArtifactoryDatabase"], result)

    @builtins.property
    def artifactory_database_sg(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesArtifactoryDatabaseSg"]:
        '''
        :schema: CfnModulePropsResources#ArtifactoryDatabaseSG
        '''
        result = self._values.get("artifactory_database_sg")
        return typing.cast(typing.Optional["CfnModulePropsResourcesArtifactoryDatabaseSg"], result)

    @builtins.property
    def artifactory_database_subnet_group(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesArtifactoryDatabaseSubnetGroup"]:
        '''
        :schema: CfnModulePropsResources#ArtifactoryDatabaseSubnetGroup
        '''
        result = self._values.get("artifactory_database_subnet_group")
        return typing.cast(typing.Optional["CfnModulePropsResourcesArtifactoryDatabaseSubnetGroup"], result)

    @builtins.property
    def artifactory_efs_file_system(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesArtifactoryEfsFileSystem"]:
        '''
        :schema: CfnModulePropsResources#ArtifactoryEfsFileSystem
        '''
        result = self._values.get("artifactory_efs_file_system")
        return typing.cast(typing.Optional["CfnModulePropsResourcesArtifactoryEfsFileSystem"], result)

    @builtins.property
    def artifactory_efs_mount_target1(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesArtifactoryEfsMountTarget1"]:
        '''
        :schema: CfnModulePropsResources#ArtifactoryEfsMountTarget1
        '''
        result = self._values.get("artifactory_efs_mount_target1")
        return typing.cast(typing.Optional["CfnModulePropsResourcesArtifactoryEfsMountTarget1"], result)

    @builtins.property
    def artifactory_efs_mount_target2(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesArtifactoryEfsMountTarget2"]:
        '''
        :schema: CfnModulePropsResources#ArtifactoryEfsMountTarget2
        '''
        result = self._values.get("artifactory_efs_mount_target2")
        return typing.cast(typing.Optional["CfnModulePropsResourcesArtifactoryEfsMountTarget2"], result)

    @builtins.property
    def artifactory_s3_bucket(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesArtifactoryS3Bucket"]:
        '''
        :schema: CfnModulePropsResources#ArtifactoryS3Bucket
        '''
        result = self._values.get("artifactory_s3_bucket")
        return typing.cast(typing.Optional["CfnModulePropsResourcesArtifactoryS3Bucket"], result)

    @builtins.property
    def artifactory_s3_iam_policy(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesArtifactoryS3IamPolicy"]:
        '''
        :schema: CfnModulePropsResources#ArtifactoryS3IAMPolicy
        '''
        result = self._values.get("artifactory_s3_iam_policy")
        return typing.cast(typing.Optional["CfnModulePropsResourcesArtifactoryS3IamPolicy"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResources(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-core-module.CfnModulePropsResourcesArtifactoryDatabase",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesArtifactoryDatabase:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesArtifactoryDatabase
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesArtifactoryDatabase#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesArtifactoryDatabase#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesArtifactoryDatabase(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-core-module.CfnModulePropsResourcesArtifactoryDatabaseSg",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesArtifactoryDatabaseSg:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesArtifactoryDatabaseSg
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesArtifactoryDatabaseSg#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesArtifactoryDatabaseSg#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesArtifactoryDatabaseSg(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-core-module.CfnModulePropsResourcesArtifactoryDatabaseSubnetGroup",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesArtifactoryDatabaseSubnetGroup:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesArtifactoryDatabaseSubnetGroup
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesArtifactoryDatabaseSubnetGroup#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesArtifactoryDatabaseSubnetGroup#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesArtifactoryDatabaseSubnetGroup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-core-module.CfnModulePropsResourcesArtifactoryEfsFileSystem",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesArtifactoryEfsFileSystem:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesArtifactoryEfsFileSystem
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesArtifactoryEfsFileSystem#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesArtifactoryEfsFileSystem#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesArtifactoryEfsFileSystem(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-core-module.CfnModulePropsResourcesArtifactoryEfsMountTarget1",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesArtifactoryEfsMountTarget1:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesArtifactoryEfsMountTarget1
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesArtifactoryEfsMountTarget1#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesArtifactoryEfsMountTarget1#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesArtifactoryEfsMountTarget1(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-core-module.CfnModulePropsResourcesArtifactoryEfsMountTarget2",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesArtifactoryEfsMountTarget2:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesArtifactoryEfsMountTarget2
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesArtifactoryEfsMountTarget2#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesArtifactoryEfsMountTarget2#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesArtifactoryEfsMountTarget2(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-core-module.CfnModulePropsResourcesArtifactoryS3Bucket",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesArtifactoryS3Bucket:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesArtifactoryS3Bucket
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesArtifactoryS3Bucket#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesArtifactoryS3Bucket#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesArtifactoryS3Bucket(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/jfrog-artifactory-core-module.CfnModulePropsResourcesArtifactoryS3IamPolicy",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesArtifactoryS3IamPolicy:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesArtifactoryS3IamPolicy
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesArtifactoryS3IamPolicy#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesArtifactoryS3IamPolicy#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesArtifactoryS3IamPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnModule",
    "CfnModuleProps",
    "CfnModulePropsParameters",
    "CfnModulePropsParametersArtifactoryHostRole",
    "CfnModulePropsParametersArtifactoryProduct",
    "CfnModulePropsParametersAvailabilityZone1",
    "CfnModulePropsParametersAvailabilityZone2",
    "CfnModulePropsParametersDatabaseAllocatedStorage",
    "CfnModulePropsParametersDatabaseEngine",
    "CfnModulePropsParametersDatabaseInstance",
    "CfnModulePropsParametersDatabaseName",
    "CfnModulePropsParametersDatabasePassword",
    "CfnModulePropsParametersDatabasePreferredAz",
    "CfnModulePropsParametersDatabaseUser",
    "CfnModulePropsParametersEfsSecurityGroup",
    "CfnModulePropsParametersInstanceType",
    "CfnModulePropsParametersMultiAzDatabase",
    "CfnModulePropsParametersPrivateSubnet1Cidr",
    "CfnModulePropsParametersPrivateSubnet1Id",
    "CfnModulePropsParametersPrivateSubnet2Cidr",
    "CfnModulePropsParametersPrivateSubnet2Id",
    "CfnModulePropsParametersPrivateSubnet3Cidr",
    "CfnModulePropsParametersReleaseStage",
    "CfnModulePropsParametersVpcCidr",
    "CfnModulePropsParametersVpcId",
    "CfnModulePropsResources",
    "CfnModulePropsResourcesArtifactoryDatabase",
    "CfnModulePropsResourcesArtifactoryDatabaseSg",
    "CfnModulePropsResourcesArtifactoryDatabaseSubnetGroup",
    "CfnModulePropsResourcesArtifactoryEfsFileSystem",
    "CfnModulePropsResourcesArtifactoryEfsMountTarget1",
    "CfnModulePropsResourcesArtifactoryEfsMountTarget2",
    "CfnModulePropsResourcesArtifactoryS3Bucket",
    "CfnModulePropsResourcesArtifactoryS3IamPolicy",
]

publication.publish()
