'''
# AWS CDK CloudFormation Constructs for Atlassian::Opsgenie::Integration

Opsgenie Integration Resource definition

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


class CfnIntegration(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/atlassian-opsgenie-integration.CfnIntegration",
):
    '''A CloudFormation ``Atlassian::Opsgenie::Integration``.

    :cloudformationResource: Atlassian::Opsgenie::Integration
    :link: https://github.com/opsgenie/opsgenie-cloudformation-resources
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        enabled: builtins.bool,
        integration_type: builtins.str,
        name: builtins.str,
        opsgenie_api_endpoint: builtins.str,
        opsgenie_api_key: builtins.str,
        allow_configuration_access: typing.Optional[builtins.bool] = None,
        allow_delete_access: typing.Optional[builtins.bool] = None,
        allow_read_access: typing.Optional[builtins.bool] = None,
        allow_write_access: typing.Optional[builtins.bool] = None,
        owner_team_id: typing.Optional[builtins.str] = None,
        owner_team_name: typing.Optional[builtins.str] = None,
        responders: typing.Optional[typing.Sequence["RespondersProperty"]] = None,
    ) -> None:
        '''Create a new ``Atlassian::Opsgenie::Integration``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param enabled: Integration status, default is true.
        :param integration_type: Integration types, only api integration types supported.
        :param name: Integration name.
        :param opsgenie_api_endpoint: 
        :param opsgenie_api_key: 
        :param allow_configuration_access: This parameter is for allowing or restricting the configuration access.
        :param allow_delete_access: This parameter is for configuring the delete access of integration.
        :param allow_read_access: This parameter is for configuring the read access of integration.
        :param allow_write_access: This parameter is for configuring the write access of integration.
        :param owner_team_id: Id of the integration owner team.
        :param owner_team_name: Name of the integration owner team.
        :param responders: 
        '''
        props = CfnIntegrationProps(
            enabled=enabled,
            integration_type=integration_type,
            name=name,
            opsgenie_api_endpoint=opsgenie_api_endpoint,
            opsgenie_api_key=opsgenie_api_key,
            allow_configuration_access=allow_configuration_access,
            allow_delete_access=allow_delete_access,
            allow_read_access=allow_read_access,
            allow_write_access=allow_write_access,
            owner_team_id=owner_team_id,
            owner_team_name=owner_team_name,
            responders=responders,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrIntegrationApiKey")
    def attr_integration_api_key(self) -> builtins.str:
        '''Attribute ``Atlassian::Opsgenie::Integration.IntegrationApiKey``.

        :link: https://github.com/opsgenie/opsgenie-cloudformation-resources
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrIntegrationApiKey"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrIntegrationId")
    def attr_integration_id(self) -> builtins.str:
        '''Attribute ``Atlassian::Opsgenie::Integration.IntegrationId``.

        :link: https://github.com/opsgenie/opsgenie-cloudformation-resources
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrIntegrationId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnIntegrationProps":
        '''Resource props.'''
        return typing.cast("CfnIntegrationProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/atlassian-opsgenie-integration.CfnIntegrationProps",
    jsii_struct_bases=[],
    name_mapping={
        "enabled": "enabled",
        "integration_type": "integrationType",
        "name": "name",
        "opsgenie_api_endpoint": "opsgenieApiEndpoint",
        "opsgenie_api_key": "opsgenieApiKey",
        "allow_configuration_access": "allowConfigurationAccess",
        "allow_delete_access": "allowDeleteAccess",
        "allow_read_access": "allowReadAccess",
        "allow_write_access": "allowWriteAccess",
        "owner_team_id": "ownerTeamId",
        "owner_team_name": "ownerTeamName",
        "responders": "responders",
    },
)
class CfnIntegrationProps:
    def __init__(
        self,
        *,
        enabled: builtins.bool,
        integration_type: builtins.str,
        name: builtins.str,
        opsgenie_api_endpoint: builtins.str,
        opsgenie_api_key: builtins.str,
        allow_configuration_access: typing.Optional[builtins.bool] = None,
        allow_delete_access: typing.Optional[builtins.bool] = None,
        allow_read_access: typing.Optional[builtins.bool] = None,
        allow_write_access: typing.Optional[builtins.bool] = None,
        owner_team_id: typing.Optional[builtins.str] = None,
        owner_team_name: typing.Optional[builtins.str] = None,
        responders: typing.Optional[typing.Sequence["RespondersProperty"]] = None,
    ) -> None:
        '''Opsgenie Integration Resource definition.

        :param enabled: Integration status, default is true.
        :param integration_type: Integration types, only api integration types supported.
        :param name: Integration name.
        :param opsgenie_api_endpoint: 
        :param opsgenie_api_key: 
        :param allow_configuration_access: This parameter is for allowing or restricting the configuration access.
        :param allow_delete_access: This parameter is for configuring the delete access of integration.
        :param allow_read_access: This parameter is for configuring the read access of integration.
        :param allow_write_access: This parameter is for configuring the write access of integration.
        :param owner_team_id: Id of the integration owner team.
        :param owner_team_name: Name of the integration owner team.
        :param responders: 

        :schema: CfnIntegrationProps
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "enabled": enabled,
            "integration_type": integration_type,
            "name": name,
            "opsgenie_api_endpoint": opsgenie_api_endpoint,
            "opsgenie_api_key": opsgenie_api_key,
        }
        if allow_configuration_access is not None:
            self._values["allow_configuration_access"] = allow_configuration_access
        if allow_delete_access is not None:
            self._values["allow_delete_access"] = allow_delete_access
        if allow_read_access is not None:
            self._values["allow_read_access"] = allow_read_access
        if allow_write_access is not None:
            self._values["allow_write_access"] = allow_write_access
        if owner_team_id is not None:
            self._values["owner_team_id"] = owner_team_id
        if owner_team_name is not None:
            self._values["owner_team_name"] = owner_team_name
        if responders is not None:
            self._values["responders"] = responders

    @builtins.property
    def enabled(self) -> builtins.bool:
        '''Integration status, default is true.

        :schema: CfnIntegrationProps#Enabled
        '''
        result = self._values.get("enabled")
        assert result is not None, "Required property 'enabled' is missing"
        return typing.cast(builtins.bool, result)

    @builtins.property
    def integration_type(self) -> builtins.str:
        '''Integration types, only api integration types supported.

        :schema: CfnIntegrationProps#IntegrationType
        '''
        result = self._values.get("integration_type")
        assert result is not None, "Required property 'integration_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Integration name.

        :schema: CfnIntegrationProps#Name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def opsgenie_api_endpoint(self) -> builtins.str:
        '''
        :schema: CfnIntegrationProps#OpsgenieApiEndpoint
        '''
        result = self._values.get("opsgenie_api_endpoint")
        assert result is not None, "Required property 'opsgenie_api_endpoint' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def opsgenie_api_key(self) -> builtins.str:
        '''
        :schema: CfnIntegrationProps#OpsgenieApiKey
        '''
        result = self._values.get("opsgenie_api_key")
        assert result is not None, "Required property 'opsgenie_api_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allow_configuration_access(self) -> typing.Optional[builtins.bool]:
        '''This parameter is for allowing or restricting the configuration access.

        :schema: CfnIntegrationProps#AllowConfigurationAccess
        '''
        result = self._values.get("allow_configuration_access")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def allow_delete_access(self) -> typing.Optional[builtins.bool]:
        '''This parameter is for configuring the delete access of integration.

        :schema: CfnIntegrationProps#AllowDeleteAccess
        '''
        result = self._values.get("allow_delete_access")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def allow_read_access(self) -> typing.Optional[builtins.bool]:
        '''This parameter is for configuring the read access of integration.

        :schema: CfnIntegrationProps#AllowReadAccess
        '''
        result = self._values.get("allow_read_access")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def allow_write_access(self) -> typing.Optional[builtins.bool]:
        '''This parameter is for configuring the write access of integration.

        :schema: CfnIntegrationProps#AllowWriteAccess
        '''
        result = self._values.get("allow_write_access")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def owner_team_id(self) -> typing.Optional[builtins.str]:
        '''Id of the integration owner team.

        :schema: CfnIntegrationProps#OwnerTeamId
        '''
        result = self._values.get("owner_team_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def owner_team_name(self) -> typing.Optional[builtins.str]:
        '''Name of the integration owner team.

        :schema: CfnIntegrationProps#OwnerTeamName
        '''
        result = self._values.get("owner_team_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def responders(self) -> typing.Optional[typing.List["RespondersProperty"]]:
        '''
        :schema: CfnIntegrationProps#Responders
        '''
        result = self._values.get("responders")
        return typing.cast(typing.Optional[typing.List["RespondersProperty"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnIntegrationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/atlassian-opsgenie-integration.RespondersProperty",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "type": "type", "username": "username"},
)
class RespondersProperty:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
        username: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Responder name if available.
        :param type: Responder type.
        :param username: Responder username, if responder type is user.

        :schema: respondersProperty
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if type is not None:
            self._values["type"] = type
        if username is not None:
            self._values["username"] = username

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Responder name if available.

        :schema: respondersProperty#name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Responder type.

        :schema: respondersProperty#type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def username(self) -> typing.Optional[builtins.str]:
        '''Responder username, if responder type is user.

        :schema: respondersProperty#username
        '''
        result = self._values.get("username")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RespondersProperty(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnIntegration",
    "CfnIntegrationProps",
    "RespondersProperty",
]

publication.publish()
