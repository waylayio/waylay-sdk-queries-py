"""Waylay Query: timeseries queries (v1 protocol) models.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import TypeAlias

from ..models.series_spec_count import SeriesSpecCount
from ..models.series_spec_first import SeriesSpecFirst
from ..models.series_spec_last import SeriesSpecLast
from ..models.series_spec_max import SeriesSpecMax
from ..models.series_spec_mean import SeriesSpecMean
from ..models.series_spec_median import SeriesSpecMedian
from ..models.series_spec_min import SeriesSpecMin
from ..models.series_spec_std import SeriesSpecStd
from ..models.series_spec_sum import SeriesSpecSum

Aggregration: TypeAlias = SeriesSpecFirst | SeriesSpecLast | SeriesSpecMean | SeriesSpecMedian | SeriesSpecSum | SeriesSpecCount | SeriesSpecStd | SeriesSpecMax | SeriesSpecMin
"""Aggregation method for the series (if aggregated). If missing, the query default is used.."""
