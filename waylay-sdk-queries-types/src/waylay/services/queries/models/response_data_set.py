"""Waylay Query: timeseries queries (v1 protocol) models.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import TypeAlias

from ..models.column_data_set import ColumnDataSet
from ..models.object_data_set import ObjectDataSet
from ..models.row_data_set import RowDataSet
from ..models.series_data_set import SeriesDataSet

ResponseDataSet: TypeAlias = RowDataSet | SeriesDataSet | ColumnDataSet | ObjectDataSet
"""Result timeseries data set, with one time dimension.."""
