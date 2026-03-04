# AlignmentTimezone

 The timezone to use when shifting boundaries, especially at day granularity. Also affects the rendering of timestamps when `render.iso_timestamp` is enabled.  When not specified, the `UTC` timezone is used. 

**Source:** `waylay.services.queries.models.alignment_timezone`



## Union Type (One Of)

This type allows one of the following:

Type | Description
------------ | -------------
**str** | [ICANN timezone identifier](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)
**str** | [UTC offset](https://en.wikipedia.org/wiki/UTC_offset)

## Example

```python
from waylay.services.queries.models.alignment_timezone import AlignmentTimezone

# Use any of the accepted types (see table above)
my_alignment_timezone: AlignmentTimezone = ...
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


