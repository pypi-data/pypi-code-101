'''
# AWS CDK CloudFormation Constructs for Atlassian::Opsgenie::User

Opsgenie User

## References

* [Source](https://github.com/opsgenie/opsgenie-cloudformation-resources)

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


class CfnUser(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/atlassian-opsgenie-user.CfnUser",
):
    '''A CloudFormation ``Atlassian::Opsgenie::User``.

    :cloudformationResource: Atlassian::Opsgenie::User
    :link: https://github.com/opsgenie/opsgenie-cloudformation-resources
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        full_name: builtins.str,
        opsgenie_api_endpoint: builtins.str,
        opsgenie_api_key: builtins.str,
        role: builtins.str,
        username: builtins.str,
    ) -> None:
        '''Create a new ``Atlassian::Opsgenie::User``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param full_name: User full name.
        :param opsgenie_api_endpoint: 
        :param opsgenie_api_key: 
        :param role: User role, default is User.
        :param username: Opsgenie Username the mail address of the user.
        '''
        props = CfnUserProps(
            full_name=full_name,
            opsgenie_api_endpoint=opsgenie_api_endpoint,
            opsgenie_api_key=opsgenie_api_key,
            role=role,
            username=username,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrUserId")
    def attr_user_id(self) -> builtins.str:
        '''Attribute ``Atlassian::Opsgenie::User.UserId``.

        :link: https://github.com/opsgenie/opsgenie-cloudformation-resources
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUserId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnUserProps":
        '''Resource props.'''
        return typing.cast("CfnUserProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/atlassian-opsgenie-user.CfnUserProps",
    jsii_struct_bases=[],
    name_mapping={
        "full_name": "fullName",
        "opsgenie_api_endpoint": "opsgenieApiEndpoint",
        "opsgenie_api_key": "opsgenieApiKey",
        "role": "role",
        "username": "username",
    },
)
class CfnUserProps:
    def __init__(
        self,
        *,
        full_name: builtins.str,
        opsgenie_api_endpoint: builtins.str,
        opsgenie_api_key: builtins.str,
        role: builtins.str,
        username: builtins.str,
    ) -> None:
        '''Opsgenie User.

        :param full_name: User full name.
        :param opsgenie_api_endpoint: 
        :param opsgenie_api_key: 
        :param role: User role, default is User.
        :param username: Opsgenie Username the mail address of the user.

        :schema: CfnUserProps
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "full_name": full_name,
            "opsgenie_api_endpoint": opsgenie_api_endpoint,
            "opsgenie_api_key": opsgenie_api_key,
            "role": role,
            "username": username,
        }

    @builtins.property
    def full_name(self) -> builtins.str:
        '''User full name.

        :schema: CfnUserProps#FullName
        '''
        result = self._values.get("full_name")
        assert result is not None, "Required property 'full_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def opsgenie_api_endpoint(self) -> builtins.str:
        '''
        :schema: CfnUserProps#OpsgenieApiEndpoint
        '''
        result = self._values.get("opsgenie_api_endpoint")
        assert result is not None, "Required property 'opsgenie_api_endpoint' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def opsgenie_api_key(self) -> builtins.str:
        '''
        :schema: CfnUserProps#OpsgenieApiKey
        '''
        result = self._values.get("opsgenie_api_key")
        assert result is not None, "Required property 'opsgenie_api_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role(self) -> builtins.str:
        '''User role, default is User.

        :schema: CfnUserProps#Role
        '''
        result = self._values.get("role")
        assert result is not None, "Required property 'role' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def username(self) -> builtins.str:
        '''Opsgenie Username the mail address of the user.

        :schema: CfnUserProps#Username
        '''
        result = self._values.get("username")
        assert result is not None, "Required property 'username' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnUserProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnUser",
    "CfnUserProps",
]

publication.publish()
