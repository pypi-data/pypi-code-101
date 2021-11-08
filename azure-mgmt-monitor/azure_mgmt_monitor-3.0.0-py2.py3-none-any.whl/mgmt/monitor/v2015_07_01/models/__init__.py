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
    from ._models_py3 import DimensionProperties
    from ._models_py3 import ErrorContract
    from ._models_py3 import ErrorResponse
    from ._models_py3 import LocalizableString
    from ._models_py3 import LocationThresholdRuleCondition
    from ._models_py3 import LogSettings
    from ._models_py3 import LogSpecification
    from ._models_py3 import ManagementEventAggregationCondition
    from ._models_py3 import ManagementEventRuleCondition
    from ._models_py3 import MetricAvailability
    from ._models_py3 import MetricAvailabilityLocation
    from ._models_py3 import MetricDefinition
    from ._models_py3 import MetricDefinitionCollection
    from ._models_py3 import MetricSettings
    from ._models_py3 import MetricSpecification
    from ._models_py3 import Operation
    from ._models_py3 import OperationDisplay
    from ._models_py3 import OperationListResult
    from ._models_py3 import Resource
    from ._models_py3 import RetentionPolicy
    from ._models_py3 import RuleAction
    from ._models_py3 import RuleCondition
    from ._models_py3 import RuleDataSource
    from ._models_py3 import RuleEmailAction
    from ._models_py3 import RuleManagementEventClaimsDataSource
    from ._models_py3 import RuleManagementEventDataSource
    from ._models_py3 import RuleMetricDataSource
    from ._models_py3 import RuleWebhookAction
    from ._models_py3 import ServiceDiagnosticSettingsResource
    from ._models_py3 import ServiceSpecification
    from ._models_py3 import TableInfoEntry
    from ._models_py3 import ThresholdRuleCondition
except (SyntaxError, ImportError):
    from ._models import AlertRuleResource  # type: ignore
    from ._models import AlertRuleResourceCollection  # type: ignore
    from ._models import AlertRuleResourcePatch  # type: ignore
    from ._models import DimensionProperties  # type: ignore
    from ._models import ErrorContract  # type: ignore
    from ._models import ErrorResponse  # type: ignore
    from ._models import LocalizableString  # type: ignore
    from ._models import LocationThresholdRuleCondition  # type: ignore
    from ._models import LogSettings  # type: ignore
    from ._models import LogSpecification  # type: ignore
    from ._models import ManagementEventAggregationCondition  # type: ignore
    from ._models import ManagementEventRuleCondition  # type: ignore
    from ._models import MetricAvailability  # type: ignore
    from ._models import MetricAvailabilityLocation  # type: ignore
    from ._models import MetricDefinition  # type: ignore
    from ._models import MetricDefinitionCollection  # type: ignore
    from ._models import MetricSettings  # type: ignore
    from ._models import MetricSpecification  # type: ignore
    from ._models import Operation  # type: ignore
    from ._models import OperationDisplay  # type: ignore
    from ._models import OperationListResult  # type: ignore
    from ._models import Resource  # type: ignore
    from ._models import RetentionPolicy  # type: ignore
    from ._models import RuleAction  # type: ignore
    from ._models import RuleCondition  # type: ignore
    from ._models import RuleDataSource  # type: ignore
    from ._models import RuleEmailAction  # type: ignore
    from ._models import RuleManagementEventClaimsDataSource  # type: ignore
    from ._models import RuleManagementEventDataSource  # type: ignore
    from ._models import RuleMetricDataSource  # type: ignore
    from ._models import RuleWebhookAction  # type: ignore
    from ._models import ServiceDiagnosticSettingsResource  # type: ignore
    from ._models import ServiceSpecification  # type: ignore
    from ._models import TableInfoEntry  # type: ignore
    from ._models import ThresholdRuleCondition  # type: ignore

from ._monitor_management_client_enums import (
    AggregationType,
    ConditionOperator,
    TimeAggregationOperator,
    Unit,
)

__all__ = [
    'AlertRuleResource',
    'AlertRuleResourceCollection',
    'AlertRuleResourcePatch',
    'DimensionProperties',
    'ErrorContract',
    'ErrorResponse',
    'LocalizableString',
    'LocationThresholdRuleCondition',
    'LogSettings',
    'LogSpecification',
    'ManagementEventAggregationCondition',
    'ManagementEventRuleCondition',
    'MetricAvailability',
    'MetricAvailabilityLocation',
    'MetricDefinition',
    'MetricDefinitionCollection',
    'MetricSettings',
    'MetricSpecification',
    'Operation',
    'OperationDisplay',
    'OperationListResult',
    'Resource',
    'RetentionPolicy',
    'RuleAction',
    'RuleCondition',
    'RuleDataSource',
    'RuleEmailAction',
    'RuleManagementEventClaimsDataSource',
    'RuleManagementEventDataSource',
    'RuleMetricDataSource',
    'RuleWebhookAction',
    'ServiceDiagnosticSettingsResource',
    'ServiceSpecification',
    'TableInfoEntry',
    'ThresholdRuleCondition',
    'AggregationType',
    'ConditionOperator',
    'TimeAggregationOperator',
    'Unit',
]
