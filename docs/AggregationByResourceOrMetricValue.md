# AggregationByResourceOrMetricValue


**Source:** `waylay.services.queries.models.aggregation_by_resource_or_metric_value`



## Union Type (Any Of)

This type allows any of the following:

Type | Description
------------ | -------------
[**Aggregation**](Aggregation.md) | -
[**List[AggregationsInner]**](AggregationsInner.md) | Aggregation methods, leading to sepearate series.

## Example

```python
from waylay.services.queries.models.aggregation_by_resource_or_metric_value import (
    AggregationByResourceOrMetricValue,
)

# Use any of the accepted types (see table above)
my_aggregation_by_resource_or_metric_value: AggregationByResourceOrMetricValue = ...
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


