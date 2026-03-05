# DeleteResponse

Confirmation of a delete request.

**Source:** `waylay.services.queries.models.delete_response`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**messages** | [**List[Message]**](Message.md) |  | [optional] 
**links** | [**Dict[str, LinksValue]**](LinksValue.md) | HAL links, indexed by link relation. | [optional] 
**embeddings** | [**Dict[str, EmbeddingsValue]**](EmbeddingsValue.md) | Hal embeddings, indexed by relation. | [optional] 


## Example

```python
from waylay.services.queries.models.delete_response import DeleteResponse

delete_response = DeleteResponse(messages=..., links=..., embeddings=...)

# Create from JSON
delete_response = DeleteResponse.from_json(
    '{ "messages": ..., "_links": ..., "_embeddings": ... }'
)

# Export to dictionary
delete_response_dict = delete_response.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


