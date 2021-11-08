'''
# AWS CDK CloudFormation Constructs for Stackery::Open::Bastion::MODULE

Schema for Module Fragment of type Stackery::Open::Bastion::MODULE

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
    jsii_type="@cdk-cloudformation/stackery-open-bastion-module.CfnModule",
):
    '''A CloudFormation ``Stackery::Open::Bastion::MODULE``.

    :cloudformationResource: Stackery::Open::Bastion::MODULE
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
        '''Create a new ``Stackery::Open::Bastion::MODULE``.

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
    jsii_type="@cdk-cloudformation/stackery-open-bastion-module.CfnModuleProps",
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
        '''Schema for Module Fragment of type Stackery::Open::Bastion::MODULE.

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
    jsii_type="@cdk-cloudformation/stackery-open-bastion-module.CfnModulePropsParameters",
    jsii_struct_bases=[],
    name_mapping={
        "instance_class": "instanceClass",
        "vpc_id": "vpcId",
        "vpc_subnets": "vpcSubnets",
    },
)
class CfnModulePropsParameters:
    def __init__(
        self,
        *,
        instance_class: typing.Optional["CfnModulePropsParametersInstanceClass"] = None,
        vpc_id: typing.Optional["CfnModulePropsParametersVpcId"] = None,
        vpc_subnets: typing.Optional["CfnModulePropsParametersVpcSubnets"] = None,
    ) -> None:
        '''
        :param instance_class: EC2 instance class to provision.
        :param vpc_id: VPC to run bastion server in.
        :param vpc_subnets: Subnets to pick from to run a bastion server in.

        :schema: CfnModulePropsParameters
        '''
        if isinstance(instance_class, dict):
            instance_class = CfnModulePropsParametersInstanceClass(**instance_class)
        if isinstance(vpc_id, dict):
            vpc_id = CfnModulePropsParametersVpcId(**vpc_id)
        if isinstance(vpc_subnets, dict):
            vpc_subnets = CfnModulePropsParametersVpcSubnets(**vpc_subnets)
        self._values: typing.Dict[str, typing.Any] = {}
        if instance_class is not None:
            self._values["instance_class"] = instance_class
        if vpc_id is not None:
            self._values["vpc_id"] = vpc_id
        if vpc_subnets is not None:
            self._values["vpc_subnets"] = vpc_subnets

    @builtins.property
    def instance_class(
        self,
    ) -> typing.Optional["CfnModulePropsParametersInstanceClass"]:
        '''EC2 instance class to provision.

        :schema: CfnModulePropsParameters#InstanceClass
        '''
        result = self._values.get("instance_class")
        return typing.cast(typing.Optional["CfnModulePropsParametersInstanceClass"], result)

    @builtins.property
    def vpc_id(self) -> typing.Optional["CfnModulePropsParametersVpcId"]:
        '''VPC to run bastion server in.

        :schema: CfnModulePropsParameters#VPCId
        '''
        result = self._values.get("vpc_id")
        return typing.cast(typing.Optional["CfnModulePropsParametersVpcId"], result)

    @builtins.property
    def vpc_subnets(self) -> typing.Optional["CfnModulePropsParametersVpcSubnets"]:
        '''Subnets to pick from to run a bastion server in.

        :schema: CfnModulePropsParameters#VPCSubnets
        '''
        result = self._values.get("vpc_subnets")
        return typing.cast(typing.Optional["CfnModulePropsParametersVpcSubnets"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/stackery-open-bastion-module.CfnModulePropsParametersInstanceClass",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersInstanceClass:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''EC2 instance class to provision.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersInstanceClass
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersInstanceClass#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersInstanceClass#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersInstanceClass(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/stackery-open-bastion-module.CfnModulePropsParametersVpcId",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersVpcId:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''VPC to run bastion server in.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersVpcId
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersVpcId#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

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
    jsii_type="@cdk-cloudformation/stackery-open-bastion-module.CfnModulePropsParametersVpcSubnets",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnModulePropsParametersVpcSubnets:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Subnets to pick from to run a bastion server in.

        :param description: 
        :param type: 

        :schema: CfnModulePropsParametersVpcSubnets
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersVpcSubnets#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnModulePropsParametersVpcSubnets#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsParametersVpcSubnets(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/stackery-open-bastion-module.CfnModulePropsResources",
    jsii_struct_bases=[],
    name_mapping={
        "auto_scaling_group": "autoScalingGroup",
        "cloud_watch_agent_auto_update": "cloudWatchAgentAutoUpdate",
        "cloud_watch_agent_update_and_start": "cloudWatchAgentUpdateAndStart",
        "iam_instance_profile": "iamInstanceProfile",
        "iam_role": "iamRole",
        "instances_security_group": "instancesSecurityGroup",
        "launch_configuration": "launchConfiguration",
        "ssm_agent_auto_update": "ssmAgentAutoUpdate",
    },
)
class CfnModulePropsResources:
    def __init__(
        self,
        *,
        auto_scaling_group: typing.Optional["CfnModulePropsResourcesAutoScalingGroup"] = None,
        cloud_watch_agent_auto_update: typing.Optional["CfnModulePropsResourcesCloudWatchAgentAutoUpdate"] = None,
        cloud_watch_agent_update_and_start: typing.Optional["CfnModulePropsResourcesCloudWatchAgentUpdateAndStart"] = None,
        iam_instance_profile: typing.Optional["CfnModulePropsResourcesIamInstanceProfile"] = None,
        iam_role: typing.Optional["CfnModulePropsResourcesIamRole"] = None,
        instances_security_group: typing.Optional["CfnModulePropsResourcesInstancesSecurityGroup"] = None,
        launch_configuration: typing.Optional["CfnModulePropsResourcesLaunchConfiguration"] = None,
        ssm_agent_auto_update: typing.Optional["CfnModulePropsResourcesSsmAgentAutoUpdate"] = None,
    ) -> None:
        '''
        :param auto_scaling_group: 
        :param cloud_watch_agent_auto_update: 
        :param cloud_watch_agent_update_and_start: 
        :param iam_instance_profile: 
        :param iam_role: 
        :param instances_security_group: 
        :param launch_configuration: 
        :param ssm_agent_auto_update: 

        :schema: CfnModulePropsResources
        '''
        if isinstance(auto_scaling_group, dict):
            auto_scaling_group = CfnModulePropsResourcesAutoScalingGroup(**auto_scaling_group)
        if isinstance(cloud_watch_agent_auto_update, dict):
            cloud_watch_agent_auto_update = CfnModulePropsResourcesCloudWatchAgentAutoUpdate(**cloud_watch_agent_auto_update)
        if isinstance(cloud_watch_agent_update_and_start, dict):
            cloud_watch_agent_update_and_start = CfnModulePropsResourcesCloudWatchAgentUpdateAndStart(**cloud_watch_agent_update_and_start)
        if isinstance(iam_instance_profile, dict):
            iam_instance_profile = CfnModulePropsResourcesIamInstanceProfile(**iam_instance_profile)
        if isinstance(iam_role, dict):
            iam_role = CfnModulePropsResourcesIamRole(**iam_role)
        if isinstance(instances_security_group, dict):
            instances_security_group = CfnModulePropsResourcesInstancesSecurityGroup(**instances_security_group)
        if isinstance(launch_configuration, dict):
            launch_configuration = CfnModulePropsResourcesLaunchConfiguration(**launch_configuration)
        if isinstance(ssm_agent_auto_update, dict):
            ssm_agent_auto_update = CfnModulePropsResourcesSsmAgentAutoUpdate(**ssm_agent_auto_update)
        self._values: typing.Dict[str, typing.Any] = {}
        if auto_scaling_group is not None:
            self._values["auto_scaling_group"] = auto_scaling_group
        if cloud_watch_agent_auto_update is not None:
            self._values["cloud_watch_agent_auto_update"] = cloud_watch_agent_auto_update
        if cloud_watch_agent_update_and_start is not None:
            self._values["cloud_watch_agent_update_and_start"] = cloud_watch_agent_update_and_start
        if iam_instance_profile is not None:
            self._values["iam_instance_profile"] = iam_instance_profile
        if iam_role is not None:
            self._values["iam_role"] = iam_role
        if instances_security_group is not None:
            self._values["instances_security_group"] = instances_security_group
        if launch_configuration is not None:
            self._values["launch_configuration"] = launch_configuration
        if ssm_agent_auto_update is not None:
            self._values["ssm_agent_auto_update"] = ssm_agent_auto_update

    @builtins.property
    def auto_scaling_group(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesAutoScalingGroup"]:
        '''
        :schema: CfnModulePropsResources#AutoScalingGroup
        '''
        result = self._values.get("auto_scaling_group")
        return typing.cast(typing.Optional["CfnModulePropsResourcesAutoScalingGroup"], result)

    @builtins.property
    def cloud_watch_agent_auto_update(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesCloudWatchAgentAutoUpdate"]:
        '''
        :schema: CfnModulePropsResources#CloudWatchAgentAutoUpdate
        '''
        result = self._values.get("cloud_watch_agent_auto_update")
        return typing.cast(typing.Optional["CfnModulePropsResourcesCloudWatchAgentAutoUpdate"], result)

    @builtins.property
    def cloud_watch_agent_update_and_start(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesCloudWatchAgentUpdateAndStart"]:
        '''
        :schema: CfnModulePropsResources#CloudWatchAgentUpdateAndStart
        '''
        result = self._values.get("cloud_watch_agent_update_and_start")
        return typing.cast(typing.Optional["CfnModulePropsResourcesCloudWatchAgentUpdateAndStart"], result)

    @builtins.property
    def iam_instance_profile(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesIamInstanceProfile"]:
        '''
        :schema: CfnModulePropsResources#IAMInstanceProfile
        '''
        result = self._values.get("iam_instance_profile")
        return typing.cast(typing.Optional["CfnModulePropsResourcesIamInstanceProfile"], result)

    @builtins.property
    def iam_role(self) -> typing.Optional["CfnModulePropsResourcesIamRole"]:
        '''
        :schema: CfnModulePropsResources#IAMRole
        '''
        result = self._values.get("iam_role")
        return typing.cast(typing.Optional["CfnModulePropsResourcesIamRole"], result)

    @builtins.property
    def instances_security_group(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesInstancesSecurityGroup"]:
        '''
        :schema: CfnModulePropsResources#InstancesSecurityGroup
        '''
        result = self._values.get("instances_security_group")
        return typing.cast(typing.Optional["CfnModulePropsResourcesInstancesSecurityGroup"], result)

    @builtins.property
    def launch_configuration(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesLaunchConfiguration"]:
        '''
        :schema: CfnModulePropsResources#LaunchConfiguration
        '''
        result = self._values.get("launch_configuration")
        return typing.cast(typing.Optional["CfnModulePropsResourcesLaunchConfiguration"], result)

    @builtins.property
    def ssm_agent_auto_update(
        self,
    ) -> typing.Optional["CfnModulePropsResourcesSsmAgentAutoUpdate"]:
        '''
        :schema: CfnModulePropsResources#SSMAgentAutoUpdate
        '''
        result = self._values.get("ssm_agent_auto_update")
        return typing.cast(typing.Optional["CfnModulePropsResourcesSsmAgentAutoUpdate"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResources(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/stackery-open-bastion-module.CfnModulePropsResourcesAutoScalingGroup",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesAutoScalingGroup:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesAutoScalingGroup
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesAutoScalingGroup#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesAutoScalingGroup#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesAutoScalingGroup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/stackery-open-bastion-module.CfnModulePropsResourcesCloudWatchAgentAutoUpdate",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesCloudWatchAgentAutoUpdate:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesCloudWatchAgentAutoUpdate
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesCloudWatchAgentAutoUpdate#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesCloudWatchAgentAutoUpdate#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesCloudWatchAgentAutoUpdate(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/stackery-open-bastion-module.CfnModulePropsResourcesCloudWatchAgentUpdateAndStart",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesCloudWatchAgentUpdateAndStart:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesCloudWatchAgentUpdateAndStart
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesCloudWatchAgentUpdateAndStart#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesCloudWatchAgentUpdateAndStart#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesCloudWatchAgentUpdateAndStart(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/stackery-open-bastion-module.CfnModulePropsResourcesIamInstanceProfile",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesIamInstanceProfile:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesIamInstanceProfile
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesIamInstanceProfile#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesIamInstanceProfile#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesIamInstanceProfile(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/stackery-open-bastion-module.CfnModulePropsResourcesIamRole",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesIamRole:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesIamRole
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesIamRole#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesIamRole#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesIamRole(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/stackery-open-bastion-module.CfnModulePropsResourcesInstancesSecurityGroup",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesInstancesSecurityGroup:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesInstancesSecurityGroup
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesInstancesSecurityGroup#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesInstancesSecurityGroup#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesInstancesSecurityGroup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/stackery-open-bastion-module.CfnModulePropsResourcesLaunchConfiguration",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesLaunchConfiguration:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesLaunchConfiguration
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesLaunchConfiguration#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesLaunchConfiguration#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesLaunchConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/stackery-open-bastion-module.CfnModulePropsResourcesSsmAgentAutoUpdate",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesSsmAgentAutoUpdate:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesSsmAgentAutoUpdate
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesSsmAgentAutoUpdate#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesSsmAgentAutoUpdate#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesSsmAgentAutoUpdate(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnModule",
    "CfnModuleProps",
    "CfnModulePropsParameters",
    "CfnModulePropsParametersInstanceClass",
    "CfnModulePropsParametersVpcId",
    "CfnModulePropsParametersVpcSubnets",
    "CfnModulePropsResources",
    "CfnModulePropsResourcesAutoScalingGroup",
    "CfnModulePropsResourcesCloudWatchAgentAutoUpdate",
    "CfnModulePropsResourcesCloudWatchAgentUpdateAndStart",
    "CfnModulePropsResourcesIamInstanceProfile",
    "CfnModulePropsResourcesIamRole",
    "CfnModulePropsResourcesInstancesSecurityGroup",
    "CfnModulePropsResourcesLaunchConfiguration",
    "CfnModulePropsResourcesSsmAgentAutoUpdate",
]

publication.publish()
