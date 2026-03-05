"""Waylay Query: timeseries queries (v1 protocol) models.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Do not edit the class manually.

"""

from __future__ import annotations

from enum import Enum


class AlignmentWrap(str, Enum):
    """Shift first boundary backward, and last boundary forward to align with the grid."""

    WRAP = "wrap"

    def __str__(self) -> str:
        return str(self.value)
