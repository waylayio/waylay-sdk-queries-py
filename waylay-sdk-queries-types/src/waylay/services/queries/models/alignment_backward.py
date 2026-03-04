"""Waylay Query: timeseries queries (v1 protocol) models.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Do not edit the class manually.

"""

from __future__ import annotations

from enum import Enum


class AlignmentBackward(str, Enum):
    """Shift both boundaries (`align.at=grid`) or first boundary (`align.at=until`) backward to align with the grid.."""

    BACKWARD = "backward"

    def __str__(self) -> str:
        return str(self.value)
