# DataSetAttributes

Data Set Attributes.  Data attributes that apply to all data in this set.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** | The role of series specification that was used to compile this data set. | [optional] 

## Example

```python
from waylay.services.queries.models.data_set_attributes import DataSetAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of DataSetAttributes from a JSON string
data_set_attributes_instance = DataSetAttributes.from_json(json)
# print the JSON string representation of the object
print DataSetAttributes.to_json()

# convert the object into a dict
data_set_attributes_dict = data_set_attributes_instance.to_dict()
# create an instance of DataSetAttributes from a dict
data_set_attributes_form_dict = data_set_attributes.from_dict(data_set_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


