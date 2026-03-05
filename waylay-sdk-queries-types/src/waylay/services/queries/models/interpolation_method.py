"""Waylay Query: timeseries queries (v1 protocol) models.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import TypeAlias

from ..models.interpolation_spec_akima import InterpolationSpecAkima
from ..models.interpolation_spec_backfill import InterpolationSpecBackfill
from ..models.interpolation_spec_cubic import InterpolationSpecCubic
from ..models.interpolation_spec_fixed import InterpolationSpecFixed
from ..models.interpolation_spec_from_derivatives import (
    InterpolationSpecFromDerivatives,
)
from ..models.interpolation_spec_linear import InterpolationSpecLinear
from ..models.interpolation_spec_nearest import InterpolationSpecNearest
from ..models.interpolation_spec_pad import InterpolationSpecPad
from ..models.interpolation_spec_pchip import InterpolationSpecPchip
from ..models.interpolation_spec_polynomial import InterpolationSpecPolynomial
from ..models.interpolation_spec_quadratic import InterpolationSpecQuadratic
from ..models.interpolation_spec_slinear import InterpolationSpecSlinear
from ..models.interpolation_spec_spline import InterpolationSpecSpline
from ..models.interpolation_spec_zero import InterpolationSpecZero

InterpolationMethod: TypeAlias = InterpolationSpecPad | InterpolationSpecFixed | InterpolationSpecBackfill | InterpolationSpecLinear | InterpolationSpecNearest | InterpolationSpecZero | InterpolationSpecSlinear | InterpolationSpecQuadratic | InterpolationSpecCubic | InterpolationSpecPolynomial | InterpolationSpecSpline | InterpolationSpecFromDerivatives | InterpolationSpecPchip | InterpolationSpecAkima
"""InterpolationMethod."""
