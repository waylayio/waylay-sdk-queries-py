# ColumnHeader

Column attributes.  Attributes that identify and describe the data in this column.

**Source:** `waylay.services.queries.models.column_header`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource** | **str** |  | 
**metric** | **str** |  | 
**aggregation** | **str** |  | [optional] 


## Example

```python
from waylay.services.queries.models.column_header import ColumnHeader

column_header = ColumnHeader(resource=..., metric=..., aggregation=...)

# Create from JSON
column_header = ColumnHeader.from_json(
    '{ "resource": ..., "metric": ..., "aggregation": ... }'
)

# Export to dictionary
column_header_dict = column_header.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


