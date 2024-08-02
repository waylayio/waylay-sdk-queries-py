# TimeWindowFrom

The start of the time window for which results will be returned. One of the [time line](https://docs.waylay.io/#/api/query/?id=time-line-properties)  specifiers.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from waylay.services.queries.models.time_window_from import TimeWindowFrom

# TODO update the JSON string below
json = "{}"
# create an instance of TimeWindowFrom from a JSON string
time_window_from_instance = TimeWindowFrom.from_json(json)
# print the JSON string representation of the object
print TimeWindowFrom.to_json()

# convert the object into a dict
time_window_from_dict = time_window_from_instance.to_dict()
# create an instance of TimeWindowFrom from a dict
time_window_from_form_dict = time_window_from.from_dict(time_window_from_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


