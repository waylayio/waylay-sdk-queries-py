"""Waylay Query: timeseries queries (v1 protocol) models.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Do not edit the class manually.

"""

from __future__ import annotations

from enum import Enum


class AlignmentGrid(str, Enum):
    """Align to a fixed grid defined by the alignment `frequency` and `timezone`.."""

    GRID = "grid"

    def __str__(self) -> str:
        return str(self.value)
