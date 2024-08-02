# coding: utf-8
"""Waylay Query: timeseries queries (v1 protocol) models.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""

from __future__ import annotations

from enum import Enum


class RenderModeOneOf6(str, Enum):
    """Render an hierarchical object for each observation. Shows an iso timestamp.  ###### options - `iso_timestamp`: `True` - `hierarchical`: `True` - `show_levels`: `True` - `roll_up`: `True`."""

    HIER_DICT = "HIER_DICT"

    def __str__(self) -> str:
        return str(self.value)