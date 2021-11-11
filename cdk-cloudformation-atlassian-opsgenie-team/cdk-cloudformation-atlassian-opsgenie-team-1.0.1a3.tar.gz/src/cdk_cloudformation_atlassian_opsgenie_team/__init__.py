'''
# atlassian-opsgenie-team

> AWS CDK [L1 construct](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html) and data structures for the [AWS CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) type `Atlassian::Opsgenie::Team` v1.0.1.

## Description

Opsgenie Team resource schema

## References

* [Source](https://github.com/opsgenie/opsgenie-cloudformation-resources)

## Usage

In order to use this library, you will need to activate this AWS CloudFormation Registry type in your account. You can do this via the AWS Management Console or using the [AWS CLI](https://aws.amazon.com/cli/) using the following command:

```sh
aws cloudformation activate-type \
  --type-name Atlassian::Opsgenie::Team \
  --publisher-id 4fb8713ab4ce2587ce74e0559d7661bb6e01e72b \
  --type RESOURCE \
  --execution-role-arn ROLE-ARN
```

Alternatively:

```sh
aws cloudformation activate-type \
  --public-type-arn arn:aws:cloudformation:us-east-1::type/resource/4fb8713ab4ce2587ce74e0559d7661bb6e01e72b/Atlassian-Opsgenie-Team \
  --execution-role-arn ROLE-ARN
```

You can find more information about activating this type in the [AWS CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html).

## Feedback

This library is auto-generated and published to all supported programming languages by the [cdklabs/cdk-cloudformation](https://github.com/cdklabs/cdk-cloudformation) project based on the API schema published for `Atlassian::Opsgenie::Team`.

* Issues related to this generated library should be [reported here](https://github.com/cdklabs/cdk-cloudformation/issues/new?title=Issue+with+%40cdk-cloudformation%2Fatlassian-opsgenie-team+v1.0.1).
* Issues related to `Atlassian::Opsgenie::Team` should be reported to the [publisher](https://github.com/opsgenie/opsgenie-cloudformation-resources).

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


class CfnTeam(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/atlassian-opsgenie-team.CfnTeam",
):
    '''A CloudFormation ``Atlassian::Opsgenie::Team``.

    :cloudformationResource: Atlassian::Opsgenie::Team
    :link: https://github.com/opsgenie/opsgenie-cloudformation-resources
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        members: typing.Optional[typing.Sequence["Member"]] = None,
        opsgenie_api_endpoint: typing.Optional[builtins.str] = None,
        opsgenie_api_key: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``Atlassian::Opsgenie::Team``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param name: Team name.
        :param description: Team description.
        :param members: Array of members.
        :param opsgenie_api_endpoint: Api endpoint.
        :param opsgenie_api_key: Api Key.
        '''
        props = CfnTeamProps(
            name=name,
            description=description,
            members=members,
            opsgenie_api_endpoint=opsgenie_api_endpoint,
            opsgenie_api_key=opsgenie_api_key,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrTeamId")
    def attr_team_id(self) -> builtins.str:
        '''Attribute ``Atlassian::Opsgenie::Team.TeamId``.

        :link: https://github.com/opsgenie/opsgenie-cloudformation-resources
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrTeamId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnTeamProps":
        '''Resource props.'''
        return typing.cast("CfnTeamProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/atlassian-opsgenie-team.CfnTeamProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "description": "description",
        "members": "members",
        "opsgenie_api_endpoint": "opsgenieApiEndpoint",
        "opsgenie_api_key": "opsgenieApiKey",
    },
)
class CfnTeamProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        members: typing.Optional[typing.Sequence["Member"]] = None,
        opsgenie_api_endpoint: typing.Optional[builtins.str] = None,
        opsgenie_api_key: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Opsgenie Team resource schema.

        :param name: Team name.
        :param description: Team description.
        :param members: Array of members.
        :param opsgenie_api_endpoint: Api endpoint.
        :param opsgenie_api_key: Api Key.

        :schema: CfnTeamProps
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if members is not None:
            self._values["members"] = members
        if opsgenie_api_endpoint is not None:
            self._values["opsgenie_api_endpoint"] = opsgenie_api_endpoint
        if opsgenie_api_key is not None:
            self._values["opsgenie_api_key"] = opsgenie_api_key

    @builtins.property
    def name(self) -> builtins.str:
        '''Team name.

        :schema: CfnTeamProps#Name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Team description.

        :schema: CfnTeamProps#Description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def members(self) -> typing.Optional[typing.List["Member"]]:
        '''Array of members.

        :schema: CfnTeamProps#Members
        '''
        result = self._values.get("members")
        return typing.cast(typing.Optional[typing.List["Member"]], result)

    @builtins.property
    def opsgenie_api_endpoint(self) -> typing.Optional[builtins.str]:
        '''Api endpoint.

        :schema: CfnTeamProps#OpsgenieApiEndpoint
        '''
        result = self._values.get("opsgenie_api_endpoint")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def opsgenie_api_key(self) -> typing.Optional[builtins.str]:
        '''Api Key.

        :schema: CfnTeamProps#OpsgenieApiKey
        '''
        result = self._values.get("opsgenie_api_key")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnTeamProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/atlassian-opsgenie-team.Member",
    jsii_struct_bases=[],
    name_mapping={"role": "role", "user_id": "userId"},
)
class Member:
    def __init__(
        self,
        *,
        role: typing.Optional[builtins.str] = None,
        user_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param role: 
        :param user_id: 

        :schema: Member
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if role is not None:
            self._values["role"] = role
        if user_id is not None:
            self._values["user_id"] = user_id

    @builtins.property
    def role(self) -> typing.Optional[builtins.str]:
        '''
        :schema: Member#Role
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def user_id(self) -> typing.Optional[builtins.str]:
        '''
        :schema: Member#UserId
        '''
        result = self._values.get("user_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Member(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnTeam",
    "CfnTeamProps",
    "Member",
]

publication.publish()
