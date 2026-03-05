# Aggregration

Aggregation method for the series (if aggregated). If missing, the query default is used.

**Source:** `waylay.services.queries.models.aggregration`



## Union Type (One Of)

This type allows one of the following:

Type | Description
------------ | -------------
[**SeriesSpecFirst**](SeriesSpecFirst.md) | -
[**SeriesSpecLast**](SeriesSpecLast.md) | -
[**SeriesSpecMean**](SeriesSpecMean.md) | -
[**SeriesSpecMedian**](SeriesSpecMedian.md) | -
[**SeriesSpecSum**](SeriesSpecSum.md) | -
[**SeriesSpecCount**](SeriesSpecCount.md) | -
[**SeriesSpecCountNumeric**](SeriesSpecCountNumeric.md) | -
[**SeriesSpecCountNonNumeric**](SeriesSpecCountNonNumeric.md) | -
[**SeriesSpecStd**](SeriesSpecStd.md) | -
[**SeriesSpecMax**](SeriesSpecMax.md) | -
[**SeriesSpecMin**](SeriesSpecMin.md) | -

## Example

```python
from waylay.services.queries.models.aggregration import Aggregration

# Use any of the accepted types (see table above)
my_aggregration: Aggregration = ...
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


