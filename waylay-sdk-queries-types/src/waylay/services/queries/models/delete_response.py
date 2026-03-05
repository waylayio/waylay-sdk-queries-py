"""Waylay Query: timeseries queries (v1 protocol) models.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Do not edit the class manually.

"""

from __future__ import annotations

from pydantic import (
    ConfigDict,
    Field,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.embeddings_value import EmbeddingsValue
from ..models.links_value import LinksValue
from ..models.message import Message


class DeleteResponse(WaylayBaseModel):
    """Confirmation of a delete request.."""

    messages: list[Message] | None = None
    links: dict[str, LinksValue] | None = Field(
        default=None, description="HAL links, indexed by link relation.", alias="_links"
    )
    embeddings: dict[str, EmbeddingsValue] | None = Field(
        default=None,
        description="Hal embeddings, indexed by relation.",
        alias="_embeddings",
    )

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
