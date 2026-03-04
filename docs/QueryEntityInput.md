# QueryEntityInput

Input data to create a query definition.

**Source:** `waylay.services.queries.models.query_entity_input`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the stored query definition. | 
**meta** | **Dict[str, object]** | User metadata for the query definition. | [optional] 
**query** | [**QueryInput**](QueryInput.md) |  | 


## Example

```python
from waylay.services.queries.models.query_entity_input import QueryEntityInput

query_entity_input = QueryEntityInput(name=..., meta=..., query=...)

# Create from JSON
query_entity_input = QueryEntityInput.from_json(
    '{ "name": ..., "meta": ..., "query": ... }'
)

# Export to dictionary
query_entity_input_dict = query_entity_input.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


