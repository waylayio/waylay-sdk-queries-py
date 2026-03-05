"""Waylay Query: timeseries queries (v1 protocol) models.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Do not edit the class manually.

"""

from __future__ import annotations

from enum import Enum


class SeriesSpecCountNonNumeric(str, Enum):
    """Use the count of non-numeric observations in the sample interval.."""

    COUNT_MINUS_NON_MINUS_NUMERIC = "count-non-numeric"

    def __str__(self) -> str:
        return str(self.value)
