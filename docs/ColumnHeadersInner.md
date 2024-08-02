# ColumnHeadersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource** | **str** |  | 
**metric** | **str** |  | 
**aggregation** | **str** |  | [optional] 

## Example

```python
from waylay.services.queries.models.column_headers_inner import ColumnHeadersInner

# TODO update the JSON string below
json = "{}"
# create an instance of ColumnHeadersInner from a JSON string
column_headers_inner_instance = ColumnHeadersInner.from_json(json)
# print the JSON string representation of the object
print ColumnHeadersInner.to_json()

# convert the object into a dict
column_headers_inner_dict = column_headers_inner_instance.to_dict()
# create an instance of ColumnHeadersInner from a dict
column_headers_inner_form_dict = column_headers_inner.from_dict(column_headers_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


