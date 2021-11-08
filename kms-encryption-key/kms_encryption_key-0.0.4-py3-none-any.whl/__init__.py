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


class KmsEncryptionKey(
    aws_cdk.core.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="kms-encryption-key.KmsEncryptionKey",
):
    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        description: typing.Optional[builtins.str] = None,
        environment_name: typing.Optional[builtins.str] = None,
        key_name: typing.Optional[builtins.str] = None,
        kms_administrator_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param description: 
        :param environment_name: 
        :param key_name: 
        :param kms_administrator_arns: 
        '''
        props = KmsEncryptionKeyProps(
            description=description,
            environment_name=environment_name,
            key_name=key_name,
            kms_administrator_arns=kms_administrator_arns,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="createKeyPolicy") # type: ignore[misc]
    @builtins.classmethod
    def create_key_policy(
        cls,
        kms_administrator_arns: typing.Sequence[builtins.str],
    ) -> aws_cdk.aws_iam.PolicyDocument:
        '''
        :param kms_administrator_arns: -
        '''
        return typing.cast(aws_cdk.aws_iam.PolicyDocument, jsii.sinvoke(cls, "createKeyPolicy", [kms_administrator_arns]))

    @jsii.member(jsii_name="getAdministratorArns") # type: ignore[misc]
    @builtins.classmethod
    def get_administrator_arns(
        cls,
        kms_administrator_arns: typing.Sequence[builtins.str],
    ) -> typing.List[aws_cdk.aws_iam.CompositePrincipal]:
        '''
        :param kms_administrator_arns: -
        '''
        return typing.cast(typing.List[aws_cdk.aws_iam.CompositePrincipal], jsii.sinvoke(cls, "getAdministratorArns", [kms_administrator_arns]))

    @jsii.member(jsii_name="getArnPrincipals") # type: ignore[misc]
    @builtins.classmethod
    def get_arn_principals(
        cls,
        kms_administrator_arns: typing.Sequence[builtins.str],
    ) -> typing.List[aws_cdk.aws_iam.ArnPrincipal]:
        '''
        :param kms_administrator_arns: -
        '''
        return typing.cast(typing.List[aws_cdk.aws_iam.ArnPrincipal], jsii.sinvoke(cls, "getArnPrincipals", [kms_administrator_arns]))

    @jsii.member(jsii_name="addTags")
    def add_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "addTags", []))

    @jsii.member(jsii_name="createKmsKey")
    def create_kms_key(
        self,
        kms_administrator_arns: typing.Sequence[builtins.str],
    ) -> aws_cdk.aws_kms.Key:
        '''
        :param kms_administrator_arns: -
        '''
        return typing.cast(aws_cdk.aws_kms.Key, jsii.invoke(self, "createKmsKey", [kms_administrator_arns]))

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
    def kms_key(self) -> aws_cdk.aws_kms.Key:
        return typing.cast(aws_cdk.aws_kms.Key, jsii.get(self, "kmsKey"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="environmentName")
    def environment_name(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "environmentName"))


@jsii.data_type(
    jsii_type="kms-encryption-key.KmsEncryptionKeyProps",
    jsii_struct_bases=[],
    name_mapping={
        "description": "description",
        "environment_name": "environmentName",
        "key_name": "keyName",
        "kms_administrator_arns": "kmsAdministratorArns",
    },
)
class KmsEncryptionKeyProps:
    def __init__(
        self,
        *,
        description: typing.Optional[builtins.str] = None,
        environment_name: typing.Optional[builtins.str] = None,
        key_name: typing.Optional[builtins.str] = None,
        kms_administrator_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param description: 
        :param environment_name: 
        :param key_name: 
        :param kms_administrator_arns: 
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if description is not None:
            self._values["description"] = description
        if environment_name is not None:
            self._values["environment_name"] = environment_name
        if key_name is not None:
            self._values["key_name"] = key_name
        if kms_administrator_arns is not None:
            self._values["kms_administrator_arns"] = kms_administrator_arns

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def environment_name(self) -> typing.Optional[builtins.str]:
        result = self._values.get("environment_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def key_name(self) -> typing.Optional[builtins.str]:
        result = self._values.get("key_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_administrator_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        result = self._values.get("kms_administrator_arns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KmsEncryptionKeyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "KmsEncryptionKey",
    "KmsEncryptionKeyProps",
]

publication.publish()
