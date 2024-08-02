# MessageProperties

Additional message arguments.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource** | **str** |  | [optional] 
**metric** | **str** |  | [optional] 

## Example

```python
from waylay.services.queries.models.message_properties import MessageProperties

# TODO update the JSON string below
json = "{}"
# create an instance of MessageProperties from a JSON string
message_properties_instance = MessageProperties.from_json(json)
# print the JSON string representation of the object
print MessageProperties.to_json()

# convert the object into a dict
message_properties_dict = message_properties_instance.to_dict()
# create an instance of MessageProperties from a dict
message_properties_form_dict = message_properties.from_dict(message_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


