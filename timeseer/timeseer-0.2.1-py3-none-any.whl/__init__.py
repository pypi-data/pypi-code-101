"""Timeseer Client provides convenient remote access to Timeseer.

Data, metadata and event frames are exposed as Python objects."""

from kukur import DataType, Dictionary, InterpolationType, Metadata, SeriesSelector

from .base import AugmentationStrategy, ProcessType, TimeseerClientException
from .client import Client, filter_event_frames, filter_series
from .metadata.fields import register_custom_fields


register_custom_fields(Metadata)


__all__ = [
    "AugmentationStrategy",
    "Client",
    "DataType",
    "Dictionary",
    "InterpolationType",
    "Metadata",
    "ProcessType",
    "SeriesSelector",
    "TimeseerClientException",
    "filter_event_frames",
    "filter_series",
]
