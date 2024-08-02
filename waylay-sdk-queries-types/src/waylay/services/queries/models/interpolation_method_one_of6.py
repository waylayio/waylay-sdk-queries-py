# coding: utf-8
"""Waylay Query: timeseries queries (v1 protocol) models.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""

from __future__ import annotations

from enum import Enum


class InterpolationMethodOneOf6(str, Enum):
    """Interpolate with a spline function of order 1, which is a piecewise polynomial.."""

    SLINEAR = "slinear"

    def __str__(self) -> str:
        return str(self.value)
