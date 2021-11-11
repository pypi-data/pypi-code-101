'''
# stackery-open-bastion-module

> AWS CDK [L1 construct](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html) and data structures for the [AWS CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) type `Stackery::Open::Bastion::MODULE` v1.0.0.

## Description

Schema for Module Fragment of type Stackery::Open::Bastion::MODULE

## Usage

In order to use this library, you will need to activate this AWS CloudFormation Registry type in your account. You can do this via the AWS Management Console or using the [AWS CLI](https://aws.amazon.com/cli/) using the following command:

```sh
aws cloudformation activate-type \
  --type-name Stackery::Open::Bastion::MODULE \
  --publisher-id c7a1566696d21e673a0e14208c79edfc9dd639e3 \
  --type MODULE \
  --execution-role-arn ROLE-ARN
```

Alternatively:

```sh
aws cloudformation activate-type \
  --public-type-arn arn:aws:cloudformation:us-east-1::type/module/c7a1566696d21e673a0e14208c79edfc9dd639e3/Stackery-Open-Bastion-MODULE \
  --execution-role-arn ROLE-ARN
```

You can find more information about activating this type in the [AWS CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html).

## Feedback

This library is auto-generated and published to all supported programming languages by the [cdklabs/cdk-cloudformation](https://github.com/cdklabs/cdk-cloudformation) project based on the API schema published for `Stackery::Open::Bastion::MODULE`.

* Issues related to this generated library should be [reported here](https://github.com/cdklabs/cdk-cloudformation/issues/new?title=Issue+with+%40cdk-cloudformation%2Fstackery-open-bastion-module+v1.0.0).
* Issues related to `Stackery::Open::Bastion::MODULE` should be reported to the [publisher](undefined).

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


class CfnBastionModule(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/stackery-open-bastion-module.CfnBastionModule",
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
        parameters: typing.Optional["CfnBastionModulePropsParameters"] = None,
        resources: typing.Optional["CfnBastionModulePropsResources"] = None,
    ) -> None:
        '''Create a new ``Stackery::Open::Bastion::MODULE``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param parameters: 
        :param resources: 
        '''
        props = CfnBastionModuleProps(parameters=parameters, resources=resources)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnBastionModuleProps":
        '''Resource props.'''
        return typing.cast("CfnBastionModuleProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/stackery-open-bastion-module.CfnBastionModuleProps",
    jsii_struct_bases=[],
    name_mapping={"parameters": "parameters", "resources": "resources"},
)
class CfnBastionModuleProps:
    def __init__(
        self,
        *,
        parameters: typing.Optional["CfnBastionModulePropsParameters"] = None,
        resources: typing.Optional["CfnBastionModulePropsResources"] = None,
    ) -> None:
        '''Schema for Module Fragment of type Stackery::Open::Bastion::MODULE.

        :param parameters: 
        :param resources: 

        :schema: CfnBastionModuleProps
        '''
        if isinstance(parameters, dict):
            parameters = CfnBastionModulePropsParameters(**parameters)
        if isinstance(resources, dict):
            resources = CfnBastionModulePropsResources(**resources)
        self._values: typing.Dict[str, typing.Any] = {}
        if parameters is not None:
            self._values["parameters"] = parameters
        if resources is not None:
            self._values["resources"] = resources

    @builtins.property
    def parameters(self) -> typing.Optional["CfnBastionModulePropsParameters"]:
        '''
        :schema: CfnBastionModuleProps#Parameters
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional["CfnBastionModulePropsParameters"], result)

    @builtins.property
    def resources(self) -> typing.Optional["CfnBastionModulePropsResources"]:
        '''
        :schema: CfnBastionModuleProps#Resources
        '''
        result = self._values.get("resources")
        return typing.cast(typing.Optional["CfnBastionModulePropsResources"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnBastionModuleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/stackery-open-bastion-module.CfnBastionModulePropsParameters",
    jsii_struct_bases=[],
    name_mapping={
        "instance_class": "instanceClass",
        "vpc_id": "vpcId",
        "vpc_subnets": "vpcSubnets",
    },
)
class CfnBastionModulePropsParameters:
    def __init__(
        self,
        *,
        instance_class: typing.Optional["CfnBastionModulePropsParametersInstanceClass"] = None,
        vpc_id: typing.Optional["CfnBastionModulePropsParametersVpcId"] = None,
        vpc_subnets: typing.Optional["CfnBastionModulePropsParametersVpcSubnets"] = None,
    ) -> None:
        '''
        :param instance_class: EC2 instance class to provision.
        :param vpc_id: VPC to run bastion server in.
        :param vpc_subnets: Subnets to pick from to run a bastion server in.

        :schema: CfnBastionModulePropsParameters
        '''
        if isinstance(instance_class, dict):
            instance_class = CfnBastionModulePropsParametersInstanceClass(**instance_class)
        if isinstance(vpc_id, dict):
            vpc_id = CfnBastionModulePropsParametersVpcId(**vpc_id)
        if isinstance(vpc_subnets, dict):
            vpc_subnets = CfnBastionModulePropsParametersVpcSubnets(**vpc_subnets)
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
    ) -> typing.Optional["CfnBastionModulePropsParametersInstanceClass"]:
        '''EC2 instance class to provision.

        :schema: CfnBastionModulePropsParameters#InstanceClass
        '''
        result = self._values.get("instance_class")
        return typing.cast(typing.Optional["CfnBastionModulePropsParametersInstanceClass"], result)

    @builtins.property
    def vpc_id(self) -> typing.Optional["CfnBastionModulePropsParametersVpcId"]:
        '''VPC to run bastion server in.

        :schema: CfnBastionModulePropsParameters#VPCId
        '''
        result = self._values.get("vpc_id")
        return typing.cast(typing.Optional["CfnBastionModulePropsParametersVpcId"], result)

    @builtins.property
    def vpc_subnets(
        self,
    ) -> typing.Optional["CfnBastionModulePropsParametersVpcSubnets"]:
        '''Subnets to pick from to run a bastion server in.

        :schema: CfnBastionModulePropsParameters#VPCSubnets
        '''
        result = self._values.get("vpc_subnets")
        return typing.cast(typing.Optional["CfnBastionModulePropsParametersVpcSubnets"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnBastionModulePropsParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/stackery-open-bastion-module.CfnBastionModulePropsParametersInstanceClass",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnBastionModulePropsParametersInstanceClass:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''EC2 instance class to provision.

        :param description: 
        :param type: 

        :schema: CfnBastionModulePropsParametersInstanceClass
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnBastionModulePropsParametersInstanceClass#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnBastionModulePropsParametersInstanceClass#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnBastionModulePropsParametersInstanceClass(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/stackery-open-bastion-module.CfnBastionModulePropsParametersVpcId",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnBastionModulePropsParametersVpcId:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''VPC to run bastion server in.

        :param description: 
        :param type: 

        :schema: CfnBastionModulePropsParametersVpcId
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnBastionModulePropsParametersVpcId#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnBastionModulePropsParametersVpcId#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnBastionModulePropsParametersVpcId(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/stackery-open-bastion-module.CfnBastionModulePropsParametersVpcSubnets",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnBastionModulePropsParametersVpcSubnets:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Subnets to pick from to run a bastion server in.

        :param description: 
        :param type: 

        :schema: CfnBastionModulePropsParametersVpcSubnets
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnBastionModulePropsParametersVpcSubnets#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnBastionModulePropsParametersVpcSubnets#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnBastionModulePropsParametersVpcSubnets(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/stackery-open-bastion-module.CfnBastionModulePropsResources",
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
class CfnBastionModulePropsResources:
    def __init__(
        self,
        *,
        auto_scaling_group: typing.Optional["CfnBastionModulePropsResourcesAutoScalingGroup"] = None,
        cloud_watch_agent_auto_update: typing.Optional["CfnBastionModulePropsResourcesCloudWatchAgentAutoUpdate"] = None,
        cloud_watch_agent_update_and_start: typing.Optional["CfnBastionModulePropsResourcesCloudWatchAgentUpdateAndStart"] = None,
        iam_instance_profile: typing.Optional["CfnBastionModulePropsResourcesIamInstanceProfile"] = None,
        iam_role: typing.Optional["CfnBastionModulePropsResourcesIamRole"] = None,
        instances_security_group: typing.Optional["CfnBastionModulePropsResourcesInstancesSecurityGroup"] = None,
        launch_configuration: typing.Optional["CfnBastionModulePropsResourcesLaunchConfiguration"] = None,
        ssm_agent_auto_update: typing.Optional["CfnBastionModulePropsResourcesSsmAgentAutoUpdate"] = None,
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

        :schema: CfnBastionModulePropsResources
        '''
        if isinstance(auto_scaling_group, dict):
            auto_scaling_group = CfnBastionModulePropsResourcesAutoScalingGroup(**auto_scaling_group)
        if isinstance(cloud_watch_agent_auto_update, dict):
            cloud_watch_agent_auto_update = CfnBastionModulePropsResourcesCloudWatchAgentAutoUpdate(**cloud_watch_agent_auto_update)
        if isinstance(cloud_watch_agent_update_and_start, dict):
            cloud_watch_agent_update_and_start = CfnBastionModulePropsResourcesCloudWatchAgentUpdateAndStart(**cloud_watch_agent_update_and_start)
        if isinstance(iam_instance_profile, dict):
            iam_instance_profile = CfnBastionModulePropsResourcesIamInstanceProfile(**iam_instance_profile)
        if isinstance(iam_role, dict):
            iam_role = CfnBastionModulePropsResourcesIamRole(**iam_role)
        if isinstance(instances_security_group, dict):
            instances_security_group = CfnBastionModulePropsResourcesInstancesSecurityGroup(**instances_security_group)
        if isinstance(launch_configuration, dict):
            launch_configuration = CfnBastionModulePropsResourcesLaunchConfiguration(**launch_configuration)
        if isinstance(ssm_agent_auto_update, dict):
            ssm_agent_auto_update = CfnBastionModulePropsResourcesSsmAgentAutoUpdate(**ssm_agent_auto_update)
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
    ) -> typing.Optional["CfnBastionModulePropsResourcesAutoScalingGroup"]:
        '''
        :schema: CfnBastionModulePropsResources#AutoScalingGroup
        '''
        result = self._values.get("auto_scaling_group")
        return typing.cast(typing.Optional["CfnBastionModulePropsResourcesAutoScalingGroup"], result)

    @builtins.property
    def cloud_watch_agent_auto_update(
        self,
    ) -> typing.Optional["CfnBastionModulePropsResourcesCloudWatchAgentAutoUpdate"]:
        '''
        :schema: CfnBastionModulePropsResources#CloudWatchAgentAutoUpdate
        '''
        result = self._values.get("cloud_watch_agent_auto_update")
        return typing.cast(typing.Optional["CfnBastionModulePropsResourcesCloudWatchAgentAutoUpdate"], result)

    @builtins.property
    def cloud_watch_agent_update_and_start(
        self,
    ) -> typing.Optional["CfnBastionModulePropsResourcesCloudWatchAgentUpdateAndStart"]:
        '''
        :schema: CfnBastionModulePropsResources#CloudWatchAgentUpdateAndStart
        '''
        result = self._values.get("cloud_watch_agent_update_and_start")
        return typing.cast(typing.Optional["CfnBastionModulePropsResourcesCloudWatchAgentUpdateAndStart"], result)

    @builtins.property
    def iam_instance_profile(
        self,
    ) -> typing.Optional["CfnBastionModulePropsResourcesIamInstanceProfile"]:
        '''
        :schema: CfnBastionModulePropsResources#IAMInstanceProfile
        '''
        result = self._values.get("iam_instance_profile")
        return typing.cast(typing.Optional["CfnBastionModulePropsResourcesIamInstanceProfile"], result)

    @builtins.property
    def iam_role(self) -> typing.Optional["CfnBastionModulePropsResourcesIamRole"]:
        '''
        :schema: CfnBastionModulePropsResources#IAMRole
        '''
        result = self._values.get("iam_role")
        return typing.cast(typing.Optional["CfnBastionModulePropsResourcesIamRole"], result)

    @builtins.property
    def instances_security_group(
        self,
    ) -> typing.Optional["CfnBastionModulePropsResourcesInstancesSecurityGroup"]:
        '''
        :schema: CfnBastionModulePropsResources#InstancesSecurityGroup
        '''
        result = self._values.get("instances_security_group")
        return typing.cast(typing.Optional["CfnBastionModulePropsResourcesInstancesSecurityGroup"], result)

    @builtins.property
    def launch_configuration(
        self,
    ) -> typing.Optional["CfnBastionModulePropsResourcesLaunchConfiguration"]:
        '''
        :schema: CfnBastionModulePropsResources#LaunchConfiguration
        '''
        result = self._values.get("launch_configuration")
        return typing.cast(typing.Optional["CfnBastionModulePropsResourcesLaunchConfiguration"], result)

    @builtins.property
    def ssm_agent_auto_update(
        self,
    ) -> typing.Optional["CfnBastionModulePropsResourcesSsmAgentAutoUpdate"]:
        '''
        :schema: CfnBastionModulePropsResources#SSMAgentAutoUpdate
        '''
        result = self._values.get("ssm_agent_auto_update")
        return typing.cast(typing.Optional["CfnBastionModulePropsResourcesSsmAgentAutoUpdate"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnBastionModulePropsResources(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/stackery-open-bastion-module.CfnBastionModulePropsResourcesAutoScalingGroup",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnBastionModulePropsResourcesAutoScalingGroup:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnBastionModulePropsResourcesAutoScalingGroup
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnBastionModulePropsResourcesAutoScalingGroup#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnBastionModulePropsResourcesAutoScalingGroup#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnBastionModulePropsResourcesAutoScalingGroup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/stackery-open-bastion-module.CfnBastionModulePropsResourcesCloudWatchAgentAutoUpdate",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnBastionModulePropsResourcesCloudWatchAgentAutoUpdate:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnBastionModulePropsResourcesCloudWatchAgentAutoUpdate
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnBastionModulePropsResourcesCloudWatchAgentAutoUpdate#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnBastionModulePropsResourcesCloudWatchAgentAutoUpdate#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnBastionModulePropsResourcesCloudWatchAgentAutoUpdate(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/stackery-open-bastion-module.CfnBastionModulePropsResourcesCloudWatchAgentUpdateAndStart",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnBastionModulePropsResourcesCloudWatchAgentUpdateAndStart:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnBastionModulePropsResourcesCloudWatchAgentUpdateAndStart
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnBastionModulePropsResourcesCloudWatchAgentUpdateAndStart#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnBastionModulePropsResourcesCloudWatchAgentUpdateAndStart#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnBastionModulePropsResourcesCloudWatchAgentUpdateAndStart(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/stackery-open-bastion-module.CfnBastionModulePropsResourcesIamInstanceProfile",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnBastionModulePropsResourcesIamInstanceProfile:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnBastionModulePropsResourcesIamInstanceProfile
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnBastionModulePropsResourcesIamInstanceProfile#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnBastionModulePropsResourcesIamInstanceProfile#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnBastionModulePropsResourcesIamInstanceProfile(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/stackery-open-bastion-module.CfnBastionModulePropsResourcesIamRole",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnBastionModulePropsResourcesIamRole:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnBastionModulePropsResourcesIamRole
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnBastionModulePropsResourcesIamRole#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnBastionModulePropsResourcesIamRole#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnBastionModulePropsResourcesIamRole(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/stackery-open-bastion-module.CfnBastionModulePropsResourcesInstancesSecurityGroup",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnBastionModulePropsResourcesInstancesSecurityGroup:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnBastionModulePropsResourcesInstancesSecurityGroup
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnBastionModulePropsResourcesInstancesSecurityGroup#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnBastionModulePropsResourcesInstancesSecurityGroup#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnBastionModulePropsResourcesInstancesSecurityGroup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/stackery-open-bastion-module.CfnBastionModulePropsResourcesLaunchConfiguration",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnBastionModulePropsResourcesLaunchConfiguration:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnBastionModulePropsResourcesLaunchConfiguration
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnBastionModulePropsResourcesLaunchConfiguration#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnBastionModulePropsResourcesLaunchConfiguration#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnBastionModulePropsResourcesLaunchConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/stackery-open-bastion-module.CfnBastionModulePropsResourcesSsmAgentAutoUpdate",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnBastionModulePropsResourcesSsmAgentAutoUpdate:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnBastionModulePropsResourcesSsmAgentAutoUpdate
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnBastionModulePropsResourcesSsmAgentAutoUpdate#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnBastionModulePropsResourcesSsmAgentAutoUpdate#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnBastionModulePropsResourcesSsmAgentAutoUpdate(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnBastionModule",
    "CfnBastionModuleProps",
    "CfnBastionModulePropsParameters",
    "CfnBastionModulePropsParametersInstanceClass",
    "CfnBastionModulePropsParametersVpcId",
    "CfnBastionModulePropsParametersVpcSubnets",
    "CfnBastionModulePropsResources",
    "CfnBastionModulePropsResourcesAutoScalingGroup",
    "CfnBastionModulePropsResourcesCloudWatchAgentAutoUpdate",
    "CfnBastionModulePropsResourcesCloudWatchAgentUpdateAndStart",
    "CfnBastionModulePropsResourcesIamInstanceProfile",
    "CfnBastionModulePropsResourcesIamRole",
    "CfnBastionModulePropsResourcesInstancesSecurityGroup",
    "CfnBastionModulePropsResourcesLaunchConfiguration",
    "CfnBastionModulePropsResourcesSsmAgentAutoUpdate",
]

publication.publish()
