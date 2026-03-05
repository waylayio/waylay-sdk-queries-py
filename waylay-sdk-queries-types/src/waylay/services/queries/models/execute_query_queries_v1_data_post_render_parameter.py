"""Waylay Query: timeseries queries (v1 protocol) models.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import TypeAlias

from ..models.execute_query_queries_v1_data_post_render_compact import (
    ExecuteQueryQueriesV1DataPostRenderCOMPACT,
)
from ..models.execute_query_queries_v1_data_post_render_compactws import (
    ExecuteQueryQueriesV1DataPostRenderCOMPACTWS,
)
from ..models.execute_query_queries_v1_data_post_render_csv import (
    ExecuteQueryQueriesV1DataPostRenderCSV,
)
from ..models.execute_query_queries_v1_data_post_render_flatdict import (
    ExecuteQueryQueriesV1DataPostRenderFLATDICT,
)
from ..models.execute_query_queries_v1_data_post_render_headercolumn import (
    ExecuteQueryQueriesV1DataPostRenderHEADERCOLUMN,
)
from ..models.execute_query_queries_v1_data_post_render_headerrow import (
    ExecuteQueryQueriesV1DataPostRenderHEADERROW,
)
from ..models.execute_query_queries_v1_data_post_render_hierdict import (
    ExecuteQueryQueriesV1DataPostRenderHIERDICT,
)
from ..models.execute_query_queries_v1_data_post_render_metricflatdict import (
    ExecuteQueryQueriesV1DataPostRenderMETRICFLATDICT,
)
from ..models.execute_query_queries_v1_data_post_render_series import (
    ExecuteQueryQueriesV1DataPostRenderSERIES,
)
from ..models.execute_query_queries_v1_data_post_render_upload import (
    ExecuteQueryQueriesV1DataPostRenderUPLOAD,
)

ExecuteQueryQueriesV1DataPostRenderParameter: TypeAlias = ExecuteQueryQueriesV1DataPostRenderHEADERROW | ExecuteQueryQueriesV1DataPostRenderCOMPACT | ExecuteQueryQueriesV1DataPostRenderCOMPACTWS | ExecuteQueryQueriesV1DataPostRenderSERIES | ExecuteQueryQueriesV1DataPostRenderHEADERCOLUMN | ExecuteQueryQueriesV1DataPostRenderFLATDICT | ExecuteQueryQueriesV1DataPostRenderHIERDICT | ExecuteQueryQueriesV1DataPostRenderMETRICFLATDICT | ExecuteQueryQueriesV1DataPostRenderUPLOAD | ExecuteQueryQueriesV1DataPostRenderCSV
"""ExecuteQueryQueriesV1DataPostRenderParameter."""
