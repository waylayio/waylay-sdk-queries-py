# coding: utf-8
"""Waylay Query: timeseries queries (v1 protocol) models.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""

from __future__ import annotations

from typing import Any, Dict, List

from pydantic import (
    ConfigDict,
    Field,
    StrictStr,
)

from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.message import Message
from ..models.query_hal_links import QueryHALLinks
from ..models.query_output import QueryOutput


class QueryResponse(WaylayBaseModel):
    """Represents a single named query.."""

    links: QueryHALLinks = Field(alias="_links")
    attrs: Dict[str, Any] = Field(
        description="System provided metadata for the query definition."
    )
    name: StrictStr = Field(description="Name of the stored query definition.")
    meta: Dict[str, Any] | None = Field(
        default=None, description="User metadata for the query definition."
    )
    query: QueryOutput
    messages: List[Message] | None = None

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
