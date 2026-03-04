# DefaultAggregation

Default aggregation method(s) for the series in the query.

**Source:** `waylay.services.queries.models.default_aggregation`



## Union Type (Any Of)

This type allows any of the following:

Type | Description
------------ | -------------
[**Aggregation**](Aggregation.md) | -
[**List[AggregationsInner]**](AggregationsInner.md) | Aggregation methods, leading to sepearate series.
[**Dict[str, AggregationByResourceOrMetricValue]**](AggregationByResourceOrMetricValue.md) | Aggregation methods specified per resource or metric.
[**Dict[str, AggregationByResourceAndMetricValue]**](AggregationByResourceAndMetricValue.md) | Aggregation methods specified per resource and metric.

## Example

```python
from waylay.services.queries.models.default_aggregation import DefaultAggregation

# Use any of the accepted types (see table above)
my_default_aggregation: DefaultAggregation = ...
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


