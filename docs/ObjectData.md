# ObjectData

Result data for a timestamp in object format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **int** | Unix epoch milliseconds timestamp. | 
**timestamp_iso** | **datetime** | ISO8601 rendering of the timestamp, present when &#x60;render.iso_timestamp&#x3D;true&#x60; | [optional] 
**role** | **str** | The role of series specification that was used to compile this data set. | [optional] 
**resource** | **str** | Series resource id, if applicable for all values. | [optional] 
**metric** | **str** | Series metric, if applicable for all values. | [optional] 
**aggregation** | **str** | Series aggregation, if applicable for all values. | [optional] 
**levels** | **List[str]** | Attribute level names used to key the values for this observation.  Levels that are flattened have a dot-separated key.  If all observations have the same attribute for a level, that level might be omitted. | [optional] 

## Example

```python
from waylay.services.queries.models.object_data import ObjectData

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectData from a JSON string
object_data_instance = ObjectData.from_json(json)
# print the JSON string representation of the object
print ObjectData.to_json()

# convert the object into a dict
object_data_dict = object_data_instance.to_dict()
# create an instance of ObjectData from a dict
object_data_form_dict = object_data.from_dict(object_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


