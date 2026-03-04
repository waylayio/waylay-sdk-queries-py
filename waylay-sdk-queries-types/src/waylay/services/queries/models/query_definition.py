"""Waylay Query: timeseries queries (v1 protocol) models.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import TypeAlias

from ..models.query_input import QueryInput
from ..models.query_update_input import QueryUpdateInput

QueryDefinition: TypeAlias = QueryUpdateInput | QueryInput
"""QueryDefinition."""
