# ObjectDataSet

Data result in object format.  Result item when render option `render.header_array` is not set.  The data values are keyed by their attributes (`resource`, `metric`, `aggregation`), according to the render options: * _hierachical_: for each level, a sub-object is created   (e.g. `render.mode=hier_dict`) * _flattened_: the attributes are '.'-separated concatenation   of the attributes (e.g `render.mode=flat_dict`) * _mixed_: (.e.g. `render.mode=metric_flat_dict`) a single level     (e.g. `metric`) is used as main key, any remaining levels     (`resource`,`aggregation`) are indicated with a flattened subkey.  When `render.rollup=true`, the attribute levels that are the same for all series are not used as key, but reported as a data or table attribute.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**DataSetAttributes**](DataSetAttributes.md) |  | [optional] 
**window_spec** | [**DataSetWindow**](DataSetWindow.md) |  | [optional] 
**data** | [**List[ObjectData]**](ObjectData.md) |  | 

## Example

```python
from waylay.services.queries.models.object_data_set import ObjectDataSet

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectDataSet from a JSON string
object_data_set_instance = ObjectDataSet.from_json(json)
# print the JSON string representation of the object
print ObjectDataSet.to_json()

# convert the object into a dict
object_data_set_dict = object_data_set_instance.to_dict()
# create an instance of ObjectDataSet from a dict
object_data_set_form_dict = object_data_set.from_dict(object_data_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


