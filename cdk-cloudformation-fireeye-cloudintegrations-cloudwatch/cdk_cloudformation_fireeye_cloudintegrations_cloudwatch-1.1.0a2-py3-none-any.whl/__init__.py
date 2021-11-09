'''
# fireeye-cloudintegrations-cloudwatch

> AWS CDK [L1 construct](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html) and data structures for the [AWS CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) type `FireEye::CloudIntegrations::Cloudwatch` v1.1.0.

## Description

This Resource Type will create necessary resources in your AWS account to forward cloudwatch logs to FireEye Helix. Visit FireEye Cloud Integration Portal for more info and to generate a pre-populated CloudFormation Template

## Usage

In order to use this library, you will need to activate this AWS CloudFormation Registry type in your account. You can do this via the AWS Management Console or using the [AWS CLI](https://aws.amazon.com/cli/) using the following command:

```sh
aws cloudformation activate-type \
  --type-name FireEye::CloudIntegrations::Cloudwatch \
  --publisher-id 264c59dceccf8b8a42e60198f3ba62cb0aa9f0bf \
  --type RESOURCE \
  --execution-role-arn ROLE-ARN
```

Alternatively:

```sh
aws cloudformation activate-type \
  --public-type-arn arn:aws:cloudformation:us-east-1::type/resource/264c59dceccf8b8a42e60198f3ba62cb0aa9f0bf/FireEye-CloudIntegrations-Cloudwatch \
  --execution-role-arn ROLE-ARN
```

You can find more information about activating this type in the [AWS CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html).

## Feedback

This library is auto-generated and published to all supported programming languages by the [cdklabs/cdk-cloudformation](https://github.com/cdklabs/cdk-cloudformation) project based on the API schema published for `FireEye::CloudIntegrations::Cloudwatch`.

* Issues related to this generated library should be [reported here](https://github.com/cdklabs/cdk-cloudformation/issues/new?title=Issue+with+%40cdk-cloudformation%2Ffireeye-cloudintegrations-cloudwatch+v1.1.0).
* Issues related to `FireEye::CloudIntegrations::Cloudwatch` should be reported to the [publisher](undefined).

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
