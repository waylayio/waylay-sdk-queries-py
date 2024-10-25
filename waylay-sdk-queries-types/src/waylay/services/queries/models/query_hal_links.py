# coding: utf-8
"""Waylay Query: timeseries queries (v1 protocol) models.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""

from __future__ import annotations

from pydantic import (
    ConfigDict,
    Field,
)

from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.hal_link import HALLink


class QueryHALLinks(WaylayBaseModel):
    """HAL Links for a query entity.."""

    var_self: HALLink = Field(alias="self")
    execute: HALLink

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
