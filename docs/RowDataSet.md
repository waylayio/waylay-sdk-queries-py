# RowDataSet

Row-oriented dataset.  Timeseries data layout with a column header and a data row per timestamp. Result for render options `data_axis=column` and `header_array=row`.\",

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**DataSetAttributes**](DataSetAttributes.md) |  | [optional] 
**window_spec** | [**DataSetWindow**](DataSetWindow.md) |  | [optional] 
**data_axis** | [**RowDataSetDataAxis**](RowDataSetDataAxis.md) |  | [optional] [default to RowDataSetDataAxis.COLUMN]
**columns** | [**List[ColumnHeadersInner]**](ColumnHeadersInner.md) | Header Attributes for the column data.  The initial string-valued headers (normally a single &#x60;timestamp&#x60;) indicate that column to contain row index data (i.e. timestamps).  The remaining object-valued column headers identify and describe the actual series data. | 
**data** | **List[List[Datum]]** |  | 

## Example

```python
from waylay.services.queries.models.row_data_set import RowDataSet

# TODO update the JSON string below
json = "{}"
# create an instance of RowDataSet from a JSON string
row_data_set_instance = RowDataSet.from_json(json)
# print the JSON string representation of the object
print RowDataSet.to_json()

# convert the object into a dict
row_data_set_dict = row_data_set_instance.to_dict()
# create an instance of RowDataSet from a dict
row_data_set_form_dict = row_data_set.from_dict(row_data_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


