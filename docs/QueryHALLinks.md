# QueryHALLinks

HAL Links for a query entity.

**Source:** `waylay.services.queries.models.query_hal_links`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | [**HALLink**](HALLink.md) |  | 
**execute** | [**HALLink**](HALLink.md) |  | 


## Example

```python
from waylay.services.queries.models.query_hal_links import QueryHALLinks

query_hal_links = QueryHALLinks(var_self=..., execute=...)

# Create from JSON
query_hal_links = QueryHALLinks.from_json('{ "self": ..., "execute": ... }')

# Export to dictionary
query_hal_links_dict = query_hal_links.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


