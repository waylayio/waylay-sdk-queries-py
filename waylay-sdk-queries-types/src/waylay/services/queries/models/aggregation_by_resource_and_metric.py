# coding: utf-8
"""Waylay Query: timeseries queries (v1 protocol) models.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""

from __future__ import annotations

from typing import (
    Dict,
    Union,
)

from typing_extensions import (
    Annotated,  # >=3.9
)

from ..models.aggregation_by_resource_or_metric import AggregationByResourceOrMetric

AggregationByResourceAndMetric = Union[
    Annotated[
        Dict[str, AggregationByResourceOrMetric],
        "Aggregation methods specified per resource or metric.",
    ]
]
"""AggregationByResourceAndMetric."""