"""Waylay Query: timeseries queries (v1 protocol) models.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Do not edit the class manually.

"""

from __future__ import annotations

from pydantic import (
    ConfigDict,
    StrictStr,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel


class CauseException(WaylayBaseModel):
    """Describes the exception that caused a message.."""

    type: StrictStr
    message: StrictStr
    stacktrace: list[StrictStr]

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
