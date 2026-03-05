"""Waylay Query: timeseries queries (v1 protocol) models.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Do not edit the class manually.

"""

from __future__ import annotations

from pydantic import (
    ConfigDict,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.validation_error import ValidationError


class HTTPValidationError(WaylayBaseModel):
    """HTTPValidationError."""

    detail: list[ValidationError] | None = None

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
