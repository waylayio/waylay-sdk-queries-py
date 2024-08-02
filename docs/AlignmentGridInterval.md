# AlignmentGridInterval

 Defines the grid used to align the aggregation window. The window will align at whole-unit multiples of this interval.  For intervals like `PT1D`, that are timezone-dependent, use the  `align.timezone` to fix the absolute timestamp of the grid boundaries.  If not specified, defaults to the `freq` aggregation interval. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from waylay.services.queries.models.alignment_grid_interval import AlignmentGridInterval

# TODO update the JSON string below
json = "{}"
# create an instance of AlignmentGridInterval from a JSON string
alignment_grid_interval_instance = AlignmentGridInterval.from_json(json)
# print the JSON string representation of the object
print AlignmentGridInterval.to_json()

# convert the object into a dict
alignment_grid_interval_dict = alignment_grid_interval_instance.to_dict()
# create an instance of AlignmentGridInterval from a dict
alignment_grid_interval_form_dict = alignment_grid_interval.from_dict(alignment_grid_interval_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


