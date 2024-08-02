# Hierarchical

if true, use hierarchical objects to represent multiple row (or column) dimensions, otherwise multi-keys get concatenated with a dot-delimiter. If the value is a list, only these levels are kept as separate levels, while remaining levels get concatenated keys

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from waylay.services.queries.models.hierarchical import Hierarchical

# TODO update the JSON string below
json = "{}"
# create an instance of Hierarchical from a JSON string
hierarchical_instance = Hierarchical.from_json(json)
# print the JSON string representation of the object
print Hierarchical.to_json()

# convert the object into a dict
hierarchical_dict = hierarchical_instance.to_dict()
# create an instance of Hierarchical from a dict
hierarchical_form_dict = hierarchical.from_dict(hierarchical_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


