# GroupingInterval

Interval used to aggregate or regularize data. One of the [time line](https://docs.waylay.io/#/api/query/?id=time-line-properties) specifiers.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from waylay.services.queries.models.grouping_interval import GroupingInterval

# TODO update the JSON string below
json = "{}"
# create an instance of GroupingInterval from a JSON string
grouping_interval_instance = GroupingInterval.from_json(json)
# print the JSON string representation of the object
print GroupingInterval.to_json()

# convert the object into a dict
grouping_interval_dict = grouping_interval_instance.to_dict()
# create an instance of GroupingInterval from a dict
grouping_interval_form_dict = grouping_interval.from_dict(grouping_interval_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


