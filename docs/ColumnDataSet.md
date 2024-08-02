# ColumnDataSet

Column-oriented dataset with rows header.  Timeseries data layout with a rows header containing the index data. The data array contains series data prefixed by series attributes. The `rows` index is prefix by the names of these series attributes. Result for render options `data_axis=row` and `header_array=column`.

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

# TODO update the JSON string below
json = "{}"
# create an instance of ColumnDataSet from a JSON string
column_data_set_instance = ColumnDataSet.from_json(json)
# print the JSON string representation of the object
print ColumnDataSet.to_json()

# convert the object into a dict
column_data_set_dict = column_data_set_instance.to_dict()
# create an instance of ColumnDataSet from a dict
column_data_set_form_dict = column_data_set.from_dict(column_data_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


