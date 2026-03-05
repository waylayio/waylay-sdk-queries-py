"""Waylay Query: timeseries queries (v1 protocol) models.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Do not edit the class manually.

"""

from __future__ import annotations

from enum import Enum


class ExecuteByNameQueriesV1DataQueryNameGetAggregationMedian(str, Enum):
    """Aggregate data by the median value: The n/2-th value when ordered, the average of the (n-1)/2-th and (n+1)/2-th value when n is uneven.."""

    MEDIAN = "median"

    def __str__(self) -> str:
        return str(self.value)
