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
)

from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.data_set_attributes import DataSetAttributes
from ..models.data_set_window import DataSetWindow
from ..models.object_data import ObjectData


class ObjectDataSet(WaylayBaseModel):
    """Data result in object format.  Result item when render option `render.header_array` is not set.  The data values are keyed by their attributes (`resource`, `metric`, `aggregation`), according to the render options: * _hierachical_: for each level, a sub-object is created   (e.g. `render.mode=hier_dict`) * _flattened_: the attributes are '.'-separated concatenation   of the attributes (e.g `render.mode=flat_dict`) * _mixed_: (.e.g. `render.mode=metric_flat_dict`) a single level     (e.g. `metric`) is used as main key, any remaining levels     (`resource`,`aggregation`) are indicated with a flattened subkey.  When `render.rollup=true`, the attribute levels that are the same for all series are not used as key, but reported as a data or table attribute.."""

    attributes: DataSetAttributes | None = None
    window_spec: DataSetWindow | None = None
    data: List[ObjectData]

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
