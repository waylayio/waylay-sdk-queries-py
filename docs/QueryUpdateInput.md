# QueryUpdateInput

Input data to update a query definition.

**Source:** `waylay.services.queries.models.query_update_input`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | **Dict[str, object]** | User metadata for the query definition. | [optional] 
**query** | [**QueryInput**](QueryInput.md) |  | [optional] 


## Example

```python
from waylay.services.queries.models.query_update_input import QueryUpdateInput

query_update_input = QueryUpdateInput(meta=..., query=...)

# Create from JSON
query_update_input = QueryUpdateInput.from_json('{ "meta": ..., "query": ... }')

# Export to dictionary
query_update_input_dict = query_update_input.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


