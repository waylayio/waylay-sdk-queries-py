"""Waylay Query: timeseries queries (v1 protocol) api tests.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Do not edit the class manually.
"""

import json
import re
from importlib.util import find_spec
from urllib.parse import quote

import pytest
from pytest_httpx import HTTPXMock
from typeguard import check_type
from waylay.sdk import ApiClient, WaylayClient
from waylay.sdk.api._models import Model
from waylay.services.queries.api import ExecuteQueriesApi
from waylay.services.queries.service import QueriesService

from ..types.execute_by_name_queries_v1_data_query_name_get_aggregation_stub import (
    ExecuteByNameQueriesV1DataQueryNameGetAggregationStub,
)
from ..types.execute_by_name_queries_v1_data_query_name_get_freq_stub import (
    ExecuteByNameQueriesV1DataQueryNameGetFreqStub,
)
from ..types.execute_by_name_queries_v1_data_query_name_get_from_stub import (
    ExecuteByNameQueriesV1DataQueryNameGetFromStub,
)
from ..types.execute_by_name_queries_v1_data_query_name_get_interpolation_stub import (
    ExecuteByNameQueriesV1DataQueryNameGetInterpolationStub,
)
from ..types.execute_by_name_queries_v1_data_query_name_get_render_stub import (
    ExecuteByNameQueriesV1DataQueryNameGetRenderStub,
)
from ..types.execute_by_name_queries_v1_data_query_name_get_until_stub import (
    ExecuteByNameQueriesV1DataQueryNameGetUntilStub,
)
from ..types.execute_by_name_queries_v1_data_query_name_get_window_stub import (
    ExecuteByNameQueriesV1DataQueryNameGetWindowStub,
)
from ..types.execute_query_queries_v1_data_post_aggregation_stub import (
    ExecuteQueryQueriesV1DataPostAggregationStub,
)
from ..types.execute_query_queries_v1_data_post_freq_stub import (
    ExecuteQueryQueriesV1DataPostFreqStub,
)
from ..types.execute_query_queries_v1_data_post_from_stub import (
    ExecuteQueryQueriesV1DataPostFromStub,
)
from ..types.execute_query_queries_v1_data_post_interpolation_stub import (
    ExecuteQueryQueriesV1DataPostInterpolationStub,
)
from ..types.execute_query_queries_v1_data_post_render_stub import (
    ExecuteQueryQueriesV1DataPostRenderStub,
)
from ..types.execute_query_queries_v1_data_post_until_stub import (
    ExecuteQueryQueriesV1DataPostUntilStub,
)
from ..types.execute_query_queries_v1_data_post_window_stub import (
    ExecuteQueryQueriesV1DataPostWindowStub,
)
from ..types.query_input_stub import QueryInputStub
from ..types.query_result_stub import QueryResultStub

MODELS_AVAILABLE = (
    find_spec("waylay.services.queries.models") is not None
)

if MODELS_AVAILABLE:
    from waylay.services.queries.models import QueryResult
    from waylay.services.queries.queries.execute_queries_api import (
        ExecuteByNameQuery,
        ExecuteQuery,
    )


# some mappings that are needed for some <example> interpolations
null, true, false = None, True, False


@pytest.fixture
def execute_queries_api(waylay_api_client: ApiClient) -> ExecuteQueriesApi:
    return ExecuteQueriesApi(waylay_api_client)


def test_registered(waylay_client: WaylayClient):
    """Test that ExecuteQueriesApi api is registered in the sdk client."""
    assert isinstance(waylay_client.queries.execute_queries, ExecuteQueriesApi)


def _execute_by_name_set_mock_response(
    httpx_mock: HTTPXMock, gateway_url: str, query_name: str
):
    mock_response = QueryResultStub.create_json()
    httpx_mock_kwargs = {
        "method": "GET",
        "url": re.compile(f"^{gateway_url}/queries/v1/data/{query_name}(\\?.*)?"),
        "content": json.dumps(mock_response, default=str),
        "status_code": 200,
    }
    httpx_mock.add_response(**httpx_mock_kwargs)


@pytest.mark.asyncio
@pytest.mark.skipif(not MODELS_AVAILABLE, reason="Types not installed.")
async def test_execute_by_name(
    service: QueriesService, gateway_url: str, httpx_mock: HTTPXMock
):
    """Test case for execute_by_name
    Execute Named Query
    """
    # set path params
    query_name = "query_name_example"

    kwargs = {
        # optionally use ExecuteByNameQuery to validate and reuse parameters
        "query": ExecuteByNameQuery(
            resource="13efb488-75ac-4dac-828a-d49c5c2ebbfc",
            metric="temperature",
            aggregation=ExecuteByNameQueriesV1DataQueryNameGetAggregationStub.create_json(),
            interpolation=ExecuteByNameQueriesV1DataQueryNameGetInterpolationStub.create_json(),
            freq=ExecuteByNameQueriesV1DataQueryNameGetFreqStub.create_json(),
            var_from=ExecuteByNameQueriesV1DataQueryNameGetFromStub.create_json(),
            until=ExecuteByNameQueriesV1DataQueryNameGetUntilStub.create_json(),
            window=ExecuteByNameQueriesV1DataQueryNameGetWindowStub.create_json(),
            periods=56,
            render=ExecuteByNameQueriesV1DataQueryNameGetRenderStub.create_json(),
        ),
    }
    _execute_by_name_set_mock_response(httpx_mock, gateway_url, quote(str(query_name)))
    resp = await service.execute_queries.execute_by_name(query_name, **kwargs)
    check_type(resp, QueryResult)


