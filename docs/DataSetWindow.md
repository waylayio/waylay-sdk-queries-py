# DataSetWindow

Data Window.  Statistics of the time axis of a data set. Present with render option `include_window_spec=true`.\",

**Source:** `waylay.services.queries.models.data_set_window`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**until** | **int** | Exclusive higher bound of the time axis in unix epoch milliseconds. | 
**window** | **str** | Time axis length as ISO8601 period. | 
**freq** | **str** | Time axis aggregation interval as an ISO8601 period . | 


## Example

```python
from waylay.services.queries.models.data_set_window import DataSetWindow

data_set_window = DataSetWindow(until=..., window=..., freq=...)

# Create from JSON
data_set_window = DataSetWindow.from_json(
    '{ "until": ..., "window": ..., "freq": ... }'
)

# Export to dictionary
data_set_window_dict = data_set_window.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


