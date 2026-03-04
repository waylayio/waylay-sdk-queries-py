"""Waylay Query: timeseries queries (v1 protocol) models.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import Annotated, TypeAlias

from ..models.aggregation_by_resource_or_metric_value1 import (
    AggregationByResourceOrMetricValue1,
)

AggregationByResourceAndMetricValue1: TypeAlias = (Annotated[
        dict[str, AggregationByResourceOrMetricValue1],
        "Aggregation methods specified per resource or metric.",
    ])
"""AggregationByResourceAndMetricValue1."""
