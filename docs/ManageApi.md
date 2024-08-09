# waylay.services.queries.ManageApi

All URIs are relative to *https://api.waylay.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](ManageApi.md#create) | **POST** /queries/v1/query | Post Query
[**get**](ManageApi.md#get) | **GET** /queries/v1/query/{query_name} | Get Query
[**list**](ManageApi.md#list) | **GET** /queries/v1/query | List Queries
[**remove**](ManageApi.md#remove) | **DELETE** /queries/v1/query/{query_name} | Remove Query
[**update**](ManageApi.md#update) | **PUT** /queries/v1/query/{query_name} | Update Query

# **create**
> create(
> headers
> ) -> QueryResponse

Post Query

Create a new named query.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-queries-types` is installed
from waylay.services.queries.models.query_entity_input import QueryEntityInput
from waylay.services.queries.models.query_response import QueryResponse
try:
    # Post Query
    # calls `POST /queries/v1/query`
    api_response = await waylay_client.queries.manage.create(
        # json data: use a generated model or a json-serializable python data structure (dict, list)
        json = waylay.services.queries.QueryEntityInput() # QueryEntityInput | 
    )
    print("The response of queries.manage.create:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling queries.manage.create: %s\n" % e)
```

### Endpoint
```
POST /queries/v1/query
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**json** | [**QueryEntityInput**](QueryEntityInput.md) | json request body |  | 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`QueryResponse`** |  | [QueryResponse](QueryResponse.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> get(
> query_name: str,
> headers
> ) -> QueryResponse

Get Query

Get the definition of a named query.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-queries-types` is installed
from waylay.services.queries.models.query_response import QueryResponse
try:
    # Get Query
    # calls `GET /queries/v1/query/{query_name}`
    api_response = await waylay_client.queries.manage.get(
        'query_name_example', # query_name | path param "query_name"
    )
    print("The response of queries.manage.get:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling queries.manage.get: %s\n" % e)
```

### Endpoint
```
GET /queries/v1/query/{query_name}
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**query_name** | **str** | path parameter `"query_name"` | Name of the stored query. | 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`QueryResponse`** |  | [QueryResponse](QueryResponse.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> list(
> query: ListQuery,
> headers
> ) -> QueriesListResponse

List Queries

List named queries.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-queries-types` is installed
from waylay.services.queries.models.queries_list_response import QueriesListResponse
try:
    # List Queries
    # calls `GET /queries/v1/query`
    api_response = await waylay_client.queries.manage.list(
        # query parameters:
        query = {
            'q': ''
            'limit': 10
            'offset': 0
        },
    )
    print("The response of queries.manage.list:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling queries.manage.list: %s\n" % e)
```

### Endpoint
```
GET /queries/v1/query
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['q']** (dict) <br> **query.q** (Query) | **str** | query parameter `"q"` | The QDSL filter condition for the stored queries. Note that this value needs to be escaped when passed as an url paramater. | [optional] [default &#39;&#39;]
**query['limit']** (dict) <br> **query.limit** (Query) | **int** | query parameter `"limit"` | Maximal number of items return in one response. | [optional] [default 10]
**query['offset']** (dict) <br> **query.offset** (Query) | **int** | query parameter `"offset"` | Numbers of items to skip before listing results in the response page. | [optional] [default 0]
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`QueriesListResponse`** |  | [QueriesListResponse](QueriesListResponse.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove**
> remove(
> query_name: str,
> headers
> ) -> DeleteResponse

Remove Query

Remove definition of a named query.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-queries-types` is installed
from waylay.services.queries.models.delete_response import DeleteResponse
try:
    # Remove Query
    # calls `DELETE /queries/v1/query/{query_name}`
    api_response = await waylay_client.queries.manage.remove(
        'query_name_example', # query_name | path param "query_name"
    )
    print("The response of queries.manage.remove:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling queries.manage.remove: %s\n" % e)
```

### Endpoint
```
DELETE /queries/v1/query/{query_name}
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**query_name** | **str** | path parameter `"query_name"` | Name of the stored query. | 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`DeleteResponse`** |  | [DeleteResponse](DeleteResponse.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> update(
> query_name: str,
> headers
> ) -> QueryResponse

Update Query

Create or update a named query definition.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-queries-types` is installed
from waylay.services.queries.models.query_definition import QueryDefinition
from waylay.services.queries.models.query_response import QueryResponse
try:
    # Update Query
    # calls `PUT /queries/v1/query/{query_name}`
    api_response = await waylay_client.queries.manage.update(
        'query_name_example', # query_name | path param "query_name"
        # json data: use a generated model or a json-serializable python data structure (dict, list)
        json = waylay.services.queries.QueryDefinition() # QueryDefinition | 
    )
    print("The response of queries.manage.update:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling queries.manage.update: %s\n" % e)
```

### Endpoint
```
PUT /queries/v1/query/{query_name}
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**query_name** | **str** | path parameter `"query_name"` | Name of the stored query. | 
**json** | [**QueryDefinition**](QueryDefinition.md) | json request body |  | 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`QueryResponse`** |  | [QueryResponse](QueryResponse.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

