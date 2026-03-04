"""Waylay Query: timeseries queries (v1 protocol) models.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Do not edit the class manually.

"""

from __future__ import annotations

from enum import Enum


class InterpolationSpecFixed(str, Enum):
    """Interpolate with a fixed, user-specified value. This method also extrapolates.."""

    FIXED = "fixed"

    def __str__(self) -> str:
        return str(self.value)
