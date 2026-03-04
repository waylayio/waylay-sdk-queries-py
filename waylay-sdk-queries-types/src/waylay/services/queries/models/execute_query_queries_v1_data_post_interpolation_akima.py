"""Waylay Query: timeseries queries (v1 protocol) models.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Do not edit the class manually.

"""

from __future__ import annotations

from enum import Enum


class ExecuteQueryQueriesV1DataPostInterpolationAkima(str, Enum):
    """Interpolate with a non-smoothing spline of order 2, called Akima interpolation.."""

    AKIMA = "akima"

    def __str__(self) -> str:
        return str(self.value)
