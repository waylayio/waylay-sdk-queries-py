# TimeWindowUntil

The end (not-inclusive) of the time window for which results will be returned. One of the [time line](https://docs.waylay.io/#/api/query/?id=time-line-properties)specifiers.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from waylay.services.queries.models.time_window_until import TimeWindowUntil

# TODO update the JSON string below
json = "{}"
# create an instance of TimeWindowUntil from a JSON string
time_window_until_instance = TimeWindowUntil.from_json(json)
# print the JSON string representation of the object
print TimeWindowUntil.to_json()

# convert the object into a dict
time_window_until_dict = time_window_until_instance.to_dict()
# create an instance of TimeWindowUntil from a dict
time_window_until_form_dict = time_window_until.from_dict(time_window_until_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


