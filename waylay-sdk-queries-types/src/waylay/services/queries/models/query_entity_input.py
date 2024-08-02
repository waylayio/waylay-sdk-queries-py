# coding: utf-8
"""Waylay Query: timeseries queries (v1 protocol) models.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""

from __future__ import annotations

from typing import Any, Dict

from pydantic import (
    ConfigDict,
    Field,
    StrictStr,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.query_input import QueryInput


class QueryEntityInput(WaylayBaseModel):
    """Input data to create a query definition.."""

    name: StrictStr = Field(description="Name of the stored query definition.")
    meta: Dict[str, Any] | None = Field(
        default=None, description="User metadata for the query definition."
    )
    query: QueryInput

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
