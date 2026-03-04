# QueryListHALLinks

HAL Links for a query entity.

**Source:** `waylay.services.queries.models.query_list_hal_links`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | [**HALLink**](HALLink.md) |  | 
**first** | [**HALLink**](HALLink.md) |  | [optional] 
**prev** | [**HALLink**](HALLink.md) |  | [optional] 
**next** | [**HALLink**](HALLink.md) |  | [optional] 
**last** | [**HALLink**](HALLink.md) |  | [optional] 


## Example

```python
from waylay.services.queries.models.query_list_hal_links import QueryListHALLinks

query_list_hal_links = QueryListHALLinks(
    var_self=..., first=..., prev=..., next=..., last=...
)

# Create from JSON
query_list_hal_links = QueryListHALLinks.from_json(
    '{ "self": ..., "first": ..., "prev": ..., "next": ..., "last": ... }'
)

# Export to dictionary
query_list_hal_links_dict = query_list_hal_links.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


