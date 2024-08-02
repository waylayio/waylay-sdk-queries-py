# ObjectDataValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from waylay.services.queries.models.object_data_value import ObjectDataValue

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectDataValue from a JSON string
object_data_value_instance = ObjectDataValue.from_json(json)
# print the JSON string representation of the object
print ObjectDataValue.to_json()

# convert the object into a dict
object_data_value_dict = object_data_value_instance.to_dict()
# create an instance of ObjectDataValue from a dict
object_data_value_form_dict = object_data_value.from_dict(object_data_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


