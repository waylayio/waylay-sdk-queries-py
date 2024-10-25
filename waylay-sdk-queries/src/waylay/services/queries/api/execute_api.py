# coding: utf-8
"""Waylay Query: timeseries queries (v1 protocol) api.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

from __future__ import annotations  # for Python 3.7–3.9

from typing import (
    TYPE_CHECKING,
    Any,
    Dict,
    Literal,
    TypeVar,
    overload,
)

from pydantic import (
    StrictBool,
    StrictStr,
    TypeAdapter,
)

from waylay.sdk.api import (
    HeaderTypes,
    QueryParamTypes,
    Response,
)
from waylay.sdk.api._models import Model
from waylay.sdk.plugin import WithApiClient

if TYPE_CHECKING:
    from waylay.services.queries.models import (
        HTTPValidationError,
        QueryInput,
        QueryResult,
    )
    from waylay.services.queries.queries.execute_api import (
        ExecuteByNameQuery,
        ExecuteQuery,
    )


try:
    from waylay.services.queries.models import (
        HTTPValidationError,
        QueryInput,
        QueryResult,
    )
    from waylay.services.queries.queries.execute_api import (
        ExecuteByNameQuery,
        ExecuteQuery,
    )

    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

    if not TYPE_CHECKING:
        ExecuteByNameQuery = dict
        QueryResult = Model

        HTTPValidationError = Model

        QueryInput = Model

        ExecuteQuery = dict
        QueryResult = Model

        HTTPValidationError = Model


T = TypeVar("T")


class ExecuteApi(WithApiClient):
    """ExecuteApi service methods.

    NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    @overload
    async def execute_by_name(
        self,
        query_name: StrictStr,
        *,
        query: ExecuteByNameQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: Literal[""] = "",
        response_type: Literal[None] = None,
        validate_request: StrictBool = True,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> QueryResult: ...

    @overload
    async def execute_by_name(
        self,
        query_name: StrictStr,
        *,
        query: ExecuteByNameQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: Literal[""] = "",
        response_type: T,
        validate_request: StrictBool = True,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> T: ...

    @overload
    async def execute_by_name(
        self,
        query_name: StrictStr,
        *,
        query: ExecuteByNameQuery | QueryParamTypes | None = None,
        raw_response: Literal[True],
        select_path: Literal["_not_used_"] = "_not_used_",
        response_type: Literal[None] = None,  # not used
        validate_request: StrictBool = True,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> Response: ...

    @overload
    async def execute_by_name(
        self,
        query_name: StrictStr,
        *,
        query: ExecuteByNameQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: str,
        response_type: Literal[None] = None,
        validate_request: StrictBool = True,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> Model: ...

    @overload
    async def execute_by_name(
        self,
        query_name: StrictStr,
        *,
        query: ExecuteByNameQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: str,
        response_type: T,
        validate_request: StrictBool = True,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> T: ...

    async def execute_by_name(
        self,
        query_name: StrictStr,
        *,
        query: ExecuteByNameQuery | QueryParamTypes | None = None,
        raw_response: StrictBool = False,
        select_path: str = "",
        response_type: T | None = None,
        validate_request: StrictBool = True,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> QueryResult | T | Response | Model:
        """Execute Named Query.

        Execute a named timeseries query.  Retrieves a stored query definition by name, applies overrides from the url parameters, and executes it.
        :param query_name: (required)
        :type query_name: str
        :param query: URL Query parameters.
        :type query: ExecuteByNameQuery | QueryParamTypes, optional
        :param query['resource'] (dict) <br> query.resource (Query) : Default Resource Override.
        :type query['resource']: str
        :param query['metric'] (dict) <br> query.metric (Query) : Default Metric Override.
        :type query['metric']: str
        :param query['aggregation'] (dict) <br> query.aggregation (Query) :
        :type query['aggregation']: AggregationMethod
        :param query['interpolation'] (dict) <br> query.interpolation (Query) :
        :type query['interpolation']: Interpolation
        :param query['freq'] (dict) <br> query.freq (Query) : Override for the `freq` query attribute.
        :type query['freq']: GroupingIntervalOverride
        :param query['from'] (dict) <br> query.var_from (Query) :
        :type query['from']: FromOverride
        :param query['until'] (dict) <br> query.until (Query) :
        :type query['until']: FromOverride
        :param query['window'] (dict) <br> query.window (Query) :
        :type query['window']: WindowOverride
        :param query['periods'] (dict) <br> query.periods (Query) :
        :type query['periods']: int
        :param query['render'] (dict) <br> query.render (Query) :
        :type query['render']: Render1
        :param raw_response: If true, return the http Response object instead of returning an api model object, or throwing an ApiError.
        :param select_path: Denotes the json path applied to the response object before returning it.
                Set it to the empty string `""` to receive the full response object.
        :param response_type: If specified, the response is parsed into an instance of the specified type.
        :param validate_request: If set to false, the request body and query parameters are NOT validated against the models in the service types package, even when available.
        :param headers: Header parameters for this request
        :type headers: dict, optional
        :param `**kwargs`: Additional parameters passed on to the http client.
            See below.
        :Keyword Arguments:
            * timeout: a single numeric timeout in seconds,
                or a tuple of _connect_, _read_, _write_ and _pool_ timeouts.
            * stream: if true, the response will be in streaming mode
            * cookies
            * extensions
            * auth
            * follow_redirects: bool

        :return: Returns the result object if the http request succeeded with status code '2XX'.
        :raises APIError: If the http request has a status code different from `2XX`. This
            object wraps both the http Response and any parsed data.
        """

        # path parameters
        path_params: Dict[str, str] = {
            "query_name": str(query_name),
        }

        ## named body parameters
        body_args: Dict[str, Any] = {}

        # query parameters
        if query is not None and MODELS_AVAILABLE and validate_request:
            query = TypeAdapter(ExecuteByNameQuery).validate_python(query)

        response_types_map: Dict[str, Any] = (
            {"2XX": response_type}
            if response_type is not None
            else {
                "200": QueryResult if not select_path else Model,
            }
        )
        non_200_response_types_map: Dict[str, Any] = {
            "422": HTTPValidationError,
        }
        response_types_map.update(non_200_response_types_map)

        ## peform request
        return await self.api_client.request(
            method="GET",
            resource_path="/queries/v1/data/{query_name}",
            path_params=path_params,
            params=query,
            **body_args,
            headers=headers,
            **kwargs,
            response_type=response_types_map,
            select_path=select_path,
            raw_response=raw_response,
        )

    @overload
    async def execute(
        self,
        *,
        json: QueryInput,
        query: ExecuteQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: Literal[""] = "",
        response_type: Literal[None] = None,
        validate_request: StrictBool = True,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> QueryResult: ...

    @overload
    async def execute(
        self,
        *,
        json: QueryInput,
        query: ExecuteQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: Literal[""] = "",
        response_type: T,
        validate_request: StrictBool = True,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> T: ...

    @overload
    async def execute(
        self,
        *,
        json: QueryInput,
        query: ExecuteQuery | QueryParamTypes | None = None,
        raw_response: Literal[True],
        select_path: Literal["_not_used_"] = "_not_used_",
        response_type: Literal[None] = None,  # not used
        validate_request: StrictBool = True,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> Response: ...

    @overload
    async def execute(
        self,
        *,
        json: QueryInput,
        query: ExecuteQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: str,
        response_type: Literal[None] = None,
        validate_request: StrictBool = True,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> Model: ...

    @overload
    async def execute(
        self,
        *,
        json: QueryInput,
        query: ExecuteQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: str,
        response_type: T,
        validate_request: StrictBool = True,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> T: ...

    async def execute(
        self,
        *,
        json: QueryInput,
        query: ExecuteQuery | QueryParamTypes | None = None,
        raw_response: StrictBool = False,
        select_path: str = "",
        response_type: T | None = None,
        validate_request: StrictBool = True,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> QueryResult | T | Response | Model:
        """Execute Query.

        Execute a timeseries query.  Executes the timeseries query specified in the request body, after applying any overrides from the url parameters.
        :param json: The json request body.
        :type json: QueryInput, optional
        :param query: URL Query parameters.
        :type query: ExecuteQuery | QueryParamTypes, optional
        :param query['resource'] (dict) <br> query.resource (Query) : Default Resource Override.
        :type query['resource']: str
        :param query['metric'] (dict) <br> query.metric (Query) : Default Metric Override.
        :type query['metric']: str
        :param query['aggregation'] (dict) <br> query.aggregation (Query) :
        :type query['aggregation']: AggregationMethod
        :param query['interpolation'] (dict) <br> query.interpolation (Query) :
        :type query['interpolation']: Interpolation
        :param query['freq'] (dict) <br> query.freq (Query) : Override for the `freq` query attribute.
        :type query['freq']: GroupingIntervalOverride
        :param query['from'] (dict) <br> query.var_from (Query) :
        :type query['from']: FromOverride
        :param query['until'] (dict) <br> query.until (Query) :
        :type query['until']: FromOverride
        :param query['window'] (dict) <br> query.window (Query) :
        :type query['window']: WindowOverride
        :param query['periods'] (dict) <br> query.periods (Query) :
        :type query['periods']: int
        :param query['render'] (dict) <br> query.render (Query) :
        :type query['render']: Render1
        :param raw_response: If true, return the http Response object instead of returning an api model object, or throwing an ApiError.
        :param select_path: Denotes the json path applied to the response object before returning it.
                Set it to the empty string `""` to receive the full response object.
        :param response_type: If specified, the response is parsed into an instance of the specified type.
        :param validate_request: If set to false, the request body and query parameters are NOT validated against the models in the service types package, even when available.
        :param headers: Header parameters for this request
        :type headers: dict, optional
        :param `**kwargs`: Additional parameters passed on to the http client.
            See below.
        :Keyword Arguments:
            * timeout: a single numeric timeout in seconds,
                or a tuple of _connect_, _read_, _write_ and _pool_ timeouts.
            * stream: if true, the response will be in streaming mode
            * cookies
            * extensions
            * auth
            * follow_redirects: bool

        :return: Returns the result object if the http request succeeded with status code '2XX'.
        :raises APIError: If the http request has a status code different from `2XX`. This
            object wraps both the http Response and any parsed data.
        """

        # path parameters
        path_params: Dict[str, str] = {}

        ## named body parameters
        body_args: Dict[str, Any] = {}
        if json is not None and validate_request:
            body_adapter: Any = TypeAdapter(QueryInput)
            json = body_adapter.validate_python(json)  # type: ignore # https://github.com/pydantic/pydantic/discussions/7094
        body_args["json"] = json

        # query parameters
        if query is not None and MODELS_AVAILABLE and validate_request:
            query = TypeAdapter(ExecuteQuery).validate_python(query)

        response_types_map: Dict[str, Any] = (
            {"2XX": response_type}
            if response_type is not None
            else {
                "200": QueryResult if not select_path else Model,
            }
        )
        non_200_response_types_map: Dict[str, Any] = {
            "422": HTTPValidationError,
        }
        response_types_map.update(non_200_response_types_map)

        ## peform request
        return await self.api_client.request(
            method="POST",
            resource_path="/queries/v1/data",
            path_params=path_params,
            params=query,
            **body_args,
            headers=headers,
            **kwargs,
            response_type=response_types_map,
            select_path=select_path,
            raw_response=raw_response,
        )
