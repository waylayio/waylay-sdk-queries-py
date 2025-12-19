# QueryEntityInput

Input data to create a query definition.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the stored query definition. | 
**meta** | **Dict[str, object]** | User metadata for the query definition. | [optional] 
**query** | [**QueryInput**](QueryInput.md) |  | 

## Example

```python
from waylay.services.queries.models.query_entity_input import QueryEntityInput

# TODO update the JSON string below
json = "{}"
# create an instance of QueryEntityInput from a JSON string
query_entity_input_instance = QueryEntityInput.from_json(json)
# print the JSON string representation of the object
print QueryEntityInput.to_json()

# convert the object into a dict
query_entity_input_dict = query_entity_input_instance.to_dict()
# create an instance of QueryEntityInput from a dict
query_entity_input_form_dict = query_entity_input.from_dict(query_entity_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


