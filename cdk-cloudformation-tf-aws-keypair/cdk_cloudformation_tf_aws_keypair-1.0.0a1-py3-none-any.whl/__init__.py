'''
# AWS CDK CloudFormation Constructs for TF::AWS::KeyPair

Provides an [EC2 key pair](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html) resource. A key pair is used to control login access to EC2 instances.

Currently this resource requires an existing user-supplied key pair. This key pair's public key will be registered with AWS to allow logging-in to EC2 instances.

When importing an existing key pair the public key material may be in any format supported by AWS. Supported formats (per the [AWS documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html#how-to-generate-your-own-key-and-import-it-to-aws)) are:

* OpenSSH public key format (the format in ~/.ssh/authorized_keys)
* Base64 encoded DER format
* SSH public key file format as specified in RFC4716

## References

* [Documentation](https://github.com/iann0036/cfn-tf-custom-types/blob/docs/resources/aws/TF-AWS-KeyPair/docs/README.md)
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


class CfnKeypair(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/tf-aws-keypair.CfnKeypair",
):
    '''A CloudFormation ``TF::AWS::KeyPair``.

    :cloudformationResource: TF::AWS::KeyPair
    :link: https://github.com/iann0036/cfn-tf-custom-types.git
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        public_key: builtins.str,
        key_name: typing.Optional[builtins.str] = None,
        key_name_prefix: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence["TagsDefinition"]] = None,
        tags_all: typing.Optional[typing.Sequence["TagsAllDefinition"]] = None,
    ) -> None:
        '''Create a new ``TF::AWS::KeyPair``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param public_key: The public key material.
        :param key_name: The name for the key pair.
        :param key_name_prefix: Creates a unique name beginning with the specified prefix. Conflicts with ``key_name``.
        :param tags: Key-value map of resource tags. If configured with a provider ```default_tags`` configuration block <https://www.terraform.io/docs/providers/aws/index.html#default_tags-configuration-block>`_ present, tags with matching keys will overwrite those defined at the provider-level.
        :param tags_all: 
        '''
        props = CfnKeypairProps(
            public_key=public_key,
            key_name=key_name,
            key_name_prefix=key_name_prefix,
            tags=tags,
            tags_all=tags_all,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''Attribute ``TF::AWS::KeyPair.Arn``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrFingerprint")
    def attr_fingerprint(self) -> builtins.str:
        '''Attribute ``TF::AWS::KeyPair.Fingerprint``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrFingerprint"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''Attribute ``TF::AWS::KeyPair.Id``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrKeyPairId")
    def attr_key_pair_id(self) -> builtins.str:
        '''Attribute ``TF::AWS::KeyPair.KeyPairId``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrKeyPairId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrTfcfnid")
    def attr_tfcfnid(self) -> builtins.str:
        '''Attribute ``TF::AWS::KeyPair.tfcfnid``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrTfcfnid"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnKeypairProps":
        '''Resource props.'''
        return typing.cast("CfnKeypairProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/tf-aws-keypair.CfnKeypairProps",
    jsii_struct_bases=[],
    name_mapping={
        "public_key": "publicKey",
        "key_name": "keyName",
        "key_name_prefix": "keyNamePrefix",
        "tags": "tags",
        "tags_all": "tagsAll",
    },
)
class CfnKeypairProps:
    def __init__(
        self,
        *,
        public_key: builtins.str,
        key_name: typing.Optional[builtins.str] = None,
        key_name_prefix: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence["TagsDefinition"]] = None,
        tags_all: typing.Optional[typing.Sequence["TagsAllDefinition"]] = None,
    ) -> None:
        '''Provides an `EC2 key pair <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html>`_ resource. A key pair is used to control login access to EC2 instances.

        Currently this resource requires an existing user-supplied key pair. This key pair's public key will be registered with AWS to allow logging-in to EC2 instances.

        When importing an existing key pair the public key material may be in any format supported by AWS. Supported formats (per the `AWS documentation <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html#how-to-generate-your-own-key-and-import-it-to-aws>`_) are:

        - OpenSSH public key format (the format in ~/.ssh/authorized_keys)
        - Base64 encoded DER format
        - SSH public key file format as specified in RFC4716

        :param public_key: The public key material.
        :param key_name: The name for the key pair.
        :param key_name_prefix: Creates a unique name beginning with the specified prefix. Conflicts with ``key_name``.
        :param tags: Key-value map of resource tags. If configured with a provider ```default_tags`` configuration block <https://www.terraform.io/docs/providers/aws/index.html#default_tags-configuration-block>`_ present, tags with matching keys will overwrite those defined at the provider-level.
        :param tags_all: 

        :schema: CfnKeypairProps
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "public_key": public_key,
        }
        if key_name is not None:
            self._values["key_name"] = key_name
        if key_name_prefix is not None:
            self._values["key_name_prefix"] = key_name_prefix
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all

    @builtins.property
    def public_key(self) -> builtins.str:
        '''The public key material.

        :schema: CfnKeypairProps#PublicKey
        '''
        result = self._values.get("public_key")
        assert result is not None, "Required property 'public_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def key_name(self) -> typing.Optional[builtins.str]:
        '''The name for the key pair.

        :schema: CfnKeypairProps#KeyName
        '''
        result = self._values.get("key_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def key_name_prefix(self) -> typing.Optional[builtins.str]:
        '''Creates a unique name beginning with the specified prefix.

        Conflicts with ``key_name``.

        :schema: CfnKeypairProps#KeyNamePrefix
        '''
        result = self._values.get("key_name_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["TagsDefinition"]]:
        '''Key-value map of resource tags.

        If configured with a provider ```default_tags`` configuration block <https://www.terraform.io/docs/providers/aws/index.html#default_tags-configuration-block>`_ present, tags with matching keys will overwrite those defined at the provider-level.

        :schema: CfnKeypairProps#Tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["TagsDefinition"]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.List["TagsAllDefinition"]]:
        '''
        :schema: CfnKeypairProps#TagsAll
        '''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.List["TagsAllDefinition"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnKeypairProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/tf-aws-keypair.TagsAllDefinition",
    jsii_struct_bases=[],
    name_mapping={"map_key": "mapKey", "map_value": "mapValue"},
)
class TagsAllDefinition:
    def __init__(self, *, map_key: builtins.str, map_value: builtins.str) -> None:
        '''
        :param map_key: 
        :param map_value: 

        :schema: TagsAllDefinition
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "map_key": map_key,
            "map_value": map_value,
        }

    @builtins.property
    def map_key(self) -> builtins.str:
        '''
        :schema: TagsAllDefinition#MapKey
        '''
        result = self._values.get("map_key")
        assert result is not None, "Required property 'map_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def map_value(self) -> builtins.str:
        '''
        :schema: TagsAllDefinition#MapValue
        '''
        result = self._values.get("map_value")
        assert result is not None, "Required property 'map_value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TagsAllDefinition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/tf-aws-keypair.TagsDefinition",
    jsii_struct_bases=[],
    name_mapping={"map_key": "mapKey", "map_value": "mapValue"},
)
class TagsDefinition:
    def __init__(self, *, map_key: builtins.str, map_value: builtins.str) -> None:
        '''
        :param map_key: 
        :param map_value: 

        :schema: TagsDefinition
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "map_key": map_key,
            "map_value": map_value,
        }

    @builtins.property
    def map_key(self) -> builtins.str:
        '''
        :schema: TagsDefinition#MapKey
        '''
        result = self._values.get("map_key")
        assert result is not None, "Required property 'map_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def map_value(self) -> builtins.str:
        '''
        :schema: TagsDefinition#MapValue
        '''
        result = self._values.get("map_value")
        assert result is not None, "Required property 'map_value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TagsDefinition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnKeypair",
    "CfnKeypairProps",
    "TagsAllDefinition",
    "TagsDefinition",
]

publication.publish()
