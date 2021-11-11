'''
# datadog-dashboards-dashboard

> AWS CDK [L1 construct](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html) and data structures for the [AWS CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) type `Datadog::Dashboards::Dashboard` v2.0.2.

## Description

Datadog Dashboard 2.0.2

## Usage

In order to use this library, you will need to activate this AWS CloudFormation Registry type in your account. You can do this via the AWS Management Console or using the [AWS CLI](https://aws.amazon.com/cli/) using the following command:

```sh
aws cloudformation activate-type \
  --type-name Datadog::Dashboards::Dashboard \
  --publisher-id 7171b96e5d207b947eb72ca9ce05247c246de623 \
  --type RESOURCE \
  --execution-role-arn ROLE-ARN
```

Alternatively:

```sh
aws cloudformation activate-type \
  --public-type-arn arn:aws:cloudformation:us-east-1::type/resource/7171b96e5d207b947eb72ca9ce05247c246de623/Datadog-Dashboards-Dashboard \
  --execution-role-arn ROLE-ARN
```

You can find more information about activating this type in the [AWS CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html).

## Feedback

This library is auto-generated and published to all supported programming languages by the [cdklabs/cdk-cloudformation](https://github.com/cdklabs/cdk-cloudformation) project based on the API schema published for `Datadog::Dashboards::Dashboard`.

* Issues related to this generated library should be [reported here](https://github.com/cdklabs/cdk-cloudformation/issues/new?title=Issue+with+%40cdk-cloudformation%2Fdatadog-dashboards-dashboard+v2.0.2).
* Issues related to `Datadog::Dashboards::Dashboard` should be reported to the [publisher](undefined).

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


class CfnDashboard(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/datadog-dashboards-dashboard.CfnDashboard",
):
    '''A CloudFormation ``Datadog::Dashboards::Dashboard``.

    :cloudformationResource: Datadog::Dashboards::Dashboard
    :link: http://unknown-url
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        dashboard_definition: builtins.str,
    ) -> None:
        '''Create a new ``Datadog::Dashboards::Dashboard``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param dashboard_definition: JSON string of the dashboard definition.
        '''
        props = CfnDashboardProps(dashboard_definition=dashboard_definition)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''Attribute ``Datadog::Dashboards::Dashboard.Id``.

        :link: http://unknown-url
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrUrl")
    def attr_url(self) -> builtins.str:
        '''Attribute ``Datadog::Dashboards::Dashboard.Url``.

        :link: http://unknown-url
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUrl"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnDashboardProps":
        '''Resource props.'''
        return typing.cast("CfnDashboardProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/datadog-dashboards-dashboard.CfnDashboardProps",
    jsii_struct_bases=[],
    name_mapping={"dashboard_definition": "dashboardDefinition"},
)
class CfnDashboardProps:
    def __init__(self, *, dashboard_definition: builtins.str) -> None:
        '''Datadog Dashboard 2.0.2.

        :param dashboard_definition: JSON string of the dashboard definition.

        :schema: CfnDashboardProps
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "dashboard_definition": dashboard_definition,
        }

    @builtins.property
    def dashboard_definition(self) -> builtins.str:
        '''JSON string of the dashboard definition.

        :schema: CfnDashboardProps#DashboardDefinition
        '''
        result = self._values.get("dashboard_definition")
        assert result is not None, "Required property 'dashboard_definition' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDashboardProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnDashboard",
    "CfnDashboardProps",
]

publication.publish()
