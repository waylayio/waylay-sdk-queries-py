"""Waylay Query: timeseries queries (v1 protocol) models.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Do not edit the class manually.

"""

from __future__ import annotations

from enum import Enum


class AlignmentUntil(str, Enum):
    """Align a the `until` window boundary."""

    UNTIL = "until"

    def __str__(self) -> str:
        return str(self.value)
