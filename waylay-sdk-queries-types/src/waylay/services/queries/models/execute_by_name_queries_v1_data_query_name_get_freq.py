"""Waylay Query: timeseries queries (v1 protocol) models.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import Annotated, TypeAlias

from ..models.execute_by_name_queries_v1_data_query_name_get_freq_inferred import (
    ExecuteByNameQueriesV1DataQueryNameGetFreqInferred,
)

ExecuteByNameQueriesV1DataQueryNameGetFreq: TypeAlias = Annotated[str, "A period in [ISO8601 duration](https://en.wikipedia.org/wiki/ISO_8601#Durations) format."] | ExecuteByNameQueriesV1DataQueryNameGetFreqInferred
"""Override for the `freq` query attribute.."""
