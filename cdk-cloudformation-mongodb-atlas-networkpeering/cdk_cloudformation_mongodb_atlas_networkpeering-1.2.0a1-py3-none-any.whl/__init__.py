'''
# AWS CDK CloudFormation Constructs for MongoDB::Atlas::NetworkPeering

This resource allows to create, read, update and delete a network peering

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
    jsii_type="@cdk-cloudformation/mongodb-atlas-networkpeering.ApiKeyDefinition",
    jsii_struct_bases=[],
    name_mapping={"private_key": "privateKey", "public_key": "publicKey"},
)
class ApiKeyDefinition:
    def __init__(
        self,
        *,
        private_key: typing.Optional[builtins.str] = None,
        public_key: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param private_key: 
        :param public_key: 

        :schema: apiKeyDefinition
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if private_key is not None:
            self._values["private_key"] = private_key
        if public_key is not None:
            self._values["public_key"] = public_key

    @builtins.property
    def private_key(self) -> typing.Optional[builtins.str]:
        '''
        :schema: apiKeyDefinition#PrivateKey
        '''
        result = self._values.get("private_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def public_key(self) -> typing.Optional[builtins.str]:
        '''
        :schema: apiKeyDefinition#PublicKey
        '''
        result = self._values.get("public_key")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiKeyDefinition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CfnNetworkpeering(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/mongodb-atlas-networkpeering.CfnNetworkpeering",
):
    '''A CloudFormation ``MongoDB::Atlas::NetworkPeering``.

    :cloudformationResource: MongoDB::Atlas::NetworkPeering
    :link: http://unknown-url
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        api_keys: ApiKeyDefinition,
        project_id: builtins.str,
        vpc_id: builtins.str,
        accepter_region_name: typing.Optional[builtins.str] = None,
        aws_account_id: typing.Optional[builtins.str] = None,
        connection_id: typing.Optional[builtins.str] = None,
        container_id: typing.Optional[builtins.str] = None,
        provider_name: typing.Optional[builtins.str] = None,
        route_table_cidr_block: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``MongoDB::Atlas::NetworkPeering``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param api_keys: 
        :param project_id: The unique identifier of the project.
        :param vpc_id: Unique identifier of the peer VPC.
        :param accepter_region_name: AWS region where the peer VPC resides. Returns null if the region is the same region in which the Atlas VPC resides.
        :param aws_account_id: AWS account ID of the owner of the peer VPC.
        :param connection_id: Unique identifier for the peering connection.
        :param container_id: Unique identifier of the Atlas VPC container for the AWS region.
        :param provider_name: The name of the provider.
        :param route_table_cidr_block: Peer VPC CIDR block or subnet.
        '''
        props = CfnNetworkpeeringProps(
            api_keys=api_keys,
            project_id=project_id,
            vpc_id=vpc_id,
            accepter_region_name=accepter_region_name,
            aws_account_id=aws_account_id,
            connection_id=connection_id,
            container_id=container_id,
            provider_name=provider_name,
            route_table_cidr_block=route_table_cidr_block,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrErrorStateName")
    def attr_error_state_name(self) -> builtins.str:
        '''Attribute ``MongoDB::Atlas::NetworkPeering.ErrorStateName``.

        :link: http://unknown-url
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrErrorStateName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''Attribute ``MongoDB::Atlas::NetworkPeering.Id``.

        :link: http://unknown-url
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrStatusName")
    def attr_status_name(self) -> builtins.str:
        '''Attribute ``MongoDB::Atlas::NetworkPeering.StatusName``.

        :link: http://unknown-url
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatusName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnNetworkpeeringProps":
        '''Resource props.'''
        return typing.cast("CfnNetworkpeeringProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/mongodb-atlas-networkpeering.CfnNetworkpeeringProps",
    jsii_struct_bases=[],
    name_mapping={
        "api_keys": "apiKeys",
        "project_id": "projectId",
        "vpc_id": "vpcId",
        "accepter_region_name": "accepterRegionName",
        "aws_account_id": "awsAccountId",
        "connection_id": "connectionId",
        "container_id": "containerId",
        "provider_name": "providerName",
        "route_table_cidr_block": "routeTableCidrBlock",
    },
)
class CfnNetworkpeeringProps:
    def __init__(
        self,
        *,
        api_keys: ApiKeyDefinition,
        project_id: builtins.str,
        vpc_id: builtins.str,
        accepter_region_name: typing.Optional[builtins.str] = None,
        aws_account_id: typing.Optional[builtins.str] = None,
        connection_id: typing.Optional[builtins.str] = None,
        container_id: typing.Optional[builtins.str] = None,
        provider_name: typing.Optional[builtins.str] = None,
        route_table_cidr_block: typing.Optional[builtins.str] = None,
    ) -> None:
        '''This resource allows to create, read, update and delete a network peering.

        :param api_keys: 
        :param project_id: The unique identifier of the project.
        :param vpc_id: Unique identifier of the peer VPC.
        :param accepter_region_name: AWS region where the peer VPC resides. Returns null if the region is the same region in which the Atlas VPC resides.
        :param aws_account_id: AWS account ID of the owner of the peer VPC.
        :param connection_id: Unique identifier for the peering connection.
        :param container_id: Unique identifier of the Atlas VPC container for the AWS region.
        :param provider_name: The name of the provider.
        :param route_table_cidr_block: Peer VPC CIDR block or subnet.

        :schema: CfnNetworkpeeringProps
        '''
        if isinstance(api_keys, dict):
            api_keys = ApiKeyDefinition(**api_keys)
        self._values: typing.Dict[str, typing.Any] = {
            "api_keys": api_keys,
            "project_id": project_id,
            "vpc_id": vpc_id,
        }
        if accepter_region_name is not None:
            self._values["accepter_region_name"] = accepter_region_name
        if aws_account_id is not None:
            self._values["aws_account_id"] = aws_account_id
        if connection_id is not None:
            self._values["connection_id"] = connection_id
        if container_id is not None:
            self._values["container_id"] = container_id
        if provider_name is not None:
            self._values["provider_name"] = provider_name
        if route_table_cidr_block is not None:
            self._values["route_table_cidr_block"] = route_table_cidr_block

    @builtins.property
    def api_keys(self) -> ApiKeyDefinition:
        '''
        :schema: CfnNetworkpeeringProps#ApiKeys
        '''
        result = self._values.get("api_keys")
        assert result is not None, "Required property 'api_keys' is missing"
        return typing.cast(ApiKeyDefinition, result)

    @builtins.property
    def project_id(self) -> builtins.str:
        '''The unique identifier of the project.

        :schema: CfnNetworkpeeringProps#ProjectId
        '''
        result = self._values.get("project_id")
        assert result is not None, "Required property 'project_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def vpc_id(self) -> builtins.str:
        '''Unique identifier of the peer VPC.

        :schema: CfnNetworkpeeringProps#VpcId
        '''
        result = self._values.get("vpc_id")
        assert result is not None, "Required property 'vpc_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def accepter_region_name(self) -> typing.Optional[builtins.str]:
        '''AWS region where the peer VPC resides.

        Returns null if the region is the same region in which the Atlas VPC resides.

        :schema: CfnNetworkpeeringProps#AccepterRegionName
        '''
        result = self._values.get("accepter_region_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def aws_account_id(self) -> typing.Optional[builtins.str]:
        '''AWS account ID of the owner of the peer VPC.

        :schema: CfnNetworkpeeringProps#AwsAccountId
        '''
        result = self._values.get("aws_account_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def connection_id(self) -> typing.Optional[builtins.str]:
        '''Unique identifier for the peering connection.

        :schema: CfnNetworkpeeringProps#ConnectionId
        '''
        result = self._values.get("connection_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def container_id(self) -> typing.Optional[builtins.str]:
        '''Unique identifier of the Atlas VPC container for the AWS region.

        :schema: CfnNetworkpeeringProps#ContainerId
        '''
        result = self._values.get("container_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def provider_name(self) -> typing.Optional[builtins.str]:
        '''The name of the provider.

        :schema: CfnNetworkpeeringProps#ProviderName
        '''
        result = self._values.get("provider_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def route_table_cidr_block(self) -> typing.Optional[builtins.str]:
        '''Peer VPC CIDR block or subnet.

        :schema: CfnNetworkpeeringProps#RouteTableCIDRBlock
        '''
        result = self._values.get("route_table_cidr_block")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnNetworkpeeringProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ApiKeyDefinition",
    "CfnNetworkpeering",
    "CfnNetworkpeeringProps",
]

publication.publish()
