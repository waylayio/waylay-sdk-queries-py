# DeleteResponse

Confirmation of a delete request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**messages** | [**List[Message]**](Message.md) |  | [optional] 
**links** | [**Dict[str, Links]**](Links.md) | HAL links, indexed by link relation. | [optional] 
**embeddings** | [**Dict[str, Embeddings]**](Embeddings.md) | Hal embeddings, indexed by relation. | [optional] 

## Example

```python
from waylay.services.queries.models.delete_response import DeleteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteResponse from a JSON string
delete_response_instance = DeleteResponse.from_json(json)
# print the JSON string representation of the object
print DeleteResponse.to_json()

# convert the object into a dict
delete_response_dict = delete_response_instance.to_dict()
# create an instance of DeleteResponse from a dict
delete_response_form_dict = delete_response.from_dict(delete_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


