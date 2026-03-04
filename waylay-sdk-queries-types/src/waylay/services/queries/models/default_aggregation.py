"""Waylay Query: timeseries queries (v1 protocol) models.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import Annotated, TypeAlias

from ..models.aggregation import Aggregation
from ..models.aggregation_by_resource_and_metric_value import (
    AggregationByResourceAndMetricValue,
)
from ..models.aggregation_by_resource_or_metric_value import (
    AggregationByResourceOrMetricValue,
)
from ..models.aggregations_inner import AggregationsInner

DefaultAggregation: TypeAlias = Aggregation | Annotated[list[AggregationsInner], "Aggregation methods, leading to sepearate series."] | Annotated[dict[str, AggregationByResourceOrMetricValue], "Aggregation methods specified per resource or metric."] | Annotated[dict[str, AggregationByResourceAndMetricValue], "Aggregation methods specified per resource and metric."]
"""Default aggregation method(s) for the series in the query.."""
