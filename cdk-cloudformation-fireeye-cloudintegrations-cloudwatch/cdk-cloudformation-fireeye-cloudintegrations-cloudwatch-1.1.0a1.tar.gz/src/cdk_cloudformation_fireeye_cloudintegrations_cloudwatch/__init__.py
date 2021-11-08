'''
# AWS CDK CloudFormation Constructs for FireEye::CloudIntegrations::Cloudwatch

This Resource Type will create necessary resources in your AWS account to forward cloudwatch logs to FireEye Helix. Visit FireEye Cloud Integration Portal for more info and to generate a pre-populated CloudFormation Template

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


class CfnCloudwatch(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/fireeye-cloudintegrations-cloudwatch.CfnCloudwatch",
):
    '''A CloudFormation ``FireEye::CloudIntegrations::Cloudwatch``.

    :cloudformationResource: FireEye::CloudIntegrations::Cloudwatch
    :link: http://unknown-url
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        api_key: builtins.str,
        exec_role: builtins.str,
        helix_upload_url: builtins.str,
        log_group_name: builtins.str,
        region: builtins.str,
    ) -> None:
        '''Create a new ``FireEye::CloudIntegrations::Cloudwatch``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param api_key: Helix API Key.
        :param exec_role: Lambda Execution role.
        :param helix_upload_url: Helix API upload URL.
        :param log_group_name: CloudWatch LogGroup to monitor.
        :param region: LogGroup AWS region.
        '''
        props = CfnCloudwatchProps(
            api_key=api_key,
            exec_role=exec_role,
            helix_upload_url=helix_upload_url,
            log_group_name=log_group_name,
            region=region,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrPrimaryIdentifier")
    def attr_primary_identifier(self) -> builtins.str:
        '''Attribute ``FireEye::CloudIntegrations::Cloudwatch.primaryIdentifier``.

        :link: http://unknown-url
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPrimaryIdentifier"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnCloudwatchProps":
        '''Resource props.'''
        return typing.cast("CfnCloudwatchProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/fireeye-cloudintegrations-cloudwatch.CfnCloudwatchProps",
    jsii_struct_bases=[],
    name_mapping={
        "api_key": "apiKey",
        "exec_role": "execRole",
        "helix_upload_url": "helixUploadUrl",
        "log_group_name": "logGroupName",
        "region": "region",
    },
)
class CfnCloudwatchProps:
    def __init__(
        self,
        *,
        api_key: builtins.str,
        exec_role: builtins.str,
        helix_upload_url: builtins.str,
        log_group_name: builtins.str,
        region: builtins.str,
    ) -> None:
        '''This Resource Type will create necessary resources in your AWS account to forward cloudwatch logs to FireEye Helix.

        Visit FireEye Cloud Integration Portal for more info and to generate a pre-populated CloudFormation Template

        :param api_key: Helix API Key.
        :param exec_role: Lambda Execution role.
        :param helix_upload_url: Helix API upload URL.
        :param log_group_name: CloudWatch LogGroup to monitor.
        :param region: LogGroup AWS region.

        :schema: CfnCloudwatchProps
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "api_key": api_key,
            "exec_role": exec_role,
            "helix_upload_url": helix_upload_url,
            "log_group_name": log_group_name,
            "region": region,
        }

    @builtins.property
    def api_key(self) -> builtins.str:
        '''Helix API Key.

        :schema: CfnCloudwatchProps#ApiKey
        '''
        result = self._values.get("api_key")
        assert result is not None, "Required property 'api_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def exec_role(self) -> builtins.str:
        '''Lambda Execution role.

        :schema: CfnCloudwatchProps#ExecRole
        '''
        result = self._values.get("exec_role")
        assert result is not None, "Required property 'exec_role' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def helix_upload_url(self) -> builtins.str:
        '''Helix API upload URL.

        :schema: CfnCloudwatchProps#HelixUploadUrl
        '''
        result = self._values.get("helix_upload_url")
        assert result is not None, "Required property 'helix_upload_url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def log_group_name(self) -> builtins.str:
        '''CloudWatch LogGroup to monitor.

        :schema: CfnCloudwatchProps#LogGroupName
        '''
        result = self._values.get("log_group_name")
        assert result is not None, "Required property 'log_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def region(self) -> builtins.str:
        '''LogGroup AWS region.

        :schema: CfnCloudwatchProps#Region
        '''
        result = self._values.get("region")
        assert result is not None, "Required property 'region' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudwatchProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnCloudwatch",
    "CfnCloudwatchProps",
]

publication.publish()
