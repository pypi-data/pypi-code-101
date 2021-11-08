'''
# AWS CDK CloudFormation Constructs for Datadog::Dashboards::Dashboard

Datadog Dashboard 2.0.2

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
