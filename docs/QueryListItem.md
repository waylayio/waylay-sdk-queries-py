# QueryListItem

Listing of a query definition item.

**Source:** `waylay.services.queries.models.query_list_item`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**QueryHALLinks**](QueryHALLinks.md) |  | 
**attrs** | **Dict[str, object]** | System provided metadata for the query definition. | 
**name** | **str** | Name of the stored query definition. | 
**meta** | **Dict[str, object]** | User metadata for the query definition. | [optional] 


## Example

```python
from waylay.services.queries.models.query_list_item import QueryListItem

query_list_item = QueryListItem(links=..., attrs=..., name=..., meta=...)

# Create from JSON
query_list_item = QueryListItem.from_json(
    '{ "_links": ..., "attrs": ..., "name": ..., "meta": ... }'
)

# Export to dictionary
query_list_item_dict = query_list_item.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


