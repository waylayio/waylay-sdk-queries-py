# AlignmentGridInterval

 Defines the grid used to align the aggregation window. The window will align at whole-unit multiples of this interval.  For intervals like `PT1D`, that are timezone-dependent, use the  `align.timezone` to fix the absolute timestamp of the grid boundaries.  If not specified, defaults to the `freq` aggregation interval. 

**Source:** `waylay.services.queries.models.alignment_grid_interval`



## Union Type (One Of)

This type allows one of the following:

Type | Description
------------ | -------------
**str** | A period in [ISO8601 duration](https://en.wikipedia.org/wiki/ISO_8601#Durations) format.
[**AlignmentInferred**](AlignmentInferred.md) | -

## Example

```python
from waylay.services.queries.models.alignment_grid_interval import AlignmentGridInterval

# Use any of the accepted types (see table above)
my_alignment_grid_interval: AlignmentGridInterval = ...
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


