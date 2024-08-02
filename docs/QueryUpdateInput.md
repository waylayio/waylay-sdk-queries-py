# QueryUpdateInput

Input data to update a query definition.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | **object** | User metadata for the query definition. | [optional] 
**query** | [**QueryInput**](QueryInput.md) |  | [optional] 

## Example

```python
from waylay.services.queries.models.query_update_input import QueryUpdateInput

# TODO update the JSON string below
json = "{}"
# create an instance of QueryUpdateInput from a JSON string
query_update_input_instance = QueryUpdateInput.from_json(json)
# print the JSON string representation of the object
print QueryUpdateInput.to_json()

# convert the object into a dict
query_update_input_dict = query_update_input_instance.to_dict()
# create an instance of QueryUpdateInput from a dict
query_update_input_form_dict = query_update_input.from_dict(query_update_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


