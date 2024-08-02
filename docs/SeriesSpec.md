# SeriesSpec

Query specification for a single series.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Optional alias name for the series. This name is used when exporting the dataset to CSV format. | [optional] 
**resource** | **str** | Resource id for the series, required unless it is specified as a query default. | [optional] 
**metric** | **str** | Metric name for the series, required unless it is specified as a query default. | [optional] 
**aggregration** | [**AggregationMethod**](AggregationMethod.md) |  | [optional] 
**interpolation** | [**Interpolation**](Interpolation.md) |  | [optional] 

## Example

```python
from waylay.services.queries.models.series_spec import SeriesSpec

# TODO update the JSON string below
json = "{}"
# create an instance of SeriesSpec from a JSON string
series_spec_instance = SeriesSpec.from_json(json)
# print the JSON string representation of the object
print SeriesSpec.to_json()

# convert the object into a dict
series_spec_dict = series_spec_instance.to_dict()
# create an instance of SeriesSpec from a dict
series_spec_form_dict = series_spec.from_dict(series_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


