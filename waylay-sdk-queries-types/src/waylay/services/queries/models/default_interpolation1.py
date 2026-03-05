"""Waylay Query: timeseries queries (v1 protocol) models.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import TypeAlias

from ..models.default_interpolation1_any_of import DefaultInterpolation1AnyOf
from ..models.interpolation_spec2 import InterpolationSpec2

DefaultInterpolation1: TypeAlias = InterpolationSpec2 | DefaultInterpolation1AnyOf
"""Default Interpolation method for the series (if aggregated).."""
