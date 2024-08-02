# RowHeadersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **int** | Unix epoch milliseconds timestamp. | 
**timestamp_iso** | **datetime** | ISO8601 rendering of the timestamp, present when &#x60;render.iso_timestamp&#x3D;true&#x60; | [optional] 

## Example

```python
from waylay.services.queries.models.row_headers_inner import RowHeadersInner

# TODO update the JSON string below
json = "{}"
# create an instance of RowHeadersInner from a JSON string
row_headers_inner_instance = RowHeadersInner.from_json(json)
# print the JSON string representation of the object
print RowHeadersInner.to_json()

# convert the object into a dict
row_headers_inner_dict = row_headers_inner_instance.to_dict()
# create an instance of RowHeadersInner from a dict
row_headers_inner_form_dict = row_headers_inner.from_dict(row_headers_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


