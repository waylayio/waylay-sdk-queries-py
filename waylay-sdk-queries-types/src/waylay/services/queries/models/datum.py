"""Waylay Query: timeseries queries (v1 protocol) models.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import TypeAlias

Datum: TypeAlias = float | str | bool
"""A single metric value for a timeseries.  A null value indicates that no (aggregated/interpolated) value  exists for the corresponding timestamp.."""
