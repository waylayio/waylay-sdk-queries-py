# QueryDefinition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | **Dict[str, object]** | User metadata for the query definition. | [optional] 
**query** | [**QueryInput**](QueryInput.md) |  | [optional] 
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
from waylay.services.queries.models.query_definition import QueryDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of QueryDefinition from a JSON string
query_definition_instance = QueryDefinition.from_json(json)
# print the JSON string representation of the object
print QueryDefinition.to_json()

# convert the object into a dict
query_definition_dict = query_definition_instance.to_dict()
# create an instance of QueryDefinition from a dict
query_definition_form_dict = query_definition.from_dict(query_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


