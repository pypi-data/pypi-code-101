'''
# AWS CDK CloudFormation Constructs for Datadog::Monitors::Downtime

Datadog Monitors Downtime 3.0.0

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


class CfnDowntime(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/datadog-monitors-downtime.CfnDowntime",
):
    '''A CloudFormation ``Datadog::Monitors::Downtime``.

    :cloudformationResource: Datadog::Monitors::Downtime
    :link: http://unknown-url
    '''

    def __init__(
        self,
        scope_: aws_cdk.core.Construct,
        id_: builtins.str,
        *,
        scope: typing.Sequence[builtins.str],
        active: typing.Optional[builtins.bool] = None,
        canceled: typing.Optional[jsii.Number] = None,
        creator_id: typing.Optional[jsii.Number] = None,
        disabled: typing.Optional[builtins.bool] = None,
        downtime_type: typing.Optional[jsii.Number] = None,
        end: typing.Optional[jsii.Number] = None,
        id: typing.Optional[jsii.Number] = None,
        message: typing.Optional[builtins.str] = None,
        monitor_id: typing.Optional[jsii.Number] = None,
        monitor_tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        parent_id: typing.Optional[jsii.Number] = None,
        start: typing.Optional[jsii.Number] = None,
        timezone: typing.Optional[builtins.str] = None,
        updater_id: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Create a new ``Datadog::Monitors::Downtime``.

        :param scope_: - scope in which this resource is defined.
        :param id_: - scoped id of the resource.
        :param scope: The scope(s) to which the downtime applies.
        :param active: Whether or not this downtime is currently active.
        :param canceled: POSIX Timestamp of cancellation of this downtime (null if not canceled).
        :param creator_id: Id of the user who created this downtime.
        :param disabled: Whether or not this downtime is disabled.
        :param downtime_type: Type of this downtime.
        :param end: POSIX timestamp to end the downtime. If not provided, the downtime is in effect indefinitely (i.e. until you cancel it).
        :param id: Id of this downtime.
        :param message: Message on the downtime.
        :param monitor_id: A single monitor to which the downtime applies. If not provided, the downtime applies to all monitors.
        :param monitor_tags: A comma-separated list of monitor tags, to which the downtime applies. The resulting downtime applies to monitors that match ALL provided monitor tags.
        :param parent_id: The ID of the parent downtime to this one.
        :param start: POSIX timestamp to start the downtime. If not provided, the downtime starts the moment it is created.
        :param timezone: The timezone for the downtime.
        :param updater_id: Id of the user who updated this downtime.
        '''
        props = CfnDowntimeProps(
            scope=scope,
            active=active,
            canceled=canceled,
            creator_id=creator_id,
            disabled=disabled,
            downtime_type=downtime_type,
            end=end,
            id=id,
            message=message,
            monitor_id=monitor_id,
            monitor_tags=monitor_tags,
            parent_id=parent_id,
            start=start,
            timezone=timezone,
            updater_id=updater_id,
        )

        jsii.create(self.__class__, self, [scope_, id_, props])

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnDowntimeProps":
        '''Resource props.'''
        return typing.cast("CfnDowntimeProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/datadog-monitors-downtime.CfnDowntimeProps",
    jsii_struct_bases=[],
    name_mapping={
        "scope": "scope",
        "active": "active",
        "canceled": "canceled",
        "creator_id": "creatorId",
        "disabled": "disabled",
        "downtime_type": "downtimeType",
        "end": "end",
        "id": "id",
        "message": "message",
        "monitor_id": "monitorId",
        "monitor_tags": "monitorTags",
        "parent_id": "parentId",
        "start": "start",
        "timezone": "timezone",
        "updater_id": "updaterId",
    },
)
class CfnDowntimeProps:
    def __init__(
        self,
        *,
        scope: typing.Sequence[builtins.str],
        active: typing.Optional[builtins.bool] = None,
        canceled: typing.Optional[jsii.Number] = None,
        creator_id: typing.Optional[jsii.Number] = None,
        disabled: typing.Optional[builtins.bool] = None,
        downtime_type: typing.Optional[jsii.Number] = None,
        end: typing.Optional[jsii.Number] = None,
        id: typing.Optional[jsii.Number] = None,
        message: typing.Optional[builtins.str] = None,
        monitor_id: typing.Optional[jsii.Number] = None,
        monitor_tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        parent_id: typing.Optional[jsii.Number] = None,
        start: typing.Optional[jsii.Number] = None,
        timezone: typing.Optional[builtins.str] = None,
        updater_id: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Datadog Monitors Downtime 3.0.0.

        :param scope: The scope(s) to which the downtime applies.
        :param active: Whether or not this downtime is currently active.
        :param canceled: POSIX Timestamp of cancellation of this downtime (null if not canceled).
        :param creator_id: Id of the user who created this downtime.
        :param disabled: Whether or not this downtime is disabled.
        :param downtime_type: Type of this downtime.
        :param end: POSIX timestamp to end the downtime. If not provided, the downtime is in effect indefinitely (i.e. until you cancel it).
        :param id: Id of this downtime.
        :param message: Message on the downtime.
        :param monitor_id: A single monitor to which the downtime applies. If not provided, the downtime applies to all monitors.
        :param monitor_tags: A comma-separated list of monitor tags, to which the downtime applies. The resulting downtime applies to monitors that match ALL provided monitor tags.
        :param parent_id: The ID of the parent downtime to this one.
        :param start: POSIX timestamp to start the downtime. If not provided, the downtime starts the moment it is created.
        :param timezone: The timezone for the downtime.
        :param updater_id: Id of the user who updated this downtime.

        :schema: CfnDowntimeProps
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "scope": scope,
        }
        if active is not None:
            self._values["active"] = active
        if canceled is not None:
            self._values["canceled"] = canceled
        if creator_id is not None:
            self._values["creator_id"] = creator_id
        if disabled is not None:
            self._values["disabled"] = disabled
        if downtime_type is not None:
            self._values["downtime_type"] = downtime_type
        if end is not None:
            self._values["end"] = end
        if id is not None:
            self._values["id"] = id
        if message is not None:
            self._values["message"] = message
        if monitor_id is not None:
            self._values["monitor_id"] = monitor_id
        if monitor_tags is not None:
            self._values["monitor_tags"] = monitor_tags
        if parent_id is not None:
            self._values["parent_id"] = parent_id
        if start is not None:
            self._values["start"] = start
        if timezone is not None:
            self._values["timezone"] = timezone
        if updater_id is not None:
            self._values["updater_id"] = updater_id

    @builtins.property
    def scope(self) -> typing.List[builtins.str]:
        '''The scope(s) to which the downtime applies.

        :schema: CfnDowntimeProps#Scope
        '''
        result = self._values.get("scope")
        assert result is not None, "Required property 'scope' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def active(self) -> typing.Optional[builtins.bool]:
        '''Whether or not this downtime is currently active.

        :schema: CfnDowntimeProps#Active
        '''
        result = self._values.get("active")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def canceled(self) -> typing.Optional[jsii.Number]:
        '''POSIX Timestamp of cancellation of this downtime (null if not canceled).

        :schema: CfnDowntimeProps#Canceled
        '''
        result = self._values.get("canceled")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def creator_id(self) -> typing.Optional[jsii.Number]:
        '''Id of the user who created this downtime.

        :schema: CfnDowntimeProps#CreatorId
        '''
        result = self._values.get("creator_id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def disabled(self) -> typing.Optional[builtins.bool]:
        '''Whether or not this downtime is disabled.

        :schema: CfnDowntimeProps#Disabled
        '''
        result = self._values.get("disabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def downtime_type(self) -> typing.Optional[jsii.Number]:
        '''Type of this downtime.

        :schema: CfnDowntimeProps#DowntimeType
        '''
        result = self._values.get("downtime_type")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def end(self) -> typing.Optional[jsii.Number]:
        '''POSIX timestamp to end the downtime.

        If not provided, the downtime is in effect indefinitely (i.e. until you cancel it).

        :schema: CfnDowntimeProps#End
        '''
        result = self._values.get("end")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def id(self) -> typing.Optional[jsii.Number]:
        '''Id of this downtime.

        :schema: CfnDowntimeProps#Id
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def message(self) -> typing.Optional[builtins.str]:
        '''Message on the downtime.

        :schema: CfnDowntimeProps#Message
        '''
        result = self._values.get("message")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def monitor_id(self) -> typing.Optional[jsii.Number]:
        '''A single monitor to which the downtime applies.

        If not provided, the downtime applies to all monitors.

        :schema: CfnDowntimeProps#MonitorId
        '''
        result = self._values.get("monitor_id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def monitor_tags(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A comma-separated list of monitor tags, to which the downtime applies.

        The resulting downtime applies to monitors that match ALL provided monitor tags.

        :schema: CfnDowntimeProps#MonitorTags
        '''
        result = self._values.get("monitor_tags")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def parent_id(self) -> typing.Optional[jsii.Number]:
        '''The ID of the parent downtime to this one.

        :schema: CfnDowntimeProps#ParentId
        '''
        result = self._values.get("parent_id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def start(self) -> typing.Optional[jsii.Number]:
        '''POSIX timestamp to start the downtime.

        If not provided, the downtime starts the moment it is created.

        :schema: CfnDowntimeProps#Start
        '''
        result = self._values.get("start")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def timezone(self) -> typing.Optional[builtins.str]:
        '''The timezone for the downtime.

        :schema: CfnDowntimeProps#Timezone
        '''
        result = self._values.get("timezone")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def updater_id(self) -> typing.Optional[jsii.Number]:
        '''Id of the user who updated this downtime.

        :schema: CfnDowntimeProps#UpdaterId
        '''
        result = self._values.get("updater_id")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDowntimeProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnDowntime",
    "CfnDowntimeProps",
]

publication.publish()
