"""Waylay Query: timeseries queries (v1 protocol) models.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import TypeAlias

from ..models.execute_query_queries_v1_data_post_aggregation_count import (
    ExecuteQueryQueriesV1DataPostAggregationCount,
)
from ..models.execute_query_queries_v1_data_post_aggregation_first import (
    ExecuteQueryQueriesV1DataPostAggregationFirst,
)
from ..models.execute_query_queries_v1_data_post_aggregation_last import (
    ExecuteQueryQueriesV1DataPostAggregationLast,
)
from ..models.execute_query_queries_v1_data_post_aggregation_max import (
    ExecuteQueryQueriesV1DataPostAggregationMax,
)
from ..models.execute_query_queries_v1_data_post_aggregation_mean import (
    ExecuteQueryQueriesV1DataPostAggregationMean,
)
from ..models.execute_query_queries_v1_data_post_aggregation_median import (
    ExecuteQueryQueriesV1DataPostAggregationMedian,
)
from ..models.execute_query_queries_v1_data_post_aggregation_min import (
    ExecuteQueryQueriesV1DataPostAggregationMin,
)
from ..models.execute_query_queries_v1_data_post_aggregation_std import (
    ExecuteQueryQueriesV1DataPostAggregationStd,
)
from ..models.execute_query_queries_v1_data_post_aggregation_sum import (
    ExecuteQueryQueriesV1DataPostAggregationSum,
)

ExecuteQueryQueriesV1DataPostAggregation: TypeAlias = ExecuteQueryQueriesV1DataPostAggregationFirst | ExecuteQueryQueriesV1DataPostAggregationLast | ExecuteQueryQueriesV1DataPostAggregationMean | ExecuteQueryQueriesV1DataPostAggregationMedian | ExecuteQueryQueriesV1DataPostAggregationSum | ExecuteQueryQueriesV1DataPostAggregationCount | ExecuteQueryQueriesV1DataPostAggregationStd | ExecuteQueryQueriesV1DataPostAggregationMax | ExecuteQueryQueriesV1DataPostAggregationMin
"""ExecuteQueryQueriesV1DataPostAggregation."""
