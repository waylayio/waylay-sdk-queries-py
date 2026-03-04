"""Waylay Query: timeseries queries (v1 protocol) models.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import Annotated, TypeAlias

from ..models.aggregation1 import Aggregation1
from ..models.aggregation_by_resource_and_metric_value1 import (
    AggregationByResourceAndMetricValue1,
)
from ..models.aggregation_by_resource_or_metric_value1 import (
    AggregationByResourceOrMetricValue1,
)
from ..models.aggregations_inner1 import AggregationsInner1

DefaultAggregation1: TypeAlias = Aggregation1 | Annotated[list[AggregationsInner1], "Aggregation methods, leading to sepearate series."] | Annotated[dict[str, AggregationByResourceOrMetricValue1], "Aggregation methods specified per resource or metric."] | Annotated[dict[str, AggregationByResourceAndMetricValue1], "Aggregation methods specified per resource and metric."]
"""Default aggregation method(s) for the series in the query.."""
