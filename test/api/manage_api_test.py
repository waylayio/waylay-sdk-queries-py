# coding: utf-8
"""Waylay Query: timeseries queries (v1 protocol) api tests.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

import json
import re
from importlib.util import find_spec
from typing import Union
from urllib.parse import quote

import pytest
from pytest_httpx import HTTPXMock
from typeguard import check_type
from waylay.sdk import ApiClient, WaylayClient
from waylay.sdk.api._models import Model
from waylay.services.queries.api import ManageApi
from waylay.services.queries.service import QueriesService

from ..types.delete_response_stub import DeleteResponseStub
from ..types.queries_list_response_stub import QueriesListResponseStub
from ..types.query_definition_stub import QueryDefinitionStub
from ..types.query_entity_input_stub import QueryEntityInputStub
from ..types.query_response_stub import QueryResponseStub

MODELS_AVAILABLE = (
    True if find_spec("waylay.services.queries.models") is not None else False
)

if MODELS_AVAILABLE:
    from waylay.services.queries.models import (
        DeleteResponse,
        QueriesListResponse,
        QueryResponse,
    )
    from waylay.services.queries.queries.manage_api import ListQuery


# some mappings that are needed for some <example> interpolations
null, true, false = None, True, False


@pytest.fixture
def manage_api(waylay_api_client: ApiClient) -> ManageApi:
    return ManageApi(waylay_api_client)


def test_registered(waylay_client: WaylayClient):
    """Test that ManageApi api is registered in the sdk client."""
    assert isinstance(waylay_client.queries.manage, ManageApi)


def _create_set_mock_response(httpx_mock: HTTPXMock, gateway_url: str):
    mock_response = QueryResponseStub.create_json()
    httpx_mock_kwargs = {
        "method": "POST",
        "url": re.compile(f"^{gateway_url}/queries/v1/queries/v1/query(\\?.*)?"),
        "content": json.dumps(mock_response, default=str),
        "status_code": 200,
    }
    httpx_mock.add_response(**httpx_mock_kwargs)


@pytest.mark.asyncio
@pytest.mark.skipif(not MODELS_AVAILABLE, reason="Types not installed.")
async def test_create(service: QueriesService, gateway_url: str, httpx_mock: HTTPXMock):
    """Test case for create
    Post Query
    """
    # set path params
    kwargs = {
        "json": QueryEntityInputStub.create_instance(),
    }
    _create_set_mock_response(httpx_mock, gateway_url)
    resp = await service.manage.create(**kwargs)
    check_type(resp, Union[QueryResponse,])


@pytest.mark.asyncio
@pytest.mark.skipif(MODELS_AVAILABLE, reason="Types installed.")
async def test_create_without_types(
    service: QueriesService, gateway_url: str, httpx_mock: HTTPXMock
):
    """Test case for create with models not installed
    Post Query
    """
    # set path params
    kwargs = {
        "json": QueryEntityInputStub.create_json(),
    }
    _create_set_mock_response(httpx_mock, gateway_url)
    resp = await service.manage.create(**kwargs)
    check_type(resp, Model)


def _get_set_mock_response(httpx_mock: HTTPXMock, gateway_url: str, query_name: str):
    mock_response = QueryResponseStub.create_json()
    httpx_mock_kwargs = {
        "method": "GET",
        "url": re.compile(
            f"^{gateway_url}/queries/v1/queries/v1/query/{query_name}(\\?.*)?"
        ),
        "content": json.dumps(mock_response, default=str),
        "status_code": 200,
    }
    httpx_mock.add_response(**httpx_mock_kwargs)


@pytest.mark.asyncio
@pytest.mark.skipif(not MODELS_AVAILABLE, reason="Types not installed.")
async def test_get(service: QueriesService, gateway_url: str, httpx_mock: HTTPXMock):
    """Test case for get
    Get Query
    """
    # set path params
    query_name = "query_name_example"

    kwargs = {}
    _get_set_mock_response(httpx_mock, gateway_url, quote(str(query_name)))
    resp = await service.manage.get(query_name, **kwargs)
    check_type(resp, Union[QueryResponse,])


@pytest.mark.asyncio
@pytest.mark.skipif(MODELS_AVAILABLE, reason="Types installed.")
async def test_get_without_types(
    service: QueriesService, gateway_url: str, httpx_mock: HTTPXMock
):
    """Test case for get with models not installed
    Get Query
    """
    # set path params
    query_name = "query_name_example"

    kwargs = {}
    _get_set_mock_response(httpx_mock, gateway_url, quote(str(query_name)))
    resp = await service.manage.get(query_name, **kwargs)
    check_type(resp, Model)


def _list_set_mock_response(httpx_mock: HTTPXMock, gateway_url: str):
    mock_response = QueriesListResponseStub.create_json()
    httpx_mock_kwargs = {
        "method": "GET",
        "url": re.compile(f"^{gateway_url}/queries/v1/queries/v1/query(\\?.*)?"),
        "content": json.dumps(mock_response, default=str),
        "status_code": 200,
    }
    httpx_mock.add_response(**httpx_mock_kwargs)


@pytest.mark.asyncio
@pytest.mark.skipif(not MODELS_AVAILABLE, reason="Types not installed.")
async def test_list(service: QueriesService, gateway_url: str, httpx_mock: HTTPXMock):
    """Test case for list
    List Queries
    """
    # set path params
    kwargs = {
        # optionally use ListQuery to validate and reuse parameters
        "query": ListQuery(
            q="",
            limit=10,
            offset=0,
        ),
    }
    _list_set_mock_response(httpx_mock, gateway_url)
    resp = await service.manage.list(**kwargs)
    check_type(resp, Union[QueriesListResponse,])


@pytest.mark.asyncio
@pytest.mark.skipif(MODELS_AVAILABLE, reason="Types installed.")
async def test_list_without_types(
    service: QueriesService, gateway_url: str, httpx_mock: HTTPXMock
):
    """Test case for list with models not installed
    List Queries
    """
    # set path params
    kwargs = {
        "query": {
            "q": "",
            "limit": 10,
            "offset": 0,
        },
    }
    _list_set_mock_response(httpx_mock, gateway_url)
    resp = await service.manage.list(**kwargs)
    check_type(resp, Model)


def _remove_set_mock_response(httpx_mock: HTTPXMock, gateway_url: str, query_name: str):
    mock_response = DeleteResponseStub.create_json()
    httpx_mock_kwargs = {
        "method": "DELETE",
        "url": re.compile(
            f"^{gateway_url}/queries/v1/queries/v1/query/{query_name}(\\?.*)?"
        ),
        "content": json.dumps(mock_response, default=str),
        "status_code": 200,
    }
    httpx_mock.add_response(**httpx_mock_kwargs)


@pytest.mark.asyncio
@pytest.mark.skipif(not MODELS_AVAILABLE, reason="Types not installed.")
async def test_remove(service: QueriesService, gateway_url: str, httpx_mock: HTTPXMock):
    """Test case for remove
    Remove Query
    """
    # set path params
    query_name = "query_name_example"

    kwargs = {}
    _remove_set_mock_response(httpx_mock, gateway_url, quote(str(query_name)))
    resp = await service.manage.remove(query_name, **kwargs)
    check_type(resp, Union[DeleteResponse,])


@pytest.mark.asyncio
@pytest.mark.skipif(MODELS_AVAILABLE, reason="Types installed.")
async def test_remove_without_types(
    service: QueriesService, gateway_url: str, httpx_mock: HTTPXMock
):
    """Test case for remove with models not installed
    Remove Query
    """
    # set path params
    query_name = "query_name_example"

    kwargs = {}
    _remove_set_mock_response(httpx_mock, gateway_url, quote(str(query_name)))
    resp = await service.manage.remove(query_name, **kwargs)
    check_type(resp, Model)


def _update_set_mock_response(httpx_mock: HTTPXMock, gateway_url: str, query_name: str):
    mock_response = QueryResponseStub.create_json()
    httpx_mock_kwargs = {
        "method": "PUT",
        "url": re.compile(
            f"^{gateway_url}/queries/v1/queries/v1/query/{query_name}(\\?.*)?"
        ),
        "content": json.dumps(mock_response, default=str),
        "status_code": 200,
    }
    httpx_mock.add_response(**httpx_mock_kwargs)


@pytest.mark.asyncio
@pytest.mark.skipif(not MODELS_AVAILABLE, reason="Types not installed.")
async def test_update(service: QueriesService, gateway_url: str, httpx_mock: HTTPXMock):
    """Test case for update
    Update Query
    """
    # set path params
    query_name = "query_name_example"

    kwargs = {
        "json": QueryDefinitionStub.create_instance(),
    }
    _update_set_mock_response(httpx_mock, gateway_url, quote(str(query_name)))
    resp = await service.manage.update(query_name, **kwargs)
    check_type(resp, Union[QueryResponse,])


@pytest.mark.asyncio
@pytest.mark.skipif(MODELS_AVAILABLE, reason="Types installed.")
async def test_update_without_types(
    service: QueriesService, gateway_url: str, httpx_mock: HTTPXMock
):
    """Test case for update with models not installed
    Update Query
    """
    # set path params
    query_name = "query_name_example"

    kwargs = {
        "json": QueryDefinitionStub.create_json(),
    }
    _update_set_mock_response(httpx_mock, gateway_url, quote(str(query_name)))
    resp = await service.manage.update(query_name, **kwargs)
    check_type(resp, Model)