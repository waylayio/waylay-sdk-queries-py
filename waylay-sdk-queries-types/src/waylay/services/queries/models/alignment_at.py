"""Waylay Query: timeseries queries (v1 protocol) models.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import TypeAlias

from ..models.alignment_boundary import AlignmentBoundary
from ..models.alignment_from import AlignmentFrom
from ..models.alignment_grid import AlignmentGrid
from ..models.alignment_until import AlignmentUntil

AlignmentAt: TypeAlias = AlignmentGrid | AlignmentBoundary | AlignmentFrom | AlignmentUntil
"""AlignmentAt."""
