# coding: utf-8
"""Waylay Query: timeseries queries (v1 protocol) models.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""

from __future__ import annotations

from enum import Enum


class ColumnDataSetDataAxis(str, Enum):
    """ColumnDataSetDataAxis."""

    ROW = "row"

    def __str__(self) -> str:
        return str(self.value)
