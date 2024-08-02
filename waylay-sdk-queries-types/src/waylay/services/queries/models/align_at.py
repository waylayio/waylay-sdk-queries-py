# coding: utf-8
"""Waylay Query: timeseries queries (v1 protocol) models.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""

from __future__ import annotations

from enum import Enum


class AlignAt(str, Enum):
    """Possible values for `align.at`.  * 'grid' Align to a fixed grid (possibly using timezone information) * 'from' Align a the `from` boundary * 'until' Align a the `until` boundary * 'boundary' Align a the `from` boundary if specified,    otherwise the `until` boundary.  When not specified, 'grid' is used.."""

    GRID = "grid"
    BOUNDARY = "boundary"
    FROM = "from"
    UNTIL = "until"

    def __str__(self) -> str:
        return str(self.value)
