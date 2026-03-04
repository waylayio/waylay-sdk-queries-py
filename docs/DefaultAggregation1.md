# DefaultAggregation1

Default aggregation method(s) for the series in the query.

**Source:** `waylay.services.queries.models.default_aggregation1`



## Union Type (Any Of)

This type allows any of the following:

Type | Description
------------ | -------------
[**Aggregation1**](Aggregation1.md) | -
[**List[AggregationsInner1]**](AggregationsInner1.md) | Aggregation methods, leading to sepearate series.
[**Dict[str, AggregationByResourceOrMetricValue1]**](AggregationByResourceOrMetricValue1.md) | Aggregation methods specified per resource or metric.
[**Dict[str, AggregationByResourceAndMetricValue1]**](AggregationByResourceAndMetricValue1.md) | Aggregation methods specified per resource and metric.

## Example

```python
from waylay.services.queries.models.default_aggregation1 import DefaultAggregation1

# Use any of the accepted types (see table above)
my_default_aggregation1: DefaultAggregation1 = ...
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


