# Render1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | [**Render1AnyOf**](Render1AnyOf.md) |  | [optional] 
**roll_up** | **bool** | move up attributes on rows (or columns) that are the same for             all rows (or columns) to a table attribute.             Levels enumerated in &#39;hierarchical&#39; are excluded. | [optional] 
**hierarchical** | [**Hierarchical**](Hierarchical.md) |  | [optional] 
**value_key** | **str** | if set, use this key in the value object to report data values | [optional] 
**show_levels** | **bool** | if set, report the levels used in the data values (either hierarchical or flat) | [optional] 
**iso_timestamp** | **bool** | if set, render timestamps in a row or column index with both epoch and iso representations | [optional] 
**row_key** | **str** | if set, use this key as name of the row-dimension for single-dimensional rows | [optional] 
**column_key** | **str** | if set, use this key as name of the column-dimension for single-dimensional columns | [optional] 
**header_array** | [**HeaderArrayOption**](HeaderArrayOption.md) |  | [optional] 
**data_axis** | [**DataAxisOption**](DataAxisOption.md) |  | [optional] 
**key_seperator** | **str** | character used to concatenate multi-key columns or rows when required | [optional] 
**key_skip_empty** | **bool** | skip empty values in concatenating multi-key column or row headers | [optional] 
**include_window_spec** | **bool** | if set, include window specification in render modes that support it | [optional] 

## Example

```python
from waylay.services.queries.models.render1 import Render1

# TODO update the JSON string below
json = "{}"
# create an instance of Render1 from a JSON string
render1_instance = Render1.from_json(json)
# print the JSON string representation of the object
print Render1.to_json()

# convert the object into a dict
render1_dict = render1_instance.to_dict()
# create an instance of Render1 from a dict
render1_form_dict = render1.from_dict(render1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


