# Aggregration

Aggregation method for the series (if aggregated). If missing, the query default is used.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from waylay.services.queries.models.aggregration import Aggregration

# TODO update the JSON string below
json = "{}"
# create an instance of Aggregration from a JSON string
aggregration_instance = Aggregration.from_json(json)
# print the JSON string representation of the object
print Aggregration.to_json()

# convert the object into a dict
aggregration_dict = aggregration_instance.to_dict()
# create an instance of Aggregration from a dict
aggregration_form_dict = aggregration.from_dict(aggregration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


