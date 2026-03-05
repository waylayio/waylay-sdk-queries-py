"""Waylay Query: timeseries queries (v1 protocol) models.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import Annotated, TypeAlias

from ..models.datum import Datum

Data: TypeAlias = Annotated[object, "Values for the series whose attributes corresponds with the key. Keyed by sub-levels."] | Datum
"""Data."""
