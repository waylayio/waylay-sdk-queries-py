"""Waylay Query: timeseries queries (v1 protocol) models.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import TypeAlias

from ..models.execute_by_name_aggregation_count import ExecuteByNameAggregationCount
from ..models.execute_by_name_aggregation_count_non_numeric import (
    ExecuteByNameAggregationCountNonNumeric,
)
from ..models.execute_by_name_aggregation_count_numeric import (
    ExecuteByNameAggregationCountNumeric,
)
from ..models.execute_by_name_aggregation_first import ExecuteByNameAggregationFirst
from ..models.execute_by_name_aggregation_last import ExecuteByNameAggregationLast
from ..models.execute_by_name_aggregation_max import ExecuteByNameAggregationMax
from ..models.execute_by_name_aggregation_mean import ExecuteByNameAggregationMean
from ..models.execute_by_name_aggregation_median import ExecuteByNameAggregationMedian
from ..models.execute_by_name_aggregation_min import ExecuteByNameAggregationMin
from ..models.execute_by_name_aggregation_std import ExecuteByNameAggregationStd
from ..models.execute_by_name_aggregation_sum import ExecuteByNameAggregationSum

ExecuteByNameAggregation: TypeAlias = ExecuteByNameAggregationFirst | ExecuteByNameAggregationLast | ExecuteByNameAggregationMean | ExecuteByNameAggregationMedian | ExecuteByNameAggregationSum | ExecuteByNameAggregationCount | ExecuteByNameAggregationCountNumeric | ExecuteByNameAggregationCountNonNumeric | ExecuteByNameAggregationStd | ExecuteByNameAggregationMax | ExecuteByNameAggregationMin
"""ExecuteByNameAggregation."""
