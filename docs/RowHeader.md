# RowHeader

Index entry attributes.  Attributes for a timestamp index entry.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **int** | Unix epoch milliseconds timestamp. | 
**timestamp_iso** | **datetime** | ISO8601 rendering of the timestamp, present when &#x60;render.iso_timestamp&#x3D;true&#x60; | [optional] 

## Example

```python
from waylay.services.queries.models.row_header import RowHeader

# TODO update the JSON string below
json = "{}"
# create an instance of RowHeader from a JSON string
row_header_instance = RowHeader.from_json(json)
# print the JSON string representation of the object
print RowHeader.to_json()

# convert the object into a dict
row_header_dict = row_header_instance.to_dict()
# create an instance of RowHeader from a dict
row_header_form_dict = row_header.from_dict(row_header_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


