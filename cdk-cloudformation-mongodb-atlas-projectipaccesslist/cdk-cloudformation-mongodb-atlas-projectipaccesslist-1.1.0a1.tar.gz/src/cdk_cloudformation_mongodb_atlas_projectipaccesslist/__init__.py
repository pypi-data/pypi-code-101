'''
# AWS CDK CloudFormation Constructs for MongoDB::Atlas::ProjectIpAccessList

An example resource schema demonstrating some basic constructs and validation rules.

## References

* [Source](https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git)

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
    jsii_type="@cdk-cloudformation/mongodb-atlas-projectipaccesslist.AccessListDefinition",
    jsii_struct_bases=[],
    name_mapping={
        "aws_security_group": "awsSecurityGroup",
        "cidr_block": "cidrBlock",
        "comment": "comment",
        "ip_address": "ipAddress",
        "project_id": "projectId",
    },
)
class AccessListDefinition:
    def __init__(
        self,
        *,
        aws_security_group: typing.Optional[builtins.str] = None,
        cidr_block: typing.Optional[builtins.str] = None,
        comment: typing.Optional[builtins.str] = None,
        ip_address: typing.Optional[builtins.str] = None,
        project_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aws_security_group: ID of the AWS security group to allow access. Mutually exclusive with CIDRBlock and IPAddress.
        :param cidr_block: Accessable entry in Classless Inter-Domain Routing (CIDR) notation. Mutually exclusive with ipAddress and AwsSecurityGroup.
        :param comment: Comment associated with the ip access list entry.
        :param ip_address: Accessable IP address. Mutually exclusive with CIDRBlock and AwsSecurityGroup.
        :param project_id: The unique identifier for the project to which you want to add one or more ip access list entries.

        :schema: accessListDefinition
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if aws_security_group is not None:
            self._values["aws_security_group"] = aws_security_group
        if cidr_block is not None:
            self._values["cidr_block"] = cidr_block
        if comment is not None:
            self._values["comment"] = comment
        if ip_address is not None:
            self._values["ip_address"] = ip_address
        if project_id is not None:
            self._values["project_id"] = project_id

    @builtins.property
    def aws_security_group(self) -> typing.Optional[builtins.str]:
        '''ID of the AWS security group to allow access.

        Mutually exclusive with CIDRBlock and IPAddress.

        :schema: accessListDefinition#AwsSecurityGroup
        '''
        result = self._values.get("aws_security_group")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cidr_block(self) -> typing.Optional[builtins.str]:
        '''Accessable entry in Classless Inter-Domain Routing (CIDR) notation.

        Mutually exclusive with ipAddress and AwsSecurityGroup.

        :schema: accessListDefinition#CIDRBlock
        '''
        result = self._values.get("cidr_block")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        '''Comment associated with the ip access list entry.

        :schema: accessListDefinition#Comment
        '''
        result = self._values.get("comment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ip_address(self) -> typing.Optional[builtins.str]:
        '''Accessable IP address.

        Mutually exclusive with CIDRBlock and AwsSecurityGroup.

        :schema: accessListDefinition#IPAddress
        '''
        result = self._values.get("ip_address")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def project_id(self) -> typing.Optional[builtins.str]:
        '''The unique identifier for the project to which you want to add one or more ip access list entries.

        :schema: accessListDefinition#ProjectId
        '''
        result = self._values.get("project_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AccessListDefinition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/mongodb-atlas-projectipaccesslist.ApiKeyDefinition",
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


class CfnProjectipaccesslist(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/mongodb-atlas-projectipaccesslist.CfnProjectipaccesslist",
):
    '''A CloudFormation ``MongoDB::Atlas::ProjectIpAccessList``.

    :cloudformationResource: MongoDB::Atlas::ProjectIpAccessList
    :link: https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        access_list: typing.Sequence[AccessListDefinition],
        api_keys: ApiKeyDefinition,
        project_id: builtins.str,
        total_count: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Create a new ``MongoDB::Atlas::ProjectIpAccessList``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param access_list: 
        :param api_keys: 
        :param project_id: The unique identifier for the project to which you want to add one or more ip access list entries.
        :param total_count: The unique identifier for the Project ip access list rules.
        '''
        props = CfnProjectipaccesslistProps(
            access_list=access_list,
            api_keys=api_keys,
            project_id=project_id,
            total_count=total_count,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''Attribute ``MongoDB::Atlas::ProjectIpAccessList.Id``.

        :link: https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnProjectipaccesslistProps":
        '''Resource props.'''
        return typing.cast("CfnProjectipaccesslistProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/mongodb-atlas-projectipaccesslist.CfnProjectipaccesslistProps",
    jsii_struct_bases=[],
    name_mapping={
        "access_list": "accessList",
        "api_keys": "apiKeys",
        "project_id": "projectId",
        "total_count": "totalCount",
    },
)
class CfnProjectipaccesslistProps:
    def __init__(
        self,
        *,
        access_list: typing.Sequence[AccessListDefinition],
        api_keys: ApiKeyDefinition,
        project_id: builtins.str,
        total_count: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''An example resource schema demonstrating some basic constructs and validation rules.

        :param access_list: 
        :param api_keys: 
        :param project_id: The unique identifier for the project to which you want to add one or more ip access list entries.
        :param total_count: The unique identifier for the Project ip access list rules.

        :schema: CfnProjectipaccesslistProps
        '''
        if isinstance(api_keys, dict):
            api_keys = ApiKeyDefinition(**api_keys)
        self._values: typing.Dict[str, typing.Any] = {
            "access_list": access_list,
            "api_keys": api_keys,
            "project_id": project_id,
        }
        if total_count is not None:
            self._values["total_count"] = total_count

    @builtins.property
    def access_list(self) -> typing.List[AccessListDefinition]:
        '''
        :schema: CfnProjectipaccesslistProps#AccessList
        '''
        result = self._values.get("access_list")
        assert result is not None, "Required property 'access_list' is missing"
        return typing.cast(typing.List[AccessListDefinition], result)

    @builtins.property
    def api_keys(self) -> ApiKeyDefinition:
        '''
        :schema: CfnProjectipaccesslistProps#ApiKeys
        '''
        result = self._values.get("api_keys")
        assert result is not None, "Required property 'api_keys' is missing"
        return typing.cast(ApiKeyDefinition, result)

    @builtins.property
    def project_id(self) -> builtins.str:
        '''The unique identifier for the project to which you want to add one or more ip access list entries.

        :schema: CfnProjectipaccesslistProps#ProjectId
        '''
        result = self._values.get("project_id")
        assert result is not None, "Required property 'project_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def total_count(self) -> typing.Optional[jsii.Number]:
        '''The unique identifier for the Project ip access list rules.

        :schema: CfnProjectipaccesslistProps#TotalCount
        '''
        result = self._values.get("total_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnProjectipaccesslistProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AccessListDefinition",
    "ApiKeyDefinition",
    "CfnProjectipaccesslist",
    "CfnProjectipaccesslistProps",
]

publication.publish()
