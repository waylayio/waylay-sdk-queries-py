# coding: utf-8
"""Waylay Query: timeseries queries (v1 protocol) models.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""

from __future__ import annotations

from datetime import datetime
from typing import List

from pydantic import (
    ConfigDict,
    Field,
    StrictInt,
    StrictStr,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel


class ObjectData(WaylayBaseModel):
    """Result data for a timestamp in object format.."""

    timestamp: StrictInt = Field(description="Unix epoch milliseconds timestamp.")
    timestamp_iso: datetime | None = Field(
        default=None,
        description="ISO8601 rendering of the timestamp, present when `render.iso_timestamp=true`",
    )
    role: StrictStr | None = Field(
        default=None,
        description="The role of series specification that was used to compile this data set.",
    )
    resource: StrictStr | None = Field(
        default=None, description="Series resource id, if applicable for all values."
    )
    metric: StrictStr | None = Field(
        default=None, description="Series metric, if applicable for all values."
    )
    aggregation: StrictStr | None = Field(
        default=None, description="Series aggregation, if applicable for all values."
    )
    levels: List[StrictStr] | None = Field(
        default=None,
        description="Attribute level names used to key the values for this observation.  Levels that are flattened have a dot-separated key.  If all observations have the same attribute for a level, that level might be omitted.",
    )

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )