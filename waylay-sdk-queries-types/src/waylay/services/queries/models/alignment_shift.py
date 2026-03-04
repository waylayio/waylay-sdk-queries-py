"""Waylay Query: timeseries queries (v1 protocol) models.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import TypeAlias

from ..models.alignment_backward import AlignmentBackward
from ..models.alignment_forward import AlignmentForward
from ..models.alignment_wrap import AlignmentWrap

AlignmentShift: TypeAlias = AlignmentBackward | AlignmentForward | AlignmentWrap
"""AlignmentShift."""
