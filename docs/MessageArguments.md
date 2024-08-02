# MessageArguments


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource** | **str** |  | [optional] 
**metric** | **str** |  | [optional] 

## Example

```python
from waylay.services.queries.models.message_arguments import MessageArguments

# TODO update the JSON string below
json = "{}"
# create an instance of MessageArguments from a JSON string
message_arguments_instance = MessageArguments.from_json(json)
# print the JSON string representation of the object
print MessageArguments.to_json()

# convert the object into a dict
message_arguments_dict = message_arguments_instance.to_dict()
# create an instance of MessageArguments from a dict
message_arguments_form_dict = message_arguments.from_dict(message_arguments_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


