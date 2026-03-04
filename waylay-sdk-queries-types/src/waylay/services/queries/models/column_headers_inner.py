"""Waylay Query: timeseries queries (v1 protocol) models.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import Annotated, TypeAlias

from ..models.column_header import ColumnHeader

ColumnHeadersInner: TypeAlias = Annotated[str, "Header for a column containing a (representation of) the row index value. These headers precede the header attributes for row data."] | ColumnHeader
"""ColumnHeadersInner."""
