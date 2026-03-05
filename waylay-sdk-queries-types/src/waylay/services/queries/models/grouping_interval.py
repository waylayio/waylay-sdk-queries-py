"""Waylay Query: timeseries queries (v1 protocol) models.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import Annotated, TypeAlias

from ..models.query_input_inferred import QueryInputInferred

GroupingInterval: TypeAlias = Annotated[str, "A period in [ISO8601 duration](https://en.wikipedia.org/wiki/ISO_8601#Durations) format."] | QueryInputInferred
"""Interval used to aggregate or regularize data. One of the [time line](https://docs.waylay.io/#/api/query/?id=time-line-properties) specifiers.."""
