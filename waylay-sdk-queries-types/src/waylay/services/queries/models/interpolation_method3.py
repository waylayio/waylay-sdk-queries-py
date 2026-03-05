"""Waylay Query: timeseries queries (v1 protocol) models.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import TypeAlias

from ..models.series_spec_akima import SeriesSpecAkima
from ..models.series_spec_backfill import SeriesSpecBackfill
from ..models.series_spec_cubic import SeriesSpecCubic
from ..models.series_spec_fixed import SeriesSpecFixed
from ..models.series_spec_from_derivatives import SeriesSpecFromDerivatives
from ..models.series_spec_linear import SeriesSpecLinear
from ..models.series_spec_nearest import SeriesSpecNearest
from ..models.series_spec_pad import SeriesSpecPad
from ..models.series_spec_pchip import SeriesSpecPchip
from ..models.series_spec_polynomial import SeriesSpecPolynomial
from ..models.series_spec_quadratic import SeriesSpecQuadratic
from ..models.series_spec_slinear import SeriesSpecSlinear
from ..models.series_spec_spline import SeriesSpecSpline
from ..models.series_spec_zero import SeriesSpecZero

InterpolationMethod3: TypeAlias = SeriesSpecPad | SeriesSpecFixed | SeriesSpecBackfill | SeriesSpecLinear | SeriesSpecNearest | SeriesSpecZero | SeriesSpecSlinear | SeriesSpecQuadratic | SeriesSpecCubic | SeriesSpecPolynomial | SeriesSpecSpline | SeriesSpecFromDerivatives | SeriesSpecPchip | SeriesSpecAkima
"""InterpolationMethod3."""
