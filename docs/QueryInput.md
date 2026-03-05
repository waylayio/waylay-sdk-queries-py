# QueryInput

Query definition for a Waylay analytics query.  See also [api docs](https://docs.waylay.io/#/api/query/?id=data-query-json-representation).

**Source:** `waylay.services.queries.models.query_input`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource** | **str** | Default resource for the series in the query. | [optional] 
**metric** | **str** | Default metric for the series in the query. | [optional] 
**aggregation** | [**DefaultAggregation**](DefaultAggregation.md) |  | [optional] 
**interpolation** | [**DefaultInterpolation**](DefaultInterpolation.md) |  | [optional] 
**freq** | [**GroupingInterval**](GroupingInterval.md) |  | [optional] 
**var_from** | [**TimeWindowFrom**](TimeWindowFrom.md) |  | [optional] 
**until** | [**TimeWindowUntil**](TimeWindowUntil.md) |  | [optional] 
**window** | [**Window**](Window.md) |  | [optional] 
**periods** | **int** | The size of the time window in number of &#x60;freq&#x60; units. One of the [time line](https://docs.waylay.io/#/api/query/?id&#x3D;time-line-properties) specifiers. | [optional] 
**align** | [**Alignment**](Alignment.md) |  | [optional] 
**data** | [**List[SeriesSpec]**](SeriesSpec.md) | List of series specifications. When not specified, a single default series specification is assumed(&#x60;[{}]&#x60;, using the default &#x60;metric&#x60;,&#x60;resource&#x60;, ... ). | [optional] 
**render** | [**Render**](Render.md) |  | [optional] 
**lookback** | **bool** | If enabled, the **last-known value** for each of the series will be taken into account in the result.  For **unaggregated** series, that value will be included as is (with a timestamp before the result window). For **aggregated** series, that value will be used at the first timestamp, but only if  * no aggregated value on the first timestamp could be computed  * and the aggregation is compatible with the value, i.e. in mean, min, max, first, last, median | [optional] 


## Example

```python
from waylay.services.queries.models.query_input import QueryInput

query_input = QueryInput(
    resource=...,
    metric=...,
    aggregation=...,
    interpolation=...,
    freq=...,
    var_from=...,
    until=...,
    window=...,
    periods=...,
    align=...,
    data=...,
    render=...,
    lookback=...,
)

# Create from JSON
query_input = QueryInput.from_json(
    '{ "resource": ..., "metric": ..., "aggregation": ..., "interpolation": ..., "freq": ..., "from": ..., "until": ..., "window": ..., "periods": ..., "align": ..., "data": ..., "render": ..., "lookback": ... }'
)

# Export to dictionary
query_input_dict = query_input.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


