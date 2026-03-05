"""Waylay Query: timeseries queries (v1 protocol) models.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Do not edit the class manually.

"""

from __future__ import annotations

from enum import Enum


class ExecuteByNameQueriesV1DataQueryNameGetRenderUPLOAD(str, Enum):
    """Render in an object format compatible with the `/data/v1/events` upload.  ###### options - `iso_timestamp`: `False` - `hierarchical`: `False` - `show_levels`: `False` - `roll_up`: `True`."""

    UPLOAD = "UPLOAD"

    def __str__(self) -> str:
        return str(self.value)
