# coding: utf-8
"""Waylay Query: timeseries queries (v1 protocol) models.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""

from __future__ import annotations

from typing import (
    Union,
)

from typing_extensions import (
    Annotated,  # >=3.9
)

Datum = Union[Annotated[float, ""], Annotated[str, ""], Annotated[bool, ""]]
"""A single metric value for a timeseries.  A null value indicates that no (aggregated/interpolated) value  exists for the corresponding timestamp.."""