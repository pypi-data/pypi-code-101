'''
# AWS CDK CloudFormation Constructs for Alexa::ASK::Skill

Constructs for Alexa::ASK::Skill

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
    jsii_type="@cdk-cloudformation/alexa-ask-skill.AuthenticationConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "client_id": "clientId",
        "client_secret": "clientSecret",
        "refresh_token": "refreshToken",
    },
)
class AuthenticationConfiguration:
    def __init__(
        self,
        *,
        client_id: builtins.str,
        client_secret: builtins.str,
        refresh_token: builtins.str,
    ) -> None:
        '''
        :param client_id: 
        :param client_secret: 
        :param refresh_token: 

        :schema: AuthenticationConfiguration
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "client_id": client_id,
            "client_secret": client_secret,
            "refresh_token": refresh_token,
        }

    @builtins.property
    def client_id(self) -> builtins.str:
        '''
        :schema: AuthenticationConfiguration#ClientId
        '''
        result = self._values.get("client_id")
        assert result is not None, "Required property 'client_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def client_secret(self) -> builtins.str:
        '''
        :schema: AuthenticationConfiguration#ClientSecret
        '''
        result = self._values.get("client_secret")
        assert result is not None, "Required property 'client_secret' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def refresh_token(self) -> builtins.str:
        '''
        :schema: AuthenticationConfiguration#RefreshToken
        '''
        result = self._values.get("refresh_token")
        assert result is not None, "Required property 'refresh_token' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AuthenticationConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CfnSkill(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/alexa-ask-skill.CfnSkill",
):
    '''A CloudFormation ``Alexa::ASK::Skill``.

    :cloudformationResource: Alexa::ASK::Skill
    :link: http://unknown-url
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        authentication_configuration: AuthenticationConfiguration,
        skill_package: "SkillPackage",
        vendor_id: builtins.str,
    ) -> None:
        '''Create a new ``Alexa::ASK::Skill``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param authentication_configuration: 
        :param skill_package: 
        :param vendor_id: 
        '''
        props = CfnSkillProps(
            authentication_configuration=authentication_configuration,
            skill_package=skill_package,
            vendor_id=vendor_id,
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
        '''Attribute ``Alexa::ASK::Skill.Id``.

        :link: http://unknown-url
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnSkillProps":
        '''Resource props.'''
        return typing.cast("CfnSkillProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/alexa-ask-skill.CfnSkillProps",
    jsii_struct_bases=[],
    name_mapping={
        "authentication_configuration": "authenticationConfiguration",
        "skill_package": "skillPackage",
        "vendor_id": "vendorId",
    },
)
class CfnSkillProps:
    def __init__(
        self,
        *,
        authentication_configuration: AuthenticationConfiguration,
        skill_package: "SkillPackage",
        vendor_id: builtins.str,
    ) -> None:
        '''Resource Type definition for Alexa::ASK::Skill.

        :param authentication_configuration: 
        :param skill_package: 
        :param vendor_id: 

        :schema: CfnSkillProps
        '''
        if isinstance(authentication_configuration, dict):
            authentication_configuration = AuthenticationConfiguration(**authentication_configuration)
        if isinstance(skill_package, dict):
            skill_package = SkillPackage(**skill_package)
        self._values: typing.Dict[str, typing.Any] = {
            "authentication_configuration": authentication_configuration,
            "skill_package": skill_package,
            "vendor_id": vendor_id,
        }

    @builtins.property
    def authentication_configuration(self) -> AuthenticationConfiguration:
        '''
        :schema: CfnSkillProps#AuthenticationConfiguration
        '''
        result = self._values.get("authentication_configuration")
        assert result is not None, "Required property 'authentication_configuration' is missing"
        return typing.cast(AuthenticationConfiguration, result)

    @builtins.property
    def skill_package(self) -> "SkillPackage":
        '''
        :schema: CfnSkillProps#SkillPackage
        '''
        result = self._values.get("skill_package")
        assert result is not None, "Required property 'skill_package' is missing"
        return typing.cast("SkillPackage", result)

    @builtins.property
    def vendor_id(self) -> builtins.str:
        '''
        :schema: CfnSkillProps#VendorId
        '''
        result = self._values.get("vendor_id")
        assert result is not None, "Required property 'vendor_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSkillProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/alexa-ask-skill.Overrides",
    jsii_struct_bases=[],
    name_mapping={"manifest": "manifest"},
)
class Overrides:
    def __init__(self, *, manifest: typing.Any = None) -> None:
        '''
        :param manifest: 

        :schema: Overrides
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if manifest is not None:
            self._values["manifest"] = manifest

    @builtins.property
    def manifest(self) -> typing.Any:
        '''
        :schema: Overrides#Manifest
        '''
        result = self._values.get("manifest")
        return typing.cast(typing.Any, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Overrides(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/alexa-ask-skill.SkillPackage",
    jsii_struct_bases=[],
    name_mapping={
        "s3_bucket": "s3Bucket",
        "s3_key": "s3Key",
        "overrides": "overrides",
        "s3_bucket_role": "s3BucketRole",
        "s3_object_version": "s3ObjectVersion",
    },
)
class SkillPackage:
    def __init__(
        self,
        *,
        s3_bucket: builtins.str,
        s3_key: builtins.str,
        overrides: typing.Optional[Overrides] = None,
        s3_bucket_role: typing.Optional[builtins.str] = None,
        s3_object_version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param s3_bucket: 
        :param s3_key: 
        :param overrides: 
        :param s3_bucket_role: 
        :param s3_object_version: 

        :schema: SkillPackage
        '''
        if isinstance(overrides, dict):
            overrides = Overrides(**overrides)
        self._values: typing.Dict[str, typing.Any] = {
            "s3_bucket": s3_bucket,
            "s3_key": s3_key,
        }
        if overrides is not None:
            self._values["overrides"] = overrides
        if s3_bucket_role is not None:
            self._values["s3_bucket_role"] = s3_bucket_role
        if s3_object_version is not None:
            self._values["s3_object_version"] = s3_object_version

    @builtins.property
    def s3_bucket(self) -> builtins.str:
        '''
        :schema: SkillPackage#S3Bucket
        '''
        result = self._values.get("s3_bucket")
        assert result is not None, "Required property 's3_bucket' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def s3_key(self) -> builtins.str:
        '''
        :schema: SkillPackage#S3Key
        '''
        result = self._values.get("s3_key")
        assert result is not None, "Required property 's3_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def overrides(self) -> typing.Optional[Overrides]:
        '''
        :schema: SkillPackage#Overrides
        '''
        result = self._values.get("overrides")
        return typing.cast(typing.Optional[Overrides], result)

    @builtins.property
    def s3_bucket_role(self) -> typing.Optional[builtins.str]:
        '''
        :schema: SkillPackage#S3BucketRole
        '''
        result = self._values.get("s3_bucket_role")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def s3_object_version(self) -> typing.Optional[builtins.str]:
        '''
        :schema: SkillPackage#S3ObjectVersion
        '''
        result = self._values.get("s3_object_version")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SkillPackage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AuthenticationConfiguration",
    "CfnSkill",
    "CfnSkillProps",
    "Overrides",
    "SkillPackage",
]

publication.publish()
