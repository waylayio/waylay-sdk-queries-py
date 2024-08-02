# Window

The absolute size of the time window for which results will be returned. One of the [time line](https://docs.waylay.io/#/api/query/?id=time-line-properties) specifiers.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from waylay.services.queries.models.window import Window

# TODO update the JSON string below
json = "{}"
# create an instance of Window from a JSON string
window_instance = Window.from_json(json)
# print the JSON string representation of the object
print Window.to_json()

# convert the object into a dict
window_dict = window_instance.to_dict()
# create an instance of Window from a dict
window_form_dict = window.from_dict(window_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


