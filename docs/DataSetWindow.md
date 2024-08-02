# DataSetWindow

Data Window.  Statistics of the time axis of a data set. Present with render option `include_window_spec=true`.\",

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**until** | **int** | Exclusive higher bound of the time axis in unix epoch milliseconds. | 
**window** | **str** | Time axis length as ISO8601 period. | 
**freq** | **str** | Time axis aggregation interval as an ISO8601 period . | 

## Example

```python
from waylay.services.queries.models.data_set_window import DataSetWindow

# TODO update the JSON string below
json = "{}"
# create an instance of DataSetWindow from a JSON string
data_set_window_instance = DataSetWindow.from_json(json)
# print the JSON string representation of the object
print DataSetWindow.to_json()

# convert the object into a dict
data_set_window_dict = data_set_window_instance.to_dict()
# create an instance of DataSetWindow from a dict
data_set_window_form_dict = data_set_window.from_dict(data_set_window_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


