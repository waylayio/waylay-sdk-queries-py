# QueriesListResponse

Listing of named queries, with paging links.

**Source:** `waylay.services.queries.models.queries_list_response`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**messages** | [**List[Message]**](Message.md) |  | [optional] 
**queries** | [**List[QueryListItem]**](QueryListItem.md) | One page of matching query definitions. | 
**count** | **int** | Number of query definitions returned in the current response. | 
**offset** | **int** | Offset in the full listing (skipped definitions). | 
**limit** | **int** | Maximal number of query definitions returned in one response. | 
**total_count** | **int** | Total number of query definitions matching the filter. | [optional] 
**links** | [**QueryListHALLinks**](QueryListHALLinks.md) |  | 


## Example

```python
from waylay.services.queries.models.queries_list_response import QueriesListResponse

queries_list_response = QueriesListResponse(
    messages=...,
    queries=...,
    count=...,
    offset=...,
    limit=...,
    total_count=...,
    links=...,
)

# Create from JSON
queries_list_response = QueriesListResponse.from_json(
    '{ "messages": ..., "queries": ..., "count": ..., "offset": ..., "limit": ..., "total_count": ..., "_links": ... }'
)

# Export to dictionary
queries_list_response_dict = queries_list_response.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


