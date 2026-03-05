"""Waylay Query: timeseries queries (v1 protocol) models.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import Annotated, TypeAlias

from ..models.alignment_inferred import AlignmentInferred

AlignmentGridInterval: TypeAlias = Annotated[str, "A period in [ISO8601 duration](https://en.wikipedia.org/wiki/ISO_8601#Durations) format."] | AlignmentInferred
""" Defines the grid used to align the aggregation window. The window will align at whole-unit multiples of this interval.  For intervals like `PT1D`, that are timezone-dependent, use the  `align.timezone` to fix the absolute timestamp of the grid boundaries.  If not specified, defaults to the `freq` aggregation interval. ."""
