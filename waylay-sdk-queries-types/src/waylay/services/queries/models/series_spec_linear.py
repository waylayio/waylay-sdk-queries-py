"""Waylay Query: timeseries queries (v1 protocol) models.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Do not edit the class manually.

"""

from __future__ import annotations

from enum import Enum


class SeriesSpecLinear(str, Enum):
    """Linearly go from the first observed value of the gap to the last observed oneThis method also extrapolates."""

    LINEAR = "linear"

    def __str__(self) -> str:
        return str(self.value)
