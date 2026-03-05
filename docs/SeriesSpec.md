# SeriesSpec

Query specification for a single series.

**Source:** `waylay.services.queries.models.series_spec`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Optional alias name for the series. This name is used when exporting the dataset to CSV format. | [optional] 
**resource** | **str** | Resource id for the series, required unless it is specified as a query default. | [optional] 
**metric** | **str** | Metric name for the series, required unless it is specified as a query default. | [optional] 
**aggregration** | [**Aggregration**](Aggregration.md) |  | [optional] 
**interpolation** | [**InterpolationSpecification**](InterpolationSpecification.md) |  | [optional] 


## Example

```python
from waylay.services.queries.models.series_spec import SeriesSpec

series_spec = SeriesSpec(
    name=..., resource=..., metric=..., aggregration=..., interpolation=...
)

# Create from JSON
series_spec = SeriesSpec.from_json(
    '{ "name": ..., "resource": ..., "metric": ..., "aggregration": ..., "interpolation": ... }'
)

# Export to dictionary
series_spec_dict = series_spec.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


