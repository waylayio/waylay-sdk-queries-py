"""Waylay Query: timeseries queries (v1 protocol) models.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import TypeAlias

from ..models.query_input_count import QueryInputCount
from ..models.query_input_count_non_numeric import QueryInputCountNonNumeric
from ..models.query_input_count_numeric import QueryInputCountNumeric
from ..models.query_input_first import QueryInputFirst
from ..models.query_input_last import QueryInputLast
from ..models.query_input_max import QueryInputMax
from ..models.query_input_mean import QueryInputMean
from ..models.query_input_median import QueryInputMedian
from ..models.query_input_min import QueryInputMin
from ..models.query_input_std import QueryInputStd
from ..models.query_input_sum import QueryInputSum

Aggregation: TypeAlias = QueryInputFirst | QueryInputLast | QueryInputMean | QueryInputMedian | QueryInputSum | QueryInputCount | QueryInputCountNumeric | QueryInputCountNonNumeric | QueryInputStd | QueryInputMax | QueryInputMin
"""Aggregation method for a series in the query.."""
