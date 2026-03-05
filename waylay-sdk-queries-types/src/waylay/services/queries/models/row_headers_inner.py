"""Waylay Query: timeseries queries (v1 protocol) models.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import Annotated, TypeAlias

from ..models.row_header import RowHeader

RowHeadersInner: TypeAlias = Annotated[str, "Label for a series attribute"] | RowHeader
"""RowHeadersInner."""
