# waylay.services.queries.ExecuteApi

All URIs are relative to *https://api.waylay.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**execute_by_name**](ExecuteApi.md#execute_by_name) | **GET** /queries/v1/data/{query_name} | Execute Named Query
[**execute**](ExecuteApi.md#execute) | **POST** /queries/v1/data | Execute Query

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
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-queries-types` is installed
from waylay.services.queries.models.query_result import QueryResult
try:
    # Execute Named Query
    # calls `GET /queries/v1/data/{query_name}`
    api_response = await waylay_client.queries.execute.execute_by_name(
        'query_name_example', # query_name | path param "query_name"
        # query parameters:
        query = {
            'resource': '13efb488-75ac-4dac-828a-d49c5c2ebbfc'
            'metric': 'temperature'
        },
        headers = {
            'accept': 'accept_example',
        },
    )
    print("The response of queries.execute.execute_by_name:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling queries.execute.execute_by_name: %s\n" % e)
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
**query['aggregation']** (dict) <br> **query.aggregation** (Query) | **AggregationMethod** | query parameter `"aggregation"` |  | [optional] 
**query['interpolation']** (dict) <br> **query.interpolation** (Query) | [**Interpolation**](.md) | query parameter `"interpolation"` |  | [optional] 
**query['freq']** (dict) <br> **query.freq** (Query) | **GroupingIntervalOverride** | query parameter `"freq"` | Override for the &#x60;freq&#x60; query attribute. | [optional] 
**query['from']** (dict) <br> **query.var_from** (Query) | **FromOverride** | query parameter `"from"` |  | [optional] 
**query['until']** (dict) <br> **query.until** (Query) | **FromOverride** | query parameter `"until"` |  | [optional] 
**query['window']** (dict) <br> **query.window** (Query) | **WindowOverride** | query parameter `"window"` |  | [optional] 
**query['periods']** (dict) <br> **query.periods** (Query) | **int** | query parameter `"periods"` |  | [optional] 
**query['render']** (dict) <br> **query.render** (Query) | [**Render1**](.md) | query parameter `"render"` |  | [optional] 
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

Execute a timeseries query.  Executes the timeseries query specified in the request body, after applying any overrides from the url parameters.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-queries-types` is installed
from waylay.services.queries.models.query_input import QueryInput
from waylay.services.queries.models.query_result import QueryResult
try:
    # Execute Query
    # calls `POST /queries/v1/data`
    api_response = await waylay_client.queries.execute.execute(
        # query parameters:
        query = {
            'resource': '13efb488-75ac-4dac-828a-d49c5c2ebbfc'
            'metric': 'temperature'
        },
        # json data: use a generated model or a json-serializable python data structure (dict, list)
        json = waylay.services.queries.QueryInput() # QueryInput | 
        headers = {
            'accept': 'accept_example',
        },
    )
    print("The response of queries.execute.execute:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling queries.execute.execute: %s\n" % e)
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
**query['aggregation']** (dict) <br> **query.aggregation** (Query) | **AggregationMethod** | query parameter `"aggregation"` |  | [optional] 
**query['interpolation']** (dict) <br> **query.interpolation** (Query) | [**Interpolation**](.md) | query parameter `"interpolation"` |  | [optional] 
**query['freq']** (dict) <br> **query.freq** (Query) | **GroupingIntervalOverride** | query parameter `"freq"` | Override for the &#x60;freq&#x60; query attribute. | [optional] 
**query['from']** (dict) <br> **query.var_from** (Query) | **FromOverride** | query parameter `"from"` |  | [optional] 
**query['until']** (dict) <br> **query.until** (Query) | **FromOverride** | query parameter `"until"` |  | [optional] 
**query['window']** (dict) <br> **query.window** (Query) | **WindowOverride** | query parameter `"window"` |  | [optional] 
**query['periods']** (dict) <br> **query.periods** (Query) | **int** | query parameter `"periods"` |  | [optional] 
**query['render']** (dict) <br> **query.render** (Query) | [**Render1**](.md) | query parameter `"render"` |  | [optional] 
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

