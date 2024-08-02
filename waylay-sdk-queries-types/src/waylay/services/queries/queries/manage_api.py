# coding: utf-8
"""Waylay Query: timeseries queries (v1 protocol) query parameters.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

from __future__ import annotations  # for Python 3.7–3.9

from pydantic import (
    ConfigDict,
    Field,
    StrictInt,
    StrictStr,
)
from typing_extensions import (
    Annotated,  # >=3.11
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel


def _create_query_alias_for(field_name: str) -> str:
    return field_name


class CreateQuery(WaylayBaseModel):
    """Model for `create` query parameters."""

    model_config = ConfigDict(
        protected_namespaces=(),
        extra="allow",
        alias_generator=_create_query_alias_for,
        populate_by_name=True,
    )


def _get_query_alias_for(field_name: str) -> str:
    return field_name


class GetQuery(WaylayBaseModel):
    """Model for `get` query parameters."""

    model_config = ConfigDict(
        protected_namespaces=(),
        extra="allow",
        alias_generator=_get_query_alias_for,
        populate_by_name=True,
    )


def _list_query_alias_for(field_name: str) -> str:
    if field_name == "q":
        return "q"
    if field_name == "limit":
        return "limit"
    if field_name == "offset":
        return "offset"
    return field_name


class ListQuery(WaylayBaseModel):
    """Model for `list` query parameters."""

    q: Annotated[
        StrictStr | None,
        Field(
            description="The QDSL filter condition for the stored queries. Note that this value needs to be escaped when passed as an url paramater."
        ),
    ] = None
    limit: Annotated[
        Annotated[int, Field(le=100, strict=True)] | None,
        Field(description="Maximal number of items return in one response."),
    ] = None
    offset: Annotated[
        StrictInt | None,
        Field(
            description="Numbers of items to skip before listing results in the response page."
        ),
    ] = None

    model_config = ConfigDict(
        protected_namespaces=(),
        extra="allow",
        alias_generator=_list_query_alias_for,
        populate_by_name=True,
    )


def _remove_query_alias_for(field_name: str) -> str:
    return field_name


class RemoveQuery(WaylayBaseModel):
    """Model for `remove` query parameters."""

    model_config = ConfigDict(
        protected_namespaces=(),
        extra="allow",
        alias_generator=_remove_query_alias_for,
        populate_by_name=True,
    )


def _update_query_alias_for(field_name: str) -> str:
    return field_name


class UpdateQuery(WaylayBaseModel):
    """Model for `update` query parameters."""

    model_config = ConfigDict(
        protected_namespaces=(),
        extra="allow",
        alias_generator=_update_query_alias_for,
        populate_by_name=True,
    )