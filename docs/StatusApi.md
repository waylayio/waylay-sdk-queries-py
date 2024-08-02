# waylay.services.queries.StatusApi

All URIs are relative to *https://api.waylay.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get**](StatusApi.md#get) | **GET** /queries/v1/queries/v1 | Get Version And Health

# **get**
> get(
> headers
> ) -> Dict[str, str]

Get Version And Health

Get the version and health status for waylay-query.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-queries-types` is installed
try:
    # Get Version And Health
    # calls `GET /queries/v1/queries/v1`
    api_response = await waylay_client.queries.status.get(
    )
    print("The response of queries.status.get:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling queries.status.get: %s\n" % e)
```

### Endpoint
```
GET /queries/v1/queries/v1
```
### Parameters

This endpoint does not need any parameter.
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`Dict[str, str]`** |  | 
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

