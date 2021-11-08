'''
# AWS CDK CloudFormation Constructs for MongoDB::Atlas::Project

Retrieves or creates projects in any given Atlas organization.

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
    jsii_type="@cdk-cloudformation/mongodb-atlas-project.ApiKeyDefinition",
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


class CfnProject(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/mongodb-atlas-project.CfnProject",
):
    '''A CloudFormation ``MongoDB::Atlas::Project``.

    :cloudformationResource: MongoDB::Atlas::Project
    :link: http://unknown-url
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        org_id: builtins.str,
        api_keys: typing.Optional[ApiKeyDefinition] = None,
        cluster_count: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Create a new ``MongoDB::Atlas::Project``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param name: Name of the project to create.
        :param org_id: Unique identifier of the organization within which to create the project.
        :param api_keys: 
        :param cluster_count: The number of Atlas clusters deployed in the project.
        '''
        props = CfnProjectProps(
            name=name, org_id=org_id, api_keys=api_keys, cluster_count=cluster_count
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrCreated")
    def attr_created(self) -> builtins.str:
        '''Attribute ``MongoDB::Atlas::Project.Created``.

        :link: http://unknown-url
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreated"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''Attribute ``MongoDB::Atlas::Project.Id``.

        :link: http://unknown-url
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnProjectProps":
        '''Resource props.'''
        return typing.cast("CfnProjectProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/mongodb-atlas-project.CfnProjectProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "org_id": "orgId",
        "api_keys": "apiKeys",
        "cluster_count": "clusterCount",
    },
)
class CfnProjectProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        org_id: builtins.str,
        api_keys: typing.Optional[ApiKeyDefinition] = None,
        cluster_count: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Retrieves or creates projects in any given Atlas organization.

        :param name: Name of the project to create.
        :param org_id: Unique identifier of the organization within which to create the project.
        :param api_keys: 
        :param cluster_count: The number of Atlas clusters deployed in the project.

        :schema: CfnProjectProps
        '''
        if isinstance(api_keys, dict):
            api_keys = ApiKeyDefinition(**api_keys)
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "org_id": org_id,
        }
        if api_keys is not None:
            self._values["api_keys"] = api_keys
        if cluster_count is not None:
            self._values["cluster_count"] = cluster_count

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the project to create.

        :schema: CfnProjectProps#Name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def org_id(self) -> builtins.str:
        '''Unique identifier of the organization within which to create the project.

        :schema: CfnProjectProps#OrgId
        '''
        result = self._values.get("org_id")
        assert result is not None, "Required property 'org_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def api_keys(self) -> typing.Optional[ApiKeyDefinition]:
        '''
        :schema: CfnProjectProps#ApiKeys
        '''
        result = self._values.get("api_keys")
        return typing.cast(typing.Optional[ApiKeyDefinition], result)

    @builtins.property
    def cluster_count(self) -> typing.Optional[jsii.Number]:
        '''The number of Atlas clusters deployed in the project.

        :schema: CfnProjectProps#ClusterCount
        '''
        result = self._values.get("cluster_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnProjectProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ApiKeyDefinition",
    "CfnProject",
    "CfnProjectProps",
]

publication.publish()
