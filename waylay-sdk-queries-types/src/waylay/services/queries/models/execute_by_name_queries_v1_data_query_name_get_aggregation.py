"""Waylay Query: timeseries queries (v1 protocol) models.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import TypeAlias

from ..models.execute_by_name_queries_v1_data_query_name_get_aggregation_count import (
    ExecuteByNameQueriesV1DataQueryNameGetAggregationCount,
)
from ..models.execute_by_name_queries_v1_data_query_name_get_aggregation_first import (
    ExecuteByNameQueriesV1DataQueryNameGetAggregationFirst,
)
from ..models.execute_by_name_queries_v1_data_query_name_get_aggregation_last import (
    ExecuteByNameQueriesV1DataQueryNameGetAggregationLast,
)
from ..models.execute_by_name_queries_v1_data_query_name_get_aggregation_max import (
    ExecuteByNameQueriesV1DataQueryNameGetAggregationMax,
)
from ..models.execute_by_name_queries_v1_data_query_name_get_aggregation_mean import (
    ExecuteByNameQueriesV1DataQueryNameGetAggregationMean,
)
from ..models.execute_by_name_queries_v1_data_query_name_get_aggregation_median import (
    ExecuteByNameQueriesV1DataQueryNameGetAggregationMedian,
)
from ..models.execute_by_name_queries_v1_data_query_name_get_aggregation_min import (
    ExecuteByNameQueriesV1DataQueryNameGetAggregationMin,
)
from ..models.execute_by_name_queries_v1_data_query_name_get_aggregation_std import (
    ExecuteByNameQueriesV1DataQueryNameGetAggregationStd,
)
from ..models.execute_by_name_queries_v1_data_query_name_get_aggregation_sum import (
    ExecuteByNameQueriesV1DataQueryNameGetAggregationSum,
)

ExecuteByNameQueriesV1DataQueryNameGetAggregation: TypeAlias = ExecuteByNameQueriesV1DataQueryNameGetAggregationFirst | ExecuteByNameQueriesV1DataQueryNameGetAggregationLast | ExecuteByNameQueriesV1DataQueryNameGetAggregationMean | ExecuteByNameQueriesV1DataQueryNameGetAggregationMedian | ExecuteByNameQueriesV1DataQueryNameGetAggregationSum | ExecuteByNameQueriesV1DataQueryNameGetAggregationCount | ExecuteByNameQueriesV1DataQueryNameGetAggregationStd | ExecuteByNameQueriesV1DataQueryNameGetAggregationMax | ExecuteByNameQueriesV1DataQueryNameGetAggregationMin
"""ExecuteByNameQueriesV1DataQueryNameGetAggregation."""
