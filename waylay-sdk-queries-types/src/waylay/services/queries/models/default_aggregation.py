# coding: utf-8
"""Waylay Query: timeseries queries (v1 protocol) models.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""

from __future__ import annotations

from typing import (
    Dict,
    List,
    Union,
)

from typing_extensions import (
    Annotated,  # >=3.9
)

from ..models.aggregation_by_resource_and_metric_value import (
    AggregationByResourceAndMetricValue,
)
from ..models.aggregation_by_resource_or_metric_value import (
    AggregationByResourceOrMetricValue,
)
from ..models.aggregation_method import AggregationMethod
from ..models.aggregations_inner import AggregationsInner

DefaultAggregation = Union[
    Annotated[AggregationMethod, ""],
    Annotated[
        List[AggregationsInner], "Aggregation methods, leading to sepearate series."
    ],
    Annotated[
        Dict[str, AggregationByResourceOrMetricValue],
        "Aggregation methods specified per resource or metric.",
    ],
    Annotated[
        Dict[str, AggregationByResourceAndMetricValue],
        "Aggregation methods specified per resource and metric.",
    ],
]
"""Default aggregation method(s) for the series in the query.."""
