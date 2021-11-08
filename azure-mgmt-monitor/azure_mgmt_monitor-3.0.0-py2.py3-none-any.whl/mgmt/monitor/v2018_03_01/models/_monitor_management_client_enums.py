# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum, EnumMeta
from six import with_metaclass

class _CaseInsensitiveEnumMeta(EnumMeta):
    def __getitem__(self, name):
        return super().__getitem__(name.upper())

    def __getattr__(cls, name):
        """Return the enum member matching `name`
        We use __getattr__ instead of descriptors or inserting into the enum
        class' __dict__ in order to support `name` and `value` being both
        properties for enum members (which live in the class' __dict__) and
        enum members themselves.
        """
        try:
            return cls._member_map_[name.upper()]
        except KeyError:
            raise AttributeError(name)


class AggregationTypeEnum(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """the criteria time aggregation types.
    """

    AVERAGE = "Average"
    COUNT = "Count"
    MINIMUM = "Minimum"
    MAXIMUM = "Maximum"
    TOTAL = "Total"

class CriterionType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Specifies the type of threshold criteria
    """

    STATIC_THRESHOLD_CRITERION = "StaticThresholdCriterion"
    DYNAMIC_THRESHOLD_CRITERION = "DynamicThresholdCriterion"

class DynamicThresholdOperator(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The operator used to compare the metric value against the threshold.
    """

    GREATER_THAN = "GreaterThan"
    LESS_THAN = "LessThan"
    GREATER_OR_LESS_THAN = "GreaterOrLessThan"

class DynamicThresholdSensitivity(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The extent of deviation required to trigger an alert. This will affect how tight the threshold
    is to the metric series pattern.
    """

    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"

class Odatatype(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """specifies the type of the alert criteria.
    """

    MICROSOFT_AZURE_MONITOR_SINGLE_RESOURCE_MULTIPLE_METRIC_CRITERIA = "Microsoft.Azure.Monitor.SingleResourceMultipleMetricCriteria"
    MICROSOFT_AZURE_MONITOR_MULTIPLE_RESOURCE_MULTIPLE_METRIC_CRITERIA = "Microsoft.Azure.Monitor.MultipleResourceMultipleMetricCriteria"
    MICROSOFT_AZURE_MONITOR_WEBTEST_LOCATION_AVAILABILITY_CRITERIA = "Microsoft.Azure.Monitor.WebtestLocationAvailabilityCriteria"

class Operator(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """the criteria operator.
    """

    EQUALS = "Equals"
    GREATER_THAN = "GreaterThan"
    GREATER_THAN_OR_EQUAL = "GreaterThanOrEqual"
    LESS_THAN = "LessThan"
    LESS_THAN_OR_EQUAL = "LessThanOrEqual"

class ReceiverStatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Indicates the status of the receiver. Receivers that are not Enabled will not receive any
    communications.
    """

    NOT_SPECIFIED = "NotSpecified"
    ENABLED = "Enabled"
    DISABLED = "Disabled"
