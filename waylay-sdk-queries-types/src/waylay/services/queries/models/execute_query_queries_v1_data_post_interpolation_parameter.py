"""Waylay Query: timeseries queries (v1 protocol) models.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import TypeAlias

from ..models.execute_query_queries_v1_data_post_interpolation_akima import (
    ExecuteQueryQueriesV1DataPostInterpolationAkima,
)
from ..models.execute_query_queries_v1_data_post_interpolation_backfill import (
    ExecuteQueryQueriesV1DataPostInterpolationBackfill,
)
from ..models.execute_query_queries_v1_data_post_interpolation_cubic import (
    ExecuteQueryQueriesV1DataPostInterpolationCubic,
)
from ..models.execute_query_queries_v1_data_post_interpolation_fixed import (
    ExecuteQueryQueriesV1DataPostInterpolationFixed,
)
from ..models.execute_query_queries_v1_data_post_interpolation_from_derivatives import (
    ExecuteQueryQueriesV1DataPostInterpolationFromDerivatives,
)
from ..models.execute_query_queries_v1_data_post_interpolation_linear import (
    ExecuteQueryQueriesV1DataPostInterpolationLinear,
)
from ..models.execute_query_queries_v1_data_post_interpolation_nearest import (
    ExecuteQueryQueriesV1DataPostInterpolationNearest,
)
from ..models.execute_query_queries_v1_data_post_interpolation_pad import (
    ExecuteQueryQueriesV1DataPostInterpolationPad,
)
from ..models.execute_query_queries_v1_data_post_interpolation_pchip import (
    ExecuteQueryQueriesV1DataPostInterpolationPchip,
)
from ..models.execute_query_queries_v1_data_post_interpolation_polynomial import (
    ExecuteQueryQueriesV1DataPostInterpolationPolynomial,
)
from ..models.execute_query_queries_v1_data_post_interpolation_quadratic import (
    ExecuteQueryQueriesV1DataPostInterpolationQuadratic,
)
from ..models.execute_query_queries_v1_data_post_interpolation_slinear import (
    ExecuteQueryQueriesV1DataPostInterpolationSlinear,
)
from ..models.execute_query_queries_v1_data_post_interpolation_spline import (
    ExecuteQueryQueriesV1DataPostInterpolationSpline,
)
from ..models.execute_query_queries_v1_data_post_interpolation_zero import (
    ExecuteQueryQueriesV1DataPostInterpolationZero,
)

ExecuteQueryQueriesV1DataPostInterpolationParameter: TypeAlias = ExecuteQueryQueriesV1DataPostInterpolationPad | ExecuteQueryQueriesV1DataPostInterpolationFixed | ExecuteQueryQueriesV1DataPostInterpolationBackfill | ExecuteQueryQueriesV1DataPostInterpolationLinear | ExecuteQueryQueriesV1DataPostInterpolationNearest | ExecuteQueryQueriesV1DataPostInterpolationZero | ExecuteQueryQueriesV1DataPostInterpolationSlinear | ExecuteQueryQueriesV1DataPostInterpolationQuadratic | ExecuteQueryQueriesV1DataPostInterpolationCubic | ExecuteQueryQueriesV1DataPostInterpolationPolynomial | ExecuteQueryQueriesV1DataPostInterpolationSpline | ExecuteQueryQueriesV1DataPostInterpolationFromDerivatives | ExecuteQueryQueriesV1DataPostInterpolationPchip | ExecuteQueryQueriesV1DataPostInterpolationAkima
"""ExecuteQueryQueriesV1DataPostInterpolationParameter."""
