"""Waylay Query: timeseries queries (v1 protocol) models.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Do not edit the class manually.

"""

from __future__ import annotations

from enum import Enum


class SeriesSpecBackfill(str, Enum):
    """Same as pad, but using the last observed value. This method also extrapolates."""

    BACKFILL = "backfill"

    def __str__(self) -> str:
        return str(self.value)
