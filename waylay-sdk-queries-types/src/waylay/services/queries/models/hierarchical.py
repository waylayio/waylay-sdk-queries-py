"""Waylay Query: timeseries queries (v1 protocol) models.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import TypeAlias

Hierarchical: TypeAlias = bool | list[str]
"""if true, use hierarchical objects to represent multiple row (or column) dimensions, otherwise multi-keys get concatenated with a dot-delimiter. If the value is a list, only these levels are kept as separate levels, while remaining levels get concatenated keys."""
