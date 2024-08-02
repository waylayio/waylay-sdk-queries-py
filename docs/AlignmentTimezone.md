# AlignmentTimezone

 The timezone to use when shifting boundaries, especially at day granularity. Also affects the rendering of timestamps when `render.iso_timestamp` is enabled.  When not specified, the `UTC` timezone is used. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from waylay.services.queries.models.alignment_timezone import AlignmentTimezone

# TODO update the JSON string below
json = "{}"
# create an instance of AlignmentTimezone from a JSON string
alignment_timezone_instance = AlignmentTimezone.from_json(json)
# print the JSON string representation of the object
print AlignmentTimezone.to_json()

# convert the object into a dict
alignment_timezone_dict = alignment_timezone_instance.to_dict()
# create an instance of AlignmentTimezone from a dict
alignment_timezone_form_dict = alignment_timezone.from_dict(alignment_timezone_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


