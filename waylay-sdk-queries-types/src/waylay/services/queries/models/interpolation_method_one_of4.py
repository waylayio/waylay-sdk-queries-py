# coding: utf-8
"""Waylay Query: timeseries queries (v1 protocol) models.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""

from __future__ import annotations

from enum import Enum


class InterpolationMethodOneOf4(str, Enum):
    """Use the value that is closest in time.."""

    NEAREST = "nearest"

    def __str__(self) -> str:
        return str(self.value)