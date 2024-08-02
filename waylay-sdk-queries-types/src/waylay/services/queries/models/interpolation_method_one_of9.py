# coding: utf-8
"""Waylay Query: timeseries queries (v1 protocol) models.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""

from __future__ import annotations

from enum import Enum


class InterpolationMethodOneOf9(str, Enum):
    """Interpolate with a polynomial of the lowest possible degree passing trough the data points.."""

    POLYNOMIAL = "polynomial"

    def __str__(self) -> str:
        return str(self.value)