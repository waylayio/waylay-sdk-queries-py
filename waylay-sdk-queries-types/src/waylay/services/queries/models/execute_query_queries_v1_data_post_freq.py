"""Waylay Query: timeseries queries (v1 protocol) models.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import Annotated, TypeAlias

from ..models.execute_query_queries_v1_data_post_freq_inferred import (
    ExecuteQueryQueriesV1DataPostFreqInferred,
)

ExecuteQueryQueriesV1DataPostFreq: TypeAlias = Annotated[str, "A period in [ISO8601 duration](https://en.wikipedia.org/wiki/ISO_8601#Durations) format."] | ExecuteQueryQueriesV1DataPostFreqInferred
"""Override for the `freq` query attribute.."""
