# ResponseDataSet

Result timeseries data set, with one time dimension.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**DataSetAttributes**](DataSetAttributes.md) |  | [optional] 
**window_spec** | [**DataSetWindow**](DataSetWindow.md) |  | [optional] 
**data_axis** | [**ColumnDataSetDataAxis**](ColumnDataSetDataAxis.md) |  | [optional] [default to ColumnDataSetDataAxis.ROW]
**columns** | [**List[ColumnHeadersInner]**](ColumnHeadersInner.md) | Header Attributes for the column data.  The initial string-valued headers (normally a single &#x60;timestamp&#x60;) indicate that column to contain row index data (i.e. timestamps).  The remaining object-valued column headers identify and describe the actual series data. | 
**data** | [**List[ObjectData]**](ObjectData.md) |  | 
**rows** | [**List[RowHeadersInner]**](RowHeadersInner.md) | Header Attributes for the index data.  The initial string-valued headers (normally &#x60;resource&#x60;, &#x60;metric&#x60;,&#x60;aggregation&#x60;) indicate that row to contain series attributes.  The remaining object-valued row headers contain the index data. | 

## Example

```python
from waylay.services.queries.models.response_data_set import ResponseDataSet

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseDataSet from a JSON string
response_data_set_instance = ResponseDataSet.from_json(json)
# print the JSON string representation of the object
print ResponseDataSet.to_json()

# convert the object into a dict
response_data_set_dict = response_data_set_instance.to_dict()
# create an instance of ResponseDataSet from a dict
response_data_set_form_dict = response_data_set.from_dict(response_data_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


