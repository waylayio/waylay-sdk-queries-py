"""Waylay Query: timeseries queries (v1 protocol) models.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import TypeAlias

from ..models.default_interpolation_any_of import DefaultInterpolationAnyOf
from ..models.interpolation_spec import InterpolationSpec

ExecuteByNameQueriesV1DataQueryNameGetInterpolation: TypeAlias = DefaultInterpolationAnyOf | InterpolationSpec
"""ExecuteByNameQueriesV1DataQueryNameGetInterpolation."""
