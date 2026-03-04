"""Waylay Query: timeseries queries (v1 protocol) models.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import TypeAlias

from ..models.query_input_akima import QueryInputAkima
from ..models.query_input_backfill import QueryInputBackfill
from ..models.query_input_cubic import QueryInputCubic
from ..models.query_input_fixed import QueryInputFixed
from ..models.query_input_from_derivatives import QueryInputFromDerivatives
from ..models.query_input_linear import QueryInputLinear
from ..models.query_input_nearest import QueryInputNearest
from ..models.query_input_pad import QueryInputPad
from ..models.query_input_pchip import QueryInputPchip
from ..models.query_input_polynomial import QueryInputPolynomial
from ..models.query_input_quadratic import QueryInputQuadratic
from ..models.query_input_slinear import QueryInputSlinear
from ..models.query_input_spline import QueryInputSpline
from ..models.query_input_zero import QueryInputZero

DefaultInterpolationAnyOf: TypeAlias = QueryInputPad | QueryInputFixed | QueryInputBackfill | QueryInputLinear | QueryInputNearest | QueryInputZero | QueryInputSlinear | QueryInputQuadratic | QueryInputCubic | QueryInputPolynomial | QueryInputSpline | QueryInputFromDerivatives | QueryInputPchip | QueryInputAkima
"""DefaultInterpolationAnyOf."""
