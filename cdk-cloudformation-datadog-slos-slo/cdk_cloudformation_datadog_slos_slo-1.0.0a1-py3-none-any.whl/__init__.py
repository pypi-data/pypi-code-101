'''
# AWS CDK CloudFormation Constructs for Datadog::SLOs::SLO

Datadog SLO 1.0.0

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


class CfnSlo(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/datadog-slos-slo.CfnSlo",
):
    '''A CloudFormation ``Datadog::SLOs::SLO``.

    :cloudformationResource: Datadog::SLOs::SLO
    :link: http://unknown-url
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        thresholds: typing.Sequence["Threshold"],
        type: "CfnSloPropsType",
        creator: typing.Optional["Creator"] = None,
        description: typing.Optional[builtins.str] = None,
        groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        monitor_ids: typing.Optional[typing.Sequence[jsii.Number]] = None,
        query: typing.Optional["Query"] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Create a new ``Datadog::SLOs::SLO``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param name: Name of the slo.
        :param thresholds: 
        :param type: The type of the slo.
        :param creator: 
        :param description: Description of the slo.
        :param groups: A list of (up to 20) monitor groups that narrow the scope of a monitor service level objective.
        :param monitor_ids: A list of monitor ids that defines the scope of a monitor service level objective. Required if type is monitor.
        :param query: 
        :param tags: Tags associated with the slo.
        '''
        props = CfnSloProps(
            name=name,
            thresholds=thresholds,
            type=type,
            creator=creator,
            description=description,
            groups=groups,
            monitor_ids=monitor_ids,
            query=query,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrCreated")
    def attr_created(self) -> builtins.str:
        '''Attribute ``Datadog::SLOs::SLO.Created``.

        :link: http://unknown-url
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreated"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrDeleted")
    def attr_deleted(self) -> builtins.str:
        '''Attribute ``Datadog::SLOs::SLO.Deleted``.

        :link: http://unknown-url
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDeleted"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''Attribute ``Datadog::SLOs::SLO.Id``.

        :link: http://unknown-url
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrModified")
    def attr_modified(self) -> builtins.str:
        '''Attribute ``Datadog::SLOs::SLO.Modified``.

        :link: http://unknown-url
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrModified"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnSloProps":
        '''Resource props.'''
        return typing.cast("CfnSloProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/datadog-slos-slo.CfnSloProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "thresholds": "thresholds",
        "type": "type",
        "creator": "creator",
        "description": "description",
        "groups": "groups",
        "monitor_ids": "monitorIds",
        "query": "query",
        "tags": "tags",
    },
)
class CfnSloProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        thresholds: typing.Sequence["Threshold"],
        type: "CfnSloPropsType",
        creator: typing.Optional["Creator"] = None,
        description: typing.Optional[builtins.str] = None,
        groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        monitor_ids: typing.Optional[typing.Sequence[jsii.Number]] = None,
        query: typing.Optional["Query"] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Datadog SLO 1.0.0.

        :param name: Name of the slo.
        :param thresholds: 
        :param type: The type of the slo.
        :param creator: 
        :param description: Description of the slo.
        :param groups: A list of (up to 20) monitor groups that narrow the scope of a monitor service level objective.
        :param monitor_ids: A list of monitor ids that defines the scope of a monitor service level objective. Required if type is monitor.
        :param query: 
        :param tags: Tags associated with the slo.

        :schema: CfnSloProps
        '''
        if isinstance(creator, dict):
            creator = Creator(**creator)
        if isinstance(query, dict):
            query = Query(**query)
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "thresholds": thresholds,
            "type": type,
        }
        if creator is not None:
            self._values["creator"] = creator
        if description is not None:
            self._values["description"] = description
        if groups is not None:
            self._values["groups"] = groups
        if monitor_ids is not None:
            self._values["monitor_ids"] = monitor_ids
        if query is not None:
            self._values["query"] = query
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the slo.

        :schema: CfnSloProps#Name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def thresholds(self) -> typing.List["Threshold"]:
        '''
        :schema: CfnSloProps#Thresholds
        '''
        result = self._values.get("thresholds")
        assert result is not None, "Required property 'thresholds' is missing"
        return typing.cast(typing.List["Threshold"], result)

    @builtins.property
    def type(self) -> "CfnSloPropsType":
        '''The type of the slo.

        :schema: CfnSloProps#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast("CfnSloPropsType", result)

    @builtins.property
    def creator(self) -> typing.Optional["Creator"]:
        '''
        :schema: CfnSloProps#Creator
        '''
        result = self._values.get("creator")
        return typing.cast(typing.Optional["Creator"], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Description of the slo.

        :schema: CfnSloProps#Description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of (up to 20) monitor groups that narrow the scope of a monitor service level objective.

        :schema: CfnSloProps#Groups
        '''
        result = self._values.get("groups")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def monitor_ids(self) -> typing.Optional[typing.List[jsii.Number]]:
        '''A list of monitor ids that defines the scope of a monitor service level objective.

        Required if type is monitor.

        :schema: CfnSloProps#MonitorIds
        '''
        result = self._values.get("monitor_ids")
        return typing.cast(typing.Optional[typing.List[jsii.Number]], result)

    @builtins.property
    def query(self) -> typing.Optional["Query"]:
        '''
        :schema: CfnSloProps#Query
        '''
        result = self._values.get("query")
        return typing.cast(typing.Optional["Query"], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Tags associated with the slo.

        :schema: CfnSloProps#Tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSloProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="@cdk-cloudformation/datadog-slos-slo.CfnSloPropsType")
class CfnSloPropsType(enum.Enum):
    '''The type of the slo.

    :schema: CfnSloPropsType
    '''

    MONITOR = "MONITOR"
    '''monitor.'''
    METRIC = "METRIC"
    '''metric.'''


@jsii.data_type(
    jsii_type="@cdk-cloudformation/datadog-slos-slo.Creator",
    jsii_struct_bases=[],
    name_mapping={"email": "email", "handle": "handle", "name": "name"},
)
class Creator:
    def __init__(
        self,
        *,
        email: typing.Optional[builtins.str] = None,
        handle: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param email: Email of the creator of the slo.
        :param handle: Handle of the creator of the slo.
        :param name: Name of the creator of the slo.

        :schema: Creator
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if email is not None:
            self._values["email"] = email
        if handle is not None:
            self._values["handle"] = handle
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def email(self) -> typing.Optional[builtins.str]:
        '''Email of the creator of the slo.

        :schema: Creator#Email
        '''
        result = self._values.get("email")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def handle(self) -> typing.Optional[builtins.str]:
        '''Handle of the creator of the slo.

        :schema: Creator#Handle
        '''
        result = self._values.get("handle")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the creator of the slo.

        :schema: Creator#Name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Creator(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/datadog-slos-slo.Query",
    jsii_struct_bases=[],
    name_mapping={"denominator": "denominator", "numerator": "numerator"},
)
class Query:
    def __init__(
        self,
        *,
        denominator: typing.Optional[builtins.str] = None,
        numerator: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param denominator: A Datadog metric query for good events.
        :param numerator: A Datadog metric query for total (valid) events.

        :schema: Query
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if denominator is not None:
            self._values["denominator"] = denominator
        if numerator is not None:
            self._values["numerator"] = numerator

    @builtins.property
    def denominator(self) -> typing.Optional[builtins.str]:
        '''A Datadog metric query for good events.

        :schema: Query#Denominator
        '''
        result = self._values.get("denominator")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def numerator(self) -> typing.Optional[builtins.str]:
        '''A Datadog metric query for total (valid) events.

        :schema: Query#Numerator
        '''
        result = self._values.get("numerator")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Query(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/datadog-slos-slo.Threshold",
    jsii_struct_bases=[],
    name_mapping={
        "target": "target",
        "target_display": "targetDisplay",
        "timeframe": "timeframe",
        "warning": "warning",
        "warning_display": "warningDisplay",
    },
)
class Threshold:
    def __init__(
        self,
        *,
        target: typing.Optional[jsii.Number] = None,
        target_display: typing.Optional[builtins.str] = None,
        timeframe: typing.Optional["ThresholdTimeframe"] = None,
        warning: typing.Optional[jsii.Number] = None,
        warning_display: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param target: The target value for the service level indicator within the corresponding timeframe.
        :param target_display: A string representation of the target that indicates its precision.(e.g. 98.00).
        :param timeframe: The SLO time window options. Allowed enum values: 7d,30d,90d
        :param warning: The warning value for the service level objective.
        :param warning_display: A string representation of the warning target.(e.g. 98.00).

        :schema: Threshold
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if target is not None:
            self._values["target"] = target
        if target_display is not None:
            self._values["target_display"] = target_display
        if timeframe is not None:
            self._values["timeframe"] = timeframe
        if warning is not None:
            self._values["warning"] = warning
        if warning_display is not None:
            self._values["warning_display"] = warning_display

    @builtins.property
    def target(self) -> typing.Optional[jsii.Number]:
        '''The target value for the service level indicator within the corresponding timeframe.

        :schema: Threshold#Target
        '''
        result = self._values.get("target")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def target_display(self) -> typing.Optional[builtins.str]:
        '''A string representation of the target that indicates its precision.(e.g. 98.00).

        :schema: Threshold#TargetDisplay
        '''
        result = self._values.get("target_display")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeframe(self) -> typing.Optional["ThresholdTimeframe"]:
        '''The SLO time window options.

        Allowed enum values: 7d,30d,90d

        :schema: Threshold#Timeframe
        '''
        result = self._values.get("timeframe")
        return typing.cast(typing.Optional["ThresholdTimeframe"], result)

    @builtins.property
    def warning(self) -> typing.Optional[jsii.Number]:
        '''The warning value for the service level objective.

        :schema: Threshold#Warning
        '''
        result = self._values.get("warning")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def warning_display(self) -> typing.Optional[builtins.str]:
        '''A string representation of the warning target.(e.g. 98.00).

        :schema: Threshold#WarningDisplay
        '''
        result = self._values.get("warning_display")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Threshold(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="@cdk-cloudformation/datadog-slos-slo.ThresholdTimeframe")
class ThresholdTimeframe(enum.Enum):
    '''The SLO time window options.

    Allowed enum values: 7d,30d,90d

    :schema: ThresholdTimeframe
    '''

    VALUE_7D = "VALUE_7D"
    '''7d.'''
    VALUE_30D = "VALUE_30D"
    '''30d.'''
    VALUE_90D = "VALUE_90D"
    '''90d.'''


__all__ = [
    "CfnSlo",
    "CfnSloProps",
    "CfnSloPropsType",
    "Creator",
    "Query",
    "Threshold",
    "ThresholdTimeframe",
]

publication.publish()
