"""Waylay Query: timeseries queries (v1 protocol) models.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import TypeAlias

from ..models.interpolation_spec3 import InterpolationSpec3
from ..models.interpolation_specification_any_of import InterpolationSpecificationAnyOf

InterpolationSpecification: TypeAlias = InterpolationSpec3 | InterpolationSpecificationAnyOf
"""InterpolationSpecification."""
