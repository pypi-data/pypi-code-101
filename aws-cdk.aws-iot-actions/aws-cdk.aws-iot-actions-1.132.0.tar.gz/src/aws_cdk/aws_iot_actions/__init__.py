'''
# Actions for AWS IoT Rule

<!--BEGIN STABILITY BANNER-->---


![cdk-constructs: Experimental](https://img.shields.io/badge/cdk--constructs-experimental-important.svg?style=for-the-badge)

> The APIs of higher level constructs in this module are experimental and under active development.
> They are subject to non-backward compatible changes or removal in any future version. These are
> not subject to the [Semantic Versioning](https://semver.org/) model and breaking changes will be
> announced in the release notes. This means that while you may use them, you may need to update
> your source code when upgrading to a newer version of this package.

---
<!--END STABILITY BANNER-->

This library contains integration classes to send data to any number of
supported AWS Services. Instances of these classes should be passed to
`TopicRule` defined in `@aws-cdk/aws-iot`.

Currently supported are:

* Invoke a Lambda function

## Invoke a Lambda function

The code snippet below creates an AWS IoT Rule that invoke a Lambda function
when it is triggered.

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_iot as iot
import aws_cdk.aws_iot_actions as actions
import aws_cdk.aws_lambda as lambda_

func = lambda_.Function(self, "MyFunction",
    runtime=lambda_.Runtime.NODEJS_14_X,
    handler="index.handler",
    code=lambda_.Code.from_inline("""
            exports.handler = (event) => {
              console.log("It is test for lambda action of AWS IoT Rule.", event);
            };""")
)

iot.TopicRule(self, "TopicRule",
    sql=iot.IotSql.from_string_as_ver20160323("SELECT topic(2) as device_id, timestamp() as timestamp, temperature FROM 'device/+/data'"),
    actions=[actions.LambdaFunctionAction(func)]
)
```

## Put logs to CloudWatch Logs

The code snippet below creates an AWS IoT Rule that put logs to CloudWatch Logs
when it is triggered.

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_iot as iot
import aws_cdk.aws_iot_actions as actions
import aws_cdk.aws_logs as logs

log_group = logs.LogGroup(self, "MyLogGroup")

iot.TopicRule(self, "TopicRule",
    sql=iot.IotSql.from_string_as_ver20160323("SELECT topic(2) as device_id FROM 'device/+/data'"),
    actions=[actions.CloudWatchLogsAction(log_group)]
)
```
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
import aws_cdk.aws_iot
import aws_cdk.aws_lambda
import aws_cdk.aws_logs


@jsii.implements(aws_cdk.aws_iot.IAction)
class CloudWatchLogsAction(
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-iot-actions.CloudWatchLogsAction",
):
    '''(experimental) The action to send data to Amazon CloudWatch Logs.

    :stability: experimental
    '''

    def __init__(
        self,
        log_group: aws_cdk.aws_logs.ILogGroup,
        *,
        role: typing.Optional[aws_cdk.aws_iam.IRole] = None,
    ) -> None:
        '''
        :param log_group: The CloudWatch log group to which the action sends data.
        :param role: (experimental) The IAM role that allows access to the CloudWatch log group. Default: a new role will be created

        :stability: experimental
        '''
        props = CloudWatchLogsActionProps(role=role)

        jsii.create(self.__class__, self, [log_group, props])

    @jsii.member(jsii_name="bind")
    def bind(self, rule: aws_cdk.aws_iot.ITopicRule) -> aws_cdk.aws_iot.ActionConfig:
        '''(experimental) (experimental) Returns the topic rule action specification.

        :param rule: -

        :stability: experimental
        '''
        return typing.cast(aws_cdk.aws_iot.ActionConfig, jsii.invoke(self, "bind", [rule]))


@jsii.data_type(
    jsii_type="@aws-cdk/aws-iot-actions.CloudWatchLogsActionProps",
    jsii_struct_bases=[],
    name_mapping={"role": "role"},
)
class CloudWatchLogsActionProps:
    def __init__(self, *, role: typing.Optional[aws_cdk.aws_iam.IRole] = None) -> None:
        '''(experimental) Configuration properties of an action for CloudWatch Logs.

        :param role: (experimental) The IAM role that allows access to the CloudWatch log group. Default: a new role will be created

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if role is not None:
            self._values["role"] = role

    @builtins.property
    def role(self) -> typing.Optional[aws_cdk.aws_iam.IRole]:
        '''(experimental) The IAM role that allows access to the CloudWatch log group.

        :default: a new role will be created

        :stability: experimental
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional[aws_cdk.aws_iam.IRole], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudWatchLogsActionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.aws_iot.IAction)
class LambdaFunctionAction(
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-iot-actions.LambdaFunctionAction",
):
    '''(experimental) The action to invoke an AWS Lambda function, passing in an MQTT message.

    :stability: experimental
    '''

    def __init__(self, func: aws_cdk.aws_lambda.IFunction) -> None:
        '''
        :param func: The lambda function to be invoked by this action.

        :stability: experimental
        '''
        jsii.create(self.__class__, self, [func])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        topic_rule: aws_cdk.aws_iot.ITopicRule,
    ) -> aws_cdk.aws_iot.ActionConfig:
        '''(experimental) (experimental) Returns the topic rule action specification.

        :param topic_rule: -

        :stability: experimental
        '''
        return typing.cast(aws_cdk.aws_iot.ActionConfig, jsii.invoke(self, "bind", [topic_rule]))


__all__ = [
    "CloudWatchLogsAction",
    "CloudWatchLogsActionProps",
    "LambdaFunctionAction",
]

publication.publish()
