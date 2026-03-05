"""Waylay Query: timeseries queries (v1 protocol) models.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import TypeAlias

from ..models.query_output_akima import QueryOutputAkima
from ..models.query_output_backfill import QueryOutputBackfill
from ..models.query_output_cubic import QueryOutputCubic
from ..models.query_output_fixed import QueryOutputFixed
from ..models.query_output_from_derivatives import QueryOutputFromDerivatives
from ..models.query_output_linear import QueryOutputLinear
from ..models.query_output_nearest import QueryOutputNearest
from ..models.query_output_pad import QueryOutputPad
from ..models.query_output_pchip import QueryOutputPchip
from ..models.query_output_polynomial import QueryOutputPolynomial
from ..models.query_output_quadratic import QueryOutputQuadratic
from ..models.query_output_slinear import QueryOutputSlinear
from ..models.query_output_spline import QueryOutputSpline
from ..models.query_output_zero import QueryOutputZero

DefaultInterpolation1AnyOf: TypeAlias = QueryOutputPad | QueryOutputFixed | QueryOutputBackfill | QueryOutputLinear | QueryOutputNearest | QueryOutputZero | QueryOutputSlinear | QueryOutputQuadratic | QueryOutputCubic | QueryOutputPolynomial | QueryOutputSpline | QueryOutputFromDerivatives | QueryOutputPchip | QueryOutputAkima
"""DefaultInterpolation1AnyOf."""
