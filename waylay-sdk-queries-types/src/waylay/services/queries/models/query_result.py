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

from ..models.query_execution_message import QueryExecutionMessage
from ..models.query_input import QueryInput
from ..models.response_data_set import ResponseDataSet


class QueryResult(WaylayBaseModel):
    """A json data response.  Uses the format as specified by the `render` options of the request (defaults to `COMPACT_WS`). '."""

    data: List[ResponseDataSet] = Field(
        description="A list of data sets, each with their own time axis. There will be one dataset for each `role` specified in the query (by default a single `input` role).  The data is represented according to the `render`  options in the query (default `COMPACT_WS`)."
    )
    query: QueryInput
    messages: List[QueryExecutionMessage]

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
