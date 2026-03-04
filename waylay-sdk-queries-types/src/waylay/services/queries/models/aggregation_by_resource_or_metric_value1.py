"""Waylay Query: timeseries queries (v1 protocol) models.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import Annotated, TypeAlias

from ..models.aggregation1 import Aggregation1
from ..models.aggregations_inner1 import AggregationsInner1

AggregationByResourceOrMetricValue1: TypeAlias = Aggregation1 | Annotated[list[AggregationsInner1], "Aggregation methods, leading to sepearate series."]
"""AggregationByResourceOrMetricValue1."""