@pytest.mark.asyncio
@pytest.mark.skipif(MODELS_AVAILABLE, reason="Types installed.")
async def test_execute_by_name_without_types(
    service: QueriesService, gateway_url: str, httpx_mock: HTTPXMock
):
    """Test case for execute_by_name with models not installed
    Execute Named Query
    """
    # set path params
    query_name = "query_name_example"

    kwargs = {
        "query": {
            "resource": "13efb488-75ac-4dac-828a-d49c5c2ebbfc",
            "metric": "temperature",
            "aggregation": ExecuteByNameQueriesV1DataQueryNameGetAggregationStub.create_json(),
            "interpolation": ExecuteByNameQueriesV1DataQueryNameGetInterpolationStub.create_json(),
            "freq": ExecuteByNameQueriesV1DataQueryNameGetFreqStub.create_json(),
            "from": ExecuteByNameQueriesV1DataQueryNameGetFromStub.create_json(),
            "until": ExecuteByNameQueriesV1DataQueryNameGetUntilStub.create_json(),
            "window": ExecuteByNameQueriesV1DataQueryNameGetWindowStub.create_json(),
            "periods": 56,
            "render": ExecuteByNameQueriesV1DataQueryNameGetRenderStub.create_json(),
        },
    }
    _execute_by_name_set_mock_response(httpx_mock, gateway_url, quote(str(query_name)))
    resp = await service.execute_queries.execute_by_name(query_name, **kwargs)
    check_type(resp, Model)


def _execute_set_mock_response(httpx_mock: HTTPXMock, gateway_url: str):
    mock_response = QueryResultStub.create_json()
    httpx_mock_kwargs = {
        "method": "POST",
        "url": re.compile(f"^{gateway_url}/queries/v1/data(\\?.*)?"),
        "content": json.dumps(mock_response, default=str),
        "status_code": 200,
    }
    httpx_mock.add_response(**httpx_mock_kwargs)


@pytest.mark.asyncio
@pytest.mark.skipif(not MODELS_AVAILABLE, reason="Types not installed.")
async def test_execute(
    service: QueriesService, gateway_url: str, httpx_mock: HTTPXMock
):
    """Test case for execute
    Execute Query
    """
    # set path params
    kwargs = {
        # optionally use ExecuteQuery to validate and reuse parameters
        "query": ExecuteQuery(
            resource="13efb488-75ac-4dac-828a-d49c5c2ebbfc",
            metric="temperature",
            aggregation=ExecuteQueryQueriesV1DataPostAggregationStub.create_json(),
            interpolation=ExecuteQueryQueriesV1DataPostInterpolationStub.create_json(),
            freq=ExecuteQueryQueriesV1DataPostFreqStub.create_json(),
            var_from=ExecuteQueryQueriesV1DataPostFromStub.create_json(),
            until=ExecuteQueryQueriesV1DataPostUntilStub.create_json(),
            window=ExecuteQueryQueriesV1DataPostWindowStub.create_json(),
            periods=56,
            render=ExecuteQueryQueriesV1DataPostRenderStub.create_json(),
        ),
        "json": QueryInputStub.create_instance(),
    }
    _execute_set_mock_response(httpx_mock, gateway_url)
    resp = await service.execute_queries.execute(**kwargs)
    check_type(resp, QueryResult)


@pytest.mark.asyncio
@pytest.mark.skipif(MODELS_AVAILABLE, reason="Types installed.")
async def test_execute_without_types(
    service: QueriesService, gateway_url: str, httpx_mock: HTTPXMock
):
    """Test case for execute with models not installed
    Execute Query
    """
    # set path params
    kwargs = {
        "query": {
            "resource": "13efb488-75ac-4dac-828a-d49c5c2ebbfc",
            "metric": "temperature",
            "aggregation": ExecuteQueryQueriesV1DataPostAggregationStub.create_json(),
            "interpolation": ExecuteQueryQueriesV1DataPostInterpolationStub.create_json(),
            "freq": ExecuteQueryQueriesV1DataPostFreqStub.create_json(),
            "from": ExecuteQueryQueriesV1DataPostFromStub.create_json(),
            "until": ExecuteQueryQueriesV1DataPostUntilStub.create_json(),
            "window": ExecuteQueryQueriesV1DataPostWindowStub.create_json(),
            "periods": 56,
            "render": ExecuteQueryQueriesV1DataPostRenderStub.create_json(),
        },
        "json": QueryInputStub.create_json(),
    }
    _execute_set_mock_response(httpx_mock, gateway_url)
    resp = await service.execute_queries.execute(**kwargs)
    check_type(resp, Model)
