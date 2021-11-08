'''
# AWS CDK CloudFormation Constructs for Symphonia::OpenSource::CloudFormationArtifactsBucket::MODULE

Schema for Module Fragment of type Symphonia::OpenSource::CloudFormationArtifactsBucket::MODULE

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
    jsii_type="@cdk-cloudformation/symphonia-opensource-cloudformationartifactsbucket-module.CfnModule",
):
    '''A CloudFormation ``Symphonia::OpenSource::CloudFormationArtifactsBucket::MODULE``.

    :cloudformationResource: Symphonia::OpenSource::CloudFormationArtifactsBucket::MODULE
    :link: http://unknown-url
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        resources: typing.Optional["CfnModulePropsResources"] = None,
    ) -> None:
        '''Create a new ``Symphonia::OpenSource::CloudFormationArtifactsBucket::MODULE``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param resources: 
        '''
        props = CfnModuleProps(resources=resources)

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
    jsii_type="@cdk-cloudformation/symphonia-opensource-cloudformationartifactsbucket-module.CfnModuleProps",
    jsii_struct_bases=[],
    name_mapping={"resources": "resources"},
)
class CfnModuleProps:
    def __init__(
        self,
        *,
        resources: typing.Optional["CfnModulePropsResources"] = None,
    ) -> None:
        '''Schema for Module Fragment of type Symphonia::OpenSource::CloudFormationArtifactsBucket::MODULE.

        :param resources: 

        :schema: CfnModuleProps
        '''
        if isinstance(resources, dict):
            resources = CfnModulePropsResources(**resources)
        self._values: typing.Dict[str, typing.Any] = {}
        if resources is not None:
            self._values["resources"] = resources

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
    jsii_type="@cdk-cloudformation/symphonia-opensource-cloudformationartifactsbucket-module.CfnModulePropsResources",
    jsii_struct_bases=[],
    name_mapping={"bucket": "bucket"},
)
class CfnModulePropsResources:
    def __init__(
        self,
        *,
        bucket: typing.Optional["CfnModulePropsResourcesBucket"] = None,
    ) -> None:
        '''
        :param bucket: 

        :schema: CfnModulePropsResources
        '''
        if isinstance(bucket, dict):
            bucket = CfnModulePropsResourcesBucket(**bucket)
        self._values: typing.Dict[str, typing.Any] = {}
        if bucket is not None:
            self._values["bucket"] = bucket

    @builtins.property
    def bucket(self) -> typing.Optional["CfnModulePropsResourcesBucket"]:
        '''
        :schema: CfnModulePropsResources#Bucket
        '''
        result = self._values.get("bucket")
        return typing.cast(typing.Optional["CfnModulePropsResourcesBucket"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResources(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/symphonia-opensource-cloudformationartifactsbucket-module.CfnModulePropsResourcesBucket",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnModulePropsResourcesBucket:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnModulePropsResourcesBucket
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnModulePropsResourcesBucket#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnModulePropsResourcesBucket#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModulePropsResourcesBucket(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnModule",
    "CfnModuleProps",
    "CfnModulePropsResources",
    "CfnModulePropsResourcesBucket",
]

publication.publish()
