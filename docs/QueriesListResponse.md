# QueriesListResponse

Listing of named queries, with paging links.

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

# TODO update the JSON string below
json = "{}"
# create an instance of QueriesListResponse from a JSON string
queries_list_response_instance = QueriesListResponse.from_json(json)
# print the JSON string representation of the object
print QueriesListResponse.to_json()

# convert the object into a dict
queries_list_response_dict = queries_list_response_instance.to_dict()
# create an instance of QueriesListResponse from a dict
queries_list_response_form_dict = queries_list_response.from_dict(queries_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


