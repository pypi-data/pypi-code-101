'''
# AWS CDK CloudFormation Constructs for TF::Random::Uuid

CloudFormation equivalent of random_uuid

## References

* [Documentation](https://github.com/iann0036/cfn-tf-custom-types/blob/docs/resources/random/TF-Random-Uuid/docs/README.md)
* [Source](https://github.com/iann0036/cfn-tf-custom-types.git)

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


class CfnUuid(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/tf-random-uuid.CfnUuid",
):
    '''A CloudFormation ``TF::Random::Uuid``.

    :cloudformationResource: TF::Random::Uuid
    :link: https://github.com/iann0036/cfn-tf-custom-types.git
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        keepers: typing.Optional[typing.Sequence["KeepersDefinition"]] = None,
    ) -> None:
        '''Create a new ``TF::Random::Uuid``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param keepers: 
        '''
        props = CfnUuidProps(keepers=keepers)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''Attribute ``TF::Random::Uuid.Id``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrResult")
    def attr_result(self) -> builtins.str:
        '''Attribute ``TF::Random::Uuid.Result``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrResult"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrTfcfnid")
    def attr_tfcfnid(self) -> builtins.str:
        '''Attribute ``TF::Random::Uuid.tfcfnid``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrTfcfnid"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnUuidProps":
        '''Resource props.'''
        return typing.cast("CfnUuidProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/tf-random-uuid.CfnUuidProps",
    jsii_struct_bases=[],
    name_mapping={"keepers": "keepers"},
)
class CfnUuidProps:
    def __init__(
        self,
        *,
        keepers: typing.Optional[typing.Sequence["KeepersDefinition"]] = None,
    ) -> None:
        '''CloudFormation equivalent of random_uuid.

        :param keepers: 

        :schema: CfnUuidProps
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if keepers is not None:
            self._values["keepers"] = keepers

    @builtins.property
    def keepers(self) -> typing.Optional[typing.List["KeepersDefinition"]]:
        '''
        :schema: CfnUuidProps#Keepers
        '''
        result = self._values.get("keepers")
        return typing.cast(typing.Optional[typing.List["KeepersDefinition"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnUuidProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/tf-random-uuid.KeepersDefinition",
    jsii_struct_bases=[],
    name_mapping={"map_key": "mapKey", "map_value": "mapValue"},
)
class KeepersDefinition:
    def __init__(self, *, map_key: builtins.str, map_value: builtins.str) -> None:
        '''
        :param map_key: 
        :param map_value: 

        :schema: KeepersDefinition
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "map_key": map_key,
            "map_value": map_value,
        }

    @builtins.property
    def map_key(self) -> builtins.str:
        '''
        :schema: KeepersDefinition#MapKey
        '''
        result = self._values.get("map_key")
        assert result is not None, "Required property 'map_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def map_value(self) -> builtins.str:
        '''
        :schema: KeepersDefinition#MapValue
        '''
        result = self._values.get("map_value")
        assert result is not None, "Required property 'map_value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KeepersDefinition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnUuid",
    "CfnUuidProps",
    "KeepersDefinition",
]

publication.publish()
