# waylay.services.queries.ExecuteQueriesApi

All URIs are relative to *https://api.waylay.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**execute_by_name**](ExecuteQueriesApi.md#execute_by_name) | **GET** /queries/v1/data/{query_name} | Execute Named Query
[**execute**](ExecuteQueriesApi.md#execute) | **POST** /queries/v1/data | Execute Query

# **execute_by_name**
> execute_by_name(
> query_name: str,
> query: ExecuteByNameQuery,
> headers
> ) -> QueryResult

Execute Named Query

Execute a named timeseries query.  Retrieves a stored query definition by name, applies overrides from the url parameters, and executes it.

### Example

```python
# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-queries-types` is installed
from waylay.services.queries.models.execute_query_queries_v1_data_post_interpolation_parameter import (
    ExecuteQueryQueriesV1DataPostInterpolationParameter,
)
from waylay.services.queries.models.execute_query_queries_v1_data_post_render_parameter import (
    ExecuteQueryQueriesV1DataPostRenderParameter,
)
from waylay.services.queries.models.query_result import QueryResult

try:
    # Execute Named Query
    # calls `GET /queries/v1/data/{query_name}`
    api_response = await waylay_client.queries.execute_queries.execute_by_name(
        "query_name_example",  # query_name | path param "query_name"
        # query parameters:
        query={
            "resource": "13efb488-75ac-4dac-828a-d49c5c2ebbfc",
            "metric": "temperature",
            "interpolation": "pad",
            "render": "HEADER_ROW",
        },
        headers={
            "accept": "accept_example",
        },
    )
    print(f"Response: {api_response}")
except ApiError as e:
    print("Exception when calling queries.execute_queries.execute_by_name: %s\n" % e)
```

### Endpoint
```
GET /queries/v1/data/{query_name}
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**query_name** | **str** | path parameter `"query_name"` |  | 
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['resource']** (dict) <br> **query.resource** (Query) | **str** | query parameter `"resource"` | Default Resource Override. | [optional] 
**query['metric']** (dict) <br> **query.metric** (Query) | **str** | query parameter `"metric"` | Default Metric Override. | [optional] 
**query['aggregation']** (dict) <br> **query.aggregation** (Query) | **ExecuteByNameAggregation** | query parameter `"aggregation"` |  | [optional] 
**query['interpolation']** (dict) <br> **query.interpolation** (Query) | [**ExecuteQueryQueriesV1DataPostInterpolationParameter**](ExecuteQueryQueriesV1DataPostInterpolationParameter.md) | query parameter `"interpolation"` |  | [optional] 
**query['freq']** (dict) <br> **query.freq** (Query) | **ExecuteByNameFreq** | query parameter `"freq"` | Override for the &#x60;freq&#x60; query attribute. | [optional] 
**query['from']** (dict) <br> **query.var_from** (Query) | **ExecuteByNameFrom** | query parameter `"from"` |  | [optional] 
**query['until']** (dict) <br> **query.until** (Query) | **ExecuteByNameUntil** | query parameter `"until"` |  | [optional] 
**query['window']** (dict) <br> **query.window** (Query) | **ExecuteByNameWindow** | query parameter `"window"` |  | [optional] 
**query['periods']** (dict) <br> **query.periods** (Query) | **int** | query parameter `"periods"` |  | [optional] 
**query['render']** (dict) <br> **query.render** (Query) | [**ExecuteQueryQueriesV1DataPostRenderParameter**](ExecuteQueryQueriesV1DataPostRenderParameter.md) | query parameter `"render"` |  | [optional] 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 
**headers['accept']** | **str** | request header `"accept"`  | Use a &#39;text/csv&#39; accept header to get CSV formatted results. | [optional] 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`QueryResult`** |  | [QueryResult](QueryResult.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execute**
> execute(
> query: ExecuteQuery,
> headers
> ) -> QueryResult

Execute Query

Execute a timeseries query.  Executes the timeseries query specified in the request body, after applying any overrides from the url parameters.  Note that string values in the query body can contain `{var_name}` placeholders. These will get replaced with by `var_name` bindings in the query body for that variable.  ```json {     \"station_id\": \"29758\",     \"resource\": \"weather_station_{station_id}\",     ... } ``` results in using a `weather_station_29758` resource.

### Example

```python
# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-queries-types` is installed
from waylay.services.queries.models.execute_query_queries_v1_data_post_interpolation_parameter import (
    ExecuteQueryQueriesV1DataPostInterpolationParameter,
)
from waylay.services.queries.models.execute_query_queries_v1_data_post_render_parameter import (
    ExecuteQueryQueriesV1DataPostRenderParameter,
)
from waylay.services.queries.models.query_input import QueryInput
from waylay.services.queries.models.query_result import QueryResult

try:
    # Execute Query
    # calls `POST /queries/v1/data`
    api_response = await waylay_client.queries.execute_queries.execute(
        # query parameters:
        query={
            "resource": "13efb488-75ac-4dac-828a-d49c5c2ebbfc",
            "metric": "temperature",
            "interpolation": "pad",
            "render": "HEADER_ROW",
        },
        # json data: use a generated model or a json-serializable python data structure (dict, list)
        json=waylay.services.queries.QueryInput(),  # QueryInput |
        headers={
            "accept": "accept_example",
        },
    )
    print(f"Response: {api_response}")
except ApiError as e:
    print("Exception when calling queries.execute_queries.execute: %s\n" % e)
```

### Endpoint
```
POST /queries/v1/data
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**json** | [**QueryInput**](QueryInput.md) | json request body |  | 
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['resource']** (dict) <br> **query.resource** (Query) | **str** | query parameter `"resource"` | Default Resource Override. | [optional] 
**query['metric']** (dict) <br> **query.metric** (Query) | **str** | query parameter `"metric"` | Default Metric Override. | [optional] 
**query['aggregation']** (dict) <br> **query.aggregation** (Query) | **ExecuteQueryQueriesV1DataPostAggregation** | query parameter `"aggregation"` |  | [optional] 
**query['interpolation']** (dict) <br> **query.interpolation** (Query) | [**ExecuteQueryQueriesV1DataPostInterpolationParameter**](ExecuteQueryQueriesV1DataPostInterpolationParameter.md) | query parameter `"interpolation"` |  | [optional] 
**query['freq']** (dict) <br> **query.freq** (Query) | **ExecuteQueryQueriesV1DataPostFreq** | query parameter `"freq"` | Override for the &#x60;freq&#x60; query attribute. | [optional] 
**query['from']** (dict) <br> **query.var_from** (Query) | **ExecuteQueryQueriesV1DataPostFrom** | query parameter `"from"` |  | [optional] 
**query['until']** (dict) <br> **query.until** (Query) | **ExecuteQueryQueriesV1DataPostUntil** | query parameter `"until"` |  | [optional] 
**query['window']** (dict) <br> **query.window** (Query) | **ExecuteQueryQueriesV1DataPostWindow** | query parameter `"window"` |  | [optional] 
**query['periods']** (dict) <br> **query.periods** (Query) | **int** | query parameter `"periods"` |  | [optional] 
**query['render']** (dict) <br> **query.render** (Query) | [**ExecuteQueryQueriesV1DataPostRenderParameter**](ExecuteQueryQueriesV1DataPostRenderParameter.md) | query parameter `"render"` |  | [optional] 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 
**headers['accept']** | **str** | request header `"accept"`  | Use a &#39;text/csv&#39; accept header to get CSV formatted results. | [optional] 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`QueryResult`** |  | [QueryResult](QueryResult.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/csv

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

