# DefaultAggregation

Default aggregation method(s) for the series in the query.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from waylay.services.queries.models.default_aggregation import DefaultAggregation

# TODO update the JSON string below
json = "{}"
# create an instance of DefaultAggregation from a JSON string
default_aggregation_instance = DefaultAggregation.from_json(json)
# print the JSON string representation of the object
print DefaultAggregation.to_json()

# convert the object into a dict
default_aggregation_dict = default_aggregation_instance.to_dict()
# create an instance of DefaultAggregation from a dict
default_aggregation_form_dict = default_aggregation.from_dict(default_aggregation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


