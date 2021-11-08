'''
CDK Construct to create a KMS Encryption Key
You can define Administrator roles in the Accounts by providing the role name. The Construct will create the role arn if an environment is provided.
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

import aws_cdk.aws_iam
import aws_cdk.aws_kms
import aws_cdk.core


@jsii.interface(jsii_type="kms-encryption-key.IKmsEncryptionKeyProps")
class IKmsEncryptionKeyProps(typing_extensions.Protocol):
    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="keyName")
    def key_name(self) -> builtins.str:
        ...

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="administratorRoleArns")
    def administrator_role_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        ...

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        ...

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="environmentName")
    def environment_name(self) -> typing.Optional[builtins.str]:
        ...


class _IKmsEncryptionKeyPropsProxy:
    __jsii_type__: typing.ClassVar[str] = "kms-encryption-key.IKmsEncryptionKeyProps"

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="keyName")
    def key_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="administratorRoleArns")
    def administrator_role_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "administratorRoleArns"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="environmentName")
    def environment_name(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "environmentName"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IKmsEncryptionKeyProps).__jsii_proxy_class__ = lambda : _IKmsEncryptionKeyPropsProxy


@jsii.implements(IKmsEncryptionKeyProps)
class KmsEncryptionKey(
    aws_cdk.core.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="kms-encryption-key.KmsEncryptionKey",
):
    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        props: typing.Optional[IKmsEncryptionKeyProps] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param props: -
        '''
        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="createKeyPolicy") # type: ignore[misc]
    @builtins.classmethod
    def create_key_policy(
        cls,
        administrator_role_arns: typing.Sequence[builtins.str],
    ) -> aws_cdk.aws_iam.PolicyDocument:
        '''
        :param administrator_role_arns: -
        '''
        return typing.cast(aws_cdk.aws_iam.PolicyDocument, jsii.sinvoke(cls, "createKeyPolicy", [administrator_role_arns]))

    @jsii.member(jsii_name="getAdministratorArns") # type: ignore[misc]
    @builtins.classmethod
    def get_administrator_arns(
        cls,
        administrator_role_arns: typing.Sequence[builtins.str],
    ) -> typing.List[aws_cdk.aws_iam.CompositePrincipal]:
        '''
        :param administrator_role_arns: -
        '''
        return typing.cast(typing.List[aws_cdk.aws_iam.CompositePrincipal], jsii.sinvoke(cls, "getAdministratorArns", [administrator_role_arns]))

    @jsii.member(jsii_name="getArnPrincipals") # type: ignore[misc]
    @builtins.classmethod
    def get_arn_principals(
        cls,
        administrator_role_arns: typing.Sequence[builtins.str],
    ) -> typing.List[aws_cdk.aws_iam.ArnPrincipal]:
        '''
        :param administrator_role_arns: -
        '''
        return typing.cast(typing.List[aws_cdk.aws_iam.ArnPrincipal], jsii.sinvoke(cls, "getArnPrincipals", [administrator_role_arns]))

    @jsii.member(jsii_name="addTags")
    def add_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "addTags", []))

    @jsii.member(jsii_name="createKmsKey")
    def create_kms_key(
        self,
        administrator_role_arns: typing.Sequence[builtins.str],
    ) -> aws_cdk.aws_kms.Key:
        '''
        :param administrator_role_arns: -
        '''
        return typing.cast(aws_cdk.aws_kms.Key, jsii.invoke(self, "createKmsKey", [administrator_role_arns]))

    @jsii.member(jsii_name="getKeyName")
    def get_key_name(
        self,
        key_name: typing.Optional[builtins.str] = None,
    ) -> builtins.str:
        '''
        :param key_name: -
        '''
        return typing.cast(builtins.str, jsii.invoke(self, "getKeyName", [key_name]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="keyName")
    def key_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="kmsKey")
    def kms_key(self) -> aws_cdk.aws_kms.IKey:
        return typing.cast(aws_cdk.aws_kms.IKey, jsii.get(self, "kmsKey"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="environmentName")
    def environment_name(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "environmentName"))


__all__ = [
    "IKmsEncryptionKeyProps",
    "KmsEncryptionKey",
]

publication.publish()
