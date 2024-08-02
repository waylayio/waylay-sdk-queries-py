# QueryInput

Query definition for a Waylay analytics query.  See also [api docs](https://docs.waylay.io/#/api/query/?id=data-query-json-representation).

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

## Example

```python
from waylay.services.queries.models.query_input import QueryInput

# TODO update the JSON string below
json = "{}"
# create an instance of QueryInput from a JSON string
query_input_instance = QueryInput.from_json(json)
# print the JSON string representation of the object
print QueryInput.to_json()

# convert the object into a dict
query_input_dict = query_input_instance.to_dict()
# create an instance of QueryInput from a dict
query_input_form_dict = query_input.from_dict(query_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


