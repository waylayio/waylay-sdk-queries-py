"""Waylay Query: timeseries queries (v1 protocol) models.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Do not edit the class manually.

"""

from __future__ import annotations

from enum import Enum


class RenderFLATDICT(str, Enum):
    """Render an object for each observation. Uses flattened keys.  ###### options - `iso_timestamp`: `True` - `hierarchical`: `False` - `show_levels`: `True` - `roll_up`: `False`."""

    FLAT_DICT = "FLAT_DICT"

    def __str__(self) -> str:
        return str(self.value)
