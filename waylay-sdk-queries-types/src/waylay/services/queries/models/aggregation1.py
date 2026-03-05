"""Waylay Query: timeseries queries (v1 protocol) models.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import TypeAlias

from ..models.query_output_count import QueryOutputCount
from ..models.query_output_count_non_numeric import QueryOutputCountNonNumeric
from ..models.query_output_count_numeric import QueryOutputCountNumeric
from ..models.query_output_first import QueryOutputFirst
from ..models.query_output_last import QueryOutputLast
from ..models.query_output_max import QueryOutputMax
from ..models.query_output_mean import QueryOutputMean
from ..models.query_output_median import QueryOutputMedian
from ..models.query_output_min import QueryOutputMin
from ..models.query_output_std import QueryOutputStd
from ..models.query_output_sum import QueryOutputSum

Aggregation1: TypeAlias = QueryOutputFirst | QueryOutputLast | QueryOutputMean | QueryOutputMedian | QueryOutputSum | QueryOutputCount | QueryOutputCountNumeric | QueryOutputCountNonNumeric | QueryOutputStd | QueryOutputMax | QueryOutputMin
"""Aggregation method for a series in the query.."""
