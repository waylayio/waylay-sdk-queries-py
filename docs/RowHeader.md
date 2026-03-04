# RowHeader

Index entry attributes.  Attributes for a timestamp index entry.

**Source:** `waylay.services.queries.models.row_header`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **int** | Unix epoch milliseconds timestamp. | 
**timestamp_iso** | **datetime** | ISO8601 rendering of the timestamp, present when &#x60;render.iso_timestamp&#x3D;true&#x60; | [optional] 


## Example

```python
from waylay.services.queries.models.row_header import RowHeader

row_header = RowHeader(timestamp=..., timestamp_iso=...)

# Create from JSON
row_header = RowHeader.from_json('{ "timestamp": ..., "timestamp_iso": ... }')

# Export to dictionary
row_header_dict = row_header.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


