# RowDataSet

Row-oriented dataset.  Timeseries data layout with a column header and a data row per timestamp. Result for render options `data_axis=column` and `header_array=row`.\",

**Source:** `waylay.services.queries.models.row_data_set`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**DataSetAttributes**](DataSetAttributes.md) |  | [optional] 
**window_spec** | [**DataSetWindow**](DataSetWindow.md) |  | [optional] 
**data_axis** | [**RowDataSetDataAxis**](RowDataSetDataAxis.md) |  | [optional] [default to RowDataSetDataAxis.COLUMN]
**columns** | [**List[ColumnHeadersInner]**](ColumnHeadersInner.md) | Header Attributes for the column data.  The initial string-valued headers (normally a single &#x60;timestamp&#x60;) indicate that column to contain row index data (i.e. timestamps).  The remaining object-valued column headers identify and describe the actual series data. | 
**column_names** | **List[str]** | Short names for the columns in the data set. These names are the &#x60;name&#x60; alias if given in the series specification, otherwise is composed of the &#x60;resource&#x60;, &#x60;metric&#x60; and &#x60;aggregation&#x60; attributes, concatenated with the &#x60;render.key_separator&#x60; (default &#x60;.&#x60;) as separator. | 
**data** | **List[List[Datum]]** |  | 


## Example

```python
from waylay.services.queries.models.row_data_set import RowDataSet

row_data_set = RowDataSet(
    attributes=...,
    window_spec=...,
    data_axis=...,
    columns=...,
    column_names=...,
    data=...,
)

# Create from JSON
row_data_set = RowDataSet.from_json(
    '{ "attributes": ..., "window_spec": ..., "data_axis": ..., "columns": ..., "column_names": ..., "data": ... }'
)

# Export to dictionary
row_data_set_dict = row_data_set.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


