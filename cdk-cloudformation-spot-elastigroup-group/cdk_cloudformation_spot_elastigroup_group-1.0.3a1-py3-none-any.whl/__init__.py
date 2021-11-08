'''
# AWS CDK CloudFormation Constructs for Spot::Elastigroup::Group

The Spot Elastigroup Resource allows you to create, update, manage, and delete Spot Elastigroups easily with CloudFormation

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


@jsii.data_type(
    jsii_type="@cdk-cloudformation/spot-elastigroup-group.Attribute",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "value": "value"},
)
class Attribute:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param key: 
        :param value: 

        :schema: Attribute
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if key is not None:
            self._values["key"] = key
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''
        :schema: Attribute#key
        '''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''
        :schema: Attribute#value
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Attribute(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/spot-elastigroup-group.BlockDeviceMapping",
    jsii_struct_bases=[],
    name_mapping={
        "device_name": "deviceName",
        "ebs": "ebs",
        "no_device": "noDevice",
        "virtual_name": "virtualName",
    },
)
class BlockDeviceMapping:
    def __init__(
        self,
        *,
        device_name: typing.Optional[builtins.str] = None,
        ebs: typing.Optional["BlockDeviceMappingEbs"] = None,
        no_device: typing.Optional[builtins.str] = None,
        virtual_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param device_name: 
        :param ebs: 
        :param no_device: 
        :param virtual_name: 

        :schema: BlockDeviceMapping
        '''
        if isinstance(ebs, dict):
            ebs = BlockDeviceMappingEbs(**ebs)
        self._values: typing.Dict[str, typing.Any] = {}
        if device_name is not None:
            self._values["device_name"] = device_name
        if ebs is not None:
            self._values["ebs"] = ebs
        if no_device is not None:
            self._values["no_device"] = no_device
        if virtual_name is not None:
            self._values["virtual_name"] = virtual_name

    @builtins.property
    def device_name(self) -> typing.Optional[builtins.str]:
        '''
        :schema: BlockDeviceMapping#deviceName
        '''
        result = self._values.get("device_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ebs(self) -> typing.Optional["BlockDeviceMappingEbs"]:
        '''
        :schema: BlockDeviceMapping#ebs
        '''
        result = self._values.get("ebs")
        return typing.cast(typing.Optional["BlockDeviceMappingEbs"], result)

    @builtins.property
    def no_device(self) -> typing.Optional[builtins.str]:
        '''
        :schema: BlockDeviceMapping#noDevice
        '''
        result = self._values.get("no_device")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def virtual_name(self) -> typing.Optional[builtins.str]:
        '''
        :schema: BlockDeviceMapping#virtualName
        '''
        result = self._values.get("virtual_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BlockDeviceMapping(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/spot-elastigroup-group.BlockDeviceMappingEbs",
    jsii_struct_bases=[],
    name_mapping={
        "delete_on_termination": "deleteOnTermination",
        "encrypted": "encrypted",
        "iops": "iops",
        "snapshot_id": "snapshotId",
        "volume_size": "volumeSize",
        "volume_type": "volumeType",
    },
)
class BlockDeviceMappingEbs:
    def __init__(
        self,
        *,
        delete_on_termination: typing.Optional[builtins.bool] = None,
        encrypted: typing.Optional[builtins.bool] = None,
        iops: typing.Optional[jsii.Number] = None,
        snapshot_id: typing.Optional[builtins.str] = None,
        volume_size: typing.Optional[jsii.Number] = None,
        volume_type: typing.Optional["BlockDeviceMappingEbsVolumeType"] = None,
    ) -> None:
        '''
        :param delete_on_termination: 
        :param encrypted: 
        :param iops: 
        :param snapshot_id: 
        :param volume_size: 
        :param volume_type: 

        :schema: BlockDeviceMappingEbs
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if delete_on_termination is not None:
            self._values["delete_on_termination"] = delete_on_termination
        if encrypted is not None:
            self._values["encrypted"] = encrypted
        if iops is not None:
            self._values["iops"] = iops
        if snapshot_id is not None:
            self._values["snapshot_id"] = snapshot_id
        if volume_size is not None:
            self._values["volume_size"] = volume_size
        if volume_type is not None:
            self._values["volume_type"] = volume_type

    @builtins.property
    def delete_on_termination(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: BlockDeviceMappingEbs#deleteOnTermination
        '''
        result = self._values.get("delete_on_termination")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def encrypted(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: BlockDeviceMappingEbs#encrypted
        '''
        result = self._values.get("encrypted")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def iops(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: BlockDeviceMappingEbs#iops
        '''
        result = self._values.get("iops")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def snapshot_id(self) -> typing.Optional[builtins.str]:
        '''
        :schema: BlockDeviceMappingEbs#snapshotId
        '''
        result = self._values.get("snapshot_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def volume_size(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: BlockDeviceMappingEbs#volumeSize
        '''
        result = self._values.get("volume_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def volume_type(self) -> typing.Optional["BlockDeviceMappingEbsVolumeType"]:
        '''
        :schema: BlockDeviceMappingEbs#volumeType
        '''
        result = self._values.get("volume_type")
        return typing.cast(typing.Optional["BlockDeviceMappingEbsVolumeType"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BlockDeviceMappingEbs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(
    jsii_type="@cdk-cloudformation/spot-elastigroup-group.BlockDeviceMappingEbsVolumeType"
)
class BlockDeviceMappingEbsVolumeType(enum.Enum):
    '''
    :schema: BlockDeviceMappingEbsVolumeType
    '''

    STANDARD = "STANDARD"
    '''standard.'''
    IO1 = "IO1"
    '''io1.'''
    GP2 = "GP2"
    '''gp2.'''


class CfnGroup(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/spot-elastigroup-group.CfnGroup",
):
    '''A CloudFormation ``Spot::Elastigroup::Group``.

    :cloudformationResource: Spot::Elastigroup::Group
    :link: http://unknown-url
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        credentials: "CfnGroupPropsCredentials",
        group: typing.Optional["CfnGroupPropsGroup"] = None,
    ) -> None:
        '''Create a new ``Spot::Elastigroup::Group``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param credentials: 
        :param group: 
        '''
        props = CfnGroupProps(credentials=credentials, group=group)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnGroupProps":
        '''Resource props.'''
        return typing.cast("CfnGroupProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/spot-elastigroup-group.CfnGroupProps",
    jsii_struct_bases=[],
    name_mapping={"credentials": "credentials", "group": "group"},
)
class CfnGroupProps:
    def __init__(
        self,
        *,
        credentials: "CfnGroupPropsCredentials",
        group: typing.Optional["CfnGroupPropsGroup"] = None,
    ) -> None:
        '''The Spot Elastigroup Resource allows you to create, update, manage, and delete Spot Elastigroups easily with CloudFormation.

        :param credentials: 
        :param group: 

        :schema: CfnGroupProps
        '''
        if isinstance(credentials, dict):
            credentials = CfnGroupPropsCredentials(**credentials)
        if isinstance(group, dict):
            group = CfnGroupPropsGroup(**group)
        self._values: typing.Dict[str, typing.Any] = {
            "credentials": credentials,
        }
        if group is not None:
            self._values["group"] = group

    @builtins.property
    def credentials(self) -> "CfnGroupPropsCredentials":
        '''
        :schema: CfnGroupProps#credentials
        '''
        result = self._values.get("credentials")
        assert result is not None, "Required property 'credentials' is missing"
        return typing.cast("CfnGroupPropsCredentials", result)

    @builtins.property
    def group(self) -> typing.Optional["CfnGroupPropsGroup"]:
        '''
        :schema: CfnGroupProps#group
        '''
        result = self._values.get("group")
        return typing.cast(typing.Optional["CfnGroupPropsGroup"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/spot-elastigroup-group.CfnGroupPropsCredentials",
    jsii_struct_bases=[],
    name_mapping={"access_token": "accessToken", "account_id": "accountId"},
)
class CfnGroupPropsCredentials:
    def __init__(
        self,
        *,
        access_token: typing.Optional[builtins.str] = None,
        account_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param access_token: 
        :param account_id: 

        :schema: CfnGroupPropsCredentials
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if access_token is not None:
            self._values["access_token"] = access_token
        if account_id is not None:
            self._values["account_id"] = account_id

    @builtins.property
    def access_token(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnGroupPropsCredentials#accessToken
        '''
        result = self._values.get("access_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def account_id(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnGroupPropsCredentials#accountId
        '''
        result = self._values.get("account_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnGroupPropsCredentials(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/spot-elastigroup-group.CfnGroupPropsGroup",
    jsii_struct_bases=[],
    name_mapping={
        "capacity": "capacity",
        "compute": "compute",
        "description": "description",
        "group_id": "groupId",
        "name": "name",
        "region": "region",
        "scaling": "scaling",
        "scheduling": "scheduling",
        "strategy": "strategy",
        "third_parties_integration": "thirdPartiesIntegration",
    },
)
class CfnGroupPropsGroup:
    def __init__(
        self,
        *,
        capacity: typing.Optional["CfnGroupPropsGroupCapacity"] = None,
        compute: typing.Optional["CfnGroupPropsGroupCompute"] = None,
        description: typing.Optional[builtins.str] = None,
        group_id: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        scaling: typing.Optional["CfnGroupPropsGroupScaling"] = None,
        scheduling: typing.Optional["CfnGroupPropsGroupScheduling"] = None,
        strategy: typing.Optional["CfnGroupPropsGroupStrategy"] = None,
        third_parties_integration: typing.Optional["CfnGroupPropsGroupThirdPartiesIntegration"] = None,
    ) -> None:
        '''
        :param capacity: 
        :param compute: 
        :param description: The description of the elastigroup.
        :param group_id: 
        :param name: The name of the elastigroup.
        :param region: 
        :param scaling: 
        :param scheduling: 
        :param strategy: 
        :param third_parties_integration: 

        :schema: CfnGroupPropsGroup
        '''
        if isinstance(capacity, dict):
            capacity = CfnGroupPropsGroupCapacity(**capacity)
        if isinstance(compute, dict):
            compute = CfnGroupPropsGroupCompute(**compute)
        if isinstance(scaling, dict):
            scaling = CfnGroupPropsGroupScaling(**scaling)
        if isinstance(scheduling, dict):
            scheduling = CfnGroupPropsGroupScheduling(**scheduling)
        if isinstance(strategy, dict):
            strategy = CfnGroupPropsGroupStrategy(**strategy)
        if isinstance(third_parties_integration, dict):
            third_parties_integration = CfnGroupPropsGroupThirdPartiesIntegration(**third_parties_integration)
        self._values: typing.Dict[str, typing.Any] = {}
        if capacity is not None:
            self._values["capacity"] = capacity
        if compute is not None:
            self._values["compute"] = compute
        if description is not None:
            self._values["description"] = description
        if group_id is not None:
            self._values["group_id"] = group_id
        if name is not None:
            self._values["name"] = name
        if region is not None:
            self._values["region"] = region
        if scaling is not None:
            self._values["scaling"] = scaling
        if scheduling is not None:
            self._values["scheduling"] = scheduling
        if strategy is not None:
            self._values["strategy"] = strategy
        if third_parties_integration is not None:
            self._values["third_parties_integration"] = third_parties_integration

    @builtins.property
    def capacity(self) -> typing.Optional["CfnGroupPropsGroupCapacity"]:
        '''
        :schema: CfnGroupPropsGroup#capacity
        '''
        result = self._values.get("capacity")
        return typing.cast(typing.Optional["CfnGroupPropsGroupCapacity"], result)

    @builtins.property
    def compute(self) -> typing.Optional["CfnGroupPropsGroupCompute"]:
        '''
        :schema: CfnGroupPropsGroup#compute
        '''
        result = self._values.get("compute")
        return typing.cast(typing.Optional["CfnGroupPropsGroupCompute"], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the elastigroup.

        :schema: CfnGroupPropsGroup#description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def group_id(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnGroupPropsGroup#groupId
        '''
        result = self._values.get("group_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the elastigroup.

        :schema: CfnGroupPropsGroup#name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnGroupPropsGroup#region
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scaling(self) -> typing.Optional["CfnGroupPropsGroupScaling"]:
        '''
        :schema: CfnGroupPropsGroup#scaling
        '''
        result = self._values.get("scaling")
        return typing.cast(typing.Optional["CfnGroupPropsGroupScaling"], result)

    @builtins.property
    def scheduling(self) -> typing.Optional["CfnGroupPropsGroupScheduling"]:
        '''
        :schema: CfnGroupPropsGroup#scheduling
        '''
        result = self._values.get("scheduling")
        return typing.cast(typing.Optional["CfnGroupPropsGroupScheduling"], result)

    @builtins.property
    def strategy(self) -> typing.Optional["CfnGroupPropsGroupStrategy"]:
        '''
        :schema: CfnGroupPropsGroup#strategy
        '''
        result = self._values.get("strategy")
        return typing.cast(typing.Optional["CfnGroupPropsGroupStrategy"], result)

    @builtins.property
    def third_parties_integration(
        self,
    ) -> typing.Optional["CfnGroupPropsGroupThirdPartiesIntegration"]:
        '''
        :schema: CfnGroupPropsGroup#thirdPartiesIntegration
        '''
        result = self._values.get("third_parties_integration")
        return typing.cast(typing.Optional["CfnGroupPropsGroupThirdPartiesIntegration"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnGroupPropsGroup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/spot-elastigroup-group.CfnGroupPropsGroupCapacity",
    jsii_struct_bases=[],
    name_mapping={
        "maximum": "maximum",
        "minimum": "minimum",
        "target": "target",
        "unit": "unit",
    },
)
class CfnGroupPropsGroupCapacity:
    def __init__(
        self,
        *,
        maximum: typing.Optional[jsii.Number] = None,
        minimum: typing.Optional[jsii.Number] = None,
        target: typing.Optional[jsii.Number] = None,
        unit: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param maximum: 
        :param minimum: 
        :param target: 
        :param unit: 

        :schema: CfnGroupPropsGroupCapacity
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if maximum is not None:
            self._values["maximum"] = maximum
        if minimum is not None:
            self._values["minimum"] = minimum
        if target is not None:
            self._values["target"] = target
        if unit is not None:
            self._values["unit"] = unit

    @builtins.property
    def maximum(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: CfnGroupPropsGroupCapacity#maximum
        '''
        result = self._values.get("maximum")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def minimum(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: CfnGroupPropsGroupCapacity#minimum
        '''
        result = self._values.get("minimum")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def target(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: CfnGroupPropsGroupCapacity#target
        '''
        result = self._values.get("target")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def unit(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnGroupPropsGroupCapacity#unit
        '''
        result = self._values.get("unit")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnGroupPropsGroupCapacity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/spot-elastigroup-group.CfnGroupPropsGroupCompute",
    jsii_struct_bases=[],
    name_mapping={
        "availability_zones": "availabilityZones",
        "instance_types": "instanceTypes",
        "launch_specification": "launchSpecification",
        "product": "product",
    },
)
class CfnGroupPropsGroupCompute:
    def __init__(
        self,
        *,
        availability_zones: typing.Optional[typing.Sequence["CfnGroupPropsGroupComputeAvailabilityZones"]] = None,
        instance_types: typing.Optional["CfnGroupPropsGroupComputeInstanceTypes"] = None,
        launch_specification: typing.Optional["CfnGroupPropsGroupComputeLaunchSpecification"] = None,
        product: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param availability_zones: 
        :param instance_types: 
        :param launch_specification: 
        :param product: 

        :schema: CfnGroupPropsGroupCompute
        '''
        if isinstance(instance_types, dict):
            instance_types = CfnGroupPropsGroupComputeInstanceTypes(**instance_types)
        if isinstance(launch_specification, dict):
            launch_specification = CfnGroupPropsGroupComputeLaunchSpecification(**launch_specification)
        self._values: typing.Dict[str, typing.Any] = {}
        if availability_zones is not None:
            self._values["availability_zones"] = availability_zones
        if instance_types is not None:
            self._values["instance_types"] = instance_types
        if launch_specification is not None:
            self._values["launch_specification"] = launch_specification
        if product is not None:
            self._values["product"] = product

    @builtins.property
    def availability_zones(
        self,
    ) -> typing.Optional[typing.List["CfnGroupPropsGroupComputeAvailabilityZones"]]:
        '''
        :schema: CfnGroupPropsGroupCompute#availabilityZones
        '''
        result = self._values.get("availability_zones")
        return typing.cast(typing.Optional[typing.List["CfnGroupPropsGroupComputeAvailabilityZones"]], result)

    @builtins.property
    def instance_types(
        self,
    ) -> typing.Optional["CfnGroupPropsGroupComputeInstanceTypes"]:
        '''
        :schema: CfnGroupPropsGroupCompute#instanceTypes
        '''
        result = self._values.get("instance_types")
        return typing.cast(typing.Optional["CfnGroupPropsGroupComputeInstanceTypes"], result)

    @builtins.property
    def launch_specification(
        self,
    ) -> typing.Optional["CfnGroupPropsGroupComputeLaunchSpecification"]:
        '''
        :schema: CfnGroupPropsGroupCompute#launchSpecification
        '''
        result = self._values.get("launch_specification")
        return typing.cast(typing.Optional["CfnGroupPropsGroupComputeLaunchSpecification"], result)

    @builtins.property
    def product(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnGroupPropsGroupCompute#product
        '''
        result = self._values.get("product")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnGroupPropsGroupCompute(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/spot-elastigroup-group.CfnGroupPropsGroupComputeAvailabilityZones",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "subnet_ids": "subnetIds"},
)
class CfnGroupPropsGroupComputeAvailabilityZones:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param name: 
        :param subnet_ids: 

        :schema: CfnGroupPropsGroupComputeAvailabilityZones
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if subnet_ids is not None:
            self._values["subnet_ids"] = subnet_ids

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnGroupPropsGroupComputeAvailabilityZones#name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subnet_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''
        :schema: CfnGroupPropsGroupComputeAvailabilityZones#subnetIds
        '''
        result = self._values.get("subnet_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnGroupPropsGroupComputeAvailabilityZones(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/spot-elastigroup-group.CfnGroupPropsGroupComputeInstanceTypes",
    jsii_struct_bases=[],
    name_mapping={"on_demand": "onDemand", "spot": "spot"},
)
class CfnGroupPropsGroupComputeInstanceTypes:
    def __init__(
        self,
        *,
        on_demand: typing.Optional[builtins.str] = None,
        spot: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param on_demand: 
        :param spot: 

        :schema: CfnGroupPropsGroupComputeInstanceTypes
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if on_demand is not None:
            self._values["on_demand"] = on_demand
        if spot is not None:
            self._values["spot"] = spot

    @builtins.property
    def on_demand(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnGroupPropsGroupComputeInstanceTypes#onDemand
        '''
        result = self._values.get("on_demand")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def spot(self) -> typing.Optional[typing.List[builtins.str]]:
        '''
        :schema: CfnGroupPropsGroupComputeInstanceTypes#spot
        '''
        result = self._values.get("spot")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnGroupPropsGroupComputeInstanceTypes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/spot-elastigroup-group.CfnGroupPropsGroupComputeLaunchSpecification",
    jsii_struct_bases=[],
    name_mapping={
        "block_device_mappings": "blockDeviceMappings",
        "ebs_optimized": "ebsOptimized",
        "health_check_grace_period": "healthCheckGracePeriod",
        "health_check_type": "healthCheckType",
        "health_check_unhealthy_duration_before_replacement": "healthCheckUnhealthyDurationBeforeReplacement",
        "iam_role": "iamRole",
        "image_id": "imageId",
        "key_pair": "keyPair",
        "load_balancers_config": "loadBalancersConfig",
        "monitoring": "monitoring",
        "security_group_ids": "securityGroupIds",
        "shutdown_script": "shutdownScript",
        "tags": "tags",
        "tenancy": "tenancy",
        "user_data": "userData",
    },
)
class CfnGroupPropsGroupComputeLaunchSpecification:
    def __init__(
        self,
        *,
        block_device_mappings: typing.Optional[typing.Sequence[BlockDeviceMapping]] = None,
        ebs_optimized: typing.Optional[builtins.bool] = None,
        health_check_grace_period: typing.Optional[jsii.Number] = None,
        health_check_type: typing.Optional[builtins.str] = None,
        health_check_unhealthy_duration_before_replacement: typing.Optional[jsii.Number] = None,
        iam_role: typing.Optional["CfnGroupPropsGroupComputeLaunchSpecificationIamRole"] = None,
        image_id: typing.Optional[builtins.str] = None,
        key_pair: typing.Optional[builtins.str] = None,
        load_balancers_config: typing.Optional["CfnGroupPropsGroupComputeLaunchSpecificationLoadBalancersConfig"] = None,
        monitoring: typing.Optional[builtins.bool] = None,
        security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        shutdown_script: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence["Tag"]] = None,
        tenancy: typing.Optional[builtins.str] = None,
        user_data: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param block_device_mappings: 
        :param ebs_optimized: 
        :param health_check_grace_period: 
        :param health_check_type: 
        :param health_check_unhealthy_duration_before_replacement: 
        :param iam_role: 
        :param image_id: 
        :param key_pair: 
        :param load_balancers_config: 
        :param monitoring: 
        :param security_group_ids: 
        :param shutdown_script: 
        :param tags: 
        :param tenancy: 
        :param user_data: 

        :schema: CfnGroupPropsGroupComputeLaunchSpecification
        '''
        if isinstance(iam_role, dict):
            iam_role = CfnGroupPropsGroupComputeLaunchSpecificationIamRole(**iam_role)
        if isinstance(load_balancers_config, dict):
            load_balancers_config = CfnGroupPropsGroupComputeLaunchSpecificationLoadBalancersConfig(**load_balancers_config)
        self._values: typing.Dict[str, typing.Any] = {}
        if block_device_mappings is not None:
            self._values["block_device_mappings"] = block_device_mappings
        if ebs_optimized is not None:
            self._values["ebs_optimized"] = ebs_optimized
        if health_check_grace_period is not None:
            self._values["health_check_grace_period"] = health_check_grace_period
        if health_check_type is not None:
            self._values["health_check_type"] = health_check_type
        if health_check_unhealthy_duration_before_replacement is not None:
            self._values["health_check_unhealthy_duration_before_replacement"] = health_check_unhealthy_duration_before_replacement
        if iam_role is not None:
            self._values["iam_role"] = iam_role
        if image_id is not None:
            self._values["image_id"] = image_id
        if key_pair is not None:
            self._values["key_pair"] = key_pair
        if load_balancers_config is not None:
            self._values["load_balancers_config"] = load_balancers_config
        if monitoring is not None:
            self._values["monitoring"] = monitoring
        if security_group_ids is not None:
            self._values["security_group_ids"] = security_group_ids
        if shutdown_script is not None:
            self._values["shutdown_script"] = shutdown_script
        if tags is not None:
            self._values["tags"] = tags
        if tenancy is not None:
            self._values["tenancy"] = tenancy
        if user_data is not None:
            self._values["user_data"] = user_data

    @builtins.property
    def block_device_mappings(self) -> typing.Optional[typing.List[BlockDeviceMapping]]:
        '''
        :schema: CfnGroupPropsGroupComputeLaunchSpecification#blockDeviceMappings
        '''
        result = self._values.get("block_device_mappings")
        return typing.cast(typing.Optional[typing.List[BlockDeviceMapping]], result)

    @builtins.property
    def ebs_optimized(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: CfnGroupPropsGroupComputeLaunchSpecification#ebsOptimized
        '''
        result = self._values.get("ebs_optimized")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def health_check_grace_period(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: CfnGroupPropsGroupComputeLaunchSpecification#healthCheckGracePeriod
        '''
        result = self._values.get("health_check_grace_period")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def health_check_type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnGroupPropsGroupComputeLaunchSpecification#healthCheckType
        '''
        result = self._values.get("health_check_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def health_check_unhealthy_duration_before_replacement(
        self,
    ) -> typing.Optional[jsii.Number]:
        '''
        :schema: CfnGroupPropsGroupComputeLaunchSpecification#healthCheckUnhealthyDurationBeforeReplacement
        '''
        result = self._values.get("health_check_unhealthy_duration_before_replacement")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def iam_role(
        self,
    ) -> typing.Optional["CfnGroupPropsGroupComputeLaunchSpecificationIamRole"]:
        '''
        :schema: CfnGroupPropsGroupComputeLaunchSpecification#iamRole
        '''
        result = self._values.get("iam_role")
        return typing.cast(typing.Optional["CfnGroupPropsGroupComputeLaunchSpecificationIamRole"], result)

    @builtins.property
    def image_id(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnGroupPropsGroupComputeLaunchSpecification#imageId
        '''
        result = self._values.get("image_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def key_pair(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnGroupPropsGroupComputeLaunchSpecification#keyPair
        '''
        result = self._values.get("key_pair")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def load_balancers_config(
        self,
    ) -> typing.Optional["CfnGroupPropsGroupComputeLaunchSpecificationLoadBalancersConfig"]:
        '''
        :schema: CfnGroupPropsGroupComputeLaunchSpecification#loadBalancersConfig
        '''
        result = self._values.get("load_balancers_config")
        return typing.cast(typing.Optional["CfnGroupPropsGroupComputeLaunchSpecificationLoadBalancersConfig"], result)

    @builtins.property
    def monitoring(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: CfnGroupPropsGroupComputeLaunchSpecification#monitoring
        '''
        result = self._values.get("monitoring")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''
        :schema: CfnGroupPropsGroupComputeLaunchSpecification#securityGroupIds
        '''
        result = self._values.get("security_group_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def shutdown_script(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnGroupPropsGroupComputeLaunchSpecification#shutdownScript
        '''
        result = self._values.get("shutdown_script")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["Tag"]]:
        '''
        :schema: CfnGroupPropsGroupComputeLaunchSpecification#tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["Tag"]], result)

    @builtins.property
    def tenancy(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnGroupPropsGroupComputeLaunchSpecification#tenancy
        '''
        result = self._values.get("tenancy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def user_data(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnGroupPropsGroupComputeLaunchSpecification#userData
        '''
        result = self._values.get("user_data")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnGroupPropsGroupComputeLaunchSpecification(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/spot-elastigroup-group.CfnGroupPropsGroupComputeLaunchSpecificationIamRole",
    jsii_struct_bases=[],
    name_mapping={"arn": "arn", "name": "name"},
)
class CfnGroupPropsGroupComputeLaunchSpecificationIamRole:
    def __init__(
        self,
        *,
        arn: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param arn: 
        :param name: 

        :schema: CfnGroupPropsGroupComputeLaunchSpecificationIamRole
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if arn is not None:
            self._values["arn"] = arn
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def arn(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnGroupPropsGroupComputeLaunchSpecificationIamRole#arn
        '''
        result = self._values.get("arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnGroupPropsGroupComputeLaunchSpecificationIamRole#name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnGroupPropsGroupComputeLaunchSpecificationIamRole(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/spot-elastigroup-group.CfnGroupPropsGroupComputeLaunchSpecificationLoadBalancersConfig",
    jsii_struct_bases=[],
    name_mapping={"load_balancers": "loadBalancers"},
)
class CfnGroupPropsGroupComputeLaunchSpecificationLoadBalancersConfig:
    def __init__(
        self,
        *,
        load_balancers: typing.Optional[typing.Sequence["CfnGroupPropsGroupComputeLaunchSpecificationLoadBalancersConfigLoadBalancers"]] = None,
    ) -> None:
        '''
        :param load_balancers: 

        :schema: CfnGroupPropsGroupComputeLaunchSpecificationLoadBalancersConfig
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if load_balancers is not None:
            self._values["load_balancers"] = load_balancers

    @builtins.property
    def load_balancers(
        self,
    ) -> typing.Optional[typing.List["CfnGroupPropsGroupComputeLaunchSpecificationLoadBalancersConfigLoadBalancers"]]:
        '''
        :schema: CfnGroupPropsGroupComputeLaunchSpecificationLoadBalancersConfig#loadBalancers
        '''
        result = self._values.get("load_balancers")
        return typing.cast(typing.Optional[typing.List["CfnGroupPropsGroupComputeLaunchSpecificationLoadBalancersConfigLoadBalancers"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnGroupPropsGroupComputeLaunchSpecificationLoadBalancersConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/spot-elastigroup-group.CfnGroupPropsGroupComputeLaunchSpecificationLoadBalancersConfigLoadBalancers",
    jsii_struct_bases=[],
    name_mapping={
        "arn": "arn",
        "auto_weight": "autoWeight",
        "az_awareness": "azAwareness",
        "balancer_id": "balancerId",
        "name": "name",
        "target_set_id": "targetSetId",
        "type": "type",
    },
)
class CfnGroupPropsGroupComputeLaunchSpecificationLoadBalancersConfigLoadBalancers:
    def __init__(
        self,
        *,
        arn: typing.Optional[builtins.str] = None,
        auto_weight: typing.Optional[builtins.bool] = None,
        az_awareness: typing.Optional[builtins.bool] = None,
        balancer_id: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        target_set_id: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param arn: 
        :param auto_weight: 
        :param az_awareness: 
        :param balancer_id: 
        :param name: 
        :param target_set_id: 
        :param type: 

        :schema: CfnGroupPropsGroupComputeLaunchSpecificationLoadBalancersConfigLoadBalancers
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if arn is not None:
            self._values["arn"] = arn
        if auto_weight is not None:
            self._values["auto_weight"] = auto_weight
        if az_awareness is not None:
            self._values["az_awareness"] = az_awareness
        if balancer_id is not None:
            self._values["balancer_id"] = balancer_id
        if name is not None:
            self._values["name"] = name
        if target_set_id is not None:
            self._values["target_set_id"] = target_set_id
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def arn(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnGroupPropsGroupComputeLaunchSpecificationLoadBalancersConfigLoadBalancers#arn
        '''
        result = self._values.get("arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def auto_weight(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: CfnGroupPropsGroupComputeLaunchSpecificationLoadBalancersConfigLoadBalancers#autoWeight
        '''
        result = self._values.get("auto_weight")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def az_awareness(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: CfnGroupPropsGroupComputeLaunchSpecificationLoadBalancersConfigLoadBalancers#azAwareness
        '''
        result = self._values.get("az_awareness")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def balancer_id(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnGroupPropsGroupComputeLaunchSpecificationLoadBalancersConfigLoadBalancers#balancerId
        '''
        result = self._values.get("balancer_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnGroupPropsGroupComputeLaunchSpecificationLoadBalancersConfigLoadBalancers#name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target_set_id(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnGroupPropsGroupComputeLaunchSpecificationLoadBalancersConfigLoadBalancers#targetSetId
        '''
        result = self._values.get("target_set_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnGroupPropsGroupComputeLaunchSpecificationLoadBalancersConfigLoadBalancers#type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnGroupPropsGroupComputeLaunchSpecificationLoadBalancersConfigLoadBalancers(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/spot-elastigroup-group.CfnGroupPropsGroupScaling",
    jsii_struct_bases=[],
    name_mapping={"down": "down", "up": "up"},
)
class CfnGroupPropsGroupScaling:
    def __init__(
        self,
        *,
        down: typing.Optional[typing.Sequence["ScalingPolicy"]] = None,
        up: typing.Optional[typing.Sequence["ScalingPolicy"]] = None,
    ) -> None:
        '''
        :param down: 
        :param up: 

        :schema: CfnGroupPropsGroupScaling
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if down is not None:
            self._values["down"] = down
        if up is not None:
            self._values["up"] = up

    @builtins.property
    def down(self) -> typing.Optional[typing.List["ScalingPolicy"]]:
        '''
        :schema: CfnGroupPropsGroupScaling#down
        '''
        result = self._values.get("down")
        return typing.cast(typing.Optional[typing.List["ScalingPolicy"]], result)

    @builtins.property
    def up(self) -> typing.Optional[typing.List["ScalingPolicy"]]:
        '''
        :schema: CfnGroupPropsGroupScaling#up
        '''
        result = self._values.get("up")
        return typing.cast(typing.Optional[typing.List["ScalingPolicy"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnGroupPropsGroupScaling(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/spot-elastigroup-group.CfnGroupPropsGroupScheduling",
    jsii_struct_bases=[],
    name_mapping={"tasks": "tasks"},
)
class CfnGroupPropsGroupScheduling:
    def __init__(
        self,
        *,
        tasks: typing.Optional[typing.Sequence["Task"]] = None,
    ) -> None:
        '''
        :param tasks: 

        :schema: CfnGroupPropsGroupScheduling
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if tasks is not None:
            self._values["tasks"] = tasks

    @builtins.property
    def tasks(self) -> typing.Optional[typing.List["Task"]]:
        '''
        :schema: CfnGroupPropsGroupScheduling#tasks
        '''
        result = self._values.get("tasks")
        return typing.cast(typing.Optional[typing.List["Task"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnGroupPropsGroupScheduling(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/spot-elastigroup-group.CfnGroupPropsGroupStrategy",
    jsii_struct_bases=[],
    name_mapping={
        "availability_vs_cost": "availabilityVsCost",
        "draining_timeout": "drainingTimeout",
        "fallback_to_od": "fallbackToOd",
        "lifetime_period": "lifetimePeriod",
        "on_demand_count": "onDemandCount",
        "revert_to_spot": "revertToSpot",
        "risk": "risk",
    },
)
class CfnGroupPropsGroupStrategy:
    def __init__(
        self,
        *,
        availability_vs_cost: typing.Optional[builtins.str] = None,
        draining_timeout: typing.Optional[jsii.Number] = None,
        fallback_to_od: typing.Optional[builtins.bool] = None,
        lifetime_period: typing.Optional[builtins.str] = None,
        on_demand_count: typing.Optional[jsii.Number] = None,
        revert_to_spot: typing.Optional["CfnGroupPropsGroupStrategyRevertToSpot"] = None,
        risk: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param availability_vs_cost: 
        :param draining_timeout: 
        :param fallback_to_od: 
        :param lifetime_period: 
        :param on_demand_count: 
        :param revert_to_spot: 
        :param risk: 

        :schema: CfnGroupPropsGroupStrategy
        '''
        if isinstance(revert_to_spot, dict):
            revert_to_spot = CfnGroupPropsGroupStrategyRevertToSpot(**revert_to_spot)
        self._values: typing.Dict[str, typing.Any] = {}
        if availability_vs_cost is not None:
            self._values["availability_vs_cost"] = availability_vs_cost
        if draining_timeout is not None:
            self._values["draining_timeout"] = draining_timeout
        if fallback_to_od is not None:
            self._values["fallback_to_od"] = fallback_to_od
        if lifetime_period is not None:
            self._values["lifetime_period"] = lifetime_period
        if on_demand_count is not None:
            self._values["on_demand_count"] = on_demand_count
        if revert_to_spot is not None:
            self._values["revert_to_spot"] = revert_to_spot
        if risk is not None:
            self._values["risk"] = risk

    @builtins.property
    def availability_vs_cost(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnGroupPropsGroupStrategy#availabilityVsCost
        '''
        result = self._values.get("availability_vs_cost")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def draining_timeout(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: CfnGroupPropsGroupStrategy#drainingTimeout
        '''
        result = self._values.get("draining_timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def fallback_to_od(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: CfnGroupPropsGroupStrategy#fallbackToOd
        '''
        result = self._values.get("fallback_to_od")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def lifetime_period(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnGroupPropsGroupStrategy#lifetimePeriod
        '''
        result = self._values.get("lifetime_period")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def on_demand_count(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: CfnGroupPropsGroupStrategy#onDemandCount
        '''
        result = self._values.get("on_demand_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def revert_to_spot(
        self,
    ) -> typing.Optional["CfnGroupPropsGroupStrategyRevertToSpot"]:
        '''
        :schema: CfnGroupPropsGroupStrategy#revertToSpot
        '''
        result = self._values.get("revert_to_spot")
        return typing.cast(typing.Optional["CfnGroupPropsGroupStrategyRevertToSpot"], result)

    @builtins.property
    def risk(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: CfnGroupPropsGroupStrategy#risk
        '''
        result = self._values.get("risk")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnGroupPropsGroupStrategy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/spot-elastigroup-group.CfnGroupPropsGroupStrategyRevertToSpot",
    jsii_struct_bases=[],
    name_mapping={"perform_at": "performAt", "time_windows": "timeWindows"},
)
class CfnGroupPropsGroupStrategyRevertToSpot:
    def __init__(
        self,
        *,
        perform_at: typing.Optional[builtins.str] = None,
        time_windows: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param perform_at: 
        :param time_windows: 

        :schema: CfnGroupPropsGroupStrategyRevertToSpot
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if perform_at is not None:
            self._values["perform_at"] = perform_at
        if time_windows is not None:
            self._values["time_windows"] = time_windows

    @builtins.property
    def perform_at(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnGroupPropsGroupStrategyRevertToSpot#performAt
        '''
        result = self._values.get("perform_at")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def time_windows(self) -> typing.Optional[typing.List[builtins.str]]:
        '''
        :schema: CfnGroupPropsGroupStrategyRevertToSpot#timeWindows
        '''
        result = self._values.get("time_windows")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnGroupPropsGroupStrategyRevertToSpot(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/spot-elastigroup-group.CfnGroupPropsGroupThirdPartiesIntegration",
    jsii_struct_bases=[],
    name_mapping={"code_deploy": "codeDeploy", "ecs": "ecs"},
)
class CfnGroupPropsGroupThirdPartiesIntegration:
    def __init__(
        self,
        *,
        code_deploy: typing.Optional["CfnGroupPropsGroupThirdPartiesIntegrationCodeDeploy"] = None,
        ecs: typing.Optional["Ecs"] = None,
    ) -> None:
        '''
        :param code_deploy: 
        :param ecs: 

        :schema: CfnGroupPropsGroupThirdPartiesIntegration
        '''
        if isinstance(code_deploy, dict):
            code_deploy = CfnGroupPropsGroupThirdPartiesIntegrationCodeDeploy(**code_deploy)
        if isinstance(ecs, dict):
            ecs = Ecs(**ecs)
        self._values: typing.Dict[str, typing.Any] = {}
        if code_deploy is not None:
            self._values["code_deploy"] = code_deploy
        if ecs is not None:
            self._values["ecs"] = ecs

    @builtins.property
    def code_deploy(
        self,
    ) -> typing.Optional["CfnGroupPropsGroupThirdPartiesIntegrationCodeDeploy"]:
        '''
        :schema: CfnGroupPropsGroupThirdPartiesIntegration#codeDeploy
        '''
        result = self._values.get("code_deploy")
        return typing.cast(typing.Optional["CfnGroupPropsGroupThirdPartiesIntegrationCodeDeploy"], result)

    @builtins.property
    def ecs(self) -> typing.Optional["Ecs"]:
        '''
        :schema: CfnGroupPropsGroupThirdPartiesIntegration#ecs
        '''
        result = self._values.get("ecs")
        return typing.cast(typing.Optional["Ecs"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnGroupPropsGroupThirdPartiesIntegration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/spot-elastigroup-group.CfnGroupPropsGroupThirdPartiesIntegrationCodeDeploy",
    jsii_struct_bases=[],
    name_mapping={
        "clean_up_on_failure": "cleanUpOnFailure",
        "deployment_groups": "deploymentGroups",
        "terminate_instance_on_failure": "terminateInstanceOnFailure",
    },
)
class CfnGroupPropsGroupThirdPartiesIntegrationCodeDeploy:
    def __init__(
        self,
        *,
        clean_up_on_failure: typing.Optional[builtins.bool] = None,
        deployment_groups: typing.Optional[typing.Sequence["CfnGroupPropsGroupThirdPartiesIntegrationCodeDeployDeploymentGroups"]] = None,
        terminate_instance_on_failure: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param clean_up_on_failure: 
        :param deployment_groups: 
        :param terminate_instance_on_failure: 

        :schema: CfnGroupPropsGroupThirdPartiesIntegrationCodeDeploy
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if clean_up_on_failure is not None:
            self._values["clean_up_on_failure"] = clean_up_on_failure
        if deployment_groups is not None:
            self._values["deployment_groups"] = deployment_groups
        if terminate_instance_on_failure is not None:
            self._values["terminate_instance_on_failure"] = terminate_instance_on_failure

    @builtins.property
    def clean_up_on_failure(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: CfnGroupPropsGroupThirdPartiesIntegrationCodeDeploy#cleanUpOnFailure
        '''
        result = self._values.get("clean_up_on_failure")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def deployment_groups(
        self,
    ) -> typing.Optional[typing.List["CfnGroupPropsGroupThirdPartiesIntegrationCodeDeployDeploymentGroups"]]:
        '''
        :schema: CfnGroupPropsGroupThirdPartiesIntegrationCodeDeploy#deploymentGroups
        '''
        result = self._values.get("deployment_groups")
        return typing.cast(typing.Optional[typing.List["CfnGroupPropsGroupThirdPartiesIntegrationCodeDeployDeploymentGroups"]], result)

    @builtins.property
    def terminate_instance_on_failure(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: CfnGroupPropsGroupThirdPartiesIntegrationCodeDeploy#terminateInstanceOnFailure
        '''
        result = self._values.get("terminate_instance_on_failure")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnGroupPropsGroupThirdPartiesIntegrationCodeDeploy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/spot-elastigroup-group.CfnGroupPropsGroupThirdPartiesIntegrationCodeDeployDeploymentGroups",
    jsii_struct_bases=[],
    name_mapping={
        "application_name": "applicationName",
        "deployment_group_name": "deploymentGroupName",
    },
)
class CfnGroupPropsGroupThirdPartiesIntegrationCodeDeployDeploymentGroups:
    def __init__(
        self,
        *,
        application_name: typing.Optional[builtins.str] = None,
        deployment_group_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param application_name: 
        :param deployment_group_name: 

        :schema: CfnGroupPropsGroupThirdPartiesIntegrationCodeDeployDeploymentGroups
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if application_name is not None:
            self._values["application_name"] = application_name
        if deployment_group_name is not None:
            self._values["deployment_group_name"] = deployment_group_name

    @builtins.property
    def application_name(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnGroupPropsGroupThirdPartiesIntegrationCodeDeployDeploymentGroups#applicationName
        '''
        result = self._values.get("application_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def deployment_group_name(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnGroupPropsGroupThirdPartiesIntegrationCodeDeployDeploymentGroups#deploymentGroupName
        '''
        result = self._values.get("deployment_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnGroupPropsGroupThirdPartiesIntegrationCodeDeployDeploymentGroups(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/spot-elastigroup-group.Ecs",
    jsii_struct_bases=[],
    name_mapping={
        "auto_scale": "autoScale",
        "batch": "batch",
        "cluster_name": "clusterName",
        "optimize_images": "optimizeImages",
    },
)
class Ecs:
    def __init__(
        self,
        *,
        auto_scale: typing.Optional["EcsAutoScale"] = None,
        batch: typing.Optional["EcsBatch"] = None,
        cluster_name: typing.Optional[builtins.str] = None,
        optimize_images: typing.Optional["EcsOptimizeImages"] = None,
    ) -> None:
        '''
        :param auto_scale: 
        :param batch: 
        :param cluster_name: 
        :param optimize_images: 

        :schema: ecs
        '''
        if isinstance(auto_scale, dict):
            auto_scale = EcsAutoScale(**auto_scale)
        if isinstance(batch, dict):
            batch = EcsBatch(**batch)
        if isinstance(optimize_images, dict):
            optimize_images = EcsOptimizeImages(**optimize_images)
        self._values: typing.Dict[str, typing.Any] = {}
        if auto_scale is not None:
            self._values["auto_scale"] = auto_scale
        if batch is not None:
            self._values["batch"] = batch
        if cluster_name is not None:
            self._values["cluster_name"] = cluster_name
        if optimize_images is not None:
            self._values["optimize_images"] = optimize_images

    @builtins.property
    def auto_scale(self) -> typing.Optional["EcsAutoScale"]:
        '''
        :schema: ecs#autoScale
        '''
        result = self._values.get("auto_scale")
        return typing.cast(typing.Optional["EcsAutoScale"], result)

    @builtins.property
    def batch(self) -> typing.Optional["EcsBatch"]:
        '''
        :schema: ecs#batch
        '''
        result = self._values.get("batch")
        return typing.cast(typing.Optional["EcsBatch"], result)

    @builtins.property
    def cluster_name(self) -> typing.Optional[builtins.str]:
        '''
        :schema: ecs#clusterName
        '''
        result = self._values.get("cluster_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def optimize_images(self) -> typing.Optional["EcsOptimizeImages"]:
        '''
        :schema: ecs#optimizeImages
        '''
        result = self._values.get("optimize_images")
        return typing.cast(typing.Optional["EcsOptimizeImages"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Ecs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/spot-elastigroup-group.EcsAutoScale",
    jsii_struct_bases=[],
    name_mapping={
        "attributes": "attributes",
        "cooldown": "cooldown",
        "down": "down",
        "headroom": "headroom",
        "is_auto_config": "isAutoConfig",
        "is_enabled": "isEnabled",
        "should_scale_down_non_service_tasks": "shouldScaleDownNonServiceTasks",
    },
)
class EcsAutoScale:
    def __init__(
        self,
        *,
        attributes: typing.Optional[typing.Sequence[Attribute]] = None,
        cooldown: typing.Optional[jsii.Number] = None,
        down: typing.Optional["EcsAutoScaleDown"] = None,
        headroom: typing.Optional["EcsAutoScaleHeadroom"] = None,
        is_auto_config: typing.Optional[builtins.bool] = None,
        is_enabled: typing.Optional[builtins.bool] = None,
        should_scale_down_non_service_tasks: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param attributes: 
        :param cooldown: 
        :param down: 
        :param headroom: 
        :param is_auto_config: 
        :param is_enabled: 
        :param should_scale_down_non_service_tasks: 

        :schema: EcsAutoScale
        '''
        if isinstance(down, dict):
            down = EcsAutoScaleDown(**down)
        if isinstance(headroom, dict):
            headroom = EcsAutoScaleHeadroom(**headroom)
        self._values: typing.Dict[str, typing.Any] = {}
        if attributes is not None:
            self._values["attributes"] = attributes
        if cooldown is not None:
            self._values["cooldown"] = cooldown
        if down is not None:
            self._values["down"] = down
        if headroom is not None:
            self._values["headroom"] = headroom
        if is_auto_config is not None:
            self._values["is_auto_config"] = is_auto_config
        if is_enabled is not None:
            self._values["is_enabled"] = is_enabled
        if should_scale_down_non_service_tasks is not None:
            self._values["should_scale_down_non_service_tasks"] = should_scale_down_non_service_tasks

    @builtins.property
    def attributes(self) -> typing.Optional[typing.List[Attribute]]:
        '''
        :schema: EcsAutoScale#attributes
        '''
        result = self._values.get("attributes")
        return typing.cast(typing.Optional[typing.List[Attribute]], result)

    @builtins.property
    def cooldown(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: EcsAutoScale#cooldown
        '''
        result = self._values.get("cooldown")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def down(self) -> typing.Optional["EcsAutoScaleDown"]:
        '''
        :schema: EcsAutoScale#down
        '''
        result = self._values.get("down")
        return typing.cast(typing.Optional["EcsAutoScaleDown"], result)

    @builtins.property
    def headroom(self) -> typing.Optional["EcsAutoScaleHeadroom"]:
        '''
        :schema: EcsAutoScale#headroom
        '''
        result = self._values.get("headroom")
        return typing.cast(typing.Optional["EcsAutoScaleHeadroom"], result)

    @builtins.property
    def is_auto_config(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: EcsAutoScale#isAutoConfig
        '''
        result = self._values.get("is_auto_config")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def is_enabled(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: EcsAutoScale#isEnabled
        '''
        result = self._values.get("is_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def should_scale_down_non_service_tasks(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: EcsAutoScale#shouldScaleDownNonServiceTasks
        '''
        result = self._values.get("should_scale_down_non_service_tasks")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsAutoScale(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/spot-elastigroup-group.EcsAutoScaleDown",
    jsii_struct_bases=[],
    name_mapping={
        "evaluation_periods": "evaluationPeriods",
        "max_scale_down_percentage": "maxScaleDownPercentage",
    },
)
class EcsAutoScaleDown:
    def __init__(
        self,
        *,
        evaluation_periods: typing.Optional[jsii.Number] = None,
        max_scale_down_percentage: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param evaluation_periods: 
        :param max_scale_down_percentage: 

        :schema: EcsAutoScaleDown
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if evaluation_periods is not None:
            self._values["evaluation_periods"] = evaluation_periods
        if max_scale_down_percentage is not None:
            self._values["max_scale_down_percentage"] = max_scale_down_percentage

    @builtins.property
    def evaluation_periods(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: EcsAutoScaleDown#evaluationPeriods
        '''
        result = self._values.get("evaluation_periods")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_scale_down_percentage(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: EcsAutoScaleDown#maxScaleDownPercentage
        '''
        result = self._values.get("max_scale_down_percentage")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsAutoScaleDown(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/spot-elastigroup-group.EcsAutoScaleHeadroom",
    jsii_struct_bases=[],
    name_mapping={
        "cpu_per_unit": "cpuPerUnit",
        "memory_per_unit": "memoryPerUnit",
        "num_of_units": "numOfUnits",
    },
)
class EcsAutoScaleHeadroom:
    def __init__(
        self,
        *,
        cpu_per_unit: typing.Optional[jsii.Number] = None,
        memory_per_unit: typing.Optional[jsii.Number] = None,
        num_of_units: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param cpu_per_unit: 
        :param memory_per_unit: 
        :param num_of_units: 

        :schema: EcsAutoScaleHeadroom
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if cpu_per_unit is not None:
            self._values["cpu_per_unit"] = cpu_per_unit
        if memory_per_unit is not None:
            self._values["memory_per_unit"] = memory_per_unit
        if num_of_units is not None:
            self._values["num_of_units"] = num_of_units

    @builtins.property
    def cpu_per_unit(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: EcsAutoScaleHeadroom#cpuPerUnit
        '''
        result = self._values.get("cpu_per_unit")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def memory_per_unit(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: EcsAutoScaleHeadroom#memoryPerUnit
        '''
        result = self._values.get("memory_per_unit")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def num_of_units(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: EcsAutoScaleHeadroom#numOfUnits
        '''
        result = self._values.get("num_of_units")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsAutoScaleHeadroom(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/spot-elastigroup-group.EcsBatch",
    jsii_struct_bases=[],
    name_mapping={"job_queue_names": "jobQueueNames"},
)
class EcsBatch:
    def __init__(
        self,
        *,
        job_queue_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param job_queue_names: 

        :schema: EcsBatch
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if job_queue_names is not None:
            self._values["job_queue_names"] = job_queue_names

    @builtins.property
    def job_queue_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''
        :schema: EcsBatch#jobQueueNames
        '''
        result = self._values.get("job_queue_names")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsBatch(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/spot-elastigroup-group.EcsOptimizeImages",
    jsii_struct_bases=[],
    name_mapping={
        "perform_at": "performAt",
        "should_optimize_ecs_ami": "shouldOptimizeEcsAmi",
        "time_windows": "timeWindows",
    },
)
class EcsOptimizeImages:
    def __init__(
        self,
        *,
        perform_at: typing.Optional[builtins.str] = None,
        should_optimize_ecs_ami: typing.Optional[builtins.bool] = None,
        time_windows: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param perform_at: 
        :param should_optimize_ecs_ami: 
        :param time_windows: 

        :schema: EcsOptimizeImages
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if perform_at is not None:
            self._values["perform_at"] = perform_at
        if should_optimize_ecs_ami is not None:
            self._values["should_optimize_ecs_ami"] = should_optimize_ecs_ami
        if time_windows is not None:
            self._values["time_windows"] = time_windows

    @builtins.property
    def perform_at(self) -> typing.Optional[builtins.str]:
        '''
        :schema: EcsOptimizeImages#performAt
        '''
        result = self._values.get("perform_at")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def should_optimize_ecs_ami(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: EcsOptimizeImages#shouldOptimizeEcsAmi
        '''
        result = self._values.get("should_optimize_ecs_ami")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def time_windows(self) -> typing.Optional[typing.List[builtins.str]]:
        '''
        :schema: EcsOptimizeImages#timeWindows
        '''
        result = self._values.get("time_windows")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsOptimizeImages(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/spot-elastigroup-group.ScalingPolicy",
    jsii_struct_bases=[],
    name_mapping={
        "action": "action",
        "cooldown": "cooldown",
        "dimension": "dimension",
        "evaluation_periods": "evaluationPeriods",
        "metric_name": "metricName",
        "namespace": "namespace",
        "period": "period",
        "policy_name": "policyName",
        "statistic": "statistic",
        "threshold": "threshold",
        "unit": "unit",
    },
)
class ScalingPolicy:
    def __init__(
        self,
        *,
        action: typing.Optional["ScalingPolicyAction"] = None,
        cooldown: typing.Optional[jsii.Number] = None,
        dimension: typing.Optional[typing.Sequence["ScalingPolicyDimension"]] = None,
        evaluation_periods: typing.Optional[jsii.Number] = None,
        metric_name: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
        period: typing.Optional[jsii.Number] = None,
        policy_name: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        threshold: typing.Optional[jsii.Number] = None,
        unit: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param action: 
        :param cooldown: 
        :param dimension: 
        :param evaluation_periods: 
        :param metric_name: 
        :param namespace: 
        :param period: 
        :param policy_name: 
        :param statistic: 
        :param threshold: 
        :param unit: 

        :schema: ScalingPolicy
        '''
        if isinstance(action, dict):
            action = ScalingPolicyAction(**action)
        self._values: typing.Dict[str, typing.Any] = {}
        if action is not None:
            self._values["action"] = action
        if cooldown is not None:
            self._values["cooldown"] = cooldown
        if dimension is not None:
            self._values["dimension"] = dimension
        if evaluation_periods is not None:
            self._values["evaluation_periods"] = evaluation_periods
        if metric_name is not None:
            self._values["metric_name"] = metric_name
        if namespace is not None:
            self._values["namespace"] = namespace
        if period is not None:
            self._values["period"] = period
        if policy_name is not None:
            self._values["policy_name"] = policy_name
        if statistic is not None:
            self._values["statistic"] = statistic
        if threshold is not None:
            self._values["threshold"] = threshold
        if unit is not None:
            self._values["unit"] = unit

    @builtins.property
    def action(self) -> typing.Optional["ScalingPolicyAction"]:
        '''
        :schema: ScalingPolicy#action
        '''
        result = self._values.get("action")
        return typing.cast(typing.Optional["ScalingPolicyAction"], result)

    @builtins.property
    def cooldown(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: ScalingPolicy#cooldown
        '''
        result = self._values.get("cooldown")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def dimension(self) -> typing.Optional[typing.List["ScalingPolicyDimension"]]:
        '''
        :schema: ScalingPolicy#dimension
        '''
        result = self._values.get("dimension")
        return typing.cast(typing.Optional[typing.List["ScalingPolicyDimension"]], result)

    @builtins.property
    def evaluation_periods(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: ScalingPolicy#evaluationPeriods
        '''
        result = self._values.get("evaluation_periods")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def metric_name(self) -> typing.Optional[builtins.str]:
        '''
        :schema: ScalingPolicy#metricName
        '''
        result = self._values.get("metric_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''
        :schema: ScalingPolicy#namespace
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def period(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: ScalingPolicy#period
        '''
        result = self._values.get("period")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def policy_name(self) -> typing.Optional[builtins.str]:
        '''
        :schema: ScalingPolicy#policyName
        '''
        result = self._values.get("policy_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def statistic(self) -> typing.Optional[builtins.str]:
        '''
        :schema: ScalingPolicy#statistic
        '''
        result = self._values.get("statistic")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def threshold(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: ScalingPolicy#threshold
        '''
        result = self._values.get("threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def unit(self) -> typing.Optional[builtins.str]:
        '''
        :schema: ScalingPolicy#unit
        '''
        result = self._values.get("unit")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ScalingPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/spot-elastigroup-group.ScalingPolicyAction",
    jsii_struct_bases=[],
    name_mapping={
        "adjustment": "adjustment",
        "maximum": "maximum",
        "minimum": "minimum",
        "min_target_capacity": "minTargetCapacity",
        "target": "target",
        "type": "type",
    },
)
class ScalingPolicyAction:
    def __init__(
        self,
        *,
        adjustment: typing.Optional[builtins.str] = None,
        maximum: typing.Optional[builtins.str] = None,
        minimum: typing.Optional[builtins.str] = None,
        min_target_capacity: typing.Optional[builtins.str] = None,
        target: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param adjustment: 
        :param maximum: 
        :param minimum: 
        :param min_target_capacity: 
        :param target: 
        :param type: 

        :schema: ScalingPolicyAction
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if adjustment is not None:
            self._values["adjustment"] = adjustment
        if maximum is not None:
            self._values["maximum"] = maximum
        if minimum is not None:
            self._values["minimum"] = minimum
        if min_target_capacity is not None:
            self._values["min_target_capacity"] = min_target_capacity
        if target is not None:
            self._values["target"] = target
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def adjustment(self) -> typing.Optional[builtins.str]:
        '''
        :schema: ScalingPolicyAction#adjustment
        '''
        result = self._values.get("adjustment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def maximum(self) -> typing.Optional[builtins.str]:
        '''
        :schema: ScalingPolicyAction#maximum
        '''
        result = self._values.get("maximum")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def minimum(self) -> typing.Optional[builtins.str]:
        '''
        :schema: ScalingPolicyAction#minimum
        '''
        result = self._values.get("minimum")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def min_target_capacity(self) -> typing.Optional[builtins.str]:
        '''
        :schema: ScalingPolicyAction#minTargetCapacity
        '''
        result = self._values.get("min_target_capacity")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target(self) -> typing.Optional[builtins.str]:
        '''
        :schema: ScalingPolicyAction#target
        '''
        result = self._values.get("target")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: ScalingPolicyAction#type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ScalingPolicyAction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/spot-elastigroup-group.ScalingPolicyDimension",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "value": "value"},
)
class ScalingPolicyDimension:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: 
        :param value: 

        :schema: ScalingPolicyDimension
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''
        :schema: ScalingPolicyDimension#name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''
        :schema: ScalingPolicyDimension#value
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ScalingPolicyDimension(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/spot-elastigroup-group.Tag",
    jsii_struct_bases=[],
    name_mapping={"tag_key": "tagKey", "tag_value": "tagValue"},
)
class Tag:
    def __init__(
        self,
        *,
        tag_key: typing.Optional[builtins.str] = None,
        tag_value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param tag_key: 
        :param tag_value: 

        :schema: Tag
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if tag_key is not None:
            self._values["tag_key"] = tag_key
        if tag_value is not None:
            self._values["tag_value"] = tag_value

    @builtins.property
    def tag_key(self) -> typing.Optional[builtins.str]:
        '''
        :schema: Tag#tagKey
        '''
        result = self._values.get("tag_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tag_value(self) -> typing.Optional[builtins.str]:
        '''
        :schema: Tag#tagValue
        '''
        result = self._values.get("tag_value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Tag(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/spot-elastigroup-group.Task",
    jsii_struct_bases=[],
    name_mapping={
        "adjustment": "adjustment",
        "batch_size_percentage": "batchSizePercentage",
        "cron_expression": "cronExpression",
        "frequency": "frequency",
        "grace_period": "gracePeriod",
        "is_enabled": "isEnabled",
        "scale_max_capacity": "scaleMaxCapacity",
        "scale_min_capacity": "scaleMinCapacity",
        "scale_target_capacity": "scaleTargetCapacity",
        "start_time": "startTime",
        "task_type": "taskType",
    },
)
class Task:
    def __init__(
        self,
        *,
        adjustment: typing.Optional[jsii.Number] = None,
        batch_size_percentage: typing.Optional[jsii.Number] = None,
        cron_expression: typing.Optional[builtins.str] = None,
        frequency: typing.Optional[builtins.str] = None,
        grace_period: typing.Optional[jsii.Number] = None,
        is_enabled: typing.Optional[builtins.bool] = None,
        scale_max_capacity: typing.Optional[jsii.Number] = None,
        scale_min_capacity: typing.Optional[jsii.Number] = None,
        scale_target_capacity: typing.Optional[jsii.Number] = None,
        start_time: typing.Optional[builtins.str] = None,
        task_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param adjustment: 
        :param batch_size_percentage: 
        :param cron_expression: 
        :param frequency: 
        :param grace_period: 
        :param is_enabled: 
        :param scale_max_capacity: 
        :param scale_min_capacity: 
        :param scale_target_capacity: 
        :param start_time: 
        :param task_type: 

        :schema: Task
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if adjustment is not None:
            self._values["adjustment"] = adjustment
        if batch_size_percentage is not None:
            self._values["batch_size_percentage"] = batch_size_percentage
        if cron_expression is not None:
            self._values["cron_expression"] = cron_expression
        if frequency is not None:
            self._values["frequency"] = frequency
        if grace_period is not None:
            self._values["grace_period"] = grace_period
        if is_enabled is not None:
            self._values["is_enabled"] = is_enabled
        if scale_max_capacity is not None:
            self._values["scale_max_capacity"] = scale_max_capacity
        if scale_min_capacity is not None:
            self._values["scale_min_capacity"] = scale_min_capacity
        if scale_target_capacity is not None:
            self._values["scale_target_capacity"] = scale_target_capacity
        if start_time is not None:
            self._values["start_time"] = start_time
        if task_type is not None:
            self._values["task_type"] = task_type

    @builtins.property
    def adjustment(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: Task#adjustment
        '''
        result = self._values.get("adjustment")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def batch_size_percentage(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: Task#batchSizePercentage
        '''
        result = self._values.get("batch_size_percentage")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def cron_expression(self) -> typing.Optional[builtins.str]:
        '''
        :schema: Task#cronExpression
        '''
        result = self._values.get("cron_expression")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def frequency(self) -> typing.Optional[builtins.str]:
        '''
        :schema: Task#frequency
        '''
        result = self._values.get("frequency")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def grace_period(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: Task#gracePeriod
        '''
        result = self._values.get("grace_period")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def is_enabled(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: Task#isEnabled
        '''
        result = self._values.get("is_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def scale_max_capacity(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: Task#scaleMaxCapacity
        '''
        result = self._values.get("scale_max_capacity")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def scale_min_capacity(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: Task#scaleMinCapacity
        '''
        result = self._values.get("scale_min_capacity")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def scale_target_capacity(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: Task#scaleTargetCapacity
        '''
        result = self._values.get("scale_target_capacity")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def start_time(self) -> typing.Optional[builtins.str]:
        '''
        :schema: Task#startTime
        '''
        result = self._values.get("start_time")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def task_type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: Task#taskType
        '''
        result = self._values.get("task_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Task(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "Attribute",
    "BlockDeviceMapping",
    "BlockDeviceMappingEbs",
    "BlockDeviceMappingEbsVolumeType",
    "CfnGroup",
    "CfnGroupProps",
    "CfnGroupPropsCredentials",
    "CfnGroupPropsGroup",
    "CfnGroupPropsGroupCapacity",
    "CfnGroupPropsGroupCompute",
    "CfnGroupPropsGroupComputeAvailabilityZones",
    "CfnGroupPropsGroupComputeInstanceTypes",
    "CfnGroupPropsGroupComputeLaunchSpecification",
    "CfnGroupPropsGroupComputeLaunchSpecificationIamRole",
    "CfnGroupPropsGroupComputeLaunchSpecificationLoadBalancersConfig",
    "CfnGroupPropsGroupComputeLaunchSpecificationLoadBalancersConfigLoadBalancers",
    "CfnGroupPropsGroupScaling",
    "CfnGroupPropsGroupScheduling",
    "CfnGroupPropsGroupStrategy",
    "CfnGroupPropsGroupStrategyRevertToSpot",
    "CfnGroupPropsGroupThirdPartiesIntegration",
    "CfnGroupPropsGroupThirdPartiesIntegrationCodeDeploy",
    "CfnGroupPropsGroupThirdPartiesIntegrationCodeDeployDeploymentGroups",
    "Ecs",
    "EcsAutoScale",
    "EcsAutoScaleDown",
    "EcsAutoScaleHeadroom",
    "EcsBatch",
    "EcsOptimizeImages",
    "ScalingPolicy",
    "ScalingPolicyAction",
    "ScalingPolicyDimension",
    "Tag",
    "Task",
]

publication.publish()
