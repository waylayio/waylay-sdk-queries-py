# coding: utf-8
"""Waylay Query: timeseries queries (v1 protocol) models.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""

from __future__ import annotations

from typing import List

from pydantic import (
    ConfigDict,
    Field,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.column_headers_inner import ColumnHeadersInner
from ..models.data_set_attributes import DataSetAttributes
from ..models.data_set_window import DataSetWindow
from ..models.datum import Datum
from ..models.row_data_set_data_axis import RowDataSetDataAxis


class RowDataSet(WaylayBaseModel):
    """Row-oriented dataset.  Timeseries data layout with a column header and a data row per timestamp. Result for render options `data_axis=column` and `header_array=row`.\",."""

    attributes: DataSetAttributes | None = None
    window_spec: DataSetWindow | None = None
    data_axis: RowDataSetDataAxis | None = RowDataSetDataAxis.COLUMN
    columns: List[ColumnHeadersInner] = Field(
        description="Header Attributes for the column data.  The initial string-valued headers (normally a single `timestamp`) indicate that column to contain row index data (i.e. timestamps).  The remaining object-valued column headers identify and describe the actual series data."
    )
    data: List[List[Datum]]

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
