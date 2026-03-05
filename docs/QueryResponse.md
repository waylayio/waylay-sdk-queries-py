# QueryResponse

Represents a single named query.

**Source:** `waylay.services.queries.models.query_response`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**QueryHALLinks**](QueryHALLinks.md) |  | 
**attrs** | **Dict[str, object]** | System provided metadata for the query definition. | 
**name** | **str** | Name of the stored query definition. | 
**meta** | **Dict[str, object]** | User metadata for the query definition. | [optional] 
**query** | [**QueryOutput**](QueryOutput.md) |  | 
**messages** | [**List[Message]**](Message.md) |  | [optional] 


## Example

```python
from waylay.services.queries.models.query_response import QueryResponse

query_response = QueryResponse(
    links=..., attrs=..., name=..., meta=..., query=..., messages=...
)

# Create from JSON
query_response = QueryResponse.from_json(
    '{ "_links": ..., "attrs": ..., "name": ..., "meta": ..., "query": ..., "messages": ... }'
)

# Export to dictionary
query_response_dict = query_response.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


