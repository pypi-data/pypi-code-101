'''
# AWS CDK CloudFormation Constructs for Datadog::Monitors::Monitor

Datadog Monitor 4.0.0

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


class CfnMonitor(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/datadog-monitors-monitor.CfnMonitor",
):
    '''A CloudFormation ``Datadog::Monitors::Monitor``.

    :cloudformationResource: Datadog::Monitors::Monitor
    :link: http://unknown-url
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id_: builtins.str,
        *,
        query: builtins.str,
        type: "CfnMonitorPropsType",
        creator: typing.Optional["Creator"] = None,
        id: typing.Optional[jsii.Number] = None,
        message: typing.Optional[builtins.str] = None,
        multi: typing.Optional[builtins.bool] = None,
        name: typing.Optional[builtins.str] = None,
        options: typing.Optional["MonitorOptions"] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Create a new ``Datadog::Monitors::Monitor``.

        :param scope: - scope in which this resource is defined.
        :param id_: - scoped id of the resource.
        :param query: The monitor query.
        :param type: The type of the monitor.
        :param creator: 
        :param id: ID of the monitor.
        :param message: A message to include with notifications for the monitor.
        :param multi: Whether or not the monitor is multi alert.
        :param name: Name of the monitor.
        :param options: The monitor options.
        :param tags: Tags associated with the monitor.
        '''
        props = CfnMonitorProps(
            query=query,
            type=type,
            creator=creator,
            id=id,
            message=message,
            multi=multi,
            name=name,
            options=options,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id_, props])

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrCreated")
    def attr_created(self) -> builtins.str:
        '''Attribute ``Datadog::Monitors::Monitor.Created``.

        :link: http://unknown-url
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreated"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrDeleted")
    def attr_deleted(self) -> builtins.str:
        '''Attribute ``Datadog::Monitors::Monitor.Deleted``.

        :link: http://unknown-url
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDeleted"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrModified")
    def attr_modified(self) -> builtins.str:
        '''Attribute ``Datadog::Monitors::Monitor.Modified``.

        :link: http://unknown-url
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrModified"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnMonitorProps":
        '''Resource props.'''
        return typing.cast("CfnMonitorProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/datadog-monitors-monitor.CfnMonitorProps",
    jsii_struct_bases=[],
    name_mapping={
        "query": "query",
        "type": "type",
        "creator": "creator",
        "id": "id",
        "message": "message",
        "multi": "multi",
        "name": "name",
        "options": "options",
        "tags": "tags",
    },
)
class CfnMonitorProps:
    def __init__(
        self,
        *,
        query: builtins.str,
        type: "CfnMonitorPropsType",
        creator: typing.Optional["Creator"] = None,
        id: typing.Optional[jsii.Number] = None,
        message: typing.Optional[builtins.str] = None,
        multi: typing.Optional[builtins.bool] = None,
        name: typing.Optional[builtins.str] = None,
        options: typing.Optional["MonitorOptions"] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Datadog Monitor 4.0.0.

        :param query: The monitor query.
        :param type: The type of the monitor.
        :param creator: 
        :param id: ID of the monitor.
        :param message: A message to include with notifications for the monitor.
        :param multi: Whether or not the monitor is multi alert.
        :param name: Name of the monitor.
        :param options: The monitor options.
        :param tags: Tags associated with the monitor.

        :schema: CfnMonitorProps
        '''
        if isinstance(creator, dict):
            creator = Creator(**creator)
        if isinstance(options, dict):
            options = MonitorOptions(**options)
        self._values: typing.Dict[str, typing.Any] = {
            "query": query,
            "type": type,
        }
        if creator is not None:
            self._values["creator"] = creator
        if id is not None:
            self._values["id"] = id
        if message is not None:
            self._values["message"] = message
        if multi is not None:
            self._values["multi"] = multi
        if name is not None:
            self._values["name"] = name
        if options is not None:
            self._values["options"] = options
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def query(self) -> builtins.str:
        '''The monitor query.

        :schema: CfnMonitorProps#Query
        '''
        result = self._values.get("query")
        assert result is not None, "Required property 'query' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> "CfnMonitorPropsType":
        '''The type of the monitor.

        :schema: CfnMonitorProps#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast("CfnMonitorPropsType", result)

    @builtins.property
    def creator(self) -> typing.Optional["Creator"]:
        '''
        :schema: CfnMonitorProps#Creator
        '''
        result = self._values.get("creator")
        return typing.cast(typing.Optional["Creator"], result)

    @builtins.property
    def id(self) -> typing.Optional[jsii.Number]:
        '''ID of the monitor.

        :schema: CfnMonitorProps#Id
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def message(self) -> typing.Optional[builtins.str]:
        '''A message to include with notifications for the monitor.

        :schema: CfnMonitorProps#Message
        '''
        result = self._values.get("message")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def multi(self) -> typing.Optional[builtins.bool]:
        '''Whether or not the monitor is multi alert.

        :schema: CfnMonitorProps#Multi
        '''
        result = self._values.get("multi")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the monitor.

        :schema: CfnMonitorProps#Name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def options(self) -> typing.Optional["MonitorOptions"]:
        '''The monitor options.

        :schema: CfnMonitorProps#Options
        '''
        result = self._values.get("options")
        return typing.cast(typing.Optional["MonitorOptions"], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Tags associated with the monitor.

        :schema: CfnMonitorProps#Tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMonitorProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(
    jsii_type="@cdk-cloudformation/datadog-monitors-monitor.CfnMonitorPropsType"
)
class CfnMonitorPropsType(enum.Enum):
    '''The type of the monitor.

    :schema: CfnMonitorPropsType
    '''

    COMPOSITE = "COMPOSITE"
    '''composite.'''
    EVENT_ALERT = "EVENT_ALERT"
    '''event alert.'''
    LOG_ALERT = "LOG_ALERT"
    '''log alert.'''
    METRIC_ALERT = "METRIC_ALERT"
    '''metric alert.'''
    PROCESS_ALERT = "PROCESS_ALERT"
    '''process alert.'''
    QUERY_ALERT = "QUERY_ALERT"
    '''query alert.'''
    SERVICE_CHECK = "SERVICE_CHECK"
    '''service check.'''
    SYNTHETICS_ALERT = "SYNTHETICS_ALERT"
    '''synthetics alert.'''
    TRACE_ANALYTICS_ALERT = "TRACE_ANALYTICS_ALERT"
    '''trace-analytics alert.'''
    SLO_ALERT = "SLO_ALERT"
    '''slo alert.'''


@jsii.data_type(
    jsii_type="@cdk-cloudformation/datadog-monitors-monitor.Creator",
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
        :param email: Email of the creator of the monitor.
        :param handle: Handle of the creator of the monitor.
        :param name: Name of the creator of the monitor.

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
        '''Email of the creator of the monitor.

        :schema: Creator#Email
        '''
        result = self._values.get("email")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def handle(self) -> typing.Optional[builtins.str]:
        '''Handle of the creator of the monitor.

        :schema: Creator#Handle
        '''
        result = self._values.get("handle")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the creator of the monitor.

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
    jsii_type="@cdk-cloudformation/datadog-monitors-monitor.MonitorOptions",
    jsii_struct_bases=[],
    name_mapping={
        "enable_logs_sample": "enableLogsSample",
        "escalation_message": "escalationMessage",
        "evaluation_delay": "evaluationDelay",
        "include_tags": "includeTags",
        "locked": "locked",
        "min_location_failed": "minLocationFailed",
        "new_host_delay": "newHostDelay",
        "no_data_timeframe": "noDataTimeframe",
        "notify_audit": "notifyAudit",
        "notify_no_data": "notifyNoData",
        "renotify_interval": "renotifyInterval",
        "require_full_window": "requireFullWindow",
        "synthetics_check_id": "syntheticsCheckId",
        "thresholds": "thresholds",
        "threshold_windows": "thresholdWindows",
        "timeout_h": "timeoutH",
    },
)
class MonitorOptions:
    def __init__(
        self,
        *,
        enable_logs_sample: typing.Optional[builtins.bool] = None,
        escalation_message: typing.Optional[builtins.str] = None,
        evaluation_delay: typing.Optional[jsii.Number] = None,
        include_tags: typing.Optional[builtins.bool] = None,
        locked: typing.Optional[builtins.bool] = None,
        min_location_failed: typing.Optional[jsii.Number] = None,
        new_host_delay: typing.Optional[jsii.Number] = None,
        no_data_timeframe: typing.Optional[jsii.Number] = None,
        notify_audit: typing.Optional[builtins.bool] = None,
        notify_no_data: typing.Optional[builtins.bool] = None,
        renotify_interval: typing.Optional[jsii.Number] = None,
        require_full_window: typing.Optional[builtins.bool] = None,
        synthetics_check_id: typing.Optional[jsii.Number] = None,
        thresholds: typing.Optional["MonitorThresholds"] = None,
        threshold_windows: typing.Optional["MonitorThresholdWindows"] = None,
        timeout_h: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param enable_logs_sample: Whether or not to include a sample of the logs.
        :param escalation_message: Message to include with a re-notification when renotify_interval is set.
        :param evaluation_delay: Time in seconds to delay evaluation.
        :param include_tags: Whether or not to include triggering tags into notification title.
        :param locked: Whether or not changes to this monitor should be restricted to the creator or admins.
        :param min_location_failed: Number of locations allowed to fail before triggering alert.
        :param new_host_delay: Time in seconds to allow a host to start reporting data before starting the evaluation of monitor results.
        :param no_data_timeframe: Number of minutes data stopped reporting before notifying.
        :param notify_audit: Whether or not to notify tagged users when changes are made to the monitor.
        :param notify_no_data: Whether or not to notify when data stops reporting.
        :param renotify_interval: Number of minutes after the last notification before the monitor re-notifies on the current status.
        :param require_full_window: Whether or not the monitor requires a full window of data before it is evaluated.
        :param synthetics_check_id: ID of the corresponding synthetics check.
        :param thresholds: The threshold definitions.
        :param threshold_windows: The threshold window definitions.
        :param timeout_h: Number of hours of the monitor not reporting data before it automatically resolves.

        :schema: MonitorOptions
        '''
        if isinstance(thresholds, dict):
            thresholds = MonitorThresholds(**thresholds)
        if isinstance(threshold_windows, dict):
            threshold_windows = MonitorThresholdWindows(**threshold_windows)
        self._values: typing.Dict[str, typing.Any] = {}
        if enable_logs_sample is not None:
            self._values["enable_logs_sample"] = enable_logs_sample
        if escalation_message is not None:
            self._values["escalation_message"] = escalation_message
        if evaluation_delay is not None:
            self._values["evaluation_delay"] = evaluation_delay
        if include_tags is not None:
            self._values["include_tags"] = include_tags
        if locked is not None:
            self._values["locked"] = locked
        if min_location_failed is not None:
            self._values["min_location_failed"] = min_location_failed
        if new_host_delay is not None:
            self._values["new_host_delay"] = new_host_delay
        if no_data_timeframe is not None:
            self._values["no_data_timeframe"] = no_data_timeframe
        if notify_audit is not None:
            self._values["notify_audit"] = notify_audit
        if notify_no_data is not None:
            self._values["notify_no_data"] = notify_no_data
        if renotify_interval is not None:
            self._values["renotify_interval"] = renotify_interval
        if require_full_window is not None:
            self._values["require_full_window"] = require_full_window
        if synthetics_check_id is not None:
            self._values["synthetics_check_id"] = synthetics_check_id
        if thresholds is not None:
            self._values["thresholds"] = thresholds
        if threshold_windows is not None:
            self._values["threshold_windows"] = threshold_windows
        if timeout_h is not None:
            self._values["timeout_h"] = timeout_h

    @builtins.property
    def enable_logs_sample(self) -> typing.Optional[builtins.bool]:
        '''Whether or not to include a sample of the logs.

        :schema: MonitorOptions#EnableLogsSample
        '''
        result = self._values.get("enable_logs_sample")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def escalation_message(self) -> typing.Optional[builtins.str]:
        '''Message to include with a re-notification when renotify_interval is set.

        :schema: MonitorOptions#EscalationMessage
        '''
        result = self._values.get("escalation_message")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def evaluation_delay(self) -> typing.Optional[jsii.Number]:
        '''Time in seconds to delay evaluation.

        :schema: MonitorOptions#EvaluationDelay
        '''
        result = self._values.get("evaluation_delay")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def include_tags(self) -> typing.Optional[builtins.bool]:
        '''Whether or not to include triggering tags into notification title.

        :schema: MonitorOptions#IncludeTags
        '''
        result = self._values.get("include_tags")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def locked(self) -> typing.Optional[builtins.bool]:
        '''Whether or not changes to this monitor should be restricted to the creator or admins.

        :schema: MonitorOptions#Locked
        '''
        result = self._values.get("locked")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def min_location_failed(self) -> typing.Optional[jsii.Number]:
        '''Number of locations allowed to fail before triggering alert.

        :schema: MonitorOptions#MinLocationFailed
        '''
        result = self._values.get("min_location_failed")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def new_host_delay(self) -> typing.Optional[jsii.Number]:
        '''Time in seconds to allow a host to start reporting data before starting the evaluation of monitor results.

        :schema: MonitorOptions#NewHostDelay
        '''
        result = self._values.get("new_host_delay")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def no_data_timeframe(self) -> typing.Optional[jsii.Number]:
        '''Number of minutes data stopped reporting before notifying.

        :schema: MonitorOptions#NoDataTimeframe
        '''
        result = self._values.get("no_data_timeframe")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def notify_audit(self) -> typing.Optional[builtins.bool]:
        '''Whether or not to notify tagged users when changes are made to the monitor.

        :schema: MonitorOptions#NotifyAudit
        '''
        result = self._values.get("notify_audit")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def notify_no_data(self) -> typing.Optional[builtins.bool]:
        '''Whether or not to notify when data stops reporting.

        :schema: MonitorOptions#NotifyNoData
        '''
        result = self._values.get("notify_no_data")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def renotify_interval(self) -> typing.Optional[jsii.Number]:
        '''Number of minutes after the last notification before the monitor re-notifies on the current status.

        :schema: MonitorOptions#RenotifyInterval
        '''
        result = self._values.get("renotify_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def require_full_window(self) -> typing.Optional[builtins.bool]:
        '''Whether or not the monitor requires a full window of data before it is evaluated.

        :schema: MonitorOptions#RequireFullWindow
        '''
        result = self._values.get("require_full_window")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def synthetics_check_id(self) -> typing.Optional[jsii.Number]:
        '''ID of the corresponding synthetics check.

        :schema: MonitorOptions#SyntheticsCheckID
        '''
        result = self._values.get("synthetics_check_id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def thresholds(self) -> typing.Optional["MonitorThresholds"]:
        '''The threshold definitions.

        :schema: MonitorOptions#Thresholds
        '''
        result = self._values.get("thresholds")
        return typing.cast(typing.Optional["MonitorThresholds"], result)

    @builtins.property
    def threshold_windows(self) -> typing.Optional["MonitorThresholdWindows"]:
        '''The threshold window definitions.

        :schema: MonitorOptions#ThresholdWindows
        '''
        result = self._values.get("threshold_windows")
        return typing.cast(typing.Optional["MonitorThresholdWindows"], result)

    @builtins.property
    def timeout_h(self) -> typing.Optional[jsii.Number]:
        '''Number of hours of the monitor not reporting data before it automatically resolves.

        :schema: MonitorOptions#TimeoutH
        '''
        result = self._values.get("timeout_h")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MonitorOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/datadog-monitors-monitor.MonitorThresholdWindows",
    jsii_struct_bases=[],
    name_mapping={
        "recovery_window": "recoveryWindow",
        "trigger_window": "triggerWindow",
    },
)
class MonitorThresholdWindows:
    def __init__(
        self,
        *,
        recovery_window: typing.Optional[builtins.str] = None,
        trigger_window: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param recovery_window: How long an anomalous metric must be normal before recovering from an alert state.
        :param trigger_window: How long a metric must be anomalous before triggering an alert.

        :schema: MonitorThresholdWindows
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if recovery_window is not None:
            self._values["recovery_window"] = recovery_window
        if trigger_window is not None:
            self._values["trigger_window"] = trigger_window

    @builtins.property
    def recovery_window(self) -> typing.Optional[builtins.str]:
        '''How long an anomalous metric must be normal before recovering from an alert state.

        :schema: MonitorThresholdWindows#RecoveryWindow
        '''
        result = self._values.get("recovery_window")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def trigger_window(self) -> typing.Optional[builtins.str]:
        '''How long a metric must be anomalous before triggering an alert.

        :schema: MonitorThresholdWindows#TriggerWindow
        '''
        result = self._values.get("trigger_window")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MonitorThresholdWindows(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/datadog-monitors-monitor.MonitorThresholds",
    jsii_struct_bases=[],
    name_mapping={
        "critical": "critical",
        "critical_recovery": "criticalRecovery",
        "ok": "ok",
        "warning": "warning",
        "warning_recovery": "warningRecovery",
    },
)
class MonitorThresholds:
    def __init__(
        self,
        *,
        critical: typing.Optional[jsii.Number] = None,
        critical_recovery: typing.Optional[jsii.Number] = None,
        ok: typing.Optional[jsii.Number] = None,
        warning: typing.Optional[jsii.Number] = None,
        warning_recovery: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param critical: Threshold value for triggering an alert.
        :param critical_recovery: Threshold value for recovering from an alert state.
        :param ok: Threshold value for recovering from an alert state.
        :param warning: Threshold value for triggering a warning.
        :param warning_recovery: Threshold value for recovering from a warning state.

        :schema: MonitorThresholds
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if critical is not None:
            self._values["critical"] = critical
        if critical_recovery is not None:
            self._values["critical_recovery"] = critical_recovery
        if ok is not None:
            self._values["ok"] = ok
        if warning is not None:
            self._values["warning"] = warning
        if warning_recovery is not None:
            self._values["warning_recovery"] = warning_recovery

    @builtins.property
    def critical(self) -> typing.Optional[jsii.Number]:
        '''Threshold value for triggering an alert.

        :schema: MonitorThresholds#Critical
        '''
        result = self._values.get("critical")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def critical_recovery(self) -> typing.Optional[jsii.Number]:
        '''Threshold value for recovering from an alert state.

        :schema: MonitorThresholds#CriticalRecovery
        '''
        result = self._values.get("critical_recovery")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def ok(self) -> typing.Optional[jsii.Number]:
        '''Threshold value for recovering from an alert state.

        :schema: MonitorThresholds#OK
        '''
        result = self._values.get("ok")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def warning(self) -> typing.Optional[jsii.Number]:
        '''Threshold value for triggering a warning.

        :schema: MonitorThresholds#Warning
        '''
        result = self._values.get("warning")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def warning_recovery(self) -> typing.Optional[jsii.Number]:
        '''Threshold value for recovering from a warning state.

        :schema: MonitorThresholds#WarningRecovery
        '''
        result = self._values.get("warning_recovery")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MonitorThresholds(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnMonitor",
    "CfnMonitorProps",
    "CfnMonitorPropsType",
    "Creator",
    "MonitorOptions",
    "MonitorThresholdWindows",
    "MonitorThresholds",
]

publication.publish()
