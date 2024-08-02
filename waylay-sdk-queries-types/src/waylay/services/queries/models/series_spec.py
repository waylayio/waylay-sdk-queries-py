# coding: utf-8
"""Waylay Query: timeseries queries (v1 protocol) models.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""

from __future__ import annotations

from pydantic import (
    ConfigDict,
    Field,
    StrictStr,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.aggregation_method import AggregationMethod
from ..models.interpolation import Interpolation


class SeriesSpec(WaylayBaseModel):
    """Query specification for a single series.."""

    name: StrictStr | None = Field(
        default=None,
        description="Optional alias name for the series. This name is used when exporting the dataset to CSV format.",
    )
    resource: StrictStr | None = Field(
        default=None,
        description="Resource id for the series, required unless it is specified as a query default.",
    )
    metric: StrictStr | None = Field(
        default=None,
        description="Metric name for the series, required unless it is specified as a query default.",
    )
    aggregration: AggregationMethod | None = None
    interpolation: Interpolation | None = None

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )