"""Waylay Query: timeseries queries (v1 protocol) models.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import Any

from pydantic import (
    ConfigDict,
    StrictStr,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.message_level import MessageLevel


class Message(WaylayBaseModel):
    """Individual (info/warning/error) message in a response.."""

    code: StrictStr | None = None
    message: StrictStr
    level: MessageLevel | None = MessageLevel.INFO
    args: dict[str, Any] | None = None

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
