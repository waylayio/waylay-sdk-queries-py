"""Waylay Query: timeseries queries (v1 protocol) models.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import Annotated, TypeAlias

from ..models.aggregation import Aggregation
from ..models.aggregations_inner import AggregationsInner

AggregationByResourceOrMetricValue: TypeAlias = Aggregation | Annotated[list[AggregationsInner], "Aggregation methods, leading to sepearate series."]
"""AggregationByResourceOrMetricValue."""
