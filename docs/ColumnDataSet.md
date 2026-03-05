# ColumnDataSet

Column-oriented dataset with rows header.  Timeseries data layout with a rows header containing the index data. The data array contains series data prefixed by series attributes. The `rows` index is prefix by the names of these series attributes. Result for render options `data_axis=row` and `header_array=column`.

**Source:** `waylay.services.queries.models.column_data_set`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**DataSetAttributes**](DataSetAttributes.md) |  | [optional] 
**window_spec** | [**DataSetWindow**](DataSetWindow.md) |  | [optional] 
**data_axis** | [**ColumnDataSetDataAxis**](ColumnDataSetDataAxis.md) |  | [optional] [default to ColumnDataSetDataAxis.ROW]
**rows** | [**List[RowHeadersInner]**](RowHeadersInner.md) | Header Attributes for the index data.  The initial string-valued headers (normally &#x60;resource&#x60;, &#x60;metric&#x60;,&#x60;aggregation&#x60;) indicate that row to contain series attributes.  The remaining object-valued row headers contain the index data. | 
**data** | **List[List[Datum]]** | All metric observation values for a single series. Prefixed by the series attributes. | 


## Example

```python
from waylay.services.queries.models.column_data_set import ColumnDataSet

column_data_set = ColumnDataSet(
    attributes=..., window_spec=..., data_axis=..., rows=..., data=...
)

# Create from JSON
column_data_set = ColumnDataSet.from_json(
    '{ "attributes": ..., "window_spec": ..., "data_axis": ..., "rows": ..., "data": ... }'
)

# Export to dictionary
column_data_set_dict = column_data_set.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


