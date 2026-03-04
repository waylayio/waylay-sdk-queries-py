"""Waylay Query: timeseries queries (v1 protocol) models.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import Annotated, TypeAlias

EmbeddingsValue: TypeAlias = Annotated[dict[str, object], "Any embedded representation in a HAL response."] | list[dict[str, object]]
"""EmbeddingsValue."""
