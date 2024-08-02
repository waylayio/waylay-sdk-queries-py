# Alignment

Aggregation Alignment Options.  Specifies how the aggregation grid is aligned.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**at** | [**AlignAt**](AlignAt.md) |  | [optional] 
**shift** | [**AlignShift**](AlignShift.md) |  | [optional] 
**freq** | [**AlignmentGridInterval**](AlignmentGridInterval.md) |  | [optional] 
**timezone** | [**AlignmentTimezone**](AlignmentTimezone.md) |  | [optional] 

## Example

```python
from waylay.services.queries.models.alignment import Alignment

# TODO update the JSON string below
json = "{}"
# create an instance of Alignment from a JSON string
alignment_instance = Alignment.from_json(json)
# print the JSON string representation of the object
print Alignment.to_json()

# convert the object into a dict
alignment_dict = alignment_instance.to_dict()
# create an instance of Alignment from a dict
alignment_form_dict = alignment.from_dict(alignment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


