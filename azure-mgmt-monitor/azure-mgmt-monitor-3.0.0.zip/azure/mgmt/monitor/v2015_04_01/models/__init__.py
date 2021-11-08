# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import AlertRuleResource
    from ._models_py3 import AlertRuleResourceCollection
    from ._models_py3 import AlertRuleResourcePatch
    from ._models_py3 import AutoscaleNotification
    from ._models_py3 import AutoscaleProfile
    from ._models_py3 import AutoscaleSettingResource
    from ._models_py3 import AutoscaleSettingResourceCollection
    from ._models_py3 import AutoscaleSettingResourcePatch
    from ._models_py3 import EmailNotification
    from ._models_py3 import ErrorResponse
    from ._models_py3 import EventCategoryCollection
    from ._models_py3 import EventData
    from ._models_py3 import EventDataCollection
    from ._models_py3 import HttpRequestInfo
    from ._models_py3 import LocalizableString
    from ._models_py3 import LocationThresholdRuleCondition
    from ._models_py3 import ManagementEventAggregationCondition
    from ._models_py3 import ManagementEventRuleCondition
    from ._models_py3 import MetricTrigger
    from ._models_py3 import Operation
    from ._models_py3 import OperationDisplay
    from ._models_py3 import OperationListResult
    from ._models_py3 import Recurrence
    from ._models_py3 import RecurrentSchedule
    from ._models_py3 import Resource
    from ._models_py3 import RuleAction
    from ._models_py3 import RuleCondition
    from ._models_py3 import RuleDataSource
    from ._models_py3 import RuleEmailAction
    from ._models_py3 import RuleManagementEventClaimsDataSource
    from ._models_py3 import RuleManagementEventDataSource
    from ._models_py3 import RuleMetricDataSource
    from ._models_py3 import RuleWebhookAction
    from ._models_py3 import ScaleAction
    from ._models_py3 import ScaleCapacity
    from ._models_py3 import ScaleRule
    from ._models_py3 import ScaleRuleMetricDimension
    from ._models_py3 import SenderAuthorization
    from ._models_py3 import ThresholdRuleCondition
    from ._models_py3 import TimeWindow
    from ._models_py3 import WebhookNotification
except (SyntaxError, ImportError):
    from ._models import AlertRuleResource  # type: ignore
    from ._models import AlertRuleResourceCollection  # type: ignore
    from ._models import AlertRuleResourcePatch  # type: ignore
    from ._models import AutoscaleNotification  # type: ignore
    from ._models import AutoscaleProfile  # type: ignore
    from ._models import AutoscaleSettingResource  # type: ignore
    from ._models import AutoscaleSettingResourceCollection  # type: ignore
    from ._models import AutoscaleSettingResourcePatch  # type: ignore
    from ._models import EmailNotification  # type: ignore
    from ._models import ErrorResponse  # type: ignore
    from ._models import EventCategoryCollection  # type: ignore
    from ._models import EventData  # type: ignore
    from ._models import EventDataCollection  # type: ignore
    from ._models import HttpRequestInfo  # type: ignore
    from ._models import LocalizableString  # type: ignore
    from ._models import LocationThresholdRuleCondition  # type: ignore
    from ._models import ManagementEventAggregationCondition  # type: ignore
    from ._models import ManagementEventRuleCondition  # type: ignore
    from ._models import MetricTrigger  # type: ignore
    from ._models import Operation  # type: ignore
    from ._models import OperationDisplay  # type: ignore
    from ._models import OperationListResult  # type: ignore
    from ._models import Recurrence  # type: ignore
    from ._models import RecurrentSchedule  # type: ignore
    from ._models import Resource  # type: ignore
    from ._models import RuleAction  # type: ignore
    from ._models import RuleCondition  # type: ignore
    from ._models import RuleDataSource  # type: ignore
    from ._models import RuleEmailAction  # type: ignore
    from ._models import RuleManagementEventClaimsDataSource  # type: ignore
    from ._models import RuleManagementEventDataSource  # type: ignore
    from ._models import RuleMetricDataSource  # type: ignore
    from ._models import RuleWebhookAction  # type: ignore
    from ._models import ScaleAction  # type: ignore
    from ._models import ScaleCapacity  # type: ignore
    from ._models import ScaleRule  # type: ignore
    from ._models import ScaleRuleMetricDimension  # type: ignore
    from ._models import SenderAuthorization  # type: ignore
    from ._models import ThresholdRuleCondition  # type: ignore
    from ._models import TimeWindow  # type: ignore
    from ._models import WebhookNotification  # type: ignore

from ._monitor_management_client_enums import (
    ComparisonOperationType,
    ConditionOperator,
    EventLevel,
    MetricStatisticType,
    RecurrenceFrequency,
    ScaleDirection,
    ScaleRuleMetricDimensionOperationType,
    ScaleType,
    TimeAggregationOperator,
    TimeAggregationType,
)

__all__ = [
    'AlertRuleResource',
    'AlertRuleResourceCollection',
    'AlertRuleResourcePatch',
    'AutoscaleNotification',
    'AutoscaleProfile',
    'AutoscaleSettingResource',
    'AutoscaleSettingResourceCollection',
    'AutoscaleSettingResourcePatch',
    'EmailNotification',
    'ErrorResponse',
    'EventCategoryCollection',
    'EventData',
    'EventDataCollection',
    'HttpRequestInfo',
    'LocalizableString',
    'LocationThresholdRuleCondition',
    'ManagementEventAggregationCondition',
    'ManagementEventRuleCondition',
    'MetricTrigger',
    'Operation',
    'OperationDisplay',
    'OperationListResult',
    'Recurrence',
    'RecurrentSchedule',
    'Resource',
    'RuleAction',
    'RuleCondition',
    'RuleDataSource',
    'RuleEmailAction',
    'RuleManagementEventClaimsDataSource',
    'RuleManagementEventDataSource',
    'RuleMetricDataSource',
    'RuleWebhookAction',
    'ScaleAction',
    'ScaleCapacity',
    'ScaleRule',
    'ScaleRuleMetricDimension',
    'SenderAuthorization',
    'ThresholdRuleCondition',
    'TimeWindow',
    'WebhookNotification',
    'ComparisonOperationType',
    'ConditionOperator',
    'EventLevel',
    'MetricStatisticType',
    'RecurrenceFrequency',
    'ScaleDirection',
    'ScaleRuleMetricDimensionOperationType',
    'ScaleType',
    'TimeAggregationOperator',
    'TimeAggregationType',
]
