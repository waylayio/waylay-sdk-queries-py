# coding: utf-8
"""Waylay Query: timeseries queries (v1 protocol) models.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""

from __future__ import annotations

from pydantic import (
    ConfigDict,
    Field,
    StrictInt,
    StrictStr,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel


class DataSetWindow(WaylayBaseModel):
    """Data Window.  Statistics of the time axis of a data set. Present with render option `include_window_spec=true`.\",."""

    until: StrictInt = Field(
        description="Exclusive higher bound of the time axis in unix epoch milliseconds."
    )
    window: StrictStr = Field(description="Time axis length as ISO8601 period.")
    freq: StrictStr = Field(
        description="Time axis aggregation interval as an ISO8601 period ."
    )

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
