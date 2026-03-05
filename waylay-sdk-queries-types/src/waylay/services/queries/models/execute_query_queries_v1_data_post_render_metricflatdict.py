"""Waylay Query: timeseries queries (v1 protocol) models.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Do not edit the class manually.

"""

from __future__ import annotations

from enum import Enum


class ExecuteQueryQueriesV1DataPostRenderMETRICFLATDICT(str, Enum):
    """Render an object with metric keys for each observation. Shows an iso timestamp.  ###### options - `iso_timestamp`: `True` - `hierarchical`: `['metric']` - `show_levels`: `False` - `roll_up`: `True` - `key_skip_empty`: `True`."""

    METRIC_FLAT_DICT = "METRIC_FLAT_DICT"

    def __str__(self) -> str:
        return str(self.value)
